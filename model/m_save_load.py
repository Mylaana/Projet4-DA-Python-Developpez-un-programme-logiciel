"""
Save/load model module
"""

import sys
from abc import ABC
from CommonClass import data
sys.path.insert(0, '../CommonClass')


class SaveLoad(ABC):
    """
    Save/load model class
    """
    def __init__(self):
        """
        Initialize the SaveLoad class.

        Attributes:
        - data (data.Data): An instance of the data.Data class.
        - data_excluded (list): A list of excluded data attributes.
        - data_section_name (str): The name of the data section.

        Note: The values of the attributes 'data', 'data_excluded',
        and 'data_section_name' are initialized accordingly.

        """
        self.data: data.Data = data.Data()
        self.data_excluded = []
        self.data_section_name = ""

    def update_data(self) -> None:
        """
        Update the tournament's JSON file with the values of all attributes.

        Returns:
        - None
        """
        if self.data.data_locked:
            return

        for attribute, values in vars(self).items():
            if attribute not in self.data_excluded:
                self.data.data[self.data_section_name][attribute] = values

        self.update_data_excluded()

    def update_data_excluded(self) -> None:
        """
        Override: Update excluded data.

        Returns:
        - None
        """

    def save_data(self) -> None:
        """
        Call the save_data() function to save the data into a JSON file.

        Returns:
        - None
        """
        self.data.save_data()

    def load_data(self):
        """
        Load data from the data object.

        Returns:
        - None
        """
        for attribute, value in vars(self).items():
            if attribute not in self.data_excluded:
                setattr(self, attribute, self.data.loaded_data[self.data_section_name][attribute])

        self.load_data_excluded()

    def load_data_excluded(self):
        """
        Override: Load excluded data.

        Returns:
        - None
        """
