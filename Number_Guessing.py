# Number Guessing Game

import random
a = random.randint(1,10)
b = None
count =0

while (a != b):
    b = int(input("What's your guess? "))
    if(a<b): 
        print("Too high!")
        count +=1
    elif(a>b): 
        print("Too Low")
        count +=1
print("Your Guess is correct")
print("Number of wrong attempt is ",count)