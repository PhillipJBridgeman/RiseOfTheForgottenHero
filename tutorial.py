from player import Player
from combat import Combat
from enemy import Enemy  # Import the Enemy class

class Tutorial:
    def __init__(self, player):
        self.player = player

    def start(self):
        print('Hello sleepy head, welcome to the land of living again. I found you in a cave in the forest. You were almost dead.')
        print('I am the old lady of the forest, someone who the forces of evil have forgotten just like you.')
        
        user_input = input('Do you remember anything? ')
        print(f"No, I am sorry to say that these lands now belong to the forces of evil. {user_input or 'Perhaps'} you are the one who can save us all.")
        
        user_input = input('Do you want to help us? ')
        if user_input.lower() in ['yes', 'y']:
            print('Thank you, hero. I will help you get started on your journey.')
            print('First, let me teach you how to fight again.')
            print('Outside of my home, there are rats infesting the forest. Go and defeat them.')
            self.combat_tutorial()
        else:
            print("I see... it seems you need more time to remember who you are. Perhaps you will reconsider later.")
    
    def combat_tutorial(self):
        print("\n*** Tutorial: Combat Basics ***")
        print("You step outside the old lady's house and encounter a hostile creature.")
        print("Let's go over how combat works in this world.")

        # Introduce the first enemy using the Enemy class
        enemy = Enemy(player_level=self.player.level)  # Assume player has a level attribute
        combat = Combat(self.player, enemy)

        # Explain the basics of combat
        print("\nCombat is turn-based. Each turn, you can choose an action like 'attack' or 'use skill'.")
        print("The enemy will also take turns attacking you. Manage your stamina and health carefully!")

        # Start the tutorial combat
        combat.start_combat()

        if self.player.is_alive():
            print("\nYou have defeated the Wild Rat!")
            print("Congratulations! You now understand the basics of combat.")
            print("You can now explore the world and engage in more challenging battles.")
        else:
            print("\nYou were defeated in the tutorial. Don't worry, you can try again.")
            self.player.health = 100  # Reset player health for retry
            self.combat_tutorial()  # Restart the tutorial combat
