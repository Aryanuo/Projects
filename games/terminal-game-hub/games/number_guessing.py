import random

def number_guessing(update_score):
    n = int(input("Guess the number between 1 and 6 "))
    computer = random.randint(1,5)

    print("Computer choose ",computer)
    if(computer==n):
        print("Great job, you guessed it right")
        update_score("win")
    else:
        print("Better luck next time")
        update_score("loss")