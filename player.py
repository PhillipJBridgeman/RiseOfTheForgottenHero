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

class Player:
    def __init__(self, name, class_character, health=100, attack=10, defense=10):
        self.name = name
        self.class_character = class_character
        self.health = health
        self.attack = attack
        self.defense = defense

        # Define the skill actions for each class
        self.skills = {
            "Warrior": {
                "slash": self.slash,
                "block": self.block,
                "charge": self.charge,
                "execute": self.execute
            },
            "Mage": {
                "fireball": self.fireball,
                "heal": self.heal,
                "lightning": self.lightning
            },
            "Rogue": {
                "backstab": self.backstab,
                "dodge": self.dodge,
                "stealth": self.stealth,
                "lockpicking": self.lockpicking
            }
        }

    def attack_enemy(self, enemy):
        """Initiates an attack against an enemy."""
        print(f"{self.name} attacks {enemy.name}!")
        available_skills = self.skills.get(self.class_character, {})
        attack = input(f"What will you use? ({', '.join(available_skills.keys())}): ").lower()

        if attack in available_skills:
            available_skills[attack](enemy)
        else:
            print("Invalid skill chosen.")

    # Warrior Skills
    def slash(self, enemy):
        enemy.take_damage(20)
        print(f"{self.name} slashes {enemy.name} for 20 damage!")

    def block(self, enemy=None):
        self.defense += 10
        print(f"{self.name} blocks and increases defense by 10!")

    def charge(self, enemy):
        enemy.take_damage(30)
        self.take_damage(10)
        print(f"{self.name} charges at {enemy.name}, dealing 30 damage and taking 10 damage in return!")

    def execute(self, enemy):
        if enemy.health < 15:
            print(f"{self.name} executes {enemy.name}!")
            enemy.take_damage(100)
        else:
            print("Execute failed. Enemy health is too high.")

    # Mage Skills
    def fireball(self, enemy):
        enemy.take_damage(30)
        print(f"{self.name} casts Fireball, dealing 30 damage to {enemy.name}!")

    def heal(self, enemy=None):
        self.health += 20
        print(f"{self.name} heals for 20 health! Current health: {self.health}")

    def lightning(self, enemy):
        enemy.take_damage(40)
        print(f"{self.name} casts Lightning, dealing 40 damage to {enemy.name}!")

    # Rogue Skills
    def backstab(self, enemy):
        enemy.take_damage(40)
        print(f"{self.name} backstabs {enemy.name} for 40 damage!")

    def dodge(self, enemy=None):
        self.defense += 20
        print(f"{self.name} dodges, increasing defense by 20!")

    def stealth(self, enemy=None):
        print(f"{self.name} disappears into the shadows. You're now harder to hit!")

    def lockpicking(self, enemy=None):
        print(f"{self.name} attempts to pick the lock. It's only a matter of time...")

    # Health and Combat Management
    def take_damage(self, amount):
        """Reduces the player's health by the specified amount."""
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} now has {self.health} health left.")

    def display_stats(self):
        """Displays the player's current stats."""
        print(f"Name: {self.name}")
        print(f"Class: {self.class_character}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")

# Example usage
if __name__ == "__main__":
    player = Player(name="Aragorn", class_character="Warrior")
    enemy = Player(name="Goblin", class_character="Rogue", health=50)

    player.attack_enemy(enemy)
    enemy.attack_enemy(player)
