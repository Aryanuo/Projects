import random

def dice_roll(update_score):
    player = int(input("Enter a no. of dice"))
    computer = random.randint(1, 6)

    print("You rolled:", player)
    print("Computer rolled:", computer)


    if(player>6):
        print("You can't type anything greater than 6")
    elif player > computer:
        print("🎉 You win!")
        update_score("win")

    elif player < computer:
        print("❌ You lose!")
        update_score("loss")
    else:
        print("😮 It's a draw!")
        update_score("draw")

