import queue
import random


class Card:
    def __init__(self, rank, suit, faceUp):
        self.rank = rank
        self.suit = suit
        self.faceUp = faceUp

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def isFaceUp(self):
        if self.faceUp:
            return True
        else:
            return False

    def turnOver(self):
        if self.faceUp:
            self.faceUp = False
        else:
            self.faceUp = True

    def __eq__(self, other):
        if self.getRank() is other.getRank() and self.getSuit() is other.getSuit():
            return True
        else:
            return False

    def __str__(self):
        if self.faceUp:
            return "[ %s%s ]" % (self.rank, self.suit)
        else:
            return "[ ]"


class Deck:
    def __init__(self):
        self.queue = queue.Queue(52)

    def addCard(self, card):
        if isinstance(card, Card):
            if self.queue.full():
                print("Cannot add ", card.__str__(), " :deck is full")
            else:
                self.queue.put(card)

    def dealCard(self):
        if self.queue.empty():
            print("Cannot deal card from empty deck")
        else:
            card = self.queue.get()
            if not card.isFaceUp():
                card.turnOver()
            return card

    def deckSize(self):
        return self.queue.qsize()

    def isComplete(self):
        if self.queue.full():
            return True
        else:
            return False

    def resatDeck(self):
        cards = []
        for i in range(52):
            cards.append(self.dealCard())
        random.shuffle(cards)
        for i in range(52):
            self.addCard(cards[i])

    def __str__(self):
        strDeck = ""
        for i in range(self.queue.qsize() - 1):
            card = self.queue.get()
            if not card.isFaceUp():
                card.turnOver()
            strDeck = strDeck + card.__str__()
            strDeck = strDeck + ","
        card = self.queue.get()
        if not card.isFaceUp():
            card.turnOver()
        strDeck = strDeck + card.__str__()
        return strDeck
