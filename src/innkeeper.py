from player_options import Player_Options

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
        # Implement the logic for hot meal, similar to rent_room
        pass
    
    def offer_quests(self, player):
        # Implement logic to offer quests
        pass
