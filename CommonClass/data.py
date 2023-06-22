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
        self.player_base_file_name = "player_base.json"
        self.player_base_data = {}
        self.loaded_data = None
        self.controller_list: list = []

        # creates player_base file if not exists,
        # else, loads it
        if not os.path.exists(self._path + self.player_base_file_name):
            with open(file=self._path + self.player_base_file_name,
                      mode="w", encoding="utf-8") as data_file:
                json.dump(self.player_base_data, data_file, indent=4)
        else:
            with open(file=self._path + self.player_base_file_name, encoding="utf-8") as data_file:
                self.player_base_data = json.load(data_file)

    def save_data(self):
        """
        dumps data into the json
        """
        print("save data")
        with open(file=self._path + self.file_name, mode="w", encoding="utf-8") as data_file:
            json.dump(self.data, data_file, indent=4)

    def save_player_base(self):
        """
        dumps player info in player_base
        """
        print(self.data["player_list"]["player_group"])
        for value in self.data["player_list"]["player_group"]:
            self.player_base_data[
                self.data["player_list"]["player_group"][int(value)]['last_name'] + "-" +
                self.data["player_list"]["player_group"][int(value)]['name']] = {
                "last_name": self.data["player_list"]["player_group"][int(value)]['last_name'],
                "name": self.data["player_list"]["player_group"][int(value)]['name'],
                "birth_date": self.data["player_list"]["player_group"][int(value)]['birth_date']}

        with open(file=self._path + self.player_base_file_name, mode="w", encoding="utf-8") as data_file:
            json.dump(self.player_base_data, data_file, indent=4)

    def load_file(self, file_name):
        """
        gets data from the file_name json
        """
        with open(file=file_name, encoding="utf-8") as data_file:
            return json.load(data_file)

    def load_tournament(self):
        """
        gets data from the file_name json
        """
        self.loaded_data = self.load_file(self._path + self.file_name)

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

        tournament_list.remove(self.player_base_file_name.replace(".json", ""))

        return tournament_list

    def report_player_list(self) -> list:
        """
        gets none
        returns list
        """
        player_list = []
        for value in self.player_base_data.values():
            player_list.append(f"{value['last_name']} {value['name']} {value['birth_date']}")

        return sorted(player_list)

    def report_tournament_list(self) -> list:
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
        for value in self.data["player_list"]["player_group"].values():
            player_list.append(f"{value['last_name']} {value['name']}")

        return sorted(player_list)

    def report_tournament_info(self, tournament_name):
        """
        gets none
        returns list
        """
        filename = tournament_name + ".json"
        file_data = self.load_file(file_name=self._path + filename)

        tournament_info = []
        if "tournament" in file_data:
            tournament_info.append(f"tournoi : {file_data['tournament']['name']}")

            if file_data['tournament']['date_start'] is not None:
                tournament_info.append(
                    f"date de début : {file_data['tournament']['date_start'][0]}/"
                    f"{file_data['tournament']['date_start'][1]}/"
                    f"{file_data['tournament']['date_start'][2]}")
            else:
                tournament_info.append("date de début : le tournoi n'a pas encore commencé.")

            if file_data['tournament']['date_end'] is not None:
                tournament_info.append(
                    f"date de fin : {file_data['tournament']['date_end'][0]}/"
                    f"{file_data['tournament']['date_end'][1]}/"
                    f"{file_data['tournament']['date_end'][2]}")
            else:
                tournament_info.append("date de fin : le tournoi est toujours en cours.")

        return tournament_info

    def report_rounds_and_match(self):
        """
        gets none
        returns list
        """
        round_info = []
        player_group = self.data["round"]["player_group"]
        for key in self.data['round']['round_list'].keys():
            round_info.append(f"Round {key} :")
            for values in self.data['round']['round_list'][key]['pairing_list']:
                round_info.append(f"J{values[0][0]} {player_group[values[0][0]]['name']} VS " +
                                  f"J{values[1][0]} {player_group[values[1][0]]['name']}")

            round_info.append("")

        return round_info
