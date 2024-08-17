from player_options import Player_Options
from player import Player

class Innkeeper:
    def welcome(self):
        print("My name is Thomas, the innkeeper here. How can I assist you today?")

    def rent_room(self, player):
        price = 5
        if player.inventory['gold'] >= price:
            player.inventory['gold'] -= price
            print("You rented the room for the night. Your gold is now:", player.inventory['gold'])
            Player_Options(player).display_options()
        else:
            print("You do not have enough gold to rent the room.")

    def hot_meal(self, player):
        price = 3
        if player.inventory['gold'] >= price:
            player.inventory['gold'] -= price
            print("You enjoyed a hot meal. Your gold is now:", player.inventory['gold'])
            player.stats['health'] += 10
            print("Your health is now:", player.stats['health'])
            
            if player.class_name == 'Warrior':
                player.stats['stamina'] += 5
                print("Your stamina is now:", player.stats['stamina'])
            elif player.class_name == 'Mage':
                player.stats['mana'] += 5
                print("Your mana is now:", player.stats['mana'])
            elif player.class_name == 'Rogue':
                player.stats['attack'] += 5
                print("Your attack is now:", player.stats['attack'])
    
    def offer_quests(self, player):
        # Implement logic to offer quests
        pass
