class Card:
	""" A playing card. """
	RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
	SUITS = ["c", "d", "h", "s"]

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def __str__(self):
		reply = self.rank + self.suit
		return reply

class Hand:
	""" A hand of playing cards. """
	def __init__(self):
		self.cards = []

	def __str__(self):
		if self.cards:
			reply = ""
			for card in self.cards:
				reply += str(card) + " "
		else:
			reply = "<empty>"
		return reply
	
	def clear(self):
		self.cards = []
	
	def add(self, card):
		self.cards.append(card)

	def give(self, card, other_hand):
		self.cards.remove(card)
		other_hand.add(card)

class Deck(Hand):
	"""" A deck of playing cards. """
	def populate(self):
		for suit in Card.SUITS:
			for rank in Card.RANKS:
				self.add(Card(rank, suit))
	
	def shuffle(self):
		import random
		random.shuffle(self.cards)
	
	def deal(self, hands, per_hand = 1):
		for rounds in range(per_hand):
			for hand in hands:
				if self.cards:
					top_card = self.cards[0]
					self.give(top_card, hand)
				else:
					print("Out of cards!")

def main():
	print("This is Main Function")

if __name__ == "__main__":
	print("Created a new deck.")
	print("Deck:")
	deck1 = Deck()
	print(deck1)

	print("\nPopulated the deck.")
	print("Deck:")
	deck1.populate()
	print(deck1)

	print("\nShuffled the deck.")
	print("Deck:")
	deck1.shuffle()
	print(deck1)

	my_hand = Hand()
	your_hand = Hand()
	hands = [my_hand, your_hand]
	deck1.deal(hands, per_hand = 5)


	print("\nDealt 5 cards to my hand and yout hand.")
	print("My hand:")
	print(my_hand)

	print("Your hand:")
	print(your_hand)
	
	print("Deck:")
	print(deck1)

	deck1.clear()
	print("\nCleared the deck.")

	print("Deck:", deck1)