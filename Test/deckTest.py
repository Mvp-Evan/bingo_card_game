import unittest

from playingCards import Deck, Card


class deck_test(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        for i in range(1, 10):
            for j in ("S", "H", "D", "C"):
                card = Card(str(i), j, True)
                self.deck.addCard(card)
        for i in ("T", "J", "Q", "K"):
            for j in ("S", "H", "D", "C"):
                card = Card(str(i), j, True)
                self.deck.addCard(card)

    def test_size_card(self):
        self.assertEqual(self.deck.deckSize(), 52)

    def test_add_more(self):
        card = Card("T", "H", True)
        self.deck.addCard(card)

    def test_deal_card(self):
        self.assertTrue(self.deck.isComplete())
        card = self.deck.dealCard()
        self.assertEqual(card.__str__(), "[ 1S ]")
        self.assertFalse(self.deck.isComplete())

    def test_resat(self):
        self.deck.resatDeck()
        print(self.deck.deckSize())
        print(self.deck.__str__())

    if __name__ == '__main__':
        unittest.main()