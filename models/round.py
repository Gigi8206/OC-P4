from random import shuffle
from models.player import Player

class Round:
    def __init__(self, players,matches =[], **kwargs):
        self.players = players[:]
        self.convert_players()
        self.matches = matches
        self.convert_matches()
        if not self.matches:
             self.organize_matches()

    def convert_players(self):
        for index, player in enumerate(self.players):
            if type(player) == dict:
                self.players[index] = Player(**player)

    def convert_matches(self):
        for index, match in enumerate(self.matches):
            if type(match[0][0]) == dict:
                self.matches[index][0][0] = Player(**match[0][0])

            if type(match[1][0]) == dict:
                self.matches[index][1][0] = Player(**match[1][0])


    def organize_matches(self):
        current_players = self.players
        # if sum([player.score for player in current_players]) == 0:
        shuffle(current_players)
        self.matches = [
            ([player_pair[0], player_pair[0].score], [player_pair[1], player_pair[1].score])
            for player_pair in zip(current_players[0::2], current_players[1::2])
            if len(player_pair) == 2
        ]

    def __repr__(self) -> str:
        return f"{ [ f'{ match[0][0].first_name } { match[0][0].last_name } vs { match[1][0].first_name } { match[1][0].last_name }' for match in self.matches] }"

    def round_to_json(self):
        return {
            "players": [player.to_json() for player in self.players],
            "matches": [
                ([match[0][0].to_json(), match[0][1]], [match[1][0].to_json(), match[1][1]])
                for match in self.matches
            ],
        }