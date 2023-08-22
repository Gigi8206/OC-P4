from controllers.tournament import TournamentController
from controllers.input import Input
from models.round import Round
from models.tournament import Tournament
from views.tournament import TournamentView as View


class LoadTournamentController:
    """To continue an unfinished tournament."""
    def __init__(self):
        """Init."""
        self.view = View()
        self.tournament = None

    def display(self):
        tournament = self.tournament
        if not tournament:
            print("The value entered doesn't match any tournament !\n")

    def load_tournament(self):
        "Choose a uncompleted tournament in the database."
        tournament = self.tournament
        if not tournament:
            name = Input.for_string("Name of an Uncompleted tournament ? ")
            tournament = Tournament.get(name)
        if not tournament:
            return ""

