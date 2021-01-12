import unittest

from bingo import Bingo, Table
from playingCards import Card


class bingo_test(unittest.TestCase):
    def setUp(self):
        file = open('../callingDeck_corners_Bwins.txt')
        self.cards = []
        for i in range(50):
            line = file.readline()
            card = Card(line[0], line[1], True)
            self.cards.append(card)
        file.close()
        self.bingo = Bingo()
        self.bingo.populate(self.cards, "C")

    def test_search(self):
        self.bingo.__str__()
        card = Card("J", "H", True)
        self.bingo.search(card, False)
        self.bingo.__str__()

    def test_is_bingo(self):
        self.bingo.__str__()
        card1 = Card("J", "H", True)
        card2 = Card("2", "S", True)
        card3 = Card("8", "S", True)
        card4 = Card("2", "D", True)
        self.bingo.search(card1, False)
        self.bingo.search(card2, False)
        self.bingo.search(card3, False)
        self.bingo.search(card4, False)
        self.bingo.__str__()
        self.assertTrue(self.bingo.isBingo())

    def test_clear(self):
        cards = self.bingo.clear()
        for i in cards:
            print(i.__str__())

    if __name__ == '__main__':
        unittest.main()

class table_test(unittest.TestCase):
    def setUp(self):
        filename = "../bingoDeck.txt"
        self.table = Table()
        self.table.populateDeck(1, filename)
        filename = "../callingDeck_line_Awins.txt"
        self.table.populateDeck(0, filename)

    def test_dealBingo(self):
        self.table.dealBingo("L")
        self.table.displayTable()

    def test_call_card(self):
        card = self.table.callCard()
        self.assertEqual(card.__str__(), "[ KS ]")

    def test_update_table(self):
        self.table.dealBingo("L")
        self.table.displayTable()
        self.table.updateTable(False)

    def test_clear_reset(self):
        self.table.dealBingo("L")
        self.table.displayTable()
        self.table.clearTable()
        self.table.resetTable()
        self.table.displayTable()

    if __name__ == '__main__':
        unittest.main()
