from models.player import Player
from dateutil import parser
from models.round import Round
from json import dump, load
import os


class Tournament:
    def __init__(
        self,
        name="",
        place=None,
        date=None,
        players=[],
        rounds=[],
        nb_rounds=4,
        desc="",
        current_round=0,
    ):
        self.name = name
        self.place = place
        self.date = date
        self.convert_date()
        self.nb_rounds = nb_rounds
        self.desc = desc
        self.current_round = current_round

        self.players = players[:]
        self.convert_players()
        self.rounds = rounds[
            :
        ]  # Passing by copy, not reference to avoid strange reference
        self.convert_rounds()

        if not self.rounds:
            self.reset_scores()
            self.get_next_round()

    def __str__(self):
        return f"Tournoi: {self.name}"

    def convert_date(self):
        if type(self.date) is str:
            self.date = parser.parse(self.date)

    def convert_players(self):
        for index, player in enumerate(self.players):
            if type(player) is dict:
                self.players[index] = Player(**player)

    def convert_rounds(self):
        for index, round in enumerate(self.rounds):
            if type(round) is dict:
                self.rounds[index] = Round(**round)

    def tournament_to_json(self):
        # print(self.date.isoformat())
        return {
            "name": self.name,
            "place": self.place,
            "date": self.date.isoformat(),
            "players": [player.to_json() for player in self.players],
            "rounds": [round.round_to_json() for round in self.rounds],
            "nb_rounds": self.nb_rounds,
            "desc": self.desc,
            "current_round": self.current_round,
        }

    def reset_scores(self):
        for player in self.players:
            player.score = 0

    def get_next_round(self):
        last_pairs = []
        if len(self.rounds) < self.nb_rounds:
            if len(self.rounds) >= 1:
                for round in self.rounds:
                    last_pairs.append(
                        [[match[0][0], match[1][0]] for match in round.matches]
                    )
            self.rounds.append(Round(self.players, last_pairs=last_pairs))


class TournamentManager:
    def __init__(self):
        self.tournaments = self.load_tournaments_from_file()

    def add_tournament(self, tournament: Tournament):
        if type(tournament) is not Tournament:
            raise ValueError("add tournament")

        self.tournaments.append(tournament)
        self.save_tournaments()

    def save_tournaments(self):
        with open("tournament.json", "w", encoding="utf-8") as tournament_file:
            dump(
                [tournament.tournament_to_json() for tournament in self.tournaments],
                tournament_file,
                ensure_ascii=False,
                indent=4,
            )

    def load_tournaments_from_file(self):
        if not os.path.exists("tournament.json"):
            return []

        with open("tournament.json", "r") as file:
            tournaments_data = load(file)

        self.tournaments = []
        for data in tournaments_data:
            tournament = Tournament(**data)
            self.tournaments.append(tournament)
        return self.tournaments

    def load_tournament_by_name(self, tournament_name):
        tournaments = self.load_tournaments_from_file()
        for tournament in tournaments:
            if tournament.tournament_name == tournament_name:
                self.tournament = tournament
                return tournament
        return None

    def get_by_name(self, name):
        for tournament in self.tournaments:
            if tournament.name == name:
                return tournament