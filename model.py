"""
model dedicated module
"""
import time
from myclass import class_model as cls


class Model:
    """
    awesome model
    """
    def __init__(self):
        self.list_player = []
        self.tournament = cls.Tournament(
                            name="Tournoi club du vieux Lyon",
                            location="Lyon - France",
                            date_start=time.localtime(),
                            round_number=4
                            )
