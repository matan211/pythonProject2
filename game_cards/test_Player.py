from unittest import TestCase
from game_cards.Player import Player


class TestPlayer(TestCase):
    def setUp(self):
        self.player = Player('Yoav')

    # test valid case of init Player
    def test__init__valid(self):
        self.assertTrue(self.player.name == 'Yoav')
        self.assertTrue(self.player.num_of_cards == 26)
        self.assertTrue(self.player.all_cards == [])
        player2 = Player('Ran', 10)
        self.assertTrue(player2.name == 'Ran')
        self.assertTrue(player2.num_of_cards == 10)
        self.assertTrue(player2.all_cards == [])
        player3 = Player('')
        self.assertTrue(player3.name == '')

    #         test case of invalid value
    def test__init__invalid_value(self):
        with self.assertRaises(ValueError):
            Player('aaa', 27)
        with self.assertRaises(ValueError):
            Player('aaa', 9)

    #         test case of invalid type
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
        self.player.set_hand()
        self.assertEqual(len(self.player.all_cards), 26)


    def test_get_card(self):
        self.fail()

    def test_add_card(self):
        self.fail()
