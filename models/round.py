from random import shuffle

class Round:
    def __init__(self, players):
        self.players = players
        self.matches = self.organize_matches()

    def organize_matches(self):
        current_players = self.players
        # if sum([player.score for player in current_players]) == 0:
        shuffle(current_players)
        return [
            ([player_pair[0], player_pair[0].score], [player_pair[1], player_pair[1].score])
            for player_pair in zip(current_players[0::2], current_players[1::2])
            if len(player_pair) == 2
        ]

    def __repr__(self) -> str:
        return f"{ [ f'{ match[0][0].first_name } { match[0][0].last_name } vs { match[1][0].first_name } { match[1][0].last_name }' for match in self.matches] }"