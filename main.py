import setup
import gameloop

def main():
    deck = setup.setup()
    gameloop.Gamestate(deck)


main()