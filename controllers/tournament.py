from datetime import datetime

from controllers.input import Input
from models.tournament import Tournament
from models.tournament import TournamentManager
from views.tournament import TournamentView as View
from models.player import Player


class TournamentController():
    """Create a new tournament controller."""

    def __init__(self, player_manager):
        """Init."""
        self.view = View()
        self.manager = TournamentManager()
        self.player_manager = player_manager

    def display(self):
        self.view.display()

    def add_tournament(self):
        """Create a new tournament."""
        name = Input.for_string("Please enter tournament's name : ")
        location = Input.for_string("Please enter tournament's location : ")
        date = datetime.today().date()
        nb_rounds = 4
        rounds = []
        desc = input("Please enter tournament's description : ")

        try:
            players = self.create_list_players()
        except ValueError as error:
            print(error)
            return

        tournament = Tournament(
            name, location, date, nb_rounds, rounds, desc, players
        )
        self.manager.add_tournament(tournament)

    def choose_users(self, index):
        "Choose a player from the database to play in a tournament."
        player = None
        while not player:
            if len(self.player_manager.players) < 8:
                raise ValueError("Error: Please add at least eight players first")
            for index, player in enumerate(self.player_manager.players):
                print(f"{index}: {player}")
            message = f"PLAYER {index}: Select your player "
            numero = Input.for_string(message).capitalize()
            player = self.player_manager.players[int(numero)]
        return player

    def create_list_players(self):
        """Create a list of 8 players from the database."""
        players = []
        print("CHOOSE 8 PLAYERS FROM THE DATABASE\n")
        for index in range(8):
            player = self.choose_users(index)
            players.append(player)
        return players

