"""
model dedicated module
"""
from . import m_round as m_r
from . import m_player as m_p


class Tournament:
    """
    Model = tournament class
    """
    def __init__(self, round_number: int = 4):
        self.name = ""
        self.location = ""
        self.date_start = ""
        self.date_end = ""
        self.round_list = []
        self.round_counter = 1
        self.round_number = round_number
        self.player_list = m_p.PlayerList
        self.description = ""
        self.current_round = None

    def create_new_round(self):
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

        print("round number : " + str(self.round_counter))

        self.current_round = m_r.Round(self.player_list)
        self.current_round.generate_round_pairings(is_first_round=self.round_counter == self.round_counter)
        self.round_list.append(self.current_round)

        self.round_counter += 1
        if self.round_counter > self.round_number:
            return True
        else:
            return False

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
