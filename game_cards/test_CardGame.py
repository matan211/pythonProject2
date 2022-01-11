from unittest import TestCase
from game_cards.CardGame import CardGame


class TestCardGame(TestCase):
    def setUp(self):
        self.card_game = CardGame('Daniel', 'Matan')
        self.card_game2 = CardGame('Yoav', 'Ran', 2)
        self.card_game3 = CardGame('Daniel', 'Yoav', 10)
        self.card_game4 = CardGame('Matan', 'Yossi', 27)

    # test case valid init
    def test__init__valid(self):
        self.assertTrue(self.card_game.player1.name == 'Daniel')
        self.assertTrue(self.card_game.player2.name == 'Matan')
        self.assertEqual(self.card_game3.num_of_cards, 10)

    # test case invalid init
    def test__init__invalid(self):
        self.assertEqual(self.card_game2.num_of_cards, 26)
        self.assertEqual(self.card_game4.num_of_cards, 26)

    def test_new_game(self):
        self.assertEqual(len(self.card_game.player1.all_cards), len(self.card_game.player2.all_cards))
        self.assertEqual(len(self.card_game.player1.all_cards), 26)
        self.assertEqual(len(self.card_game3.player1.all_cards), len(self.card_game3.player2.all_cards))
        self.assertEqual(len(self.card_game3.player1.all_cards), 10)

    def test_get_winner(self):
        # test case of tie
        winner = self.card_game.get_winner()
        self.assertTrue(winner is None)
        # test case of player2 with more cards
        card = self.card_game.player1.all_cards.pop()
        winner = self.card_game.get_winner()
        self.assertTrue(winner is self.card_game.player2)
        # test case of player1 with more cards
        self.card_game.player2.all_cards.pop()
        self.card_game.player1.add_card(card)
        winner = self.card_game.get_winner()
        self.assertTrue(winner is self.card_game.player1)

