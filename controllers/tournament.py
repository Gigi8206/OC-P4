from datetime import datetime
from controllers.input import Input
from models.tournament import Tournament
from models.tournament import TournamentManager
from views.tournament import TournamentView as View
from views.view_main import MainMenuView
from models.player import Player
import json



class TournamentController():
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

        while tournament.current_rounds < tournament.nb_rounds:
            result = self.view.input_ask_next_round(tournament.current_rounds)
            while result not in ('yes', 'no'):
                result = self.view.input_ask_next_round(tournament.current_rounds)
            if result == 'no':
                return
        for match in tournament.rounds[tournament.current_rounds].matches:
            first_name = Input.for_word("Please enter player's first name: ").capitalize()
            last_name = Input.for_word("Please enter player's last name: ").capitalize()
            for player in match:
                score = input(f"Quel est le score du joueur {player.first_name} {player.last_name} ? ")
                player = Player(first_name=first_name, last_name=last_name)
                player[1] = score



        tournament.current_round += 1
        tournament.get_next_round()


    def create_list_players(self):
        """Create a list of 8 players from the database."""
        print("CHOOSE 8 PLAYERS FROM THE DATABASE\n")

        if len(self.player_manager.players) < 8:
            raise ValueError("Error: Please add at least eight players first")

        players = []
        for index in range(8):
            players_available = [player for player in self.player_manager.players if player not in players]
            for index, player in enumerate(players_available):
                print(f"{index}: {player}")
            numero = self.view.choose_user(index)
            player = players_available[numero]
            players.append(player)
        return players


