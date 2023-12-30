class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.type = None

    def receive(self, cards):
        self.hand.extend(cards)
