from random import shuffle


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def suit(self):
        return self.suit

    def value(self):
        return self.value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ['A', '2', '3', '4', '5', '6',
                  '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        removing = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-removing:]
        self.cards = self.cards[:-removing]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self

    def peek(self):
        return self.cards[-1]

    def print_deck(self):
        for card in self.cards:
            print(card)

    def add_card(self, card):
        if len(self.cards) < 52:
            self.cards.append(card)
        else:
            print("Deck is full")
