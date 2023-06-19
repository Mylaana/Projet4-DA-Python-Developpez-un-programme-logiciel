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
        self.data = {"status": {"finished": False}}
        self.loaded_data = None
        self.controller_list: list = []

    def save_data(self):
        """
        dumps data into the json
        """
        print("save json file")
        with open(file=self._path + self.file_name, mode="w", encoding="utf-8") as data_file:
            json.dump(self.data, data_file, indent=4)

    def load_file(self):
        """
        gets data from the file_name json
        """
        print("load json file")
        with open(file=self._path + self.file_name, encoding="utf-8") as data_file:
            self.loaded_data = json.load(data_file)

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
        for controller in self.controller_list:
            controller.update_data()

    def load_all(self):
        """
        gets none
        call every model update method
        returns none
        """
        for controller in self.controller_list:
            controller.load_data()

        self.loaded_data = None
