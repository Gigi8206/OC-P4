from controllers.main_menu import MainMenuController
from controllers.input import Input

def main():
    main_menu_controller = MainMenuController()
    main_menu_controller.main_loop()
    
if __name__ == '__main__':
    main()
