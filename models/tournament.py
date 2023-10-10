from models.player import Player
from dateutil import parser
from models.round import Round
from random import shuffle
from json import dump, load
import os
import json

class Tournament:
    def __init__(self, name="", place=None, date=None,
                 players=[], rounds=[], nb_rounds=4, desc=""):
        self.name = name
        self.place = place
        self.date = date
        self.players = players
        self.nb_rounds = nb_rounds
        self.rounds = rounds
        self.desc = desc

        self.players = players[:]
        self.convert_players()
        self.rounds = rounds[:] # Passing by copy, not reference to avoid strange reference
        self.convert_rounds()
        
        if not self.rounds:
            self.reset_scores()
            self.get_next_round()
        
    def __str__(self):
        return f"Tournoi: {self.name}"

    def convert_players(self):
        for index, player in enumerate(self.players):
            if type(player) == dict:
                self.players[index] = Player(**player)

    def convert_rounds(self):
        for index, round in enumerate(self.rounds):
            if type(round) == dict:
                self.rounds[index] = Round(**round)

    def tournament_to_json(self):
       return {  "name": self.name,
            "place": self.place,
            "date": self.date.isoformat(),
            "players": [player.to_json() for player in self.players],
            "rounds": [round.round_to_json() for round in self.rounds],
            "nb_rounds": self.nb_rounds,
            "desc": self.desc,
        }


    def reset_scores(self):
        for player in self.players:
            player.score = 0

    def get_next_round(self):
        if len(self.rounds) < self.nb_rounds:
            self.rounds.append(Round(self.players))


class TournamentManager:
    def __init__(self):
        self.tournaments = self.load_tournaments_from_file()

    def add_tournament(self, tournament: Tournament):
        if type(tournament) is not Tournament:
            raise ValueError("add tournament")

        self.tournaments.append(tournament)
        with open("tournament.json", "w", encoding="utf-8") as tournament_file:
            dump(
                [tournament.tournament_to_json() for tournament in self.tournaments],
                tournament_file,
                ensure_ascii=False, indent=4
            )

    def load_tournaments_from_file(self):
        if not os.path.exists('tournament.json'):
            return []
        
        with open('tournament.json', 'r') as file:
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

