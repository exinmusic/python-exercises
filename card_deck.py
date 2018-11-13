from pprint import pprint
from random import shuffle

''' 

exercise: Create a deck of playing cards. The deck must be able to have cards pulled, and you must be able to shuffle the deck. 

'''

# A deck class initializes with 52 cards in order.
class deck:

	# Builds a single card in the form of a dictionary.
	def card_gen(self,index,suit_name):
		if index == 1:
			return {'name':'Ace','suit':suit_name}
		if index == 11:
			return {'name':'Jack','suit':suit_name}
		if index == 12:
			return {'name':'Queen','suit':suit_name}
		if index == 13:
			return {'name':'King','suit':suit_name}
		else:
			return {'name':index,'suit':suit_name}

	# Builds deck of 52 playing cards as a list of dictionaries.
	def __init__(self, suits=['hearts', 'diamonds', 'clubs', 'spades']):
		self.cards=[]
		for s in suits:
			for x in range(1,13+1,1):
				self.cards.append(self.card_gen(x,s))

	def pull_card(self):
		try:
			return self.cards.pop()
		except:
			return None

	def shuffle_cards(self):
		shuffle(self.cards)