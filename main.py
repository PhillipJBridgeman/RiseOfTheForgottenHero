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

from intro import display_intro

def main():
    display_intro()
    
    while True:
        print("Main game loop")
        break

if __name__ == "__main__":
    main()