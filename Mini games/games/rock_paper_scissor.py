import random

def rock_paper_scissor(update_score):
    computer = random.choice([-1,0,1])
    you = input("enter your choice r,p,s: ")

    choice = {"r":-1,"p":0,"s":1}
    rev_choice = {-1:"rock",0:"paper",1:"scissor"}

    print(f"you choose {rev_choice[choice[you]]} computer choose {rev_choice[computer]}")

    if(computer==choice[you]):
        print("its a draw")
    else:
        if(computer==-1 and choice[you]==0):     #computer-choice[you]=-1
            print("you win")
            update_score("win")
        elif(computer==-1 and choice[you]==1):   #computer-choice[you]=0
            print("you lose")
            update_score("loss")
        elif(computer==0 and choice[you]==1):    #computer-choice[you]=-1
            print("you win")
            update_score("win")
        elif(computer==0 and choice[you]==-1):   #computer-choice[you]=1
            print("you lose")
            update_score("loss")
        elif(computer==1 and choice[you]==-1):   #computer-choice[you]=2
            print("you win")
            update_score("win")
        elif(computer==1 and choice[you]==0):    #computer-choice[you]=1
            print("you lose")
            update_score("loss")
        else:
            print("something went wrong")
