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
        player_choice = input ('Is your move Rock, Paper, or Scissors?\n\n').title()
        if player_choice == 'Rock' or player_choice == 'Paper' or player_choice == 'Scissors':
            return player_choice
        else:
            print ('not a valid option')


    def computer_move(self):
        computer_choice = random.randint(1,3)
        if computer_choice == 1:
            computer = 'Rock'
        elif computer_choice == 2:
            computer = 'Paper'
        elif computer_choice == 3:
            computer= 'Scissors'
        return computer

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

user=Game()
user.compare_moves()