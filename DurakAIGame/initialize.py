import time
import warnings
from typing import List, Tuple
from DurakAIGame import player


class InvalidDirectionWarning(Warning):
    pass


def get_user_settings(num_players_input, cards_per_player_input, direction_input) -> Tuple[int, int, int]:
    try:
        # Get the number of players
        if num_players_input is None:
            num_players = int(input("Enter the number of players: "))
        else:
            num_players = num_players_input

        # Get the number of cards per player
        if cards_per_player_input is None:
            cards_per_player = int(input("Enter the number of cards per player: "))
        else:
            cards_per_player = cards_per_player_input

        # Get the direction of the game
        if direction_input is None:
            direction = int(input("Enter the direction of the game (clockwise (1) or counterclockwise (2)): "))
        else:
            direction = direction_input

        if num_players * cards_per_player > 52:
            warnings.warn("Not enough cards!", RuntimeWarning)
            return 4, 6, 1

        if direction != 1 and direction != 2:
            warnings.warn("Invalid direction!", RuntimeWarning)
            return 4, 6, 1

    except ValueError:
        warnings.warn("Invalid input!", RuntimeWarning)
        return 4, 6, 1

    return num_players, cards_per_player, direction


def initialize_players(num_players: int, player) -> List[player.Player]:
    # Create players based on the user's input
    players = [player(f"Player {i + 1}") for i in range(num_players)]
    for player in players:
        if player.name == "Player 1":
            player.type = "Player"
        else:
            player.type = "AI"
    return players