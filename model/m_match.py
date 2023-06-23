"""
Match class
"""
import random
import time

# DELETE  DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE

class Match:
    """
    Manages one round and all match information.
    """

    def __init__(self, player_list_id: list):
        """
        Initialize a Match instance.

        Args:
        - player_list_id (list[int]): List of player IDs.

        """
        self.player_list_id: list[int] = player_list_id.copy()
        self.pairing_list: list[tuple] = []

        # initializing player score at 0
        self.player_score_round: dict[int, float] = {k: 0.0 for k in self.player_list_id}
        self.player_score_total_start_of_round: dict[int, float] = self.player_score_round.copy()
        self.player_score_total_end_of_round: dict[int, float] = self.player_score_round.copy()
        self.date_start: time = None
        self.date_end: time = None

    def generate_round_pairings(self, is_first_round: bool, previous_pairing: dict[int, list]) -> None:
        """
        Generate pairings for the round based on the round number and previous pairings.

        Args:
        - is_first_round (bool): True if it is the first round, False otherwise.
        - previous_pairing (dict[int, list]): Dictionary containing the previous pairings.

        Returns:
        - None
        """
        if is_first_round:
            self.set_pairings_random()
        else:
            self.set_pairings_descending_score(previous_pairing)

    def get_id_list_from_sorted_scores(self, score: dict, sort_reverse: bool = False) -> list:
        """
        Get a list of player IDs sorted based on the scores.

        Args:
        - score (dict): Dictionary containing player scores.
        - sort_reverse (bool, optional): True to sort in descending order, False for ascending order.
                                           Defaults to False.

        Returns:
        - list: List of player IDs.

        """
        list_of_tuple = sorted(score.items(), key=lambda x: x[1], reverse=sort_reverse)
        return [t[0] for t in list_of_tuple]

    def set_pairings_random(self):
        """
        Create pairings randomly.

        Returns:
        - None.
        """
        unpaired_players = self.player_list_id.copy()

        while unpaired_players:
            player_a = random.choice(unpaired_players)
            unpaired_players.remove(int(player_a))

            player_b = random.choice(unpaired_players)
            unpaired_players.remove(int(player_b))
            self.pairing_list.append(([player_a, 0], [player_b, 0]))

    def set_pairings_descending_score(self, previous_pairing: dict[int, list]):
        """
        Create pairings based on descending scores.

        Args:
        - previous_pairing (dict[int, list]): Dictionary containing the previous pairings.

        Returns:
        - None
        """
        # copy start of round score dict into a list to sort scores
        unpaired_players = self.get_id_list_from_sorted_scores(score=self.player_score_total_start_of_round, sort_reverse=True)

        # assigns the two first player of the list as a pair
        while unpaired_players:
            player_a = int(unpaired_players.pop(0))

            # assigns the first available player in unpaired_player which has not already been playing vs player_a
            if len(unpaired_players) > 1:
                player_b_index = self.first_player_not_in_list(player_list=unpaired_players.copy(),
                                                               player_list_to_exclude=previous_pairing[
                                                                   player_a].copy())
                player_b = unpaired_players.pop(player_b_index)
            else:
                player_b = unpaired_players.pop(0)

            # unpaired_players.pop(unpaired_players.index(player_b))
            self.pairing_list.append(([player_a, 0], [player_b, 0]))

    def first_player_not_in_list(self, player_list: list[int], player_list_to_exclude: list[int]) -> int:
        """
        Find the index of the first player in the player_list that is not in the player_list_to_exclude.

        Args:
        - player_list (list[int]): List of player IDs.
        - player_list_to_exclude (list[int]): List of player IDs to exclude.

        Returns:
        - int: Index of the first player in player_list that is not in player_list_to_exclude.
        """
        list_before_pop = player_list.copy()
        for line in player_list_to_exclude:
            if line in player_list:
                player_list.remove(line)
        first_player_after_remove = player_list.pop(0)

        return list_before_pop.index(first_player_after_remove)

    def set_player_score(self, player_id: int, player_match_result: float):
        """
        Update the score of a player for the round.

        Args:
        - player_id (int): ID of the player.
        - player_match_result (float): Match result of the player.

        Returns:
        - None.
        """
        self.player_score_round[player_id] = player_match_result
        self.player_score_total_end_of_round[player_id] = self.player_score_total_start_of_round[player_id] + \
            self.player_score_round[player_id]

        for i, match in enumerate(self.pairing_list):
            if int(match[0][0]) == int(player_id):
                self.pairing_list[i] = ([match[0][0], player_match_result], [match[1][0], match[1][1]])
            elif int(match[1][0]) == int(player_id):
                self.pairing_list[i] = ([match[0][0], match[0][1]], [match[1][0], player_match_result])
            else:
                continue
