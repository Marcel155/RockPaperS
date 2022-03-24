def player_vs_player():
    player1pts = 0
    player2pts = 0
    print('\n* Player vs Player gamemode *')
    test = True
    druhy_test = True

    while True:

        print('\nScore - Player1: ' + str(player1pts) + ' Player2: ' + str(player2pts))

        while test:
            player1_input = input("""\nPlayer1:
Your options: Rock / Paper / Scissors / Menu
>""")
            print('\n\n\n\n\n\n')
            if player1_input.lower() == 'rock':
                break
            elif player1_input.lower() == 'paper':
                break
            elif player1_input.lower() == 'scissors':
                break
            elif player1_input.lower() == 'menu':
                break
            else:
                print('\nI dont know that command, try again :)')


        if player1_input.lower() == 'menu':
            break

        while druhy_test:

            player2_input = input("""\nPlayer2:
Your options: Rock / Paper / Scissors / Menu
>""")
            print('\n\n\n\n\n\n')
            if player2_input.lower() == 'rock':
                break
            elif player2_input.lower() == 'paper':
                break
            elif player2_input.lower() == 'scissors':
                break
            elif player2_input.lower() == 'menu':
                break
            else:
                print('\nI dont know that command, try again :)')


        if player2_input.lower() == 'menu':
            break

        elif player1_input.lower() == player2_input.lower():
            print('TIE')

        elif player1_input.lower() == 'rock':

            if player2_input == 'paper':
                print('Player2 won')
                player2pts += 1

            elif player2_input == 'scissors':
                print('Player1 won')
                player1pts += 1

        elif player1_input.lower() == 'paper':

            if player2_input == 'rock':
                print('Player1 won')
                player1pts += 1

            elif player2_input == 'scissors':
                print('Player2 won')
                player2pts += 1

        elif player1_input.lower() == 'scissors':

            if player2_input == 'rock':
                print('Player2 won')
                player2pts += 1

            elif player2_input == 'paper':
                print('Player1 won')
                player1pts += 1
        else:
            print("I don't know that command, try again :)")