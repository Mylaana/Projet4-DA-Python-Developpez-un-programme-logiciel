"""
Controller module
"""
import time
from . import view as v
from . import model as m


class Controller:
    """
    Controller class
    """
    def __init__(self):

        self.model = m.Model(
                            name="Tournoi club du vieux Lyon",
                            location="Lyon - France",
                            date_start=time.localtime(),
                            round_number=4
                            )

        self.view = v.View()

        self.model.player_list = self.view.get_player_list()
