"""
Controller module
"""

import sys
from CommonClass import data
from . import m_save_load
sys.path.insert(0, '../CommonClass')


class Model(m_save_load.SaveLoad):
    """
    Model class
    """
    def __init__(self):
        """
        Initialize the Model class.

        Attributes:
        - data (data.Data): An instance of the data.Data class for data management.
        - data_section_name (str): The name of the data section for the model.
        - data_excluded (list[str]): A list of attribute names to exclude when updating or loading data.
        - player_group (dict[int, list]): A dictionary representing the player group.

        Note: The values of the attributes are initialized accordingly.

        """
        super().__init__()
        self.data: data.Data = None
        self.data_section_name = ""
        self.data_excluded = ["data", "data_section_name", "data_excluded"]
        self.player_group: dict[int, list] = {}

    def load_data(self):
        """
        Load data from the data object and reformat the player_group after loading it.
        """
        super().load_data()

        reformated_player_group = {}
        for key, value in self.player_group.items():
            reformated_player_group[int(key)] = value

        self.player_group = reformated_player_group
