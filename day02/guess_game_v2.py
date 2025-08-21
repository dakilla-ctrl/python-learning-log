# Write your code here :-)
import random

def computer_random_pick():
    num = random.randint(1,100)
    return num

def user_guess():
    guess = int(input('Guess a Number between 1 and 100: '))
    return guess

def check_guess(num):
    guess = user_guess()
    while guess != num:
        if guess < num:
            print('Too low')

        elif guess > num:
            print('Too high')
        guess = int(input('Try again: '))
    print('Correct! number is: ', num)

def playgame():
    num = computer_random_pick()
    check_guess(num)

playgame()
