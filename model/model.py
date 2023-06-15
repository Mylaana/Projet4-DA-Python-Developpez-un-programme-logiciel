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
