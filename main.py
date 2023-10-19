from views.view_main import MainMenuView
from controllers.main_menu import MainMenuController


def main():
    MainMenuView.app_title()
    main_menu_controller = MainMenuController()
    main_menu_controller.main_loop()


if __name__ == "__main__":
    main()
