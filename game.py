import random
from playerPC import player_vs_PC
from twoplayers import player_vs_player
#hrac1
#hrac2
#pc

#options = ['rock', 'paper', 'scissors']


print("Welcome to the Rock/Paper/Scissors game!\nPlease select gamemode:")

while True:

    try:
        request = int(input("""
>press 1 for player vs computer
>press 2 for player vs player
>press 0 for QUIT the game
>"""))

    except ValueError:
        print('Please enter only 1, 2 or 0')


    if request == 0:
        print('Thank you for playing, bye!')
        break

    elif request == 1:
        player_vs_PC()

    elif request == 2:
        player_vs_player()
    else:
        print('\nI dont know that command, try again :)\n')

