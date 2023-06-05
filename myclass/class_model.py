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


class PlayerList:
    """
    player list
    """
    def __init__(self):
        """
        stores player list with a dictionnaty :
        Key = id, value = class Player
        """
        self.player_dict = {}

    def get_default_player_list(self) -> list:
        """
        dummy function
        returns default player list
        """
        return [
            "Jeanne Thériault 1989/12/07",
            "Dexter Chesnay 1995/07/16",
            "Chandler Bisaillon 1969/02/15",
            "Guillaume Aoust 1994/10/12",
            "Christiane Laramée 1999/01/22",
            "Élise Lévesque 2004/03/19",
            "Orville Mireault 1984/10/06",
            "Étienne Salois 1992/12/06"
        ]

    def add_player_to_list(self, player: Player) -> None:
        """
        stores player in dict
        gets a player class argument
        returns none
        """
        self.player_dict[len(self.player_dict) + 1] = player
