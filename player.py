"""
player.py

This file contains the player class for the game "Rise of the Forgotten Hero."

Author: Phillip Bridgeman
Created: August 11, 2024
Last Modified: August 11, 2024
Contact: phillipbridgeman@gmail.com

License: MIT License
This project is licensed under the MIT License - see the LICENSE file for details.

Dependencies:
- None (uses only Python standard library)

Usage:
This file is intended to be imported and used within the main game script.

Version: 1.0.0
"""
import random

class Player:
    def __init__(self):
        self.name = self.choose_name()
        self.character_class = self.choose_class()
        self.level = 1
        self.experience_points = 0
        self.inventory = {}
        self.equipment = {
            'weapon': None,
            'armor': None,
            'accessory': None
        }
        self.stats = {
            'health': 100,
            'attack': 10,
            'defense': 5,
            'stamina': 10,
            'mana': 0,
            'intelligence': 0
        }
        self.skills = {}
        self.initialize_player_class()

    def choose_name(self):
        # Only accept letter characters for the player's name
        while True:
            name = input("What is your name, hero? ")
            if name.isalpha():
                return name
            else:
                print("Please enter a valid name using only letters.")
    
    def choose_class(self):
        while True:
            print("Choose your class:")
            print("1. Warrior")
            print("2. Mage")
            print("3. Rogue")
            class_choice = input("Enter the number of your choice: ")
            if class_choice == 'Warrior' or class_choice == '1':
                return 'Warrior'
            elif class_choice == 'Mage' or class_choice == '2':
                return 'Mage'
            elif class_choice == 'Rogue' or class_choice == '3':
                return 'Rogue'
            else:
                print("Please enter a valid class choice.")
    
    def initialize_player_class(self):
        if self.character_class == 'Warrior':
            self.stats.update({
                'health': 100,
                'attack': 20,
                'defense': 10,
                'stamina': 20
            })
            self.equipment.update({
                'weapon': 'Dull Sword',
                'armor': 'Leather Armor',
                'accessory': 'Knight Ring'
            })
            self.skills.update({
                'slash': self.slash,
                'block': self.block,
                'charge': self.charge
            })
        elif self.character_class == 'Mage':
            self.stats.update({
                'health': 75,
                'attack': 15,
                'defense': 5,
                'mana': 20,
                'intelligence': 10
            })
            self.equipment.update({
                'weapon': 'Wooden Staff',
                'armor': 'Cloth Robes',
                'accessory': 'Old Mage Amulet'
            })
            self.skills.update({
                'fireball': self.fireball,
                'heal': self.heal,
                'lightning': self.lightning
            })
        elif self.character_class == 'Rogue':
            self.stats.update({
                'health': 80,
                'attack': 18,
                'defense': 7,
                'stamina': 15
            })
            self.equipment.update({
                'weapon': 'Rusty Dagger',
                'armor': 'Leather Cloak',
                'accessory': 'Thief Bandana'
            })
            self.skills.update({
                'stab': self.stab,
                'dodge': self.dodge,
                'lockpick': self.lockpick,
                'sneak': self.sneak
            })
        else:
            print("Invalid class choice. Please choose again.")
            self.character_class = self.choose_class()
            self.initialize_player_class()
        
    def slash(self, target):
        return self.stats['attack'] + random.randint(5, 10)

    def fireball(self, target):
        return self.stats['intelligence'] * 2 + random.randint(5, 10)

    def stab(self, target):
        return self.stats['attack'] + random.randint(3, 8)

    def take_damage(self, damage):
        self.stats['health'] -= damage
        print(f"{self.name} takes {damage} damage! Health is now {self.stats['health']}.")

    def is_alive(self):
        return self.stats['health'] > 0
    
    # Block allows the player to reduce incoming damage then if the player block + defense is greater than the incoming damage, the player takes no damage 
    def block(self, target):
        return self.stats['defense'] + random.randint(1, 5)
    
    # Charge allows the player to increase their attack power for a turn
    def charge(self, target):
        return self.stats['attack'] + random.randint(5, 10)
    
    # Heal allows the player to heal themselves
    def heal(self, target):
        return self.stats['health'] + random.randint(5, 10)
    
    # Lightning allows the player to use their intelligence to attack
    def lightning(self, target):
        return self.stats['intelligence'] * 2 + random.randint(5, 10)
    
    # Dodge allows the player to dodge incoming attacks
    def dodge(self, target):
        return self.stats['defense'] + random.randint(1, 5)
    
    # Lockpick allows the player to unlock doors and chests
    def lockpick(self, target):
        return self.stats['intelligence'] * 2 + random.randint(5, 10)
    
    # Sneak allows the player to sneak past enemies
    def sneak(self, target):
        return self.stats['intelligence'] * 2 + random.randint(5, 10)
    
    def add_loot(self, loot):
        # Check if item is already in inventory if so, increase quantity, and if not, add it to inventory with quantity 1
        for item in self.inventory:
            if item == loot:
                self.inventory[item] += 1
                break
            else:
                self.inventory[loot] = 1
    
    def add_experience(self, experience):
        self.experience_points += experience
        print(f"{self.name} gains {experience} experience points!")
        if self.experience_points >= 100:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.experience_points = 0
        print(f"{self.name} has leveled up to level {self.level}!")
        self.stats['health'] += 10
        self.stats['attack'] += 2
        self.stats['defense'] += 2
        self.stats['stamina'] += 2 
        self.stats['mana'] += 4
        self.stats['intelligence'] += 4
        print(f"{self.name}'s stats have increased!")
    
    def display_stats(self):
        print(f"\n{self.name} ({self.character_class}) - Level {self.level}")
        print("Health:", self.stats['health'])
        print("Attack:", self.stats['attack'])
        print("Defense:", self.stats['defense'])
        print("Stamina:", self.stats['stamina'])
        print("Mana:", self.stats['mana'])
        print("Intelligence:", self.stats['intelligence'])
        print("Equipment:")
        for slot, item in self.equipment.items():
            print(f"- {slot}: {item}")
        print("Skills:")
        for skill_name, skill_func in self.skills.items():
            print(f"- {skill_name}: {skill_func.__doc__}")