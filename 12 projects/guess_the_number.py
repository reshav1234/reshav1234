# Guessing the random number

import random

# We define a function 
def guessing(x):
    random_number = random.randint(1, x)
    guess = 0 # Initialization
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        print(guess)
        if guess > random_number:
            print("Sorry, try again. Too high.")
        elif guess < random_number:
            print("Sorry, try again. Too low.")
    
    print("Congratulation you have guessed the right answer ", random_number)

def computer_guess(x):
    low = 1 
    high = x
    feedback = ''
    while feedback != 'c' and low != high:
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high, too low, or correct?")
        if feedback == 'h':
            high = guess - 1 
        elif feedback == 'l':
            low = guess + 1 
    print("Congratulation computer guessed your number ", guess)


#guessing(15)
computer_guess(7)