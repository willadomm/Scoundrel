class Card:
    def __init__(self, suit, digit):
        self.suit = suit
        self.digit = digit
        self.displayname = digit
    
    def __str__(self):
        return self.suit + str(self.digit)
    
    def display(self):
        match self.digit:
            case 11:
                displayname = "Jack"
            case 12: 
                displayname = "Queen"
            case 13: 
                displayname = "King"
            case 1:
                displayname = "Ace"
            case _:
                displayname = str(self.digit)
        return("The " + displayname + " of " + self.suit)
    
    
    def getSuit(self):
        return self.suit
    
    def getDigit(self):
        return self.digit
        



