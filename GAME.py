
import random

options=["rock","paper","scissor"]
print("------------------------HELLO!!-----------------------------")
print("------------------------------------------------------------")
print("----------WELCOME TO THE ROCK PAPER SCISSOR GAME------------")
print("-------------------------------------------------------------")
i=3
uscore=0
cscore=0
while i>0:
    print(f"YOUR {i} CHANCE")
    option = random.choice(options)
    print("YOUR CHOICE: ",end=" ")
    val = input()
    print(f"COMPUTER'S CHOICE IS {option}")
    if val.lower() == "rock" and option == "paper":
        print("------------YOU WON THIS LEVEL---------------------")
        print("------------------+1 TO YOUR SCORE-----------------")
        uscore+=1
    elif val.lower() == "rock" and option == "scissor":
        print("------------YOU WON THIS LEVEL---------------------")
        print("------------------+1 TO YOUR SCORE-----------------")
        uscore += 1
    elif val.lower() == "rock" and option == "rock":
        print("------------------DRAW-------------------------------")
    elif val.lower() == "paper" and option == "scissor":
        print("-------------------WELL YOU LOST THIS TIME-------------")
        cscore+=1
    elif val.lower() == "paper" and option == "rock":
        print("------------YOU WON THIS LEVEL---------------------")
        print("------------------+1 TO YOUR SCORE-----------------")
        uscore += 1
    elif val.lower() == "paper" and option == "paper":
        print("------------------DRAW-------------------------------")
    elif val.lower() == "scissor" and option == "scissor":
        print("------------------DRAW-------------------------------")
    elif val.lower() == "scissor" and option == "paper":
        print("------------YOU WON THIS LEVEL---------------------")
        print("------------------+1 TO YOUR SCORE-----------------")
        uscore += 1
    elif val.lower() == "scissor" and option == "rock":
        print("-------------------WELL YOU LOST THIS TIME-------------")
        cscore+=1
    else:
        print("something wrong")
        break
    i-=1
if uscore>cscore:
    print("-------------------------------------------------------------")
    print(f"---------YOU WON THE GAME WITH {uscore} points--------------")
    print("------------------HOORAHHHHHH!!-------------------------------")
    print("----------------------BYEEEEEEEEE------------------------------")
elif uscore==cscore:
    print("----------------------------ITS A DRAW------------------------")
else:
    print("---------------------------YOU LOOSE-----------------------------")