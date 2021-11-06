"""A simple game of Blackjack"""

import random

class Card():
    def __init__(self, value, suit) -> None:
        self.value = value
        self.suit = suit
        self.suit_symbol = {"Hearts": "♥", "Diamonds": "♦", "Spades": "♠", "Clubs": "♣"}[suit]
        self.name = f"{self.value} of {self.suit}"
        self.short_name = f"{self.value} of {self.suit_symbol}"


class CardsDeck():
    def __init__(self) -> None:
        self.values = {'King': 10, 'Queen': 10,'Jack': 10}
        self.cards = []
        self.generate()

    def generate(self) -> None:
        """Generates the deck of cards for this class (Each card in the list 'self.cards' is a 'Card' class object)"""

        card_values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'King', 'Queen', 'Jack']
        card_suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        
        for s in card_suits:
            for v in card_values:
                self.cards.append(Card(v, s))
        
        self.shuffle()

    def shuffle(self) -> None:
        """'shuffle()' is only here because it would look cleaner than 'random.shuffle()'"""

        random.shuffle(self.cards)
    
    @property
    def card_short_names(self) -> list:
        return [card.short_name for card in self.cards]

def main():
    playing = True
    while playing:
        deck = CardsDeck()
        print(*deck.card_short_names, sep='\n')
        playing = input_getter("Would you like to play again?", ['yes', 'y'])


def input_getter(s: str, options: list):
    temp = input(s)
    return temp.lower() in options


if __name__ == "__main__":
    main()
