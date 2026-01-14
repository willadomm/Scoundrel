class Card:
    def __init__(self, suit, digit):
        self.suit = suit
        self.digit = digit
    
    def __str__(self):
        return self.suit + str(self.digit)
        