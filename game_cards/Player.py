from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card
from random import randint


class Player:
    def __init__(self, name, num_of_cards=26):
        # function creates new player with name type String and number of cards type int
        if type(name) != str:
            raise TypeError("player name must be String!")
        if type(num_of_cards) != int:
            raise TypeError("number of cards must be int!")
        if num_of_cards > 26 or num_of_cards < 10:
            raise ValueError("number of cards must be between 10-26!")
        self.name = name
        self.num_of_cards = num_of_cards
        self.all_cards = []

    def __str__(self):
        return f"player name: {self.name}, number of cards: {self.num_of_cards}, player's hand: {self.all_cards}"

    # set the card list of the player
    def set_hand(self, deck):
        if type(deck) != DeckOfCards:
            raise TypeError
        for i in range(self.num_of_cards):
            card = deck.deal_one()
            if card not in self.all_cards:
                self.all_cards.append(card)

    # function returns random card from player's hand
    def get_card(self):
        location = randint(0, len(self.all_cards) - 1)
        card = self.all_cards[location]
        return card

    # function adds card to player's hand
    def add_card(self, card):
        if type(card) != Card:
            raise TypeError
        if card not in self.all_cards:
            self.all_cards.append(card)
