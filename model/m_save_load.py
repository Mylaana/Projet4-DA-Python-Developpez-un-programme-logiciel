"""
Save/load model class
"""
import sys
from abc import ABC
from CommonClass import data
sys.path.insert(0, '../CommonClass')


class SaveLoad(ABC):
    """
    blabla
    """
    def __init__(self):
        self.data = data.Data()
        self.data_excluded = []
        self.data_section_name = ""

    def update_data(self) -> None:
        """
        updates the tournament's json file with every attribute's value
        returns None
        """

        for attribute, values in vars(self).items():
            if attribute not in self.data_excluded:
                self.data.data[self.data_section_name][attribute] = values

        self.update_data_excluded()

    def update_data_excluded(self) -> None:
        """
        void function, must be overridden
        """

    def save_data(self) -> None:
        """
        calls the save data into json function
        """
        self.data.save_data()

    def load_data(self):
        """
        loads data from the data object
        returns None
        """
        for attribute, value in vars(self).items():
            if attribute not in self.data_excluded:
                setattr(self, attribute, self.data.loaded_data[self.data_section_name][attribute])
        self.load_data_excluded()

    def load_data_excluded(self):
        """
        void function, must be overridden
        """
