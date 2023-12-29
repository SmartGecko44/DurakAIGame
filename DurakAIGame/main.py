import random


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


class Deck:
    def __init__(self):
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['♠', '♣', '♥', '♦']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.cards)

    def deal(self, num_cards):
        return [self.cards.pop() for _ in range(num_cards)]


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def receive(self, cards):
        self.hand.extend(cards)


# Get the number of players from the user
num_players = int(input("Enter the number of players: "))
cards_per_player = int(input("Enter the number of cards per player: "))

# Create a deck
deck = Deck()

# Create players based on the user's input
players = [Player(f"Player {i + 1}") for i in range(num_players)]

# Deal cards to each player
try:
    for player in players:
        player.receive(deck.deal(cards_per_player))
except IndexError:
    print("Not enough cards in the deck to deal to each player!")

# Print the hands of each player
for player in players:
    print(f"{player.name}'s hand: {' ,'.join([card.rank + ' of ' + card.suit for card in player.hand])}")
