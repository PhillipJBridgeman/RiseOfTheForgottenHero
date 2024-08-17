"""
main.py

This file contains the main game loop for the game "Rise of the Forgotten Hero."

Author: Phillip Bridgeman
Created: August 11, 2024
Last Modified: August 11, 2024
Contact: phillipbridgeman@gmail.com

License: MIT License
This project is licensed under the MIT License - see the LICENSE file for details.

Dependencies:
- intro.py

Usage:
Run this file to start the game.

Version: 1.0.0
"""
# Import the Player class from player.py
from player import Player
from combat import Combat
from intro import display_intro
from tutorial import Tutorial

def main_game_loop(player):
    game_running = True
    while game_running:
        # Display player's current status
        player.display_stats()

        # Provide options to the player
        print("\nWhat would you like to do?")
        print("1. Explore")
        print("2. Rest")
        print("3. Check Inventory (Not yet implemented)")
        print("4. Quit")

        # Get player input
        choice = input("Enter your choice: ")

        # Handle the player's choice
        if choice == '1':
            # Implement explore function (e.g., encounter an enemy)
            print("\nExploring... (This feature is not yet implemented)")
        elif choice == '2':
            player.health = min(100, player.health + 20)
            print(f"\n{player.name} rests and recovers health. Current health: {player.health}")
        elif choice == '3':
            # Check inventory (to be implemented)
            print("\nChecking inventory... (This feature is not yet implemented)")
        elif choice == '4':
            print("Thank you for playing!")
            game_running = False
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    display_intro()
    player = Player()
    player.display_stats()
    print(f"\nWelcome, {player.name}! Your journey begins now.")
    tutorial = Tutorial(player)
    tutorial.start()
    #main_game_loop(player)
    