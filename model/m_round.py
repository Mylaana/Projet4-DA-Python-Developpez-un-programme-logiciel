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
        self.round_counter = 1
        self.round_max_number = round_max_number
        self.player_list_id = []
        self.current_round = None

    def create_new_round(self):
        """
        Generates new round and player pairings.
        Returns None
        """

        print("round number : " + str(self.round_counter))

        self.current_round = Round(self.player_list_id)
        self.current_round.generate_round_pairings(is_first_round=self.round_counter == self.round_counter)
        self.round_list.append(self.current_round)
        self.round_counter += 1

        return self.round_counter > self.round_max_number

    def get_current_round_pairings(self) -> list:
        """
        gets none
        returns current round pairings as list like :
        str(Table 1 :)
        str('playerA - playerB')
        str(Table 2 :)
        str('playerA - playerB')
        """
        return self.current_round.pairing_list


class Round:
    """
    manage round infos
    """
    def __init__(self, player_list_id: list):
        self.player_score_round = {}
        self.player_score_total_start_of_round = []
        self.player_score_total_end_of_round = {}
        self.player_list_id = player_list_id
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
        unpaired_players = self.player_list_id

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
        unpaired_players = self.player_list_id

        while unpaired_players:
            player_a = str(random.choice(unpaired_players))
            unpaired_players.remove(player_a)

            player_b = random.choice(unpaired_players)
            unpaired_players.remove(player_b)

            self.pairing_list.append(str(player_a) + "-" + str(player_b))
