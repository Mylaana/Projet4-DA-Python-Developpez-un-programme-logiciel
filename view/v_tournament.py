"""
view module
"""
from . import view as v


class ViewTournament(v.View):
    """
    View class
    """
    def prompt_tournament_selection(self) -> str:
        """
        Prompts user for :
        - new tournament
        - load tournament
        - exiting the program

        Returns :
        - [COMMAND_ONE] to create new tournament
        - [COMMAND_TWO] to load tournament
        - [COMMAND_SAVE] to save the tournament actual state
        - [COMMAND_LOAD] to load a previously saved tournament
        - [COMMAND_EXIT] to exit program
        """
        self.show_in_console(message=["souhaitez-vous :",
                                      f"{self.menu.command_one} créer un nouveau tournoi",
                                      f"{self.menu.command_two} charger un tournoi existant",
                                      "",
                                      f"{self.menu.command_exit} : quitter le programme."],
                             title="tournoi")
        return input("")
