from unittest import TestCase

from game_cards.Card import Card


class TestCard(TestCase):
    def setUp(self):
        self.c1 = Card(13, 1)
        self.c2 = Card(1, 4)

    # test a valid case of init
    def test__init__valid(self):
        self.assertEqual(self.c1.value, 13)
        self.assertEqual(self.c2.value, 1)
        self.assertEqual(self.c1.suit, 1)
        self.assertEqual(self.c2.suit, 4)

    # test invalid case of value
    def test__init__invalid_value(self):
        with self.assertRaises(ValueError):
            Card(0, 1)
        with self.assertRaises(ValueError):
            Card(14, 1)
        with self.assertRaises(ValueError):
            Card(1, 0)
        with self.assertRaises(ValueError):
            Card(1, 5)

    # test invalid case of type
    def test__init__invalid_type(self):
        with self.assertRaises(TypeError):
            Card('aaa', 1)
        with self.assertRaises(TypeError):
            Card(True, 1)
        with self.assertRaises(TypeError):
            Card(1, 'aaa')
        with self.assertRaises(TypeError):
            Card(1, False)

    def test__gt__valid(self):
        c3 = Card(13, 2)
        c4 = Card(1, 1)
        self.assertTrue(self.c2 > self.c1)
        self.assertTrue(c3 > self.c1)
        self.assertTrue(self.c2 > c4)
        self.assertTrue(c4 > c3)

    def test__gt__invalid(self):
        with self.assertRaises(TypeError):
            self.c1 > 2
        with self.assertRaises(TypeError):
            self.c1 > 'aa'
        with self.assertRaises(TypeError):
            self.c1 > True

