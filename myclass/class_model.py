"""
Tournament class module
"""


class Round:
    """
    manage round infos
    """
    def __init__(self, player_score_total_start_of_round: dict):
        self.player_score_round = {}
        self.player_score_total_start_of_round = player_score_total_start_of_round
        self.player_score_total_end_of_round = {}

    def generate_round_pairings(self, player_list: list):
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


class Player:
    """
    player class
    """
    def __init__(self,
                 player_id: int,
                 name: str = "",
                 family_name: str = "",
                 birth_date: str = "",
                 rank: str = "",
                 ):
        self.name = name
        self.family_name = family_name
        self.birth_date = birth_date
        self.rank = rank

        self._id = player_id
        self._already_paired_players_id = []

    def get_player_info(self):
        """
        returns player info as a string
        """
        return "name : " + self.name + "  rank : " + self.rank + " "
