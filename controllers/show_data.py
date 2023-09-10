from views.view_main import ReportMenuView
from models.tournament import TournamentManager
from controllers.tournament import TournamentController
from models.player import PlayerManager
from views.tournament import TournamentView


class ReportsMenuOptions():
    ALL_PLAYERS = 0
    TOURNAMENT_LIST = 1
    TOURNAMENT_DATE_NAME = 2
    TOURNAMENT_PLAYERS = 3
    TOURNAMENT_ROUNDS_MATCHES = 4
    EXIT = 5


class ShowDataController:
    def __init__(self, player_manager, tournament_manager) -> None:
        self.player_manager = player_manager
        self.tournament_manager = tournament_manager
        self.view = ReportMenuView()
        self.tournament_list = None
        self.tournament_date_name = None
        self.tournament_players = None
        self.rounds_matches = None
        self.file_name = 'tournament.json'

    def start_loop(self):
        option_selected = ReportsMenuOptions
        while option_selected != ReportsMenuOptions.EXIT:
            option_selected = int(self.view.select_report())
            if option_selected == ReportsMenuOptions.ALL_PLAYERS:
                TournamentView.all_players()
            players = PlayerManager.load_players(self)
            self.view.display_all_players(players)
            if option_selected == ReportsMenuOptions.TOURNAMENT_LIST:
                tournament = self.tournament_manager.load_tournaments_from_file()
                self.view.show_tournaments_list(tournament)

            if option_selected == ReportsMenuOptions.TOURNAMENT_DATE_NAME:
                tournament = self.tournament_manager.load_tournaments_from_file()
