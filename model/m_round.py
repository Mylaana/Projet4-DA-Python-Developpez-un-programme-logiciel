"""
Tournament class module
"""
import sys
import random
from . import m_match as m
from . import model
sys.path.insert(0, '../CommonClass')


class Round(model.Model):
    """
    Model = tournament class
    """

    def __init__(self, round_max_number: int = 4):
        super().__init__()
        self.round_list: list[m.Match] = []
        self.round_counter = 1
        self.round_max_number = round_max_number
        self.player_list_id = []
        self.player_group: dict[int, list] = {}
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
        Generates new round and player pairings.
        Returns None
        """

        self.current_round = m.Match(self.player_list_id.copy())

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
        gets none
        cleans round data and prepare for next
        returns none
        """
        self.round_counter += 1
        self.current_round = None
        self.current_round_step = 0

    def get_current_round_pairings(self) -> list:
        """
        gets none
        returns current round pairings as list like :
        str('playerA - playerB')
        str('playerA - playerB')
        """

        return self.current_round.pairing_list

    def set_random_scores(self):
        """
        Gets None
        randoms scores for current round
        for each match, randoms the score of the player_a and deduct the score of player_b
        returns None
        """

        for match in self.current_round.pairing_list:
            player_a_id = int(match[0][0])
            player_a_score = random.choice([0, 0.5, 1])
            player_b_id = int(match[1][0])
            player_b_score = 1.0 - player_a_score
            self.current_round.set_player_score(
                player_id=player_a_id, player_match_result=player_a_score)
            self.current_round.set_player_score(
                player_id=player_b_id, player_match_result=player_b_score)

    def add_previous_pairings(self):
        """
        adds the curent round pairings to the previous pairings dict
        """
        if not self.previous_pairings:
            for player_id in self.player_list_id:
                self.previous_pairings[player_id] = []

        for pairing in self.current_round.pairing_list:
            self.previous_pairings[int(pairing[0][0])].append(int(pairing[1][0]))
            self.previous_pairings[int(pairing[1][0])].append(int(pairing[0][0]))

    def update_data_excluded(self) -> None:
        """
        void function, must be overridden
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
        gets none
        loads match objects and tuple pairings from json file
        returns none
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

            pairing_list = self.data.loaded_data[self.data_section_name]["round_list"][str(i)]["pairing_list"]

            # formating the score result into tuple for each match for each score
            for match in pairing_list:
                match_formated: list[tuple] = []
                for score in match:
                    match_formated.append(tuple(score))

                load_match.pairing_list.append(match_formated.copy())

            self.round_list.append(load_match)
            self.current_round = load_match
            self.add_previous_pairings()

    def formated_dict_int_float(self, dict_to_format: dict) -> dict[int, float]:
        """
        gets unformated dict
        returns formated dict[int,float]
        """
        formated_dict = {}
        for key, value in dict_to_format.items():
            formated_dict[int(key)] = float(value)

        return formated_dict
