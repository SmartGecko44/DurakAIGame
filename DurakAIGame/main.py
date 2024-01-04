import random
import time

from DurakAIGame import ai

from DurakAIGame import trump
from DurakAIGame import deck
from DurakAIGame import player
from DurakAIGame import turns
from DurakAIGame import initialize

if __name__ == '__main__':
    pass
else:
    print("This file is not supposed to be imported!")
    exit()

# Get the user's settings
num_players, cards_per_player, direction = initialize.get_user_settings(None, None, None)

# Create a deck
deck = deck.Deck()

# Make sure no values are undefined
if num_players is None:
    num_players = 4
if cards_per_player is None:
    cards_per_player = 6
if direction is None:
    direction = 1

# Initialize the players
players = initialize.initialize_players(num_players, player.Player)

# Deal cards to each player
for player in players:
    player.receive(deck.deal(cards_per_player))

# Print the hands of each player
for player in players:
    # ONLY FOR BUG FIXING
    print(f"{player.name}'s hand: {' ,'.join([card.rank + ' of ' + card.suit for card in player.hand])}")

# Determine the trump suit
trump_suit = trump.determine_trump_suit()

# Find the lowest trump card and set the starting player
lowest_trump_card = None
starting_player = None

for player in players:
    for card in player.hand:
        if card.suit == trump_suit and (lowest_trump_card is None or deck.get_ranks().index(card.rank) < deck.get_ranks().index(lowest_trump_card.rank)):
            lowest_trump_card = card
            starting_player = player
if starting_player is None:
    print("No player has a trump suit... A random player will start the game.")
    starting_player = random.choice(players)

# Print the determined trump suit and starting player
print(f"The trump suit is: {trump_suit}")
if lowest_trump_card is None:
    print(f"{starting_player.name} starts the game.")
    time.sleep(1)
    print(f"There are {len(deck.cards)} cards left in the deck.")
    time.sleep(1)
else:
    print(f"{starting_player.name} has the lowest trump suit with ({lowest_trump_card.rank} of {lowest_trump_card.suit}) and therefor starts the game.")
    time.sleep(1)
    print(f"There are {len(deck.cards)} cards left in the deck.")
    time.sleep(1)

# Choose who will be attacked according to the direction of the game
if direction == 1:
    player_to_attack = players[(players.index(starting_player) + 1) % len(players)]
else:
    player_to_attack = players[(players.index(starting_player) - 1) % len(players)]

# Ask the player which card they want to play
if starting_player.type == "Player":
    print("Your turn!")
    time.sleep(2)
    print(f"You will attack {player_to_attack.name}")
    time.sleep(2)
    print("Your hand:")
    for i, card in enumerate(starting_player.hand, start=1):
        print(f"{i}. {card.rank} of {card.suit}")
        time.sleep(6 / len(starting_player.hand))

    selected_card_number = int(input("Which card do you want to play? "))

    # Check if there are any cards of the same rank in the player's hand
    selected_card = starting_player.hand[selected_card_number - 1]
    played_cards = [selected_card]
    starting_player.hand.remove(selected_card)
    cards_of_same_rank = [card for card in starting_player.hand if card.rank == selected_card.rank]
    if len(cards_of_same_rank) >= 1:
        # Ask the player, if they want to play another card of the same rank
        print(f"You have {len(cards_of_same_rank)} cards of the same rank.")
        play_another_card = input("Do you want to play another card of the same rank? (y/n) ")
        if play_another_card == "y":
            # Ask the player, which card they want to play
            for i, card in enumerate(cards_of_same_rank, start=1):
                print(f"{i}. {card.rank} of {card.suit}")
            while True:
                try:
                    # Ask the player, which card they want to play
                    for i, card in enumerate(cards_of_same_rank, start=1):
                        print(f"{i}. {card.rank} of {card.suit}")
                    selected_card_number = int(input("Which card do you want to play? (Enter 0 to cancel) "))
                    if selected_card_number != 0:
                        selected_card = cards_of_same_rank[selected_card_number - 1]
                        played_cards.append(selected_card)
                        starting_player.hand.remove(selected_card)
                        break
                except IndexError:
                    print("Invalid number!")
                except ValueError:
                    print("Invalid input!")

        else:
            # Remove the card from the player's hand
            starting_player.hand.remove(selected_card)
    else:
        # Remove the card from the player's hand
        starting_player.hand.remove(selected_card)
else:
    ai.ai_turn()

game_won = False

while True:
    if not game_won:
        if player_to_attack.type != "Player":
            ai.ai_turn_attacked()
        else:
            turns.player_attacked(played_cards, player_to_attack)
    else:
        break
