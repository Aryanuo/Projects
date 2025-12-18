import random

def roll():
    return random.randint(1, 6)

# Ask for number of players
while True:
    try:
        players = int(input("Enter number of players (2-4): "))
        if 2 <= players <= 4:
            break
        else:
            print("Invalid input. Enter a number between 2 and 4.")
    except ValueError:
        print("Please enter a valid number.")

# Game setup
WINNING_SCORE = 50
player_scores = [0 for _ in range(players)]

# Main game loop
while max(player_scores) < WINNING_SCORE:
    for player_id in range(players):
        print(f"\n🎲 Player {player_id + 1}'s turn")
        current_score = 0

        while True:
            choice = input("Roll the dice? (y/n): ").lower()

            if choice == "n":
                break
            elif choice != "y":
                print("Invalid choice. Please enter 'y' or 'n'.")
                continue

            value = roll()

            if value == 1:
                print("💀 Oops! You rolled a 1. Turn over.")
                current_score = 0
                break
            else:
                print(f"You rolled a {value}")
                current_score += value
                print("Current turn score:", current_score)

        player_scores[player_id] += current_score
        print(f"Total score of Player {player_id + 1}: {player_scores[player_id]}")

        if player_scores[player_id] >= WINNING_SCORE:
            break

# Winner announcement
winning_score = max(player_scores)
winner_id = player_scores.index(winning_score)

print("\n🎉 GAME OVER 🎉")
print(f"🏆 Player {winner_id + 1} wins with {winning_score} points!")
