import random
def coin_toss(update_score):
    computer = random.choice(["head","tail"])
    you = input("head or tails ? ")

    print(f"You choose {you} and coin shows {computer}")

    if(computer == you):
        print("you win")
        update_score("win")

    else:
        print("you lose")
        update_score("loss")
