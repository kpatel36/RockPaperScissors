# For this project, you will individually create a program that has a "player" and a "computer" advisary. The computer should randomly choose it's decision based on a list of actions it can take ("Rock", "Paper" or "Scissors").
# The player should then have a chance to input their decision. If player and computer choose the same decision then display ("Game Tied"), If the player chooses "Rock" and the computer chooses "Paper" display ("You lose"), if
# the player chooses "Scissors" and the computer chooses "Rock" display ("You Lose") and if the player chooses "Paper" and the computer chooses "Scissors" then display ("You lose") -- Vice versa for other descisions.
# Continue to ask the player for their input until they say "I quit", at which time the game will then end and display ("Thank you for playing").
# This should be done with an Object-Oriented approach!
# In this project, you will need to use the random.randint function to enable to computer to make a random decision. Full documentation on the use of this function is attached in a link to this assignment.
# Once completed, commit your code to github and submit the link to this assignment.


import random
class Game():
    def __init__(self):
        self.computer = self.computer_move()
        self.player = self.player_move()
        self.score_counter = {'player wins':0, 'computer wins': 0}

    def player_move(self):
        player_choice = input ('What\'s your move: Rock, Paper, Scissors, Lizard, Spock? \n\n').title()
        if player_choice in  ['Rock','Paper','Scissors','Lizard','Spock']:
            return player_choice
        else:
            print ('not a valid option')
            

    def computer_move(self):
        computer = random.randint(1,5)
        if computer == 1:
            computer_choice = 'Rock'
        elif computer == 2:
            computer_choice = 'Paper'
        elif computer == 3:
            computer_choice = 'Scissors'
        elif computer == 4: 
            computer_choice = 'Lizard'
        elif computer ==5:
            computer_choice = 'Spock'
        return computer_choice

    def compare_moves(self):
        computer_wins = 0
        player_wins = 0
        print (f'Player played: {self.player} and Computer played: {self.computer}\n')
        if self.player == 'Rock':
            if self.computer == 'Rock':
                print ('Tie game')
            elif self.computer == 'Paper':
                print ('Paper covers rock - You Lose')
                computer_wins += 1
                print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
            elif self.computer == 'Scissors':
                print ('Rock crushes Scissors - You Win')
                player_wins += 1
                print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
            elif self.computer == 'Lizard':
                print ('Rock crushes Lizard - You Win')
                player_wins += 1
                print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
            elif self.computer == 'Spock':
                print ('Spock vaporizes Rock - You Lose')
                computer_wins +=1
                print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
        elif self.player == 'Paper':
            if self.computer == 'Paper':
                print ('Tie game')
            elif self.computer == 'Rock':
                print ('Paper covers rock - You Win')
                player_wins += 1
                print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
            elif self.computer == 'Scissors':
                print ('Scissors cuts Paper - You Lose')
                computer_wins += 1
                print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
            elif self.computer == 'Lizard':
                print ('Lizard Eats Paper - You Lose')
                computer_wins += 1
                print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
            elif self.computer == 'Spock':
                print ('Paper disproves Spock - You Win')
                player_wins += 1
                print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
        elif self.player == 'Scissors':
            if self.computer == 'Scissors':
                print ('Tie game')
            elif self.computer == 'Paper':
                print ('Scissors cut Paper - You Win')
                player_wins += 1
                print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
            elif self.computer == 'Rock':
                print ('Rock crushes Scissors - You Lose')
                computer_wins += 1
                print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
            elif self.computer == 'Lizard':
                print ('Scissors decapitates Lizard - You Win')
                player_wins += 1
                print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
            elif self.computer == 'Spock':
                print ('Spock smashes Sciessors - You Lose')
                computer_wins += 1
                print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
        elif self.player == 'Lizard':
            if self.computer == 'Lizard':
                print ('Tie Game')
            elif self.computer == 'Rock':
                print ('Rock Crushes Lizard - You Lose')
                computer_wins += 1
                print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
            elif self.computer == 'Paper':
                print ('Lizard Eats Paper - You Win')
                player_wins += 1
                print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
            elif self.computer == 'Scissors':
                print ('Scissors decapitates Lizard - You Lose')
                computer_wins += 1
                print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
            elif self.computer == 'Spock':
                print ('Lizard poisons Spock - You Win')
                player_wins += 1
                print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
        elif self.player == 'Spock':
            if self.computer == 'Spock':
                print ('Tie Game')
            elif self.computer == 'Rock':
                print ('Spock vaporizes Rock - You Win')
                computer_wins += 1
                print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
            elif self.computer == 'Paper':
                print ('Paper disproves Spock - You Lose')
                computer_wins += 1
                print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
            elif self.computer == 'Scissors':
                print ('Spock smashes Scissors - You Win')
                computer_wins += 1
                print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')
            elif self.computer == 'Lizard':
                print ('Lizard poisons Spock - You Lose')
                computer_wins += 1
                print (f'Player Wins: {player_wins}, Computer Wins: {computer_wins}')



user=Game()
user.compare_moves()