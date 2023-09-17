from controllers.input import Input

class TournamentView:
    def display(self):
        """Display the creation of a new tournament."""
        print("\n==================================================")
        print("************CREATE A NEW TOURNAMENT**************\n")

    def display_menu(self):
        """Display the menu between 2 rounds during a tournament."""
        print("\n==================================================")
        print("\n What would you like to do ?")
        print("1 - CONTINUE THE TOURNAMENT")
        print("2 - Change the ranking from a player ?")
        print("3 - End the tournament and return to the general menu")

    def display_final_score(self, players):
        """Display the final menu with the final score of the tournament."""
        print("\n==================================================")
        print(f"FINAL RESULTS OF {self.name} :\n")
        for player in players:
            print(f"SCORE : {player.points}, {player.first_name} {player.last_name}")
        print("\n==================================================")

    def display_next_round(self, i, j):
        """Display a match of a round different to the 1st round."""
        print(f"{self[i].first_name} vs {self[j].first_name}")
    def input_tournament_name(self):
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
    def ask_for_tournament(tournaments):

        return input('Which tournament do you want to load ? ')

    def tournament_loaded(self):
        print("Tournament loaded from DataBase")

    
    def display_tournament_not_found(self):
        print("Error: Tournament not found")

    def choose_user(self, index):
        "Choose a player from the database to play in a tournament."
        message = f"Select your player: "
        numero = Input.for_integer(message)
        return numero
    def all_players():
        print("all players by name")

