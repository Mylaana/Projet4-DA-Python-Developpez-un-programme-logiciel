"""
Tournament class module
"""
import random


class Round:
    """
    manage round infos
    """
    def __init__(self, player_list: list):
        self.player_score_round = {}
        self.player_score_total_start_of_round = []
        self.player_score_total_end_of_round = {}
        self.player_list = player_list
        self.pairing_list = []

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
        unpaired_players = self.player_list

        while unpaired_players:
            player_a = str(random.choice(unpaired_players))
            unpaired_players.remove(player_a)

            player_b = random.choice(unpaired_players)
            unpaired_players.remove(player_b)

            self.pairing_list.append(str(player_a) + "-" + str(player_b))

    def pairings_descending_score(self):
        """
        create parings following descendig scores
        """
        unpaired_players = self.player_list

        while unpaired_players:
            player_a = str(random.choice(unpaired_players))
            unpaired_players.remove(player_a)

            player_b = random.choice(unpaired_players)
            unpaired_players.remove(player_b)

            self.pairing_list.append(str(player_a) + "-" + str(player_b))
