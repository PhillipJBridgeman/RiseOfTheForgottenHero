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
        print("You step outside the old lady's house and encounter hostile creatures.")
        print("Let's go over how combat works in this world.")

        while True:
            # Introduce the first enemy (a rat for the tutorial)
            enemy = Enemy(player_level=self.player.level, type_override="rat")
        
            if not self.is_rat_and_within_level(enemy):
                print("This enemy is not suitable for the tutorial. Exiting...")
                break
        
            combat = Combat(self.player, enemy)
            combat.start_combat()

            if self.player.is_alive():
                print(f"\nYou have defeated the {enemy.name}!")
                loot = enemy.enemy_loot()
                if loot:
                    self.player.add_loot(loot)
                self.player.add_experience(enemy.experience_reward)
                print("Congratulations! You now understand the basics of combat.")
                print("You can fight another rat or exit the tutorial.")
            
                continue_fighting = input("Do you want to fight another rat? (yes/no): ").lower()
                if continue_fighting != 'yes':
                    break
            else:
                print("\nYou were defeated in the tutorial. Don't worry, you can try again.")
                self.player.health = 100
                break
    
    def is_rat_and_within_level(self, enemy):
        return enemy.type == "rat" and 1 <= enemy.level <= 3
