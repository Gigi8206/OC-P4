from datetime import datetime

from views.view_main import MainMenuView
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from models.player import Player
class MatchController():
    def run_round(self):
        """Lance un tour et appelle la vue TournamentView"""
