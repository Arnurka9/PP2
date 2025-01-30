"""
Write a program able to play the "Guess the number" - game, 
where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
"""

import random

def startGame(user_name):
    guesses = 1
    
    finding_num = random.randint(1, 20)
    
    while True:
        print("Take a guess.")
        guess = int(input())
        
        print()
        
        if guess == finding_num:
            print(f"Good job, {user_name}! You guessed my number in {guesses} guesses!")
            break
        elif guess < finding_num:
            print("Your guess is too low.")
        elif guess > finding_num:
            print("Your guess is too high.")
        
        guesses += 1
    
    return 0    


print("Hello! What is your name?")
user_name = input("")
print()
print(f"Well, {user_name}, I am thinking of a number between 1 and 20.")

startGame(user_name)