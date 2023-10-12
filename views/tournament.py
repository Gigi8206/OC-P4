from controllers.input import Input

class TournamentView:

    @staticmethod
    def input_tournament_name():
        tournament_name = input("Enter tournament's name: ")
        return tournament_name

    def input_tournament(self):
        print("Choose a uncompleted tournament in the database.")
        return input("Name of an uncompleted tournament ? ")

    def input_ask_next_round(self, nb_round):
        return input(f"Do you want to launch round { nb_round } (yes / no) ? ")

    @staticmethod
    def show_tournaments_name_date(tournaments):
        for tournament in tournaments:
            name = tournament.tournament_name
            start_time = tournament.start_time
            print(f"Tournament: {name}\tStart Time: {start_time}")

    @staticmethod
    def tournament_menu(self):
        return input(
            ("Menu tournoi : Tapez le numéro de votre choix : \n"
             "1 - Créer un nouveau tournoi \n"
             "2 - Récupérer tournoi existant \n"
             "3 - Supprimer les tournois \n"
             "4 - Retour au menu principal \n")
        )

    def choose_user(self, index):
        "Choose a player from the database to play in a tournament."
        message = f"Select your player: "
        numero = Input.for_integer(message)
        return numero

    def display_tournament_not_found(self):
        print("Error: Tournament not found")


