from enum import IntEnum
from views.tournament import TournamentView
from models.player import PlayerManager
from models.round import RoundManager
from models.tournament import Tournament, TournamentManager

class ActionMenuOptions(IntEnum):
    UNASSIGNED = -1
    ADD_PLAYER = 0
    START_TOURNAMENT = 1
    END_TOURNAMENT = 2
    EXIT = 3

class ActionMenuController:
    def __init__(self, ):
        self.view = TournamentView()
        self.tournament = None
        self.player_manager = PlayerManager()
        self.tournament_manager = TournamentManager()
        self.round_manager = RoundManager()
        self.tournaments = self.tournament_manager.load_tournaments_from_file()
        self.tournament_name = None
    def start_loop(self):
