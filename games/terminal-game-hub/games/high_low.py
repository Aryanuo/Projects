import random

def high_low(update_score):
    n = int(input("enter a number bewtween 1 to 20 "))
    h_l = input("Is your no. Higher(h) or Lower(l) than the computer ")
    computer = random.randint(1,20)
    if(n>computer and h_l == "h"):
        print(f"corret, your no. {n} is higher than the computer no. {computer}")
        update_score("win")
    elif(n>computer and h_l == "l"):
        print(f"wrong, your no. {n} is higher than the computer no. {computer}")
        update_score("loss")
    elif(n<computer and h_l == "l"):
        print(f"corret, your no. {n} is lowwer than the computer no. {computer}")
        update_score("win")
    elif(n<computer and h_l == "h"):
        print(f"wrong, your no. {n} is lower than the computer no. {computer}")
        update_score("loss")
    else:
        print("both are equal")
        update_score("draw")