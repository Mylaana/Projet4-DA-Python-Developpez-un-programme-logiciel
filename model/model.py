"""
Controller module
"""

import sys
from CommonClass import data
from . import m_save_load
sys.path.insert(0, '../CommonClass')


class Model(m_save_load.SaveLoad):
    """
    Controller class
    """
    def __init__(self):
        super().__init__()
        self.data: data.Data = None
        self.data_section_name = ""
        self.data_excluded = ["data", "data_section_name", "data_excluded"]
        self.player_group: dict[int, list] = {}

    def load_data(self):
        """
        gets none
        reformat the player_group after loading it
        returns none
        """
        super().load_data()

        reformated_player_group = {}
        for key, value in self.player_group.items():
            reformated_player_group[int(key)] = value

        self.player_group = reformated_player_group
