from views.view_main import MainMenuView
from controllers.main_menu import MainMenuController
from models.player import Player
from models.tournament import Tournament
from datetime import datetime


def main():
    # players = [Player(first_name="Test", last_name=f"Player { i }", birthday=datetime.now(), identifier="AA" + f"{i}" * 5) for i in range(1, 9)]
    # tournament = Tournament(name="Grand Tournoi", place="Paris", date=datetime.now(), players=players)
    # print(tournament)
    MainMenuView.app_title()
    main_menu_controller = MainMenuController()
    main_menu_controller.main_loop()

if __name__ == '__main__':
    main()
