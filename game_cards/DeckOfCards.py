from random import shuffle, randint
from game_cards.Card import Card


class DeckOfCards:

    # function creates deck of card
    # deck has 52 cards from 1-13 values and Diamond, Spade, Heart and Club suits
    def __init__(self):
        self.stack = []
        suits = [1, 2, 3, 4]
        for suit in suits:
            for rank in range(1, 14):
                self.stack.append(Card(rank, suit))

    # function shuffles the deck
    # returns nothing
    def cards_shuffle(self):
        shuffle(self.stack)

    # function returns random card from the deck
    # the card is removed from the deck
    def deal_one(self):
        card = self.stack.pop()
        return card
