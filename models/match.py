from random import choice

class Match:
    def __init__(self, name, players_pair):
        self.player1 = players_pair[0]
        self.score_player1 = 0
        self.color_player1 = ""
        self.player2 = players_pair[1]
        self.score_player2 = 0
        self.color_player2 = ""
        self.winner = ""
        self.name = name

    def __repr__(self):
        return str(([self.player1, self.score_player1],
                    [self.player2, self.score_player2]))

    def assign_colors(self):
        if choice([True, False]):
            self.color_player1 = "Blanc"
            self.color_player2 = "Noir"
        else:
            self.color_player1 = "Noir"
            self.color_player2 = "Blanc"

    def play_match(self):

        # Assignation des couleurs
        self.assign_colors()
