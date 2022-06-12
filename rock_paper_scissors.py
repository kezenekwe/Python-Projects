"""Rock, Paper, Scissors!"""
import random

"""A rock, paper, scissors game using python."""

#simulate computer choices using imported function
#prompt the user to input choice(rock, paper, or scissors)
#if-elif-else statements depending on what the user chooses
#prompt the user to play again after each turn.
#otherwise, quit the game.


import random

print("Let's play a game of rock, paper, scissors.")

new_game = ''
while new_game != 'N':

    user_choice = input("Enter 'rock' for rock, 'paper' for paper, or 'scissors' for scissors. ")

    possible_choices = ['rock', 'paper', 'scissors']
    cpu_choice = random.choice(possible_choices)

    if user_choice == cpu_choice:
        print('Draw')
        new_game = input('Play again? Enter Y/N: ')
        if new_game == 'N':
            print("Thanks for playing")

    if cpu_choice == 'rock':
        if user_choice == 'paper':
            print(f'You picked {user_choice}, while the CPU chose {cpu_choice}.')  # copy/paste this for each outcome.
            print('You win!')
        if user_choice == 'scissors':
            print(f'You picked {user_choice}, while the CPU chose {cpu_choice}.')
            print('You lose.')
        new_game = input('Play again? Enter Y/N: ')
        if new_game == 'N':
            print("Thanks for playing")

    if cpu_choice == 'scissors':
        if user_choice == 'rock':
            print(f'You picked {user_choice}, while the CPU chose {cpu_choice}.')
            print('You win!')
        if user_choice == 'paper':
            print(f'You picked {user_choice}, while the CPU chose {cpu_choice}.')
            print('You lose.')
        new_game = input('Play again? Enter Y/N: ')
        if new_game == 'N':
            print("Thanks for playing")

    if cpu_choice == 'paper':
        if user_choice == 'scissors':
            print(f'You picked {user_choice}, while the CPU chose {cpu_choice}.')
            print('You win!')
        if user_choice == 'rock':
            print(f'You picked {user_choice}, while the CPU chose {cpu_choice}.')
            print('You lose.')
        new_game = input('Play again? Enter Y/N: ')
        if new_game == 'N':
            print("Thanks for playing.")