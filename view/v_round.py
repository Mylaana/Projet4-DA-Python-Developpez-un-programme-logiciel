"""
view module
"""
from . import view as v


class ViewRound(v.View):
    """
    View class
    """
    def dummy_generate_scores(self):
        """
        Randomly generate players scores for this round.
        This is a dummy function (the scores should be determined by every games,
        instead of randomed for app building purpose).
        """

    def display_round_pairings(self, pairing_list: list, round_number: int):
        """
        gets list of pairings with each line being 'player_a_id-player_b_id'
        returns none
        """
        round_pairings = []
        table_number = 0

        for line in pairing_list:
            table_number += 1
            round_pairings.append(f"Table {table_number} :")
            round_pairings.append("Joueur " + line.replace("-", " vs Joueur "))
            round_pairings.append("")

        self.show_in_console(round_pairings, f"round : {round_number}")

    def display_scores(self, score: dict, round_number: int, total_score: bool):
        """
        gets a list
        show list in console
        returns none
        """
        score_list = []
        print(score)

        if total_score:
            list_of_tuple = sorted(score.items(), key=lambda x: x[1], reverse=True)
            score_list = [f"Joueur {k[0]} : {float(score[k[0]])}" for k in list_of_tuple]
            title = f"classement à fin de round {round_number}"

        else:
            for key, value in score.items():
                score_list.append(f"Joueur {key} : {float(value)}")
            title = f"resultat du round {round_number}"

        self.show_in_console(message=score_list, title=title)

    def prompt_score_calculation_method(self) -> str:
        """
        Gets None\n
        Prompts user for a choice,\n
        Returns str :
        - [COMMAND_ONE] enter match results
        - [COMMAND_TWO] demo mode - use random match results
        - [COMMAND_RETURN] to return to tournament player list selection
        - [COMMAND_SAVE] to save the tournament actual state
        - [COMMAND_LOAD] to load a previously saved tournament
        - [COMMAND_EXIT] to exit program
        """
        self.show_in_console(message=["souhaitez-vous :",
                                      f"{self.menu.command_one} : entrer les scores des joueurs",
                                      f"{self.menu.command_two} : [demo mode] utiliser les scores aléatoires",
                                      "",
                                      f"{self.menu.command_save} : {self.menu.command_description_save}",
                                      f"{self.menu.command_load} : {self.menu.command_description_load}",
                                      f"{self.menu.command_return} : {self.menu.command_description_return}",
                                      f"{self.menu.command_exit} : {self.menu.command_description_exit}"],)
        return input("")

    def prompt_next_round(self):
        """
        Gets None\n
        Prompts user for a choice,\n
        Returns str :
        - [COMMAND_ONE] go to next round
        - [COMMAND_SAVE] to save the tournament actual state
        - [COMMAND_LOAD] to load a previously saved tournament
        - [COMMAND_EXIT] to exit program
        """
        self.show_in_console(message=["souhaitez-vous :",
                                      f"{self.menu.command_one} : passer au round suivant",
                                      "",
                                      f"{self.menu.command_save} : {self.menu.command_description_save}",
                                      f"{self.menu.command_load} : {self.menu.command_description_load}",
                                      f"{self.menu.command_return} : {self.menu.command_description_return}",
                                      f"{self.menu.command_exit} : {self.menu.command_description_exit}"])
        return input("")
