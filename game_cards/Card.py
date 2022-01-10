class Card:
    def __init__(self, value, suit):
        if type(value) != int:
            raise TypeError
        if type(suit) != int:
            raise TypeError
