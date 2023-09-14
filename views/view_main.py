class MainMenuView:
    def display_options(self):
        print(
            "Select an option:\n"\
            "0: Add player\n"\
            "1: Add tournament\n"\
            "2: Load tournament\n"\
            "3: Show data\n"\
            "4: Exit\n"
        )
        return input("Your choice ? ")

class ReportMenuView:
    def select_report(self):
        return input(
            "Please choose an option to continue:\n"
            "0: All players by name (A-Z)\n"
            "1: Tournament's list\n"
            "2: Tournament's name and date \n"
            "3: Tournament's players by name (A-Z)\n"
            "4: All tournament's rounds and matches\n"
            "5: Main Menu\n"
            "Your choice ? "
        )
    def display_players(self):
        print(Tournament.players)

    def tournaments_names(self):
        for name in Tournament.tournament_names:
            print(name)

    def names_and_dates(self):
        print(Tournament.tournament_dict)

    def display_all_players(self, players):
        print("**********************")
        print("All players by name : ")
        print("**********************")
        sorted_players = sorted(players,
                                key=lambda
                                player: player.last_name)
        for player in sorted_players:
            print(player)
            print("**********************")

    @staticmethod
    def display_tournament_players():
        print("**********************")
        print("Tournament's players by name : ")
        print("**********************")

    def player_infos(player):
        print(
            f"Name:{player['first_name']} {player['last_name']} Id: {player['identification']} Points: {player['points']}")
        ("**************************************")

    @staticmethod
    def show_tournaments_list(tournaments):
        print("**************************************")
        print('Tournament name || Date || Place')
        print("**************************************")
        for tournament in tournaments:
            print(
                f"{tournament.name}||{tournament.date}|| {tournament.place}||")
            print("**************************************")

    def show_tournaments(tournament):
        print("**************************************")
        print('Tournament name || Start time || place')
        print("**************************************")
        print(
            f"{tournament.tournament_name}||{tournament.start_time}|| {tournament.place}||")

    def rounds(round):
        print(f"{round.name}")

    def matches(player1, player2):
        print(
            f"Match: {player1.name}{player1.points} vs {player1.name} {player2.points}")
