"""Creating CPU players in this module"""
# Imports shuffle to randomize cards
from random import shuffle

from cards_and_deck import Deck

# Creates a deck instance
dealer = Deck()

class Player:
    """Player class"""
    def __init__(self, cards):
        """Initializes player with shuffled cards"""
        self.cards = []
        self.cards.extend(cards)
        shuffle(self.cards)

    def give_one_card(self):
        """Returns and removes the top card"""
        return self.cards.pop(0)

    def give_three_cards(self):
        """Returns and removes top 3 cards"""
        card_holder = []
        for _ in range(3):
            card_holder.append(self.cards.pop(0))
        return card_holder

    def add_won_cards(self, cards):
        """Adds won cards to the player's deck"""
        self.cards.extend(cards)

    def show_cards(self):
        """Prints all cards the player holds (for debugging)"""
        for cards in self.cards:
            print(f"Card: {cards}; value: {cards.value}")

    def __len__(self):
        """Returns number of cards the player holds"""
        return len(self.cards)

# Creates player instances with half the deck each
cpu_1 = Player(dealer.distribute_card_set_1())
cpu_2 = Player(dealer.distribute_card_set_2())

if __name__ == "__main__":
    # Only runs when executed directly
    print("This file acts as a resource for the war game created by Aishik Mukherjee")
    print("Run the main.py file, not this")
