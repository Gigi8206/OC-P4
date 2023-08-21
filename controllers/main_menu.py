from views.view_main import MainMenuView
from controllers.tournament import TournamentController
from controllers.player import PlayerController
from enum import IntEnum

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
        print("Merci d'avoir utilisé ChessManager")