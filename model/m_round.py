"""
Tournament class module
"""
import random


class RoundList:
    """
    Model = tournament class
    """

    def __init__(self, round_max_number: int = 4):
        self.round_list = []
        self.round_counter = 0
        self.round_max_number = round_max_number
        self.player_list_id = []
        self.current_round = None     

    def create_new_round(self):
        """
        Generates new round and player pairings.
        Returns None
        """
        self.round_counter += 1
        self.current_round = Round(self.player_list_id)
        self.current_round.generate_round_pairings(
            is_first_round=self.round_counter == self.round_counter)
        self.round_list.append(self.current_round)

        return self.round_counter >= self.round_max_number

    def get_current_round_pairings(self) -> list:
        """
        gets none
        returns current round pairings as list like :
        str('playerA - playerB')
        str('playerA - playerB')
        """

        return self.current_round.pairing_list

    def set_random_scores(self):
        """
        Gets None
        randoms scores for current round
        for each match, randoms the score of the player_a and deduct the score of player_b
        returns None
        """

        for match in self.current_round.pairing_list:
            player_a_id = int(match.split("-")[0])
            player_a_score = random.choice([0, 0.5, 1])
            player_b_id = int(match.split("-")[1])
            player_b_score = 1.0 - player_a_score
            self.current_round.set_player_score(
                player_id=player_a_id, player_match_result=player_a_score)
            self.current_round.set_player_score(
                player_id=player_b_id, player_match_result=player_b_score)

        for key, values in self.current_round.player_score_round.items():
            print(f"joueur {key}: {values}")


class Round:
    """
    manage round infos
    """

    def __init__(self, player_list_id: list):
        self.player_list_id = player_list_id
        self.pairing_list = []

        # initializing player score at 0
        self.player_score_round = {k: 0.0 for k in self.player_list_id}
        self.player_score_total_start_of_round = self.player_score_round.copy()
        self.player_score_total_end_of_round = self.player_score_round.copy()

    def generate_round_pairings(self, is_first_round: bool = False) -> None:
        """
        calculer nouveau appariement en supprimant de dict.R deux joueurs :
            -prendre le premier joueur de dict.R = joueur.A
            -iterer sur joueur.X de dict.R jusqu'a ne pas trouver joueur.A dans
                le dict.J de joueur.X alors joueur.B = joueur.X
            -pop joueur.B de dict.R
            -next

        for player in player_list:
            print(player.name)
        """
        if is_first_round:
            self.pairings_random()
        else:
            self.pairings_descending_score()

    def pairings_random(self):
        """
        create parings at random
        """
        unpaired_players = self.player_list_id

        while unpaired_players:
            player_a = str(random.choice(unpaired_players))
            unpaired_players.remove(int(player_a))

            player_b = str(random.choice(unpaired_players))
            unpaired_players.remove(int(player_b))
            self.pairing_list.append(str(player_a) + "-" + str(player_b))

    def pairings_descending_score(self):
        """
        create parings following descendig scores
        """
        unpaired_players = self.player_list_id

        while unpaired_players:
            player_a = str(random.choice(unpaired_players))
            unpaired_players.remove(player_a)

            player_b = random.choice(unpaired_players)
            unpaired_players.remove(player_b)

            self.pairing_list.append(str(player_a) + "-" + str(player_b))

    def set_player_score(self, player_id, player_match_result: float):
        """
        gets a player_id and a float(player_match_result)
        updates score for player_id
        returns None
        """
        self.player_score_round[player_id] = player_match_result
        self.player_score_total_end_of_round[player_id] = self.player_score_total_start_of_round[player_id] + \
            self.player_score_round[player_id]
