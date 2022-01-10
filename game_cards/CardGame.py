from Player import *


class CardGame:
    # function creates new game with 2 players
    # each player gets cards in hand
    def __init__(self, player1, player2, num_of_cards=26):
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        if num_of_cards > 26 or num_of_cards < 10:
            self.num_of_cards = 26
        else:
            self.num_of_cards = num_of_cards
        self.new_game()

    # function gives cards to each player
    def new_game(self):
        deck = DeckOfCards()
        deck.cards_shuffle()
        for i in range(self.num_of_cards):
            c1 = deck.deal_one()
            c2 = deck.deal_one()
            self.player1.add_card(c1)
            self.player2.add_card(c2)

    # function returns the winner player of the game
    # winner is the player with most cards
    # if equal, function returns None
    def get_winner(self):
        if len(self.player1.all_cards) > len(self.player2.all_cards):
            return self.player1
        elif len(self.player1.all_cards) < len(self.player2.all_cards):
            return self.player2
        else:
            return None
