"""
Controller module
"""
import time
from . import view


class Controller:
    """
    Controller class
    """
    def __init__(self):
        """
        self.model = model.Model(
                            name="Tournoi club du vieux Lyon",
                            location="Lyon - France",
                            date_start=time.localtime(),
                            round_number=4
                            )
        """
        self.view = Scripts.View()

