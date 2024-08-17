"""
This module will contain attribute and methods for the NPC class.
The NPC class will be used to create the mayor of the town.
The NPC class will also be used to create other NPCs that the player can interact with and give out quests.
"""

class Npc:
    def __init__(self, name, dialogue, role, quest=None, inventory=None):
        """
        Base class for all NPCs in the game.

        :param name: The name of the NPC.
        :param dialogue: The default dialogue for the NPC.
        :param role: The role of the NPC (e.g., "shopkeeper", "quest giver").
        :param quest: Optional; The quest the NPC may offer (defaults to None).
        :param inventory: Optional; The inventory of items for shopkeeper NPCs (defaults to None).
        """
        self.name = name
        self.dialogue = dialogue
        self.role = role
        self.quest = quest  # Quests could be an object or dictionary representing quest details
        self.inventory = inventory or []  # List of items for shopkeeper NPCs
        
    def speak(self):
        print(f"{self.name}: {self.dialogue}")
    
    def give_quest(self):
        if self.quest:
            # Logic for assigning a quest to the player
            print(f"{self.name} gives you a quest: {self.quest['name']}")
        else:
            print(f"{self.name} has no quest for you.")
    
    def show_inventory(self):
        if self.inventory:
            print(f"{self.name}'s Inventory:")
            for item in self.inventory:
                print(f"- {item}")
        else:
            print(f"{self.name} has no items to sell.")
