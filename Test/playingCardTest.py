import unittest

from playingCards import Card


class playing_card_test(unittest.TestCase):
    def setUp(self):
        self.card = Card("T", "H", True)
        self.card1 = Card("T", "H", True)
        self.card2 = Card("N", "D", False)

    def test_get_rank(self):
        self.assertEqual(self.card.getRank(), "T")

    def test_get_suit(self):
        self.assertEqual(self.card.getSuit(), "H")

    def test_is_face_up(self):
        self.assertEqual(self.card.isFaceUp(), True)

    def test_turn_over(self):
        self.card.turnOver()
        self.assertEqual(self.card.isFaceUp(), False)

    def test_eq(self):
        self.assertTrue(self.card.__eq__(self.card1))
        self.assertFalse(self.card.__eq__(self.card2))

    def test_str(self):
        self.assertEqual(self.card.__str__(), "[ TH ]")
        self.assertEqual(self.card2.__str__(), "[ ]")

    if __name__ == '__main__':
        if __name__ == '__main__':
            unittest.main()
