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

    @staticmethod
    def tournament_menu(self):
        return input(
            "Please choose an option to continue:\n"
            "0: Add player(s) to a tournament\n"
            "1: Start tournament\n"
            "2: End tournament\n"
            "3: Return to menu\n"
            "Your choice ? "
        )
    @staticmethod
    def display_all_players(players):
        print("**********************")
        print("All players by name : ")
        print("**********************")
        sorted_players = sorted(players,
                                key=lambda
                                player: player.last_name)
        for player in sorted_players:
            print(player)
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

    @staticmethod
    def show_tournaments_name_date(tournaments):
        for tournament in tournaments:
            print(
                f"{tournament.name}||{tournament.date}||")
            print("**************************************")

    @staticmethod
    def display_tournament_players(tournaments):
        for tournament in tournaments:
            print(f"Tournament { tournament.name}")
            print("**************************************")
            for player in tournament.players:
                print(f"{ player }")
            print("**************************************")

    def rounds(round):
        print(f"{round.name}")

    def matches(player1, player2):
        print(
            f"Match: {player1.name}{player1.points} vs {player1.name} {player2.points}")
