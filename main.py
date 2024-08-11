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
from intro import display_intro

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
            print("\nYou explore the area...")
            enemy = Player(name="Goblin", class_character="Rogue", health=50)
            player.attack_enemy(enemy)
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
    
    # Create a new player character
    player_name = input("Enter your hero's name: ")
    player_class = input("Choose your hero's class (Warrior, Mage, or Rogue): ").capitalize()
    player = Player(name=player_name, class_character=player_class)

    # Start the game loop
    main_game_loop(player)