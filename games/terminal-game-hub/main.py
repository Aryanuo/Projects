import json
import os

# --------Importing Games--------
from games.coin_toss import coin_toss
from games.dice_roll import dice_roll
from games.high_low import high_low
from games.number_guessing import number_guessing
from games.rock_paper_scissor import rock_paper_scissor
from games.higher_lower import higher_lower


# --------Score Board--------
score_file = os.path.join(os.path.dirname(__file__), "scoreboard.json")

def load_scoreboard():
    if os.path.exists(score_file):
        with open(score_file) as f:
            return json.load(f)
    return {"games_played":0, "wins":0, "losses":0, "draws":0}

def save_scoreboard(scoreboard):
    with open(score_file,"w") as f:
        json.dump(scoreboard,f)

scoreboard = load_scoreboard()

def update_score(result):
    scoreboard["games_played"] += 1
    if result=="win":
        scoreboard["wins"] += 1 
    elif result=="loss":
        scoreboard["losses"] += 1  
    elif result=="draw":
        scoreboard["draws"] += 1 
    save_scoreboard(scoreboard)

def show_scoreboard():
    scoreboard = load_scoreboard()
    print("==========SCOREBOARD==========")
    print("Games played: ",scoreboard["games_played"])
    print("Wins ",scoreboard["wins"])
    print("Losses: ",scoreboard["losses"])
    print("Draws: ",scoreboard["draws"])
    print("==========THANK YOU==========")

# --------Main Menu--------
def main():
    while True:
        print("\n===== MINI GAME COLLECTION =====")
        print("1. Number Guessing")
        print("2. Coin Toss")
        print("3. Dice Roll")
        print("4. Rock–Paper–Scissors")
        print("5. High or Low")
        print("6. Higher or Lower")
        print("7. Show Scoreboard")
        print("0. Exit")

        choice = input("Choose a game: ")

        if choice == "1":
            number_guessing(update_score)
        elif choice == "2":
            coin_toss(update_score)
        elif choice == "3":
            dice_roll(update_score)
        elif choice == "4":
            rock_paper_scissor(update_score)
        elif choice == "5":
            high_low(update_score)
        elif choice == "6":
            higher_lower(update_score)
        elif choice == "7":
            show_scoreboard()
        elif choice == "0":
            print("Thanks for playing! 👋")
            show_scoreboard()
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

