import time
import card


class Gamestate:
    def __init__(self,deck,):
        self.weapon = []
        self.life = 20
        self.deck = deck
        self.discard = []
        self.prevroomskipped = False
        self.room = []
        self.healthpotionused = False

        self.gameloop()
    
    
    def select(self,cardselection):
        print("You selected " + card.Card.display(cardselection))
        match cardselection.getSuit():
            case "Hearts":
                if self.healthpotionused == False:
                    self.life = self.life + cardselection.getDigit()
                    if self.life > 20:
                        self.life = 20
                    print("Your new life is: " + str(self.life))
                    time.sleep(1)
                    self.healthpotionused = True
                else:
                    print("You can only use one health potion per room!")
            case "Diamonds":
                if len(self.weapon) > 0:
                    self.discard.append(self.weapon[0])
                self.weapon = [cardselection, 100]
                
                print("Your new weapon is " + card.Card.display(cardselection))
            case _:
                self.fight(cardselection)

    def fight(self, cardselection):
        if len(self.weapon) > 0:
            fightbool = input("Would you like to fight this monster with your equipped weapon?(Press y for yes): ")
            if fightbool == "y" or fightbool == "Y":
                self.fightwithweapon(cardselection)
            else:
                self.fightbarehanded(cardselection)
        else:
            self.fightbarehanded(cardselection)

    def fightbarehanded(self, cardselection):
        self.life = self.life - card.Card.getDigit(cardselection)
        print("The monster did " + str(card.Card.getDigit(cardselection)) + " damage to you.")
        time.sleep(1)
        print("You are now at " + str(self.life) + " health")

    def fightwithweapon(self, cardselection):
        if (card.Card.getDigit(self.weapon[0])) - card.Card.getDigit(cardselection) > 0:
            print("You took no damage from the monster, as your weapon was a hogher power.")
            print("Your weapon can now only be used to slay monsters of less strength than " + str(card.Card.getDigit(cardselection)))








    def gameloop(self):
        self.room = self.deck[0:4]
        self.deck = self.deck[4:]
        self.healthpotionused = False
    
        while len(self.room) > 1:
            counter = 1
            for i in self.room:
                print(str(counter) + ". " + card.Card.display(i))
                counter += 1
            if self.prevroomskipped == False and len(self.room) == 4:
                skipask = "n"
                skipask = input("Since you haven't skipped the previous room, you may skip this one. Would you like to do this? (Press s to skip, and press anything else to not skip): ")
                if skipask == "s":
                    self.discard.extend(self.room)
                    self.prevroomskipped = True
                    self.gameloop()
            
            self.prevroomskipped = False
            
            cardselect = 0

            while cardselect < 1 or cardselect > 4:
                cardselect = int(input("Which card would you like to choose first?: "))
                if cardselect < 1 or cardselect > 4:
                    print("Please select a number from 1-4")
    
        
            self.select(self.room[cardselect-1])

            self.discard.append(self.room.pop(cardselect-1))

 
        
        
        
