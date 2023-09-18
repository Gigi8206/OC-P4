from controllers.input import Input

class TournamentView:
    @staticmethod
    def input_tournament_name():
        tournament_name = input("Enter tournament's name: ")
        return tournament_name

    def input_tournament(self):
        "Choose a uncompleted tournament in the database."
        return input("Name of an uncompleted tournament ? ")

    @staticmethod
    def show_tournaments_name_date(tournaments):
        for tournament in tournaments:
            name = tournament.tournament_name
            start_time = tournament.start_time
            print(f"Tournament: {name}\tStart Time: {start_time}")





