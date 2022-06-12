import random

    #Prompt the user to roll the dice.
    #Show the user what he/she rolled.
    #Allow user to roll again.
    #Yes = prompt the user to roll dice again.
    #No = quits dice rolling app.

roll = input("Enter 'R' to roll the dice! ")
if roll == 'R':
    reroll=""
    while reroll !='N':
        print(f"You rolled a {random.randint(1,6)}.")
        reroll = input("Roll again? Enter Y/N: ")
        if reroll == 'N':
            print("Thanks for playing!")




