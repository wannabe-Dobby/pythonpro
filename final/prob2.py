class Card:
	""" A playing card. """
	RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
	SUITS = ["c", "d", "h", "s"]

	def __init__(self, rank, suit, face_up = True):
		self.rank = rank
		self.suit = suit
		self.is_face_up = face_up
	
	def __str__(self):
		if self.is_face_up:
			reply = self.rank + self.suit
		else:
			reply = "XX"
		return reply
	
	def flip(self):
		self.is_face_up = not self.is_face_up

class Hand:
	""" A hand of playing cards. """
	def __init__(self):
		self.cards = []

	def __str__(self):
		if self.cards:  # self.card가 참일 때 (값이 존재하거나 비어있지 않은 상태) -> reply에 계속 더함
			reply = ""
			for card in self.cards:
				reply += str(card) + "\t"
		else:  # self.card가 거짓일 때 (값이 존재하지 않거나 비어있는 상태) -> reply에 <empty> 저장
			reply = "<empty>"
		return reply
	
	def clear(self):
		self.cards = []  # 카드 초기화
	
	def add(self, card):
		self.cards.append(card)  # 기존 카드에 카드 삽입

	def give(self, card, other_hand):
		self.cards.remove(card)  # 내 카드에서 카드 제거
		other_hand.add(card)  # 다른 사람 카드에 카드 삽입

class Deck(Hand):
	"""" A deck of playing cards. """
	def populate(self):
		for suit in Card.SUITS:
			for rank in Card.RANKS:
				self.add(Card(rank, suit)) # 덱에 카드 추가
	
	def shuffle(self):
		import random
		random.shuffle(self.cards)  # 카드 섞기
	
	def deal(self, hands, per_hand = 1):
		for rounds in range(per_hand):
			for hand in hands:  # 리스트 hands 안에 있는 hand들(my_hand, your_hand)
				if self.cards:  # self.card가 참일 때 (값이 존재하거나 비어있지 않은 상태) -> top_card에 첫 번째 카드 대입
					top_card = self.cards[0]
					self.give(top_card, hand)  # 상대에게 그 카드를 줌
				else:  # self.card가 거짓일 때 (값이 존재하지 않거나 비어있는 상태) -> Out of cards! 출력
					print("Out of cards!")

######################################################################################

class Player:
	""" A player for a game. """
	def __init__(self,  name, score = 0):
		self.name = name
		self.score = score

	def __str__(self):
		reply = self.name + ":\t" + str(self.score)
		return reply
	
def ask_yes_no(question):
	""" Ask a yes or no question. """
	response = None
	while response not in ("y", "n"):
		response = input(question).lower()
	return response

def ask_number(question, low, high):
	""" Ask for a number within a range.  """
	response = None
	while response not in range(low, high):
		response = int(input(question))
	return response

######################################################################################

class Positionable_Card(Card):
	""" A Blackjack Card. """
	ACE_VALUE = 1

	@property
	def value(self):
		if self.is_face_up:
			v = Positionable_Card .RANKS.index(self.rank) + 1
			if v > 10:
				v = 10
			return v

class BJ_Deck(Deck):
	""" A Blackjack Deck. """
	def populate(self):
		for suit in Positionable_Card.SUITS:
			for rank in Positionable_Card.RANKS:
				self.cards.append(Positionable_Card(rank, suit))
	
	def shuffle(self):
		import random
		random.shuffle(self.cards)  # 카드 섞기
	
	def deal(self, hands, per_hand = 1):
		for rounds in range(per_hand):
			for hand in hands:  # 리스트 hands 안에 있는 hand들(my_hand, your_hand)
				if self.cards:  # self.card가 참일 때 (값이 존재하거나 비어있지 않은 상태) -> top_card에 첫 번째 카드 대입
					top_card = self.cards[0]
					self.give(top_card, hand)  # 상대에게 그 카드를 줌
				else:  # self.card가 거짓일 때 (값이 존재하지 않거나 비어있는 상태) -> Out of cards! 출력
					print("Out of cards!")

class BJ_Hand(Hand):
	""" A Blackjack Hand. """
	def __init__(self, name):
		super(BJ_Hand, self).__init__()
		self.name = name
	
	def __str__(self):
		reply = self.name + ":\t" + super().__str__()
		if self.total:
			reply += "(" + str(self.total) + ")"
		return reply
	
	@property
	def total(self):
		# if a card in the hand = None, then total = None
		for card in self.cards:
			if not card.value:
				return 0
		t = 0  # add up card values, treat each Ace as 1
		for card in self.cards:
			t += card.value

		# determine if hand contains an Ace
		contains_ace = False
		for card in self.cards:
			if card.value == Positionable_Card.ACE_VALUE:
				contains_ace = True
		
		# if total is low, treat Ace = 11
		if contains_ace and t <= 11:
			t += 10  # add only 10 since we add 1 to Ace
		return t
	
	def is_busted(self):
		return self.total is not None and self.total > 21

class BJ_Player(BJ_Hand):
	def is_hitting(self):
		response = ask_yes_no("\n" + self.name + ", do you want a hit? (Y/N): ")
		return response == "y"
	
	def bust(self):
		print(self.name, "busts.")
		self.lose()

	def lose(self):
		print(self.name, "loses.")

	def win(self):
		print(self.name, "wins.")

	def push(self):
		print("self.name", "pushes.")

class BJ_Dealer(BJ_Hand):
	""" A Blackjack Dealer. """
	def is_hitting(self):
		return self.total is not None and self.total < 17
	
	def bust(self):
		print(self.name, "busts.")

	def flip_first_card(self):
		if self.cards:
			first_card = self.cards[0]
			first_card.flip()

class BJ_Game:
	""" A Blackjack Game """
	def __init__(self, names):
		self.players = []
		for name in names:
			player = BJ_Player(name)
			self.players.append(player)

			self.dealer = BJ_Dealer("Dealer")

			self.deck = BJ_Deck()
			self.deck.populate()
			self.deck.shuffle()

	def still_playing(self):
		sp = []
		for player in self.players:
			if not player.is_busted():
				sp.append(player)
		return sp
	
	def __additional_cards(self, player):
		while not player.is_busted() and player.is_hitting():
			self.deck.deal([player])
			print(player)
			if player.is_busted():
				player.bust()
	
	def play(self):
		# deal inital 2 cardsd to everyone
		self.deck.deal(self.players + [self.dealer], per_hand = 2)
		self.dealer.flip_first_card()  # hide dealer 1st card
		for player in self.players:
			print(player)
		print(self.dealer)

		# deal additional cards to players
		for player in self.players:
			self.__additional_cards(player)
		
		self.dealer.flip_first_card()  # reveal dealer's first

		if not self.still_playing:
			# All players have busted, show the dealer's
			print(self.dealer)
		else:
			print(self.dealer)  # deal extra cards to dealer
			self.__additional_cards(self.dealer)
			if self.dealer.is_busted():
				# everyone still playing wins
				for player in self.still_playing():
					player.win()
			else:
				# compare the player still playing to dealer
				for player in self.still_playing():
					if player.total > self.dealer.total:
						player.win()
					elif player.total < self.dealer.total:
						player.lose()
					else:
						player.push()

			# remove everyone's cards
			for player in self.players:
				player.clear()
			self.dealer.clear()

def main():
	print("\t\tWelcome to Blackjack!\n")

	names = []
	number = ask_number("How many players?,\“ (1 - 7): ", low = 1, high = 8)
	
	for i in range(number):
		name = input("Enter player name: ")
		names.append(name)
	print()

	game = BJ_Game(names)

	again = None
	while again != "n":
		game.play()
		again = ask_yes_no("\nWant to play again?:")

if __name__ == "__main__":
	main()