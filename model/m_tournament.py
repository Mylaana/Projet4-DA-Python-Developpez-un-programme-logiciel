"""
model dedicated module
"""

import sys
from CommonClass import data
from . import m_save_load
sys.path.insert(0, '../CommonClass')


class Tournament(m_save_load.SaveLoad):
    """
    Model = tournament class
    """
    def __init__(self):
        super().__init__()
        self.name = ""
        self.location = ""
        self.date_start = ""
        self.date_end = ""
        self.player_list_id: list[int] = None
        self.player_group: dict[int, dict] = {}
        self.description = ""
        self.round_number = 4

        self.data: data.Data() = None
        self.data_section_name = "tournament"
        self.data_excluded = ["data", "data_section_name", "data_excluded"]
