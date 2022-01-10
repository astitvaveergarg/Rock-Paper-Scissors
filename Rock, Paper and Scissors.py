import random   #Package

#DEFINED FUNCTIONS :-

def intro(): #Introduction Defined
    print(100*"-")
    print(34*" "+ "Welcome To Rock, Paper And Scissors")
    print(100*"-")
    print("The First One To Gain 5 Points, Wins The Game.")
    print(100*"-")

def AI_INPUT(): #AI INPUT
    a=random.randint(1, 3)
    if a==1:
        return "rock"
    elif a==2:
        return "paper"
    elif a==3:
        return "scissors"

def Refree(a, b, c, d):  #Winning Decision
    if (a == b):
        print(f"You Draw                                                               User_Score= {d}   AI_Score= {c}")
    elif (a=="rock" and b=="scissors" ):
        d=d+1
        print(f"You Won                                                                User_Score= {d}   AI_Score= {c}")
        return "won"
    elif (a=="rock" and b=="paper" ):
        c=c+1
        print(f"You Loose                                                              User_Score= {d}   AI_Score= {c}")
        return "lose"
    elif (a=="paper" and b=="scissors" ):
        c = c + 1
        print(f"You Loose                                                              User_Score= {d}   AI_Score= {c}")
        return "lose"
    elif (a=="paper" and b=="rock" ):
        d = d + 1
        print(f"You Won                                                                User_Score= {d}   AI_Score= {c}")
        return "won"
    elif (a=="scissors" and b=="rock" ):
        c = c + 1
        print(f"You Loose                                                              User_Score= {d}   AI_Score= {c}")
        return "lose"
    elif (a=="scissors" and b=="paper" ):
        d = d + 1
        print(f"You Won                                                                User_Score= {d}   AI_Score= {c}")
        return "won"
    else:
        print("Invalid Input")

#MAIN PROCESSING

while True:    #Main Loop
    AI_SCORE=0     #Variable
    USER_SCORE=0    #Variable
    intro()
    while True:     #Game Loop
        if (USER_SCORE == 5 or AI_SCORE == 5):
            break
        AI_CHOOSE = AI_INPUT()
        User_Input=input(25*" "+"Write Rock, Paper Or Scissors : ")
        User_Input=User_Input.lower()
        print(25*" "+"AI Choose : "+AI_CHOOSE)
        print(100 * "-")
        Result=Refree(User_Input, AI_CHOOSE, AI_SCORE, USER_SCORE)
        print(100 * "-")
        if (Result == "lose"):
            AI_SCORE+=1
        elif (Result=="won"):
            USER_SCORE+=1

    print(100*"-")      #Result Show
    if (USER_SCORE==5):
        print("USER WON")
    else:
        print("AI WON")
    print(100*"-")


    z=input("If You Want To Play Again, Type Yes, or Type NO to Exit ")    #Reset or Exit
    z=z.lower()
    if(z=="no"):
        break