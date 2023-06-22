"""
model dedicated module
"""

import time
from . import model as m


class Tournament(m.Model):
    """
    Model dedicated to the Tournament class.
    """
    def __init__(self):
        """
        Initialize the Tournament class.

        Attributes:
        - name (str): The name of the tournament.
        - location (str): The location of the tournament.
        - date_start (time.struct_time): The start date of the tournament.
        - date_end (time.struct_time): The end date of the tournament.
        - player_list_id (list[int]): A list of player IDs.
        - player_group (dict[int, dict]): A dictionary representing the player group.
        - description (str): The description of the tournament.
        - round_number (int): The number of rounds in the tournament.

        Note: The values of the attributes are initialized accordingly.

        """
        super().__init__()
        self.name = ""
        self.location = ""
        self.date_start: time.struct_time = None
        self.date_end: time.struct_time = None
        self.player_list_id: list[int] = None
        self.player_group: dict[int, dict] = {}
        self.description = ""
        self.round_number = 4
