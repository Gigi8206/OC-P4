from models.round import Round
from random import shuffle
from json import dump


class Tournament:
    def __init__(self, name, place, date, players, nb_rounds=4, desc=""):
        self.name = name
        self.place = place
        self.date = date
        self.players = players
        self.nb_rounds = nb_rounds
        self.rounds = []
        self.desc = desc

    def __str__(self):
        return f"Tournoi: {self.name}"

    def to_json(self):
        return {
            "name": self.name,
            "place": self.place,
            "date": self.date.isoformat(),
            "players": [player.to_json() for player in self.players],
            "nb_rounds": self.nb_rounds,
            "rounds": self.rounds,
            "desc": self.desc,
        }


class TournamentManager:
    def __init__(self):
        self.tournaments = []

    def add_tournament(self, tournament: Tournament):
        if type(tournament) is not Tournament:
            raise ValueError("add tournament")

        self.tournaments.append(tournament)
        with open("tournament.json", "w", encoding="utf-8") as tournament_file:
            dump(
                [tournament.to_json() for tournament in self.tournaments],
                tournament_file,
                ensure_ascii=False,
            )

    def get_by_name(self, name):
        for tournament in self.tournaments:
            if tournament.name == name:
                return tournament