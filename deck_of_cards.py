

import math
from random import seed
from random import randint

class Deck:
    def __init__(self, name):
        self.name = name
        self.deck = []
    
    def splitDeck(self):
        firstHalf = []
        secondHalf = []
        for i in range(0, math.floor(len(self.deck)/2)):
            firstHalf.append(self.deck[i])
        for j in range(math.floor(len(self.deck)/2), len(self.deck)):
            secondHalf.append(self.deck[j])
        return firstHalf, secondHalf

    def zipperShuffle(self): #right left zipper shuffle
        firstHalf = self.splitDeck()[0]
        secondHalf = self.splitDeck()[1]
        deck = []
        for i in range(0, len(firstHalf)):
            deck.append(secondHalf[i])
            deck.append(firstHalf[i])
        if len(self.deck)%2 != 0:
            deck.append(secondHalf[len(secondHalf)-1])
        self.deck = deck

    def addCard(self, cardSuit, cardTitle):
        card = Card(cardSuit, cardTitle)
        self.deck.append(card)

    def printCards(self):
        for i in range(0, len(self.deck)):
            print(self.deck[i].getCard())

    def getCards(self):
        deck = []
        for i in range(0, len(self.deck)):
            deck.append(self.deck[i].getCard())
        return deck

    def newDeck(self):
        if self.deck == []:
            for i in range(0,3):
                suitDict = {0 : "Diamonds",
                            1 : "Hearts",
                            2 : "Clubs",
                            3 : "Spades"}
                cardSuit = suitDict[i]
                for j in range(2, 15):
                    titleDict = {11 : "Jack",
                                    12 : "Queen",
                                    13 : "King",
                                    14 : "Ace"}
                    if j > 10:
                        cardTitle = titleDict[j]
                        self.deck.append(Card(cardTitle, cardSuit))
                    else:
                        cardTitle = str(j)
                        self.deck.append(Card(cardTitle, cardSuit))
        else: 
            self.deck = []
            self.newDeck()

    def shuffle(self): #a not really random shuffle, but a good attempt at making something that resembles random.
        seed = 1
        cards = []
        for i in range(0, randint(0,10)):
            for j in range(0, randint(0,15)):
                self.zipperShuffle()
                cards.append(self.deck.pop())
        for k in range(0, len(cards)):
            self.deck.append(cards[k])

    



        


class Card:
    def __init__(self, cardSuit , cardTitle):
        self.cardSuit = cardSuit
        self.cardTitle = cardTitle

    def setSuit(self, cardSuit):
        self.cardSuit = cardSuit

    def setTitle(self, cardTitle):
        self.cardTitle = cardTitle

    def getCard(self):
        return self.cardSuit + " of " + self.cardTitle

def main():
    deck1 = Deck("Spalding")
    deck1.addCard("Ace", "Spades")
    deck1.addCard("2", "Clubs")
    deck1.addCard("3", "Diamonds")
    deck1.addCard("4", "Hearts")
    deck1.addCard("5", "Spades")
    deck1.addCard("6", "Clubs")

    deck1.printCards()
    print('\n')
    deck1.zipperShuffle()
    deck1.printCards()
    print("\n")
    print(deck1.getCards())

    deck1.newDeck()
    deck1.printCards()
    print('\n')

    deck1.shuffle()
    deck1.printCards()
    
main()

