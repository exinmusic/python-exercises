'''

exercise: Create the game of Rock, Paper, Scissors 

'''

def determine_winner(player1, player2):
	if player1 == "rock":
		if player2 == "rock":
			return 'Tie game!'
		if player2 == "paper":
			return 'Paper beats rock! Player 2 wins!'
		if player2 == 'scissors':
			return 'Rock beats scissors! Player 1 wins!'