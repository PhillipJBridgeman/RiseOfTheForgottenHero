class Player_Options:
    def __init__(self, player):
        self.player = player

    def display_options(self):
        while True:
            user_input = input("""What would you like to do?
1. Go to the Inn
2. Go to the Town
3. Rest
4. Review your Stats
5. Read Lore
6. Review Inventory
7. Save Game
8. Quit
""")

            if user_input == "1":
                from inn import Inn
                # Implement logic to go to the inn
                print("You decided to go back to the inn.")
                inn = Inn()
                inn.interact(self.player)
            elif user_input == "2":
                # Implement logic to go to the town
                pass
            elif user_input == "3":
                # Implement logic to restpasselif user_input == "4":
                self.player.display_stats()
            elif user_input == "5":
                # Implement logic to read lorepasselif user_input == "6":
                self.player.display_inventory()
            elif user_input == "7":
                # Implement logic to save game
                pass
            elif user_input == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
