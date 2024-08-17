from innkeeper import Innkeeper

class Inn:
    def __init__(self):
        self.innkeeper = Innkeeper()

    def interact(self, player):
        # Welcome message only on first visitprint("Welcome to the Starlight Inn!")
        self.innkeeper.welcome()
        
        count = 0

        while True:
            user_input = input("""What would you like to do at the inn?
            1. Rent a room
            2. Have a hot meal
            3. Quests
            4. Leave
            """)
            
            if user_input == "1":
                self.innkeeper.rent_room(player)
                count += 1
            elif user_input == "2":
                self.innkeeper.hot_meal(player)
                count += 1
            elif user_input == "3":
                self.innkeeper.offer_quests(player)
                count += 1
            elif user_input == "4" and count > 0:
                print("Goodbye!")
                break
            elif user_input == "4" and count == 0:
                # player must choose between the first three options before leaving
                print("I am sorry but aren't you forgetting something?")
            else:
                print("Invalid option. Please try again.")