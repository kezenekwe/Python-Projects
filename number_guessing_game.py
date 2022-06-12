"""Guess that number!"""
"""A simple number guessing game using python."""

#Assign a variable to a randomly generated number from any range. (rdmn#= some random number)
#if user inputs correct number, end the program. if not, continue the program.

import random

number = random.randint(1, 10)
number = int(number)

user_number = input("Guess a number from 1 to 10: ")
user_number = int(user_number)

play_again = ""
while play_again != 'N':

    if number != user_number:
        user_number = input('Guess again. ')
        user_number = int(user_number)

    if number == user_number:
        print('You guessed right!')
        play_again = input('Play again? Y/N: ')

    #if play_again = yes, restart while loop.
    #if play_again does not equal yes or no, prompt user to enter either yes or no.
    #if play_again = no, exit the program.

        if play_again == 'N':
            print("Thanks for playing.")

        if play_again == 'Y':
            number = random.randint(1, 10)
            number = int(number)

            user_number = input("Guess a number from 1 to 10: ")
            user_number = int(user_number)

























