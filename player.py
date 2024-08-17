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
from collections import defaultdict

class Player:
    def __init__(self):
        self.name = self.choose_name()
        self.character_class = self.choose_class()
        self.level = 1
        self.experience_points = 0
        self.experience_to_next_level = 100
        self.inventory = defaultdict(int)
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
                'slash': (self.slash, 3, 0, "A powerful slashing attack."),
                'block': (self.block, 2, 0, "Block incoming attacks, reducing damage."),
                'charge': (self.charge, 5, 0, "Charge up for a powerful attack.")
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
                'fireball': (self.fireball, 0, 5, "Cast a fiery ball at the enemy."),
                'heal': (self.heal, 0, 4, "Heal yourself."),
                'lightning': (self.lightning, 0, 7, "Strike the enemy with lightning.")
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
                'stab': (self.stab, 2, 0, "A quick stabbing attack."),
                'dodge': (self.dodge, 3, 0, "Dodge incoming attacks."),
                'sneak': (self.sneak, 1, 0, "Move stealthily to avoid detection.")
            })

    def slash(self, target):
        """A powerful slashing attack."""
        return self.stats['attack'] + random.randint(5, 10)

    def fireball(self, target):
        """Cast a fiery ball at the enemy."""
        return self.stats['intelligence'] * 2 + random.randint(5, 10)

    def stab(self, target):
        """A quick stabbing attack."""
        return self.stats['attack'] + random.randint(3, 8)

    def take_damage(self, damage):
        self.stats['health'] -= damage
        print(f"{self.name} takes {damage} damage! Health is now {self.stats['health']}.")

    def is_alive(self):
        return self.stats['health'] > 0

    def block(self, target):
        """Block incoming attacks, reducing damage."""
        return self.stats['defense'] + random.randint(1, 5)

    def charge(self, target):
        """Charge up for a powerful attack."""
        return self.stats['attack'] + random.randint(5, 10)

    def heal(self, target):
        """Heal yourself."""
        return self.stats['health'] + random.randint(5, 10)

    def lightning(self, target):
        """Strike the enemy with lightning."""
        return self.stats['intelligence'] * 2 + random.randint(5, 10)

    def dodge(self, target):
        """Dodge incoming attacks."""
        return self.stats['defense'] + random.randint(1, 5)

    def sneak(self, target):
        """Move stealthily to avoid detection."""
        return self.stats['intelligence'] * 2 + random.randint(5, 10)

    def add_loot(self, loot):
        self.inventory[loot] += 1
        print(f"{loot} added to inventory. Total: {self.inventory[loot]}")

    def add_experience(self, experience):
        self.experience_points += experience
        print(f"{self.name} gains {experience} experience points!")
        if self.experience_points >= self.experience_to_next_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience_points -= self.experience_to_next_level
        self.experience_to_next_level = int(self.experience_to_next_level * 1.5)
        print(f"{self.name} has leveled up to level {self.level}!")
        self.stats['health'] += 10
        self.stats['attack'] += 2
        self.stats['defense'] += 2
        self.stats['stamina'] += 2
        self.stats['mana'] += 4
        self.stats['intelligence'] += 4
        print(f"{self.name}'s stats have increased!")
        print(self.display_stats())
        
    def display_inventory(self):
        # Sort the inventory from having the most to least items
        sorted_inventory = sorted(self.inventory.items(), key=lambda x: x[1], reverse=True)
        print("\nInventory:")
        for item, quantity in sorted_inventory:
            print(f"- {item}: {quantity}")

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
        for skill_name, skill_details in self.skills.items():
            _, stamina_cost, mana_cost, description = skill_details
            print(f"- {skill_name}: {description} (Cost: {stamina_cost} stamina, {mana_cost} mana)")