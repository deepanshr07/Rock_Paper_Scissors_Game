# create a rock, paper, scissors game.

'''
1 for rock
-1 for paper
0 for scissors
'''

import random

computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")
youdict = {"r" : 1, "p" : -1, "s" : 0}
reversedict = {1 : "Rock", -1 : "Paper", 0 : "Scissors"}

you = youdict[youstr]

print(f"you chose {reversedict[you]}\n Computer chose {reversedict[computer]}")

if(computer == you):
    print("Its a draw")
else:
    if(computer == 1 and you == -1):
        print("You win")
    elif(computer == 1 and you == 0):
        print("you lose")
    elif(computer == -1 and you == 1):
        print("You lose")
    elif(computer == -1 and you == 0):
        print("you win")
    elif(computer == 0 and you == 1):
        print("You win")
    elif(computer == 0 and you == -1):
        print("You lose")


