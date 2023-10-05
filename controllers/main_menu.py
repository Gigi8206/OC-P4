
from views.view_main import MainMenuView
from controllers.tournament import TournamentController
from controllers.player import PlayerController
from controllers.show_data import ShowDataController
from views.tournament import TournamentView
from models.tournament import TournamentManager
from views.view_main import MenuViews
from enum import IntEnum
from models.tournament import Tournament

class MenuOptions(IntEnum):
    ADD_PLAYER = 0,
    ADD_TOURNAMENT = 1,
    LOAD_TOURNAMENT = 2,
    SHOW_DATA = 3,
    EXIT = 4

class MainMenuController:
    def __init__(self):
        self.view = MainMenuView()
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController(self.player_controller.manager)
        self.show_data_controller = ShowDataController(self.player_controller.manager, self.tournament_controller.manager)

    def main_loop(self):
        option = 0
        while option != MenuOptions.EXIT:
            option_string = self.view.display_options()
            try:
                option = int(option_string)
            except ValueError:
                print("Error: You must enter a correct number")
                continue

            if option < 0 or option > 4:
                print("Error: You should enter a valid option")
                continue
            if option == MenuOptions.ADD_PLAYER:
                self.player_controller.add_player()
            elif option == MenuOptions.ADD_TOURNAMENT:
                self.tournament_controller.add_tournament()
            elif option == MenuOptions.LOAD_TOURNAMENT:
                self.tournament_controller.load_tournament()
            elif option == MenuOptions.SHOW_DATA:
                self.show_data_controller.start_loop()
            elif option == MenuOptions.EXIT:
                print("Merci d'avoir utilisé ChessManager")

class MenuTournament(IntEnum):
    ADD_TOURNAMENT = 0,
    LOAD_TOURNAMENT = 1,
    DELETE_TOURNAMENT = 2,
    EXIT =3

    def tournament_menu(self):
        option = 0
        while option != MenuTournament.EXIT:
            option_string = self.tournament_view.tournament_menu
            try:
                option = int(option_string)
            except ValueError:
                print("Error: You must enter a correct number")
                continue

            if option < 0 or option > 4:
                print("Error: You should enter a valid option")
                continue
            if option == "1":
                self.tournament_menu()
            # tournament selection
            if choice == "2":
                if self.tournament.select_tournament():
                    self.players_menu()
            # delete all tournaments
            if choice == "3":
                self.tournament.del_tournament()
            # back to first menu
            if choice == "4":
                self.first_menu()



