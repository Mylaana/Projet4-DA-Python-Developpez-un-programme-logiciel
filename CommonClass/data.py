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
        self.data_locked: bool = False

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
        Dumps data dict into the json file.

        Returns:
        - None.

        """
        if self.data_locked:
            return

        with open(file=self._path + self.file_name, mode="w", encoding="utf-8") as data_file:
            json.dump(self.data, data_file, indent=4)

    def save_player_base(self):
        """
        Dumps player info in player_base .json file.

        Returns:
        - None.

        """
        for value in self.data["player_list"]["player_group"]:
            self.player_base_data[
                self.data["player_list"]["player_group"][int(value)]['last_name'] + "-" +
                self.data["player_list"]["player_group"][int(value)]['name']] = {
                "last_name": self.data["player_list"]["player_group"][int(value)]['last_name'],
                "name": self.data["player_list"]["player_group"][int(value)]['name'],
                "birth_date": self.data["player_list"]["player_group"][int(value)]['birth_date']}

        with open(file=self._path + self.player_base_file_name, mode="w", encoding="utf-8") as data_file:
            json.dump(self.player_base_data, data_file, indent=4)

    def load_file(self, file_name: str) -> dict:
        """
        Loads a file in DATA folder matching file_name

        Attr:
        - file_name (str): name of the .json file to load

        Returns:
        - (dict).

        """
        with open(file=file_name, encoding="utf-8") as data_file:
            return json.load(data_file)

    def load_tournament(self):
        """
        Gets data from the file_name json.

        Returns:
        - None.
        """
        self.loaded_data = self.load_file(self._path + self.file_name)
        self.data["status"] = self.loaded_data["status"]

    def create_json(self, name: str):
        """
        Create a new .json file

        Attr:
        - name (str): name of the .json file.

        Returns:
        - None.
        """

        self.file_name = re.sub(r"[^a-zA-Z0-9\s-]", "", name)
        self.file_name = self.file_name.replace(" ", "-")
        self.file_name = self.file_name + ".json"

        with open(file=self._path + self.file_name, mode="w", encoding="utf-8") as data_file:
            json.dump(self.data, data_file, indent=4)

    def update_all(self):
        """
        Call every controller 'update' method.

        Returns:
        - None
        """
        for controller in self.controller_list:
            controller.update_data()

    def load_all(self):
        """
        Call every controller 'load' method.
        Returns:
        - None
        """
        for controller in self.controller_list:
            controller.load_data()

        self.loaded_data = None

    def get_file_list(self) -> list:
        """
        Returns:
        - (list) of file names found in DATA folder.
        """
        tournament_list = os.listdir(self._path)
        for index, tournament in enumerate(tournament_list):
            tournament_list[index] = tournament.replace(".json", "")

        tournament_list.remove(self.player_base_file_name.replace(".json", ""))

        return tournament_list

    def report_player_list(self) -> list:
        """
        Returns:
        - (list) of player information extracted from self.player_base_data object,
        sorted in last_name alphabetical order.
        """
        player_list = []
        for value in self.player_base_data.values():
            player_list.append(f"{value['last_name']} {value['name']} {value['birth_date']}")

        return sorted(player_list)

    def report_tournament_list(self) -> list:
        """
        Returns:
        - (list) of tournament files found in DATA folder, sorted in alphabetical order.
        """
        return sorted(self.get_file_list())

    def report_active_tournament_player_list(self) -> list:
        """
        Returns:
        - (list) of player info found in self.data object (from active tournament file).
        """
        player_list = []
        for value in self.data["player_list"]["player_group"].values():
            player_list.append(f"{value['last_name']} {value['name']}")

        return sorted(player_list)

    def report_tournament_info(self, tournament_name) -> list:
        """
        Returns:
        - (list) of tournament information (name, start date, end date).
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

    def report_rounds_and_match(self) -> list:
        """
        Returns:
        - (list) rounds and match details.
        """
        round_info = []
        player_group = {}
        for key, value in self.data["round"]["player_group"].items():
            player_group[str(key)] = value

        for key in self.data['round']['round_list'].keys():
            round_info.append(f"Round {key} :")
            for values in self.data['round']['round_list'][key]['pairing_list']:
                round_info.append(f"J{values[0][0]} {player_group[str(values[0][0])]['name']} VS " +
                                  f"J{values[1][0]} {player_group[str(values[1][0])]['name']}")
            round_info.append("")

        return round_info

    def report_tournament_result(self) -> list:
        """
        Returns:
        - (list) of total scores and tournament winner.
        """

        report_list = []
        player_group = {}
        round_data = {}
        winner = ""
        winner_score = 0
        for key, value in self.data["round"]["player_group"].items():
            player_group[str(key)] = value

        for key, value in self.data['round']['round_list'].items():
            if str(key) != str(self.data['round']['round_counter']):
                continue
            
            round_data = value['player_score_total_end_of_round']
            break

        for key, value in round_data.items():
            report_list.append(f"J{key} {player_group[str(key)]['name']}: {value}")
            if value > winner_score:
                winner_score = value
                winner = player_group[str(key)]['name']

        if self.data["status"]["finished"] is True:
            report_list.append("")
            report_list.append(f"{winner} remporte le tournoi !")

        return report_list