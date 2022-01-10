from random import shuffle

class DeckOfCards:
    def __init__(self):
        self.stuck=[]
        suits = ["clubs", "diamonds", "hearts", "spades"]
        for suit in suits:
            for rank in range(1, 14):
                self.stack.append(card(suit, rank))


    def cards_shuffle(self):
        for i in range(0, 1):
            shuffle(self.stack)
