# Scoundrel

A terminal-based dungeon crawler card game where you navigate through rooms filled with monsters, weapons, and health potions using a standard deck of cards.

## Game Overview

Scoundrel is a single-player roguelike card game where you must survive a dungeon by strategically choosing cards from rooms. Each suit has a different effect:

- **♠️ Spades & ♣️ Clubs**: Monsters that damage you
- **♦️ Diamonds**: Weapons to fight monsters
- **♥️ Hearts**: Health potions to restore life

Your goal is to make it through the entire deck without your health dropping to zero.

## Rules

### Basic Mechanics

- You start with **20 health**
- Each room contains **4 cards** from the deck
- You must choose cards **one at a time** until only one remains
- The last card in each room is placed back on top of the deck for the next room
- You can **skip one room** per game (but not consecutive rooms)

### Card Effects

**Monsters (Spades & Clubs)**
- Deal damage equal to their value (2-14, where Jack=11, Queen=12, King=13, Ace=14)
- Fighting barehanded: take full damage
- Fighting with a weapon: reduce or negate damage based on weapon strength

**Weapons (Diamonds)**
- Replace your current weapon (only one weapon at a time)
- Can block monster damage if weapon value ≥ monster value
- After use, weapon can only defeat monsters weaker than the last one fought
- Values range from 2-10

**Health Potions (Hearts)**
- Restore health equal to card value (2-10)
- Maximum health is 20 (cannot exceed)
- Only **one health potion per room** can be used

### Strategy Tips

- Save high-value weapons for powerful monsters
- Use health potions wisely (only one per room!)
- Consider skipping a difficult room if you haven't skipped recently
- Remember that weapons degrade after each use
- Plan ahead by looking at all cards in a room before choosing

## Installation & Running

### Requirements
- Python 3.10 or higher (uses `match` statements)

### How to Run

1. Ensure all four files are in the same directory:
   - `main.py`
   - `gameloop.py`
   - `card.py`
   - `setup.py`

2. Run the game:
   ```bash
   python main.py
   ```

3. Follow the on-screen prompts to play

## Game Files

- **main.py**: Entry point and game initialization
- **gameloop.py**: Core game logic and room management
- **card.py**: Card class definition and display methods
- **setup.py**: Deck creation and shuffling
- **README.md**: This file

## Winning & Losing

**Victory**: Successfully navigate through all 52 cards without dying

**Defeat**: Your health drops to 0 or below

When the game ends, you'll see:
- What killed you (if you lost)
- How many cards remained in the deck
- Your room number (progression)

## Future Improvements

The following features are planned for future development:
- Scoring system based on performance
- High score saving and tracking
- Additional card effects or special abilities
- Difficulty modes

## License

This is a personal project. Feel free to modify and enjoy!

---

*Good luck, Scoundrel! May your weapons be sharp and your health potions plentiful.*
