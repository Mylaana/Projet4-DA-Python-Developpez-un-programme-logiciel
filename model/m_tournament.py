"""
model dedicated module
"""

import time
from . import model as m


class Tournament(m.Model):
    """
    Model = tournament class
    """
    def __init__(self):
        super().__init__()
        self.name = ""
        self.location = ""
        self.date_start: time.struct_time = None
        self.date_end: time.struct_time = None
        self.player_list_id: list[int] = None
        self.player_group: dict[int, dict] = {}
        self.description = ""
        self.round_number = 4
