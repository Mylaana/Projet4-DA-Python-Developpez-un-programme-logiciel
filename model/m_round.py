"""
Tournament class module
"""
import sys
import random
import time
from . import m_match as m
from . import model
sys.path.insert(0, '../CommonClass')


class Round(model.Model):
    """
    Tournament class model.
    """

    def __init__(self, round_max_number: int = 4):
        """
        Initialize the Round model.

        Args:
        - round_max_number (int): The maximum number of rounds in the tournament.

        Attributes:
        - round_list (list[m.Match]): A list to store the rounds of the tournament.
        - round_counter (int): The current round counter.
        - round_max_number (int): The maximum number of rounds in the tournament.
        - player_list_id (list[int]): A list to store the IDs of the players.
        - player_group (dict[int, dict]): A dictionary to store player information.
        Key: player ID, Value: player dictionary.
        - current_round (m.Match): The current round of the tournament.
        - current_round_step (int): The current step of the current round.
        - previous_pairings (dict[int, list]): A dictionary to store previous pairings of players.

        Note: The values of the attributes 'round_list', 'round_counter', 'player_list_id', 'player_group',
        'current_round', 'current_round_step', and 'previous_pairings' are initialized accordingly.

        """
        super().__init__()
        self.round_list: list[m.Match] = []
        self.round_counter = 1
        self.round_max_number = round_max_number
        self.player_list_id = []
        self.player_group: dict[int, dict] = {}
        self.current_round: m.Match = None

        """
        0=not created
        1=pairings done, no results yet
        2=round finished, scores entered
        """
        self.current_round_step: int = 0

        self.data_excluded = ["data", "data_section_name", "data_excluded", "round_list", "current_round",
                              "previous_pairings"]

        """
        a dictA of dictBs
        dictA has key = playerA and value = dictBs
        dictBs has a key of playerB previously matched with playerA
        """
        self.previous_pairings: dict[int, list] = {}

    def create_new_round(self):
        """
        Generate a new round and player pairings.

        Returns:
        - bool: True if the round counter is greater than or equal to the maximum number of rounds, False otherwise.
        """

        self.current_round = m.Match(self.player_list_id.copy())
        self.current_round.date_start = time.localtime()

        if self.round_counter > 1:
            self.current_round.player_score_total_start_of_round = self.round_list[
                -1].player_score_total_end_of_round.copy()

        self.current_round.generate_round_pairings(is_first_round=self.round_counter == 1,
                                                   previous_pairing=self.previous_pairings)
        self.add_previous_pairings()
        self.round_list.append(self.current_round)

        return self.round_counter >= self.round_max_number

    def finalize_round(self):
        """
        Clean up round data and prepare for the next round.

        Returns:
        - None
        """
        self.round_counter += 1
        self.current_round.date_end = time.localtime()
        self.current_round = None
        self.current_round_step = 0

    def get_current_round_pairings(self) -> list:
        """
        Get the current round pairings.

        Returns:
        - list: The current round pairings as a list of strings in the format 'playerA - playerB'.
        """

        return self.current_round.pairing_list

    def set_current_round_player_score(self, player_id: int, player_score: float):
        """
        Set the score of a player in the current round.

        Args:
        - player_id (int): The ID of the player.
        - player_score (float): The score of the player.

        Returns:
        - None
        """
        self.current_round.set_player_score(player_id=player_id, player_match_result=player_score)

    def set_random_scores(self):
        """
        Set random scores for the current round.

        Returns:
        - None
        """

        for match in self.current_round.pairing_list:
            player_a_id = int(match[0][0])
            player_a_score = random.choice([0.0, 0.5, 1.0])
            player_b_id = int(match[1][0])
            player_b_score = 1.0 - player_a_score
            self.current_round.set_player_score(
                player_id=player_a_id, player_match_result=player_a_score)
            self.current_round.set_player_score(
                player_id=player_b_id, player_match_result=player_b_score)

    def add_previous_pairings(self):
        """
        Add the current round pairings to the previous pairings dictionary.

        Returns:
        - None
        """
        if not self.previous_pairings:
            for player_id in self.player_list_id:
                self.previous_pairings[player_id] = []

        for pairing in self.current_round.pairing_list:
            self.previous_pairings[int(pairing[0][0])].append(int(pairing[1][0]))
            self.previous_pairings[int(pairing[1][0])].append(int(pairing[0][0]))

    def update_data_excluded(self) -> None:
        """
        Override: Update excluded data.

        Returns:
        - None
        """
        counter = 1
        self.data.data["round"]["round_list"] = {}
        for match in self.round_list:
            # translates Match() in to a dict
            self.data.data[self.data_section_name]["round_list"][counter] = {}
            for attribute, values in vars(match).items():
                self.data.data[self.data_section_name]["round_list"][counter][attribute] = values

            counter += 1

    def load_data_excluded(self):
        """
        Load match objects and tuple pairings from a JSON file.

        Returns:
        - None
        """

        if self.data.loaded_data["status"]["player_list"] is False:
            return

        # custom loading round_list
        for i in range(1, self.round_counter + 1, 1):
            load_match = m.Match(self.data.loaded_data[self.data_section_name]["round_list"][str(i)]["player_list_id"])
            load_match.player_score_round = self.formated_dict_int_float(self.data.loaded_data[
                    self.data_section_name]["round_list"][str(i)]["player_score_round"])
            load_match.player_score_total_start_of_round = self.formated_dict_int_float(self.data.loaded_data[
                    self.data_section_name]["round_list"][str(i)]["player_score_total_start_of_round"])
            load_match.player_score_total_end_of_round = self.formated_dict_int_float(self.data.loaded_data[
                    self.data_section_name]["round_list"][str(i)]["player_score_total_end_of_round"])

            if i == self.round_counter and self.current_round_step < 1:
                break

            pairing_list: list[tuple(list)] = self.data.loaded_data[
                self.data_section_name]["round_list"][str(i)]["pairing_list"]

            # formating the score result into tuple for each match for each score
            for match in pairing_list:
                match_formated: tuple(list) = ([match[0][0], match[0][1]],
                                               [match[1][0], match[1][1]])
                load_match.pairing_list.append(match_formated)

            self.round_list.append(load_match)
            self.current_round = load_match
            self.add_previous_pairings()

    def formated_dict_int_float(self, dict_to_format: dict) -> dict[int, float]:
        """
        Format a dictionary with integer keys and float values.

        Args:
        - dict_to_format (dict): The dictionary to format.

        Returns:
        - dict[int, float]: The formatted dictionary.
        """
        formated_dict = {}
        for key, value in dict_to_format.items():
            formated_dict[int(key)] = float(value)

        return formated_dict
