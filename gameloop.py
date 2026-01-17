import card


class Gamestate:
    def __init__(self,deck,):
        self.weapon = None
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
                self.life = self.life + cardselection.getDigit()
                if self.life > 20:
                    self.life = 20
                print("Your new life is: " + str(self.life))
                self.healthpotionused = True



    def gameloop(self):
        self.room = self.deck[0:4]
        self.deck = self.deck[4:]
    
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


            self.discard.append(cardselect-1)
            
            self.room.pop(cardselect-1)

 
        
        
        
