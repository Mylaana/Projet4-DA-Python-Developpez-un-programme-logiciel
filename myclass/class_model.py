"""
Tournament class module
"""
class Tournament:
    """
    tournament class
    """
    def __init__(self, name, location, date_start, round_number: int = 4):
        self.name = name
        self.location = location
        self.date_start = date_start
        self.date_end = ""
        self.round_list = []
        self.round_number = round_number
        self.player_list = []
        self.description = ""

    def add_new_round(self):
        """
        Generates new round and player pairings.
        Returns None

        prérequis :
        attribuer a round un dict.R des joueurs classés par score total cumulé décroissant
        attribuer a chaque joueur un dict.J de ses appariement précédents

        calculer nouveau appariement en supprimant de dict.R deux joueurs :
            -prendre le premier joueur de dict.R = joueur.A
            -iterer sur joueur.X de dict.R jusqu'a ne pas trouver joueur.A dans 
                le dict.J de joueur.X alors joueur.B = joueur.X
            -pop joueur.B de dict.R
            -next
        """

        return None

class Round:
    """
    manage round infos
    """
    def __init__(self):
        pass

class Player:
    """
    player class
    """
    def __init__(self, name: str = "", family_name: str = "", birth_date: str = "", rank: str = ""):
        self.name = name
        self.family_name = family_name
        self.birth_date = birth_date
        self.rank = rank

    def get_player_info(self):
        """
        returns player info as a string
        """
        return "name : " + self.name + "  rank : " + self.rank + " "
