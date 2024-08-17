"""
main.py

Entry point for the game "Rise of the Forgotten Hero."

Author: Phillip Bridgeman
Created: August 11, 2024
Last Modified: August 16, 2024
Contact: phillipbridgeman@gmail.com

License: MIT License
This project is licensed under the MIT License - see the LICENSE file for details.

Dependencies:
- player.py
- tutorial.py
- town.py
- quest.py
- combat.py
- save_load.py

Usage:
Run this file to start the game.

Version: 1.0.0
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from player import Player
from tutorial import Tutorial
from town import Town
# from save_load import SaveLoad

def display_intro():
    try:
        with open("src/story_introduction.txt", "r") as file:
            intro = file.read()
            print(intro)
    except FileNotFoundError:
        print("Error: 'story_introduction.txt' file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main_menu(player):
    while True:
        print("\nMain Menu:")
        print("1. Review Stats")
        print("2. Go to Town")
        print("3. Read Lore")
        print("4. Review Inventory")
        print("5. Save Game")
        print("6. Quit")
        
        choice = input("Choose an action: ")

        if choice == "1":
            player.display_stats()
        elif choice == "2":
            enter_town(player)
        elif choice == "3":
            print("Reading lore...")
            # Implement lore reading hereelif choice == "4":
            print("Reviewing inventory...")
            # Implement inventory management hereelif choice == "5":
            save_game(player)
        elif choice == "6":
            print("Exiting the game...")
            break
        else:
            print("Invalid choice. Please try again.")

def enter_town(player):
    town = Town(player)
    town.enter()

def save_game(player):
    # save_manager = SaveLoad()
    # save_manager.save_game(player)
    # print("Game saved successfully.")
    pass

if __name__ == "__main__":
    display_intro()
    
    # Create the player character
    player = Player()

    # Start the tutorial
    tutorial = Tutorial(player)
    tutorial.start()

    # Post-tutorial, show the main menu for further choices
    main_menu(player)