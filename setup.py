import card
import random

"""
Create a randomized deck of cards, without the red face cards and red aces

"""

def setup():
    listofcards = []

    for i in [ "Spades", "Clubs"]:
        for j in range(1,14):
            cards = card.Card(i,j)
            listofcards.append(cards)
    for i in ["Hearts", "Diamonds"]:
        for j in range (2, 11):
            cards = card.Card(i,j)
            listofcards.append(cards)
    
    random.shuffle(listofcards)

    return listofcards

    
   