import random as rand

gameinplay = True
computer_wins = 0
player_wins = 0
while gameinplay:
    player_move = input('Would you like to play Rock, Paper, or Scissors? (or enter "Quit" to quit)').title()
    computer_move = rand.choice(['Rock','Paper','Scissors'])
    print (f'player {player_move} computer {computer_move}')
    if player_move == 'Rock':
        if computer_move == 'Rock':
            print ('Tie game')
        elif computer_move == 'Paper':
            print ('Paper covers rock - You Lose')
            computer_wins += 1
            print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
        elif computer_move == 'Scissors':
            print ('Rock crushes Scissors - You Win')
            player_wins += 1
            print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
    elif player_move == 'Paper':
        if computer_move == 'Paper':
            print ('Tie game')
        elif computer_move == 'Rock':
            print ('Paper covers rock - You Win')
            player_wins += 1
            print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
        elif computer_move == 'Scissors':
            print ('Scissors cuts Paper - You Lose')
            computer_wins += 1
            print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
    elif player_move == 'Scissors':
        if computer_move == 'Scissors':
            print ('Tie game')
        elif computer_move == 'Paper':
            print ('Scissors cut Paper - You Win')
            player_wins += 1
            print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
        elif computer_move == 'Rock':
            print ('Rock crushes Scissors - You Lose')
            computer_wins += 1
            print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
    elif player_move == "Quit":
        gameinplay = False
        print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
    else:
        print ('Please choose a valid option')