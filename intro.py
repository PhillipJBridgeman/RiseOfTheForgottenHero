"""
intro.py

This file contains the introduction text for the game "Rise of the Forgotten Hero."
It handles the display of the game's backstory when the player starts the game.

Author: Phillip Bridgeman
Created: August 11, 2024
Last Modified: August 11, 2024
Contact: phillipbridgeman@gmail.com

License: MIT License
This project is licensed under the MIT License - see the LICENSE file for details.

Dependencies:
- None (uses only Python standard library)

Usage:
Run this file as part of the main game script to display the introduction.

Version: 1.0.0
"""

def display_intro():
    try:
        with open(".\story_introduction.txt", "r") as file:
            intro = file.read()
            print(intro)
    except FileNotFoundError:
        print("Error: 'story_introduction.txt' file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    display_intro()