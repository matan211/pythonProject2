from random import shuffle

class DeckOfCards:

    def __init__(self):
        self.stack=[]
        suits = ["clubs", "diamonds", "hearts", "spades"]
        for suit in suits:
            for rank in range(1, 14):
                self.stack.append(card(suit, rank))


    def cards_shuffle(self):
        shuffle(self.stack)


    def deal_one(self):
        return self.stack.pop()  # we want the last card from deck


