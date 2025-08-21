# guessing game
import random

num = random.randint(1, 100)
user_guess = int(input('guess a Number :'))
while user_guess != num:
    if user_guess < num:
        print('too low')
    elif user_guess > num:
        print('too high')

    user_guess = int(input('try again :'))

print ('correct number is ', num)
