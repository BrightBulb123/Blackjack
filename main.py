"""A game of Blackjack (Ace = 1)"""

import random
from typing import Tuple

class Card():
    """The blueprint for creating a card"""

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
    """The blueprint for creating a deck of cards"""

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
    """For the purposes of __name__ == '__main__', this is the main function"""
    
    playing = True

    game_intro()

    while playing:
        turn = True  # 'turn = True' is the same as turn = "Player"

        deck = CardsDeck()

        playerHand = [deck.cards.pop(0), deck.cards.pop(1)]
        playerHandValue = value_calculator(playerHand)

        deck.shuffle()

        dealerHand = [deck.cards.pop(0), deck.cards.pop(1)]
        dealerHandValue = dealerHand[0].int_value

        while playerHandValue < 21 and dealerHandValue < 21:
            if turn:
                playerHand, playerHandValue, deck, turn = player_turn(playerHand, playerHandValue, deck, turn)
            else:
                dealerHand, dealerHandValue, deck, turn = dealer_turn(dealerHand, dealerHandValue, deck, turn, playerHandValue)

        win_checker(playerHandValue, dealerHandValue)

        playing = input("\nWould you like to play again?\n").lower() in ['yes', 'y']




def hand_printer(hand: list) -> str:
    """Returns a string for the short names of the cards in a hand"""

    return ', '.join(str(card.short_name) for card in hand)


def value_calculator(hand: list) -> int:
    """Returns the sum of the values of the cards in a hand"""

    return sum(card.int_value for card in hand)


def game_intro():
    """Just prints the title of the game (BLACKJACK)"""

    print('\n', "BLACKJACK".center(21, '='), '\n', sep='')


def player_turn(p_hand: list, p_value: int, d: CardsDeck, t: bool) -> Tuple:
    """Everything that happens in the player's turn"""

    print(f"\nPlayer's hand: {hand_printer(p_hand)}")
    print(f"Player's hand's value: {p_value}\n")

    choice = ''

    while choice != 'stand' and p_value < 21:
        choice = input("Would you like to:\n1.) Hit\n2.) Stand\n3.) Exit\n\nYour input: ").lower()

        d.shuffle()

        if choice == 'hit':
            p_hand.append(d.cards.pop(random.randint(0, len(d.cards)-1)))
        elif choice == 'stand':
            t = False
        elif choice == 'exit':
            exit()
        else:
            print("\nPlease enter 'hit', 'stand', or 'exit' (without the quotation marks)...\n")
            continue

        print(f"\nPlayer's hand: {hand_printer(p_hand)}")
        p_value = value_calculator(p_hand)
        print(f"Player's hand's value: {p_value}\n")

    t = False  # Switches the value of 't' to go to dealer's turn

    return p_hand, p_value, d, t


def dealer_turn(d_hand: list, d_value: int, d: CardsDeck, t: bool, p_value: int) -> Tuple:

    d.shuffle()
    
    while d_value < 21 and d_value < p_value:
        d_hand.append(d.cards.pop(random.randint(0, len(d.cards)-1)))
        
        print(f"\nDealer's hand: {hand_printer(d_hand)}")
        d_value = value_calculator(d_hand)
        print(f"Dealer's hand's value: {d_value}\n")
    
    t = True

    return d_hand, d_value, d, t


def win_checker(playerHandValue: list, dealerHandValue: list) -> None:
    playerWon = ((playerHandValue == 21 and playerHandValue > dealerHandValue) or dealerHandValue > 21)
    dealerWon = (dealerHandValue == 21 and dealerHandValue > playerHandValue) or playerHandValue > 21

    if playerWon:
        print("\nCongratulations! You won!\n")
    elif dealerWon:
        print("\nGood luck next time...\n")


if __name__ == "__main__":
    """Indicates this file is meant to be run as the main file, not imported"""
    
    main()
