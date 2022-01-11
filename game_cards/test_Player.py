from unittest import TestCase

from game_cards.Card import Card
from game_cards.Player import Player
from game_cards.DeckOfCards import DeckOfCards


class TestPlayer(TestCase):
    def setUp(self):
        self.player = Player('Yoav')

    # test valid case of init Player
    def test__init__valid(self):
        self.assertTrue(self.player.name == 'Yoav')
        self.assertTrue(self.player.max_num_of_cards == 26)
        self.assertTrue(self.player.all_cards == [])
        player2 = Player('Ran', 10)
        self.assertTrue(player2.name == 'Ran')
        self.assertTrue(player2.max_num_of_cards == 10)
        self.assertTrue(player2.all_cards == [])
        player3 = Player('')
        self.assertTrue(player3.name == '')

    # test case of invalid value
    def test__init__invalid_value(self):
        with self.assertRaises(ValueError):
            Player('aaa', 27)
        with self.assertRaises(ValueError):
            Player('aaa', 9)

    # test case of invalid type
    def test__init__invalid_type(self):
        with self.assertRaises(TypeError):
            Player('aaa', 'aa')
        with self.assertRaises(TypeError):
            Player(13, 12)
        with self.assertRaises(TypeError):
            Player(True, 12)
        with self.assertRaises(TypeError):
            Player('aaa', True)

    def test_set_hand_valid(self):
        deck = DeckOfCards()
        self.player.set_hand(deck)
        self.assertEqual(len(self.player.all_cards), 26)
        card = self.player.get_card()
        # add card twice to player's hand
        # card has to appear only once in player's hand
        self.player.add_card(card)
        self.player.add_card(card)
        self.assertEqual(self.player.all_cards.count(card), 1)

    # test case of invalid set hand
    def test_set_hand_invalid(self):
        with self.assertRaises(TypeError):
            self.player.set_hand(8)
        with self.assertRaises(TypeError):
            self.player.set_hand(True)
        with self.assertRaises(TypeError):
            self.player.set_hand('aaa')

    def test_get_card(self):
        deck = DeckOfCards()
        self.player.set_hand(deck)
        card = self.player.get_card()
        # card has to be removed from player's hand
        self.assertEqual(self.player.all_cards.count(card), 0)
        self.assertTrue(type(card) == Card)

    # test case of valid card
    def test_add_card_valid(self):
        deck = DeckOfCards()
        self.player.set_hand(deck)
        card = self.player.get_card()
        # card should be added to player's hand
        self.player.add_card(card)
        self.assertIn(card, self.player.all_cards)
        # card should not be added to player's hand
        self.player.add_card(card)
        self.assertEqual(self.player.all_cards.count(card), 1)

    # test case of invalid card
    def test_add_card_invalid(self):
        player2 = Player('Ran', 12)
        deck = DeckOfCards()
        player2.set_hand(deck)
        print(player2.all_cards)
        with self.assertRaises(TypeError):
            player2.add_card(12)
        with self.assertRaises(TypeError):
            player2.add_card('aaaa')
        with self.assertRaises(TypeError):
            player2.add_card(True)
