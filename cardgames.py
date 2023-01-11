import random

class Card:
    """
    Represents a standard playing card.
    Each Card has a suit and a rank.
    They are set during the creation/instantiation of the object.
    """

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']


    # this is the constructor method.

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "%s of %s" % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

class Deck:
    """
    A deck of playing cards.
    """

    def __init__(self):
        self.cards = []

        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def pop_card(self):
        return self.cards.pop()

    def __str__(self):
        temp = []
        for card in self.cards:
            temp.append(str(card))

        return "\n".join(temp)

    def deal_hand(self, hand, num_cards):
        for i in range(num_cards):
            hand.add_card(self.pop_card())

class Hand(Deck):
    """
    This represents a player.
    A player has a certain set of cards during play.
    """

    def __init__(self):
        self.cards = []

    def __str__(self):
        temp = []
        for card in self.cards:
            temp.append(str(card))

        return ",".join(temp)