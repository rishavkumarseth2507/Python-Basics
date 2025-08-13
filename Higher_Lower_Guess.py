'''
Project: Higher Lower Guess Game

Concept:
You give the player a fixed number of chances to guess the correct number, 
and after each wrong guess, you tell them whether the guess was higher or lower.
'''

import random

print("You have 5 chances for correct Guess")
a = random.randint(1,50)
count =5
i=0
while(i<count):
    b = int(input("Enter your Guess: "))
    if(a==b):
        print("That's Correct Guess")
        break
    elif(a<b):  print("Too High!")
    else:   print("Too Low!")
    i +=1
else:   print("You Failed!")

