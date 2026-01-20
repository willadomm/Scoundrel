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
        self.roomcounter = 0

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
            if self.weapon[1] > card.Card.getDigit(cardselection):
                fightbool = input("Would you like to fight this monster with your equipped weapon?(Press y for yes): ")
                if fightbool == "y" or fightbool == "Y":
                    self.fightwithweapon(cardselection)
                else:
                    self.fightbarehanded(cardselection)
            else: 
                print()
                time.sleep(0.5)
                print("Your weapon cannot be used against this monster.")
                self.fightbarehanded(cardselection)
        else:
            self.fightbarehanded(cardselection)

    def fightbarehanded(self, cardselection):
        self.life = self.life - card.Card.getDigit(cardselection)
        print("The monster did " + str(card.Card.getDigit(cardselection)) + " damage to you.")
        time.sleep(1)
        print("You are now at " + str(self.life) + " health")

    def fightwithweapon(self, cardselection):
        if (card.Card.getDigit(self.weapon[0])) - card.Card.getDigit(cardselection) >= 0:
            print("You took no damage from the monster, as your weapon was a higher power.")
            time.sleep(1)
            print("Your weapon can now only be used to slay monsters of less strength than " + str(card.Card.getDigit(cardselection)))
            self.weapon[1] = card.Card.getDigit(cardselection)
        else:
            self.life = self.life - (card.Card.getDigit(cardselection) - card.Card.getDigit(self.weapon[0]))
            print("You took " + str(card.Card.getDigit(cardselection) - card.Card.getDigit(self.weapon[0])) + " damage from the monster. ")
            time.sleep(1)
            print("Your life is now " + str(self.life))
    

    def constructroomdetails(self):
        print()
        print("Life: " + str(self.life))
        time.sleep(0.5)
        print()
        if len(self.weapon) > 0:
            print("Current Weapon: " + card.Card.display(self.weapon[0]))
            if self.weapon[1] < 20:
                print("Can only be used against monsters with power less than " + str(self.weapon[1]))
            print()

        
        time.sleep(0.5)
        print("Room number: " + str(self.roomcounter))
        print()
        print("Cards left in deck: " + str(len(self.deck)))
        print()
        



    def lifetotalcheck(self, cardselect):
        if self.life < 1:
            print()
            print("Game Over! You bled out in the dungeon.")
            print()
            print("You were killed by: " + card.Card.display(cardselect))
            print() 
            print("Cards remaining in deck: " + str(len(self.deck)))
            exit()







    def gameloop(self):
        self.room = self.deck[0:4]
        self.deck = self.deck[4:]
        self.healthpotionused = False
        self.roomcounter += 1

        time.sleep(0.5)

        self.constructroomdetails()



        time.sleep(0.5)

        if self.prevroomskipped == False and len(self.room) == 4:
            counter = 1
            for i in self.room:
                print(str(counter) + ". " + card.Card.display(i))
                counter += 1
            skipask = "n"
            print("Since you haven't skipped the previous room, you may skip this one. Would you like to do this? ")
            skipask = input("Press s to skip, or press the card number to choose that card: ")
            if skipask == "s":
                self.discard.extend(self.room)
                self.prevroomskipped = True
                self.room = []
        else:
            skipask = "n"

            

        while len(self.room) > 1:
            
            self.prevroomskipped = False

            cardselect = 0

            if skipask.isnumeric() and int(skipask)> 0 and int(skipask) <5 :
                cardselect = skipask

            else:
                counter = 1
                for i in self.room:
                    print(str(counter) + ". " + card.Card.display(i))
                    counter += 1
                while cardselect < 1 or cardselect > len(self.room):
                    cardselect = int(input("Which card would you like to choose first?: "))
                    if cardselect < 1 or cardselect > len(self.room):
                        print("Please select a number from 1-4")
                
    
            skipask = "n"

            self.select(self.room[(int(cardselect)-1)])

            self.discard.append(self.room.pop(int(cardselect)-1))



           

        if (len(self.room) > 0):
            self.deck.insert(0, self.room[0])

        self.gameloop()
        
        

 
        
        
        
