from player import Player
from combat import Combat
from enemy import Enemy

class Tutorial:
    def __init__(self, player):
        self.player = player

    def start(self):
        self.introduction()
        
        if self.prompt_player("Do you want to help us?"):
            print('Thank you, hero. I will help you get started on your journey.')
            print('First, let me teach you how to fight again.')
            print('Outside of my home, there are rats infesting the forest. Go and defeat them.')
            self.combat_tutorial()
        else:
            print("I see... it seems you need more time to remember who you are. Perhaps you will reconsider later.")

    def introduction(self):
        print('Hello sleepy head, welcome to the land of living again. I found you in a cave in the forest. You were almost dead.')
        print('I am the old lady of the forest, someone who the forces of evil have forgotten just like you.')
        user_input = input('Do you remember anything? ')
        print(f"No, I am sorry to say that these lands now belong to the forces of evil. {user_input or 'Perhaps'} you are the one who can save us all.")
    
    def prompt_player(self, prompt):
        return input(prompt).strip().lower() in ['yes', 'y']

    def combat_tutorial(self):
        print("\n*** Tutorial: Combat Basics ***")
        print("You step outside the old lady's house and encounter hostile creatures.")
        print("Let's go over how combat works in this world.")

        while self.player.level <= 3:
            enemy = Enemy(player_level=self.player.level, type_override="rat")
        
            if not self.is_rat_and_within_level(enemy):
                print("This enemy is not suitable for the tutorial. Exiting...")
                break
        
            combat = Combat(self.player, enemy)
            combat.start_combat()

            if self.player.is_alive():
                print(f"\nYou have defeated the {enemy.name}!")
                self.reward_player(enemy)
                if not self.prompt_player("Do you want to fight another rat? (yes/no): "):
                    self.exit_tutorial(early_exit=True)
                    return
            else:
                print("\nYou were defeated in the tutorial. Don't worry, you can try again.")
                self.player.health = 100  # Reset player health for retry
                break

        if self.player.level > 3:
            self.exit_tutorial(early_exit=False)

    def reward_player(self, enemy):
        loot = enemy.enemy_loot()
        if loot:
            self.player.add_loot(loot)
        self.player.add_experience(enemy.enemy_experience_reward())

    def is_rat_and_within_level(self, enemy):
        return enemy.type == "rat" and 1 <= enemy.level <= 3

    def exit_tutorial(self, early_exit):
        if early_exit:
            print("Good luck and godspeed, hero. The world awaits your journey.")
        else:
            print("Thank you, but the world needs our hero's help. It's time to move on to greater challenges.")
