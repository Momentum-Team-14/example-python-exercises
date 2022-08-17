# 52 cards in a deck, 2 - 10, J, Q, K, A of each suit
# shuffle the deck
# dealer gives two cards to each player, including themself
# each player asks for more cards (hit) one at a time
# dealer gets additional cards according to this rule:
# - if their hand is less than 17, they have to hit
# points are assigned:
# numbers - face value, face cards - 10, aces - 1 or 11
# you win by getting 21, everyone else busts (over 21), or you
# have more than dealer

# what will our classes be?
# class names capitalized, singluar
# Dealer, Player, Card, Deck, Chip, Hand, Game, Suit

''' 
Class Hierarchy
Game
    - Player, Dealer, Deck
        - Card
            - Suit
            - Rank
'''
import random

SUITS = {
    'laughs': '🤣',
    'prides': '🏳️‍🌈',
    'fires': '🔥',
    'bears': '🧸',
    }

FACECARD_RANKS = {
    'A': [1, 11],
    'J': 10,
    'Q': 10,
    'K': 10,
}


class Suit():
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name

    def __str__(self):
        return self.name


class Rank():
    def __init__(self, rank, points):
        self.rank = rank
        self.points = points

    def __str__(self):
        return f'{self.rank}'


class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit.symbol}'


class Deck():
    def __init__(self, brand=""):
        self.suits = [Suit(symbol, name) for name, symbol in SUITS.items()]
        self.ranks = [Rank(number, number) for number in range(2, 11)]
        for rank, points in FACECARD_RANKS.items():
            self.ranks.append(Rank(rank, points))
        self.cards = [Card(rank, suit) for rank in self.ranks 
                      for suit in self.suits]
        self.brand = brand

    @property
    def get_number_of_cards_in_deck(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)


deck = Deck(brand="Bicycle")
deck.shuffle()
print(f'This deck has {deck.get_number_of_cards_in_deck} cards.')
for card in deck.cards:
    print(card)
