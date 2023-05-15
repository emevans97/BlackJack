import random

CARDS = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10,'Jack','Queen','King']
SUITS = ['Diamonds', 'Hearts', 'Clubs', 'Spades']

class Deck():
    def __init__(self):
        self.deck = [[suit, card] for suit in SUITS for card in CARDS]
        # Higher or lower attribute of aces for scoring
        for card in self.deck:
            if 'Ace' in card:
                card.append('H')

    def get_card(self):
        card = random.choice(self.deck)
        pos = self.deck.index(card)
        self.deck.pop(pos)
        return card

    def twist(self):
        card = self.get_card()
        print(f"You have drawn a {card[1]} of {card[0]}\n")
        print("Your hand is:")
        return card
