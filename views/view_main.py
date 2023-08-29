class MainMenuView:
    def display_options(self):
        print(
            "Select an option:\n"\
            "0: Add player\n"\
            "1: Add tournament\n"\
            "2: Load tournament\n"\
            "3: Show data\n"\
            "4: Exit\n"
        )
        return input("Your choice ? ")