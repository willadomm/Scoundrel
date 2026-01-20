import setup
import gameloop
import time

def main():
    userinput = input("Hello! Welcome to Scoundrel. Press enter to start a new game: ")
    time.sleep(0.5)
    print("Shuffling Deck...")
    time.sleep(0.5)
    deck = setup.setup()
    gameloop.Gamestate(deck)


main()