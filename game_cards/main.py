from game_cards.Card import Card
from game_cards.DeckOfCards import DeckOfCards
from game_cards.Player import Player
# name1 = input("enter player name: ")
# name2 = input("enter player name: ")
player1 = Player('Matan')
player2 = Player('Daniel')
deck = DeckOfCards()
player1.set_hand(deck)
player2.set_hand(deck)
print(player1)
print(player2)
