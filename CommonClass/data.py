"""
Data class module
"""
import json
import os
import sys


class Data:
    """
    Manipulates the program's data
    Saves and loads
    """
    def __init__(self) -> None:
        self.file_name: str = "data.json"
        self._path = os.path.dirname(os.path.abspath(sys.argv[0])) + "/Data/"
        self.data = {"status": {"finished": False},
                     "tournament": {},
                     "player_list": {},
                     "round": {}}
        self.model_list: list = []

    def save_data(self):
        """
        dumps data into the json
        """
        with open(file=self._path + self.file_name, mode="w", encoding="utf-8") as data_file:
            json.dump(self.data, data_file, indent=4)

    def load_data(self):
        """
        gets data from the file_name json
        """
        with open(file='data.json', encoding="utf-8") as data_file:
            self.data = json.load(data_file)

    def create_json(self):
        """
        create a new tournament.json file
        """
        with open(file=self._path + self.file_name, mode="w", encoding="utf-8") as data_file:
            json.dump(self.data, data_file, indent=4)

    def update_all(self):
        """
        gets none
        call every model update method
        returns none
        """
        for model in self.model_list:
            model.update_data()
