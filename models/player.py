from json import dump, load
from dateutil import parser
import json

class Player:
    def __init__(self, **kwargs):
        self.first_name = kwargs.get("first_name", None)
        self.last_name = kwargs.get("last_name", None)
        self.birthday = kwargs.get("birthday", None)
        self.convert_birthday()
        self.identifier = kwargs.get("identifier", None)
        self.score = 0

    def __repr__(self):
        return f"{self.first_name} {self.last_name}: {self.identifier} - {self.birthday.isoformat()} - {self.score}"

    def convert_birthday(self):
        if type(self.birthday) == str:
            self.birthday = parser.parse(self.birthday).date()

    def to_json(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthday": self.birthday.isoformat(),
            "identifier": self.identifier,
            "score": self.score
        }


class PlayerManager:
    def __init__(self):
        self.players = self.load_players()

    def load_players(self):
        # Deserialization from json
        try:
            with open('players.json', 'r', encoding="utf-8") as player_file:
                players = load(player_file)
                return [Player(**player_dict) for player_dict in players]
        except FileNotFoundError:
            return []

    def add_player(self, player: Player):
        # Serialization to json
        if type(player) is not Player:
            raise ValueError("Add player should take a player")

        self.players.append(player)
        with open('players.json', 'w', encoding="utf-8") as player_file:
            json.dump(
                [player.to_json() for player in self.players],
                player_file,
                ensure_ascii=False, indent=4
            )
        return player


