from random import choice

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
	ranks = [str(n) for n in range(2, 11)] + list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		self._cards = [Card(rank, suit) for suit in self.suits
						for rank in self.ranks]

	def __len__(self):
		return len(self._cards)

	def __getitem__(self, position):
		return self._cards[position]

def print_random_card(deck):
	print('Random card: ', choice(deck))

def print_only_ases(deck):
	only_ases = deck[12::13]
	print('Only ases: ', only_ases)

def print_all_cards(deck):
	for card in deck:
		print(card)

def sort_cards_by_rank(deck):
	print('##### Print sorted cards ######')
	for card in sorted(deck, key=get_spades_high):
		print(card)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def get_spades_high(card):
	rank_value = FrenchDeck.ranks.index(card.rank)
	return rank_value * len(suit_values) + suit_values[card.suit]

if __name__ == '__main__':
	beer_card = Card('7', 'diamonds')
	print(beer_card)

	deck = FrenchDeck()
	print('Total of elements: %d' % len(deck))

	for index in range(1, 5):
		print_random_card(deck)

	print_only_ases(deck)
	print_all_cards(deck)
	sort_cards_by_rank(deck)
