from views.view_main import ReportMenuView
from models.player import PlayerManager
from views.tournament import TournamentView
import json


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


    def start_loop(self):
        user_input = input().lower()
        option_selected = None
        while option_selected != ReportsMenuOptions.EXIT:
            option_selected = int(self.view.select_report())
            if option_selected == ReportsMenuOptions.ALL_PLAYERS:
                ReportMenuView.display_all_players(self.player_manager.players)
            if option_selected == ReportsMenuOptions.TOURNAMENT_LIST:
                ReportMenuView.show_tournaments_list(self.tournament_manager.tournaments)
            if option_selected == ReportsMenuOptions.TOURNAMENT_DATE_NAME:
                ReportMenuView.show_tournaments_name_date(self.tournament_manager.tournaments)
            if option_selected == ReportsMenuOptions.TOURNAMENT_PLAYERS:
                ReportMenuView.display_tournament_players(self.tournament_manager.tournaments)
            if option_selected == ReportsMenuOptions.TOURNAMENT_ROUNDS_MATCHES:
                tournament_name = TournamentView.input_tournament_name()
                for tournament in self.tournament_manager.tournaments:
                    if tournament_name == tournament.name:
                        print("Tournament:", tournament.name)
                        for round in tournament.rounds:
                            print("Round:", round.name)
                            for match in round.matches:
                                print(f"Match: { match }")
            if user_input == "y":
                exit()
            elif user_input == "n":
                (self.start_loop())

    @staticmethod
    def back_to_menu():
        from controllers.main_menu import MainMenuController
        MainMenuController.start_loop()




