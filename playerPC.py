import random



def player_vs_PC():
    options = ['rock', 'paper', 'scissors']
    playerPts = 0
    computerPts = 0
    print('\n* Player vs Computer gamemode *')
    while True:

        compTry = random.choice(options)
        print('Score - Player: ' + str(playerPts) + ' Computer: ' + str(computerPts))

        userInput = input("""\nYour options: Rock / Paper / Scissors / Menu
>""")

        print(f'computer: {compTry}\n')
        if userInput.lower() == 'menu':
            break

        elif userInput.lower() == compTry.lower():
            print('TIE')

        elif userInput.lower() == 'rock':

            if compTry == 'paper':
                print('You lost :(')
                computerPts += 1

            elif compTry == 'scissors':
                print('You won!')
                playerPts += 1

        elif userInput.lower() == 'paper':

            if compTry == 'rock':
                print('You won!')
                playerPts += 1

            elif compTry == 'scissors':
                print('You lost :(')
                computerPts += 1

        elif userInput.lower() == 'scissors':

            if compTry == 'rock':
                print('You lost :(')
                computerPts += 1

            elif compTry == 'paper':
                print('You won!')
                playerPts += 1

        else:
            print("I don't know that command, try again :)")