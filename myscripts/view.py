"""
view module
"""


class View():
    """
    View class
    """
    def __init__(self):
        self.player_list = self.dummy_generate_player_list()

    def get_player_list(self):
        """
        Returns player list with following shape :
        [Name1 FamilyName1 Birthdate1(AAAA/MM/DD), ...]
        """

        print("voici la liste des joueurs par défaut :")
        for player_info in self.player_list:
            print(str(player_info))

        default_player_list = input("\nvoulez vous utiliser la liste des joueurs par défaut ? (y/n)\n")

        if default_player_list == "y":
            print(r"c'est parti")
            return self.player_list
        else:
            print("tant pis")
            return None

    def dummy_generate_player_list(self):
        """
        player list for testing purpose
        """
        return [
            "Jeanne Thériault 1989/12/07",
            "Dexter Chesnay 1995/07/16",
            "Chandler Bisaillon 1969/02/15",
            "Guillaume Aoust 1994/10/12",
            "Christiane Laramée 1999/01/22",
            "Élise Lévesque 2004/03/19",
            "Orville Mireault 1984/10/6",
            "Étienne Salois 1992/12/06"
        ]
