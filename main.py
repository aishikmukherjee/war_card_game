"""This module handles the logic of the war game"""
from cpu_players import cpu_1, cpu_2

def war(card1 , card2, stacked_cards):
    """Handles war situation when card values match"""
    if len(cpu_1) < 4:
        print("Result: CPU 2 won")
        return False
    if len(cpu_2) < 4:
        print("Result: CPU 1 won")
        return False

    # Add current cards and extra cards for war
    stacked_cards.extend([card1, card2])
    stacked_cards.extend(cpu_1.give_three_cards())
    stacked_cards.extend(cpu_2.give_three_cards())

    # Draw one more card from each player
    card_1 = cpu_1.give_one_card()
    card_2 = cpu_2.give_one_card()

    if card_1.value > card_2.value:
        stacked_cards.extend([card_1, card_2])
        cpu_1.add_won_cards(stacked_cards)
        print("War result: Player 1 won")
        return True

    if card_1.value < card_2.value:
        stacked_cards.extend([card_1, card_2])
        cpu_2.add_won_cards(stacked_cards)
        print("War result: Player 2 won")
        return True

    # War continues if cards are equal again
    return war(card_1, card_2, stacked_cards)

# Game loop setup
ROUND_COUNTER = 0
GAME_IS_ON = True

while GAME_IS_ON:
    if ROUND_COUNTER > 10000:
        # Max rounds reached, determine winner by card count
        X = len(cpu_1)
        Y = len(cpu_2)
        if X > Y:
            print(f"Result: Player 1 won with maximum number of cards: {X}"
                  f" as the game completed 10000 rounds")
            break
        if X < Y:
            print(f"Result: Player 2 won with maximum number of cards: {Y}"
                  f" as the game completed 10000 rounds")
            break
        print(f"Result: It's a tie as the game completed 10000 rounds "
              f"and both the players have equal number of cards {X} == {Y}")
        break

    ROUND_COUNTER += 1
    print(f"\nRound no.{ROUND_COUNTER}: ")

    # Check if any player ran out of cards
    if len(cpu_1) == 0:
        print("Result: CPU 2 won")
        break
    if len(cpu_2) == 0:
        print("Result: CPU 1 won")
        break

    # Each player draws one card
    card_of_player_1 = cpu_1.give_one_card()
    card_of_player_2 = cpu_2.give_one_card()

    # Compare card values
    if card_of_player_1.value > card_of_player_2.value:
        cpu_1.add_won_cards([card_of_player_1, card_of_player_2])
    elif card_of_player_1.value < card_of_player_2.value:
        cpu_2.add_won_cards([card_of_player_1, card_of_player_2])
    else:
        print("WAR BEGINS")
        GAME_IS_ON = war(card_of_player_1, card_of_player_2, [])
