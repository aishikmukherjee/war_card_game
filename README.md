# war_card_game

WAR CARD GAME - Python Project
==============================

Created by: Aishik Mukherjee

Description:
------------
This is a console-based simulation of the classic War card game using Python.
Two CPU players compete using a standard 52-card deck. The game continues
until one player runs out of cards or the round limit (10,000) is reached.

Files:
------
1. cards_and_deck.py
   - Contains the Cards and Deck classes.
   - Handles creation and shuffling of the deck.

2. cpu_players.py
   - Defines the Player class.
   - Creates two CPU player instances (cpu_1 and cpu_2) and distributes cards.

3. main.py (or the file where game logic runs)
   - Contains the main game loop.
   - Compares cards, manages war scenarios, and declares the winner.

How to Run:
-----------
1. Make sure all three `.py` files are in the same directory.
2. Run the main game logic file (not the modules).
   Example: `python main.py`

Rules Summary:
--------------
- Each CPU player draws the top card.
- The player with the higher card value wins both cards.
- If there's a tie, a "war" begins:
  - Each player places 3 cards face down and 1 card face up.
  - The face-up cards are compared.
  - Winner takes all cards involved.
- Game ends when:
  - A player runs out of cards.
  - 10,000 rounds have been completed (winner is player with more cards).

Notes:
------
- Suits do not affect gameplay.
- Card values: 2 (lowest) to Ace (highest).
- Debugging outputs are printed for card distribution and war rounds.

Enjoy the game!
