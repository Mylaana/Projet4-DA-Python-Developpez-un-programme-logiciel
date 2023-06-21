"""
Data class module
"""
import json
import os
import sys
import re


class Data:
    """
    Manipulates the program's data
    Saves and loads
    """
    def __init__(self) -> None:
        self.file_name: str = ""
        self._path = os.path.dirname(os.path.abspath(sys.argv[0])) + "/Data/"
        self.data = {"status": {"finished": False}}
        self.player_base_file_name = "player_base"
        self.player_base_data = {}
        self.loaded_data = None
        self.controller_list: list = []

        if not os.path.exists(self._path + self.player_base_file_name):
            with open(file=self._path + self.player_base_file_name + ".json",
                      mode="w", encoding="utf-8") as data_file:
                json.dump(self.player_base_data, data_file, indent=4)

    def save_data(self):
        """
        dumps data into the json
        """
        with open(file=self._path + self.file_name, mode="w", encoding="utf-8") as data_file:
            json.dump(self.data, data_file, indent=4)

    def load_file(self):
        """
        gets data from the file_name json
        """
        with open(file=self._path + self.file_name, encoding="utf-8") as data_file:
            self.loaded_data = json.load(data_file)

    def create_json(self, name: str):
        """
        create a new tournament.json file
        """

        self.file_name = re.sub(r"[^a-zA-Z0-9\s-]", "", name)
        self.file_name = self.file_name.replace(" ", "-")
        self.file_name = self.file_name + ".json"

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

    def get_file_list(self) -> list:
        """
        gets none
        returns list of file names
        """
        tournament_list = os.listdir(self._path)
        for index, tournament in enumerate(tournament_list):
            tournament_list[index] = tournament.replace(".json", "")

        return tournament_list

    def report_player_list(self) -> list:
        """
        gets none
        returns list
        """

    def report_file_list(self) -> list:
        """
        gets none
        returns list
        """
        return sorted(self.get_file_list())

    def report_active_tournament_player_list(self) -> list:
        """
        gets none
        returns list
        """
        player_list = []
        for value in self.data["player_list"]["player_group"]:
            player_list.append(f"{value['last_name']} {value['name']}")

        return sorted(player_list)
