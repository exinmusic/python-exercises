'''

exercise: Create the game of Rock, Paper, Scissors 

'''
import getpass
def determine_winner(player1, player2):
	if player1 == "rock":
		if player2 == 'rock':
			return 'Tie game!'
		if player2 == "paper":
			return 'Paper beats rock! Player 2 wins!'
		if player2 == 'scissors':
			return 'Rock beats scissors! Player 1 wins!'
	if player1 == "paper":
		if player2 == 'rock':
			return 'Paper beats rock! Player 1 wins!'
		if player2 == 'paper':
			return 'Tie game!'
		if player2 == 'scissors':
			return 'Scissors beats paper! Player 2 wins!'
	if player1 == 'scissors':
		if player2 == 'rock':
			return 'Rock beats scissors! Player 2 wins!'
		if player2 == 'paper':
			return 'Scissors beats paper! Player 1 wins!'
		if player2 == 'scissors':
			return 'Tie game!'

def play_rps():
	player1 = getpass.getpass('rock, paper scissors? Player 1: ').lower()
	player2 = getpass.getpass('                      Player 2: ').lower()
	print determine_winner(player1,player2)