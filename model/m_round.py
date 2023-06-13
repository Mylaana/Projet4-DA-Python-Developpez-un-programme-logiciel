"""
Tournament class module
"""
import sys
import random
from CommonClass import data
from . import m_match as m
from . import m_save_load
sys.path.insert(0, '../CommonClass')


class Round(m_save_load.SaveLoad):
    """
    Model = tournament class
    """

    def __init__(self, round_max_number: int = 4):
        super().__init__()
        self.round_list: list[m.Match] = []
        self.round_counter = 0
        self.round_max_number = round_max_number
        self.player_list_id = []
        self.player_group: dict[int, dict] = {}
        self.current_round: m.Match = None

        self.data: data.Data() = None
        self.data_section_name = "round"
        self.data_excluded = ["data", "data_section_name", "data_excluded", "round_list", "current_round"]

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
        self.round_counter += 1
        self.current_round = m.Match(self.player_list_id.copy())
        if self.round_counter > 1:
            self.current_round.player_score_total_start_of_round = self.round_list[
                -1].player_score_total_end_of_round.copy()

        self.current_round.generate_round_pairings(is_first_round=self.round_counter == 1,
                                                   previous_pairing=self.previous_pairings)
        self.add_previous_pairings()
        self.round_list.append(self.current_round)

        return self.round_counter >= self.round_max_number

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
