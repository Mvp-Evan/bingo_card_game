from playingCards import Deck, Card


class Bingo:
    def __init__(self):
        self.grid = []
        self.playMode = "L"

    def populate(self, cards, playMode):
        position = 0
        for i in range(25):
            if i % 5 == 0:
                self.grid.append([])
                position = int(i / 5)
            if i == 12:
                cards[i].turnOver()
            self.grid[position].append(cards[i])
        self.playMode = playMode

    def search(self, card, rankOnly):
        if rankOnly:
            for i in range(5):
                for j in range(5):
                    if self.grid[i][j].getRank() == card.getRank() and self.grid[i][j].isFaceUp():
                        self.grid[i][j].turnOver()
        else:
            for i in range(5):
                for j in range(5):
                    if self.grid[i][j] == card and self.grid[i][j].isFaceUp():
                        self.grid[i][j].turnOver()

    def isBingo(self):
        is_bingo = False
        if self.playMode == "C":
            if not self.grid[0][0].isFaceUp():
                if not self.grid[0][4].isFaceUp():
                    if not self.grid[4][0].isFaceUp():
                        if not self.grid[4][4].isFaceUp():
                            is_bingo = True
        elif self.playMode == "F":
            judgement = True
            for i in range(5):
                for j in range(5):
                    if self.grid[i][j].isFaceUp():
                        judgement = False
            is_bingo = judgement
        elif self.playMode == "L":
            row_first = True
            row_last = True
            column_first = True
            column_last = True
            right_down = True
            left_down = True
            for i in range(5):
                if self.grid[0][i].isFaceUp():
                    row_first = False
                if self.grid[4][i].isFaceUp():
                    row_last = False
                if self.grid[i][0].isFaceUp():
                    column_first = False
                if self.grid[i][4].isFaceUp():
                    column_last = False
                if self.grid[i][i].isFaceUp():
                    left_down = False
                if self.grid[i][4-i].isFaceUp():
                    right_down = False
            if row_first or row_last or column_first or column_last or right_down or left_down:
                is_bingo = True
        return is_bingo

    def clear(self):
        cards = self.grid.pop()
        return cards

    def __str__(self):
        for i in range(5):
            for j in range(5):
                print(self.grid[i][j].__str__(), end='')
            print("\n")
        print("\n")

class Table:
    def __init__(self):
        self.mode = ""
        self.playerA = Bingo()
        self.playerB = Bingo()
        self.bingo_card = Deck()
        self.callingCard = Deck()
        self.used_calling_card = Deck()
        self.unused_player_card = Deck()

    def populateDeck(self, deckNumber, filename):
        file = open(filename)
        if deckNumber == 0:
            for i in range(52):
                line = file.readline()
                card = Card(line[0], line[1], True)
                self.bingo_card.addCard(card)
        elif deckNumber == 1:
            for i in range(52):
                line = file.readline()
                card = Card(line[0], line[1], True)
                self.callingCard.addCard(card)
        file.close()

    def dealBingo(self, mode):
        self.mode = mode
        player_a = []
        player_b = []
        for i in range(25):
            player_a.append(self.bingo_card.dealCard())
        self.playerA.populate(player_a, mode)
        for i in range(25):
            player_b.append(self.bingo_card.dealCard())
        self.playerB.populate(player_b, mode)
        for i in range(2):
            self.unused_player_card.addCard(self.bingo_card.dealCard())

    def displayTable(self):
        print("Player A: ")
        self.playerA.__str__()
        print("Player B: ")
        self.playerB.__str__()

    def callCard(self):
        card = self.callingCard.dealCard()
        self.used_calling_card.addCard(card)
        return card

    def updateTable(self, rankOnly):
        card = self.callCard()
        self.playerA.search(card, rankOnly)
        self.playerB.search(card, rankOnly)
        #self.displayTable()
        return card

    def clearTable(self):
        for i in range(5):
            cardsA = self.playerA.clear()
            cardsB = self.playerB.clear()
            for j in cardsA:
                self.unused_player_card.addCard(j)
            for k in cardsB:
                self.unused_player_card.addCard(k)
        for i in range(self.callingCard.deckSize()):
            self.used_calling_card.addCard(self.callingCard.dealCard())

    def resetTable(self):
        self.used_calling_card.resatDeck()
        self.callingCard = self.used_calling_card
        for i in range(52):
            self.used_calling_card.dealCard()
        self.unused_player_card.resatDeck()
        self.bingo_card = self.unused_player_card
        self.dealBingo(self.mode)

    def isWinner(self):
        if self.playerA.isBingo() or self.playerB.isBingo():
            return True
        else:
            return False

    def whoWon(self):
        if self.playerA.isBingo() and self.playerB.isBingo():
            return "Tie"
        else:
            if self.playerA.isBingo():
                return "Player A won!"
            elif self.playerB.isBingo():
                return "Player B won!"



