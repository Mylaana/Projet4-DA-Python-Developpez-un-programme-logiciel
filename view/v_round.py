"""
view module
"""
from . import view as v


class ViewRound(v.View):
    """
    View class
    """
    def display_round_pairings(self, pairing_list: list, round_number: int, player_group: dict[int, dict]):
        """
        Displays the pairings for the current round.

        Args:
        - pairing_list: List of pairings, where each line is 'player_a_id-player_b_id'
        - round_number: The round number
        - player_group: Dictionary containing player information

        Returns:
        - None.
        """
        round_pairings = []
        table_number = 0

        for line in pairing_list:
            table_number += 1
            round_pairings.append(f"Table {table_number} :")
            round_pairings.append(f"J{line[0][0]}-" + player_group[line[0][0]]["name"] +
                                  f" vs J{line[1][0]}-" + player_group[line[1][0]]["name"])
            round_pairings.append("")

        self.show_in_console(round_pairings, f"round : {round_number}")

    def display_scores(self, score: dict, round_number: int, total_score: bool, player_group: dict[int, dict]):
        """
        Displays the scores for the current round.

        Args:
        - score: Dictionary containing the scores of the players
        - round_number: The round number
        - total_score: Boolean indicating whether to display total scores or individual round scores
        - player_group: Dictionary containing player information

        Returns:
        - None
        """
        score_list = []
        if total_score:
            list_of_tuple = sorted(score.items(), key=lambda x: x[1], reverse=True)
            score_list = [f"J{k[0]} {player_group[k[0]]['name']} : {float(score[k[0]])}" for k in list_of_tuple]
            title = f"round {round_number} - classement score total"

        else:
            for key, value in score.items():
                score_list.append(f"J{key} {player_group[key]['name']} : {float(value)}")
            title = f"round {round_number} - resultat"

        self.show_in_console(message=score_list, title=title)

    def prompt_score_calculation_method(self) -> str:
        """
        Prompts the user to choose a score calculation method.

        Returns:
        - [COMMAND_ONE] to enter match results
        - [COMMAND_TWO] for demo mode - use random match results
        - [COMMAND_RETURN] to return to tournament player list selection
        - [COMMAND_SAVE] to save the tournament actual state
        - [COMMAND_LOAD] to load a previously saved tournament
        - [COMMAND_EXIT] to exit the program
        """
        self.show_in_console(message=["souhaitez-vous :",
                                      f"{self.menu.command_one} : entrer les scores des joueurs",
                                      f"{self.menu.command_two} : [demo mode] utiliser les scores aléatoires",
                                      f"{self.menu.command_three} : afficher un rapport",
                                      "",
                                      f"{self.menu.command_exit} : {self.menu.command_description_exit}"],)
        return input("")

    def prompt_next_round(self):
        """
        Prompts the user for the next round.

        Returns:
        - [COMMAND_ONE] to go to the next round
        - [COMMAND_SAVE] to save the tournament actual state
        - [COMMAND_LOAD] to load a previously saved tournament
        - [COMMAND_EXIT] to exit the program
        """
        self.show_in_console(message=["souhaitez-vous :",
                                      f"{self.menu.command_one} : passer au round suivant",
                                      "",
                                      f"{self.menu.command_exit} : {self.menu.command_description_exit}"])
        return input("")

    def prompt_end_of_tournament(self):
        """
        Prompts the user for the next round.

        Returns:
        - [COMMAND_ONE] to go to the next round
        - [COMMAND_SAVE] to save the tournament actual state
        - [COMMAND_LOAD] to load a previously saved tournament
        - [COMMAND_EXIT] to exit the program
        """
        self.show_in_console(message=["souhaitez-vous :",
                                      f"{self.menu.command_one} : afficher le vainqueur",
                                      "",
                                      f"{self.menu.command_exit} : {self.menu.command_description_exit}"])
        return input("")
