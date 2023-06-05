"""
model dedicated module
"""
from myclass import class_model as cls


class Model:
    """
    Model = tournament class
    """
    def __init__(self, round_number: int = 4):
        self.name = ""
        self.location = ""
        self.date_start = ""
        self.date_end = ""
        self.round_list = []
        self.round_number = round_number
        self.player_list = []
        self.description = ""

    def create_new_round(self, is_first_round: bool = False):
        """
        Generates new round and player pairings.
        Returns None

        prérequis :
        attribuer a round un dict.R des joueurs classés par score total cumulé décroissant
        attribuer a chaque joueur une liste list.J de ses appariement précédents

        calculer nouveau appariement en supprimant de dict.R deux joueurs :
            -prendre le premier joueur de dict.R = joueur.A
            -iterer sur joueur.X de dict.R jusqu'a ne pas trouver joueur.A dans
                le dict.J de joueur.X alors joueur.B = joueur.X
            -pop joueur.B de dict.R
            -next
        """

        current_round = cls.Round({})
        current_round.generate_round_pairings(is_first_round=is_first_round)
        self.round_list.append(current_round)

        return None
