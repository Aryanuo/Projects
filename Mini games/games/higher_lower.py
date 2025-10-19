import random
def higher_lower(update_score):
    player = int(input("Enter a no. between 1 to 100 "))
    computer = random.randint(1,100)
    count=1

    while(player!=computer):
        if(player<computer):
            print("Go higher")
        else:
            print("Go lower")

        count+=1
        player = int(input("Again enter a no. between 1 to 100 "))

    print(f"You won in {count} attempts")
    update_score("win")