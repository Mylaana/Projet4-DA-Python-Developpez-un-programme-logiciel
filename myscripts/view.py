"""
view module
"""


def dummy_generate_player_list():
    """
    Generate a player list.
    This is a dummy function that should be processed by loading data or by the user manually.
    """
    player_list = []
    """
    for player_id in range(1, 9):
        player = model.cls.Player(player_id=player_id)
        player_list.append(player)
    """
    return player_list


class View():
    """
    View class
    """
    def __init__(self):
        self.player_list = self.get_player_list

    def get_player_list(self):
        """
        Returns player list
        """
        nom_joueur = input("entrer le nom du joueur")

        return nom_joueur
