from controllers.input import Input

class TournamentView:

    @staticmethod
    def input_tournament_name():
        tournament_name = input("Enter tournament's name: ")
        return tournament_name

    def input_tournament(self):
        "Choose a uncompleted tournament in the database."
        return input("Name of an uncompleted tournament ? ")

    @staticmethod
    def show_tournaments_name_date(tournaments):
        for tournament in tournaments:
            name = tournament.tournament_name
            start_time = tournament.start_time
            print(f"Tournament: {name}\tStart Time: {start_time}")

    @staticmethod
    def tournament_menu(self):
        return input(
            "Please choose an option to continue:\n"
            "0: Add player(s) to a tournament\n"
            "1: Start tournament\n"
            "2: End tournament\n"
            "3: Return to menu\n"
            "Your choice ? "
        )

    def choose_user(self, index):
        "Choose a player from the database to play in a tournament."
        message = f"Select your player: "
        numero = Input.for_integer(message)
        return numero

    def display_tournament_not_found(self):
        print("Error: Tournament not found")


