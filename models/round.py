from random import shuffle
from models.player import Player
from itertools import groupby


class Round:
    def __init__(self, players, matches=[], last_pairs=[], **kwargs):
        self.players = players[:]
        self.convert_players()
        self.matches = matches
        self.convert_matches()
        if not self.matches:
            self.organize_matches(last_pairs=last_pairs)

    def convert_players(self):
        for index, player in enumerate(self.players):
            if type(player) is dict:
                self.players[index] = Player(**player)

    def convert_matches(self):
        for index, match in enumerate(self.matches):
            if type(match[0][0]) is dict:
                self.matches[index][0][0] = Player(**match[0][0])

            if type(match[1][0]) is dict:
                self.matches[index][1][0] = Player(**match[1][0])

    def organize_matches(self, last_pairs=[]):
        current_players = self.players
        if sum([player.score for player in current_players]) == 0:
            shuffle(current_players)
            self.matches = [
                (
                    [player_pair[0], player_pair[0].score],
                    [player_pair[1], player_pair[1].score],
                )
                for player_pair in zip(current_players[0::2], current_players[1::2])
                if len(player_pair) == 2
            ]
        else:
            groups = []
            current_players = sorted(current_players, key=lambda player: player.score, reverse=True)
            for _, g in groupby(current_players, lambda player: player.score):
                groups.append(list(g))
            for group in groups:
                if len(group) > 2:
                    shuffle(group)
            current_players = [player for group in groups for player in group]
            for _ in range(int(len(self.players) / 2)):
                next_opponent = 1
                left_player = current_players[0]
                right_player = current_players[next_opponent]
                for round in last_pairs:
                    for match in round:
                        if match[0] == left_player and match[1] == right_player:
                            next_opponent += 1
                            if next_opponent < len(current_players):
                                right_player = current_players[next_opponent]
                            else:
                                next_opponent = 1
                                break
                right_player = current_players.pop(next_opponent)
                left_player = current_players.pop(0)
                self.matches.append(
                    (
                        [left_player, left_player.score],
                        [right_player, right_player.score],
                    )
                )

    def __repr__(self) -> str:
        return "{}".format(
            [
                "{} {} vs {} {}".format(
                    match[0][0].first_name,
                    match[0][0].last_name,
                    match[1][0].first_name,
                    match[1][0].last_name,
                )
                for match in self.matches
            ]
        )

    def round_to_json(self):
        return {
            "players": [player.to_json() for player in self.players],
            "matches": [
                (
                    [match[0][0].to_json(), match[0][1]],
                    [match[1][0].to_json(), match[1][1]],
                )
                for match in self.matches
            ],
        }