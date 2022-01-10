from DeckOfCards import *
from Card import *
from Player import *


class CardGame:

    def __init__(self, player1, player2, num_of_cards=26):
        self.player1 = player1
        self.player2 = player2
        if num_of_cards > 26 or num_of_cards < 10:
            self.num_of_cards = 26
        else:
            self.num_of_cards = num_of_cards
        self.new_game()

    def new_game(self):
        deck = DeckOfCards()
        deck.cards_shuffle()
        for i in range(self.num_of_cards):
            self.player1.add_card(deck.deal_one())
            self.player2.add_card(deck.deal_one())

    def get_winner(self):
        if len(self.player1.all_cards) > len(self.player2.all_cards):
            return self.player1
        elif len(self.player1.all_cards) < len(self.player2.all_cards):
            return self.player2
        else:
            return None
