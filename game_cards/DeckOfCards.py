from random import shuffle, randint
from game_cards.Card import Card


class DeckOfCards:

    def __init__(self):
        self.stack = []
        suits = [1, 2, 3, 4]
        for suit in suits:
            for rank in range(1, 14):
                self.stack.append(Card(rank, suit))

    def cards_shuffle(self):
        shuffle(self.stack)

    def deal_one(self):
        card = self.stack.pop()
        return card
