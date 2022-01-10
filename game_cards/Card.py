class Card:
    def __init__(self, value, suit):
        """function gets int value between 1-13 and int suit between 1-4 and creates new card"""
        if type(value) != int:
            raise TypeError("value must be int!")
        if type(suit) != int:
            raise TypeError("value must be int!")
        if value < 1 or value > 13:
            raise ValueError("value must be 1-13!")
        if suit < 1 or suit > 4:
            raise ValueError("suit must be 1-4!")
        self.value = value
        self.suit = suit

    # function prints the card
    def __repr__(self):
        value = self.value
        if value == 1:
            value = "ace"
        elif value == 11:
            value = "jack"
        elif value == 12:
            value = "queen"
        elif value == 13:
            value = "king"

        suit = self.suit
        if suit == 1:
            suit = 'Diamond'
        elif suit == 2:
            suit = 'Spade'
        elif suit == 3:
            suit = 'Heart'
        elif suit == 4:
            suit = 'Club'

        return "{} of {}".format(value, suit)

    def __eq__(self, other):
        if self.value == other.value and self.suit == other.suit:
            return True
        else:
            return False

    def __gt__(self, other):
        """function gets card and compares it to self card, if self is higher, it returns True, else, it returns
        False """
        if type(other) != Card:
            raise TypeError("only a card can be compared!")
        # if self value is 1 and the other value is not 1, then self is higher, returns True
        if self.value == 1 and other.value != 1:
            return True
        # if other value is 1 and the self value is not 1, then other is higher, returns False
        elif other.value == 1 and self.value != 1:
            return False
        # if both card's value is equal, compare them by its suit
        elif self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        #         compare both card's value
        elif self.value > other.value:
            return True
        else:
            return False


