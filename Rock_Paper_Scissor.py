'''
Project: Rock, Paper, Scissors
'''
import random

print("Rock, Paper, Scissors Game!")
options = ["rock","paper","scissors"]

computer = 0
player =0
NOG = 0     # Number of Games

while(NOG < 5):
    cc = random.choice(options)     # Computer_choice
    pc = input("Enter Rock/Paper/Scissors: ").lower()      # player choice

    if pc not in options:
        print("Invalid choice! Please enter Rock, Paper, or Scissors.")
        continue  # Don't count invalid inputs as rounds
    print(f"Computer chose: {cc}")
    
    if(pc == cc):
        print("It's a Tie")
    elif((pc == "rock" and cc == "scissors") or (pc == "paper" and cc == "rock") or (pc == "scissors" and cc == "paper")):   
        print("You Win this Round!")
        player +=1
    else:
        print("Computer wins this round!")
        computer += 1
    NOG +=1
if(player > computer):  print("You Win!")
elif(player < computer):    print("Computer Win!")
else:   print("Tie!")


