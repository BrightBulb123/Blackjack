"""A simple game of Blackjack"""

import random

class Card():
    def __init__(self, value, suit) -> None:
        self.value = value
        self.int_value = self.int_value_assigner()
        self.suit = suit
        self.suit_symbol = {"Hearts": "♥", "Diamonds": "♦", "Spades": "♠", "Clubs": "♣"}[suit]
        self.name = f"{self.value} of {self.suit}"
        self.short_name = f"{self.value} of {self.suit_symbol}"
    
    def int_value_assigner(self):
        card_values = {'Ace': 1, 'King': 10, 'Queen': 10,'Jack': 10}
        if self.value in card_values:
            return card_values[self.value]
        else:
            return int(self.value)


class CardsDeck():
    def __init__(self) -> None:
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

def main() -> None:
    playing = True

    game_intro()

    turn = True
    # turn = True is the same as turn = "Player"

    while playing:
        deck = CardsDeck()

        playerHand = [deck.cards.pop(0), deck.cards.pop(1)]
        playerHandValue = value_calculator(playerHand)

        deck.shuffle()

        dealerHand = [deck.cards.pop(0), deck.cards.pop(1)]
        dealerHandValue = value_calculator(dealerHand[0])

        if turn:
            player_turn(playerHand, playerHandValue)
        
        playing = input("\nWould you like to play again?\n").lower() in ['yes', 'y']


def hand_printer(hand: list) -> str:
    return ', '.join(str(card.short_name) for card in hand)


def value_calculator(hand: list) -> int:
    return sum(card.int_value for card in hand)


def game_intro():
    print('\n', "BLACKJACK".center(21, '='), '\n', sep='')


def player_turn(p_hand: list, p_value: int) -> None:
    print(f"Player's hand: {hand_printer(p_hand)}")
    print(f"Player's hand's value: {p_value}")


if __name__ == "__main__":
    main()
