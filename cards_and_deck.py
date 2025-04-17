"""This module deals with the cards and deck"""
# Imports shuffle to randomize deck
from random import shuffle

class Cards:
    """Single card class"""
    def __init__(self, suit, rank, value):
        """Initializes card with suit, rank, and value"""
        self.suit = suit
        self.rank = rank
        self.value = value

    def help(self):
        """Prints the card"""
        print(self)

    def __str__(self):
        """Returns card as string"""
        return f"{self.rank} of {self.suit}"

    def __len__(self):
        """Always returns 1 (single card)"""
        return 1

class Deck:
    """Deck of 52 cards"""
    def __init__(self):
        """Creates and shuffles the deck"""
        self.all_cards = []
        for suit in ["Shades", "Hearts", "Diamonds", "Clubs"]:
            value = 1
            for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10',
                         'Jack', 'Queen', 'King', 'Ace']:
                self.all_cards.append(Cards(suit,rank, value))
                value += 1
        shuffle(self.all_cards)

    def show_all_cards(self):
        """Prints all cards (for debugging)"""
        print("\nAll cards:")
        for x in self.all_cards:
            print(f"Card: {x}; value: {x.value}")
            if x.value == 13:
                print()

    def distribute_card_set_1(self):
        """Returns first 26 cards"""
        return self.all_cards[:26]

    def distribute_card_set_2(self):
        """Returns last 26 cards"""
        return self.all_cards[26:]

    def __str__(self):
        """Returns description of deck"""
        return ("This is a full deck of cards. It does not include Jocker card."
                "\nAvailable suits are: Shades, Hearts, Diamonds, Clubs")

    def __len__(self):
        """Returns number of cards in deck"""
        return len(self.all_cards)


if __name__ == "__main__":
    # Only runs when executed directly
    print("This file acts as a resource for the war game created by Aishik Mukherjee")
    print("Run the main.py file, not this")
