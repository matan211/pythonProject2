from unittest import TestCase

from game_cards.Card import Card
from game_cards.DeckOfCards import DeckOfCards


class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck = DeckOfCards()

    # test init of DeckOfCards
    # checks that deck has all cards from combination of value and suit
    def test__init__(self):
        for i in range(4):
            for j in range(13):
                self.assertTrue(self.deck.stack[i * 13 + j].value == j + 1)
                self.assertTrue(self.deck.stack[i * 13 + j].suit == i + 1)

    def test_cards_shuffle(self):
        self.deck.cards_shuffle()
        for i in range(1, 5):
            for j in range(1, 14):
                card = Card(j, i)
                self.assertIn(card, self.deck.stack)

    # checks card is removed from deck
    def test_deal_one(self):
        card = self.deck.deal_one()
        print(card)
        self.assertNotIn(card, self.deck.stack)
