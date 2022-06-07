# User guesses the number

import random       
def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Guess the number from 1 to {x}: "))
        if guess > x:
            print("Guess is too high, try again.")
        elif guess < x:
            print("Guess is too low, try again.")

    print("You have guessed the right number.")

guess(10)


# Computer guesses the number
import random
def guessing(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low != high:
        guess = random.randint(low, high)
        if feedback =='h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print("You have guessed the corrent number.", guess)

guessing(5)
