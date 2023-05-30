"""
view module
"""


def dummy_generate_player_list():
        """
        Generate a player list.
        This is a dummy function that should be processed by loading data or by the user manually.
        """
        player_list = []

        for player_id in range(1, 9):
            player = model.cls.Player(player_id=player_id)
            player_list.append(player)
        
        return player_list


class View():
    """
    View class
    """
    