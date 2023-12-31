from models.player import Player, PlayerManager
from views.player import CreatePlayer as View
from controllers.input import Input


class PlayerController:
    """Create a new player controller."""

    def __init__(self):
        self.view = View()
        self.manager = PlayerManager()

    def display(self):
        self.view.display()

    def add_player(self):
        """Create a new player."""
        first_name = Input.for_word("Please enter player's first name: ").capitalize()
        last_name = Input.for_word("Please enter player's last name: ").capitalize()
        birthday = Input.birthday(
            "Please enter player's birth date (format = DD/MM/YYYY): "
        )
        identifier = Input.for_identifier(
            "Please enter player's identifier (ex: AB12345): "
        )
        print("\n A player has been created.\n")
        player = Player(
            first_name=first_name,
            last_name=last_name,
            birthday=birthday,
            identifier=identifier,
        )
        result = self.manager.add_player(player)
        return result
