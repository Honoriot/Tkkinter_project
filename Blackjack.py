import random

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return " of ".join((self.suit, self.value))


class Deck():
    def __init__(self):
        self.cards = [Card(s, v) for s in ("shapde", "heart", "club", "diamond")
                                for v in ("A", 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K")]

    def shuffle(self):
        if len(self.cards)>1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards):
            return self.cards.pop(0)

class Hands():
    def __init__(self, dealer = False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def card_add(self, card):
        self.cards.append(card)

        