import unittest
from cardgames import Deck, Hand

class MyTestCase(unittest.TestCase):

    def test_something(self):
        # card1 = Card(1, 11)
        # card2 = Card(2, 1)

        # print(card1)
        # print(card2)

        mydeck = Deck()

        # print("The deck has %d cards " % (len(mydeck.cards),))
        mydeck.shuffle()
        # print(mydeck)

        player1 = Hand()
        player2 = Hand()

        mydeck.deal_hand(player1, 4)
        mydeck.deal_hand(player2, 4)

        self.assertEqual(4, len(player1.cards))
        self.assertEqual(4, len(player2.cards))

    def test_somethingelse(self):
        deck = Deck()

        self.assertEqual(101, len(deck.cards))


if __name__ == '__main__':
    unittest.main()
