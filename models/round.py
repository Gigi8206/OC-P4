import datetime
import json
import random
import copy


class Round:
    def __init__(self, name="", matches=[], start_time=None, end_time=None):
        self.name = name
        self.matches = matches
        self.start_time = start_time
        self.end_time = end_time
        self.matches = []

    def start(self):
        now = datetime.datetime.now()
        self.start_time = now.strftime("%Y-%m-%d %H:%M:%S")

    def end(self):
        now = datetime.datetime.now()
        self.end_time = now.strftime("%Y-%m-%d %H:%M:%S")

    def get_first_round_players(self, tournament):
        players = tournament.players
        random.shuffle(players)
        pairs = zip(*[iter(players)] * 2)
        for pair in pairs:
            self.matches.append(pair)

    def matchmaking_by_points(self, players):
        for i in range(0, len(players), 2):
            if i + 1 < len(players):
                pair = (players[i], players[i + 1])
            else:
                pair = (players[i], None)  # Handle odd number of players
            self.matches.append(pair)
        return self.matches


class RoundEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Round):
            round_dict = {
                'name': obj.name,
                'matches': obj.matches,
                'start_time': obj.start_time,
                'end_time': obj.end_time
            }
            return round_dict
        return super().default(obj)


def round_decoder(obj):
    if 'name' in obj:
        return Round(
            name=obj['name'],
            matches=obj['matches'],
            start_time=obj['start_time'],
            end_time=obj['end_time']
        )
    return obj


class RoundManager:
    def __init__(self):
        self.rounds = []
        self.round_instance = 1

    def create_rounds(self, tournament):
        for _ in range(tournament.nb_rounds):
            round_name = f"round{self.round_instance}"
            round_instance = Round(name=round_name)
            round_instance.start()
            tournament.rounds.append(round_instance)

            self.round_instance += 1

    def update_tournaments_rounds_file(self, tournament):
        with open('tournaments.json', 'r') as file:
            data = json.load(file)

        tournament_list = data
        for t in tournament_list:
            if t['tournament_name'] == tournament.tournament_name:
                # Create a deep copy of the tournament object to break circular reference
                updated_tournament = copy.deepcopy(tournament)

                # Update the rounds of the tournament
                updated_tournament.rounds = [
                    round_obj.__dict__ for round_obj in tournament.rounds]

                # Update the players
                updated_tournament.players = copy.deepcopy(tournament.players)

                # Update the tournament object in the data list
                t.update(updated_tournament.__dict__)
                break

        with open('tournaments.json', 'w') as file:
            json.dump(data, file, indent=4)

    def set_score(self, result, player1, player2):
        if result == 1:
            player1['points'] += 1
            player1['opponents'].append(player2['identification'])
            player2['opponents'].append(player1['identification'])
        elif result == 2:
            player2['points'] += 1
            player1['opponents'].append(player2['identification'])
            player2['opponents'].append(player1['identification'])
        elif result == 3:
            player1['points'] += 0.5
            player2['points'] += 0.5
            player1['opponents'].append(player2['identification'])
            player2['opponents'].append(player1['identification'])
            return player1, player2

        else:
            print("Invalid input. Please choose 1, 2, or 3.")

    def sort_by_points(self, players):
        return sorted(players, key=lambda player: player['points'], reverse=True)
