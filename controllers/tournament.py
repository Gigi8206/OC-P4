from datetime import datetime
from controllers.input import Input
from models.tournament import Tournament
from models.tournament import TournamentManager
from views.tournament import TournamentView as View
from views.view_main import MainMenuView
import json


class TournamentController:
    """Create a new tournament controller."""

    def __init__(self, player_manager):
        """Init."""
        self.view = View()
        self.manager = TournamentManager()
        self.player_manager = player_manager
        self.menu_view = MainMenuView()
        self.timer = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def add_tournament(self):
        """Create a new tournament."""
        name = input("Please enter tournament's name : ").strip()
        location = Input.for_word("Please enter tournament's location : ")
        date = datetime.today().date()
        nb_rounds = 4
        desc = input("Please enter tournament's description : ")

        try:
            players = self.create_list_players()
        except ValueError as error:
            print(error)
            return print("\n A New Tournament has been created.\n")

        tournament = Tournament(
            name, location, date, players, nb_rounds=nb_rounds, desc=desc
        )
        self.manager.add_tournament(tournament)
        return "main menu"

    def load_tournament(self):
        print("Tournaments available:")
        for tournament in self.manager.tournaments:
            print(tournament)
        name = self.view.input_tournament()
        tournament = self.manager.get_by_name(name)
        if not tournament:
            self.view.display_tournament_not_found()
            return
        print(f"Welcome to {tournament.name}")

        # TODO: Continuer de charger le tournoi
        self.loop_round(tournament)


    def loop_round(self, tournament):
        while tournament.current_round < tournament.nb_rounds:
            result = self.view.input_ask_next_round(tournament.current_round)
            while result not in ("yes", "no"):
                result = self.view.input_ask_next_round(tournament.current_round)

            if result == "no":
                return

            round_results = []  # Liste pour stocker les résultats de chaque match

            for index, match in enumerate(tournament.rounds[tournament.current_round].matches):
                print(
                    "Match {}: {} {} vs {} {}".format(
                        index,
                        match[0][0].first_name,
                        match[0][0].last_name,
                        match[1][0].first_name,
                        match[1][0].last_name,
                    )
                )

                winner = -1
                while winner not in range(3):
                    winner = input(
                        f"0: {match[0][0].first_name} {match[0][0].last_name}\n"
                        f"1: {match[1][0].first_name} {match[1][0].last_name}\n"
                        "2: Egalité\n"
                        "Qui gagne ? "
                    )
                    try:
                        winner = int(winner)
                    except ValueError:
                        print("L'option choisie n'est pas un nombre")

                    if winner not in range(3):
                        print("Option invalide")

                if winner == 0:
                    match[0][0].score += 1
                    match[0][1] += 1
                elif winner == 1:
                    match[1][0].score += 1
                    match[1][1] += 1
                else:
                    match[0][0].score += 0.5
                    match[0][1] += 0.5
                    match[1][0].score += 0.5
                    match[1][1] += 0.5

                # Ajout des résultats de ce match à la liste round_results
                round_results.append({
                    "Match": f"{match[0][0].first_name} {match[0][0].last_name} vs {match[1][0].first_name} {match[1][0].last_name}",
                    "Winner": winner
                })

            with open(f"Round_{tournament.current_round}_results.json", "w") as file:
                json.dump(round_results, file)

            self.manager.save_tournaments()
            tournament.current_round += 1

            # Marquer le tour comme terminé si c'est le dernier tour
            if tournament.current_round == tournament.nb_rounds:
                print("Fin du tournoi ! Bravo à tous les participants")
                return

            # Passer au tour suivant si tous les matchs sont finis
            result = self.view.input_ask_next_round(tournament.current_round)
            while result not in ("yes", "no"):
                result = self.view.input_ask_next_round(tournament.current_round)

            if result == "no":
                return

            tournament.get_next_round()
            self.manager.save_tournaments()
            tournament.get_next_round()
            tournament.current_round += 1
        print("Fin du tournoi ! Bravo à tous les participants")

    def create_list_players(self):
        """Create a list of 8 players from the database."""
        print("CHOOSE 8 PLAYERS FROM THE DATABASE\n")

        if len(self.player_manager.players) < 8:
            raise ValueError("Error: Please add at least eight players first")

        players = []
        players_available = self.player_manager.players.copy()  # Copie de la liste des joueurs disponibles

        for _ in range(8):
            available_indices = [i for i, player in enumerate(players_available) if player not in players]
            for index in available_indices:
                print(f"{index}: {players_available[index]}")

            while True:
                numero = self.view.choose_user(len(available_indices) - 1)
                if numero in available_indices:
                    break
                else:
                    print("Invalid player selection. Please choose a valid index.")

            player = players_available[numero]
            players.append(player)

        return players

