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

if __name__ == "__main__":
	print("This is a module for playing cards.")
	input("\n\nPress the enter key to exit.")