import time


def player_attacked(played_cards, player):
    print("Your turn!")
    time.sleep(1)
    print("You are being attacked with:")
    for i, card in enumerate(played_cards, start=1):
        time.sleep(6 / len(played_cards))
        print(f"{i}. {card.rank} of {card.suit}")
    time.sleep(1)
    print("Your hand:")
    for i, card in enumerate(player.hand, start=1):
        print(f"{i}. {card.rank} of {card.suit}")
        time.sleep(6 / len(player.hand))

    selected_card_number = int(input("Which card do you want to play? "))

    # Check if there are any cards of the same rank in the player's hand
    selected_card = player.hand[selected_card_number - 1]
    played_cards = [selected_card]
    player.hand.remove(selected_card)
    cards_of_same_rank = [card for card in player.hand if card.rank == selected_card.rank]
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
                        player.hand.remove(selected_card)
                        break
                except IndexError:
                    print("Invalid number!")
                except ValueError:
                    print("Invalid input!")

        else:
            # Remove the card from the player's hand
            player.hand.remove(selected_card)
    else:
        # Remove the card from the player's hand
        player.hand.remove(selected_card)