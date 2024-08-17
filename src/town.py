"""
This file will contain the Town class.
When the player first enters the town they will be greeted by the town's mayor.
The mayor will show the player around the town and give them a brief overview of the town.
Then the mayor will give the player a quest to complete to go the inn and talk to the innkeeper.

Further development will include:
- The player being able to interact with the townspeople.
- The player being able to enter the shops and buy items.
- The player being able to enter the inn and rest.
"""
from inn import Inn
from player import Player
# from blacksmith import Blacksmith
# from magic_tower import MagicTower
# from swordsmith import Swordsmith
# from potion_shop import PotionShop

class Town:
    def __init__(self, player):
        self.inn = Inn()
        self.player = player
        # self.blacksmith = Blacksmith()
        # self.magic_tower = MagicTower()
        # self.swordsmith = Swordsmith()
        # self.potion_shop = PotionShop()
    
    def enter(self):
        print("You enter the town and are greeted by the mayor.")
        print("Mayor: Welcome to our town! I hope you enjoy your stay here.")
        print("Mayor: Before you explore the town, I have a quest for you.")
        print("Mayor: Go to the inn and talk to the innkeeper. They will have further instructions for you.")
        print("Mayor: Good luck on your journey!")
        print("You are now free to explore the town.")
        self.visit_inn(self.player)

    def visit_inn(self, player):
        self.inn.interact(player)

    def visit_blacksmith(self, player):
        self.blacksmith.interact(player)

    def visit_magic_tower(self, player):
        self.magic_tower.interact(player)

    def visit_swordsmith(self, player):
        self.swordsmith.interact(player)

    def visit_potion_shop(self, player):
        self.potion_shop.interact(player)

    def town_menu(self, player):
        while True:
            print("Welcome to the Town! Where would you like to go?")
            print("1. Inn")
            print("2. Blacksmith")
            print("3. Magic Tower")
            print("4. Swordsmith")
            print("5. Potion Shop")
            print("6. Leave Town")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.visit_inn(player)
            elif choice == "2":
                self.visit_blacksmith(player)
            elif choice == "3":
                self.visit_magic_tower(player)
            elif choice == "4":
                self.visit_swordsmith(player)
            elif choice == "5":
                self.visit_potion_shop(player)
            elif choice == "6":
                print("You leave the town and head back to your journey.")
                break
            else:
                print("Invalid choice. Please try again.")