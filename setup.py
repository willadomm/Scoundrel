import card
import random

"""
Create a randomized deck of cards

"""

def setup():
    listofcards = []

    for i in ["Hearts", "Spades", "Diamonds", "Clubs"]:
        for j in range(1,14):
            cards = card.Card(i,j)
            listofcards.append(cards)
    
    random.shuffle(listofcards)

    for i in listofcards:
        print(i)

    
   