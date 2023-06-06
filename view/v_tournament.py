"""
view module
"""
import sys
from CommonClass import menu as m
sys.path.insert(0, '../CommonClass')


class View:
    """
    View class
    """
    def __init__(self):
        self.player_list = self.dummy_generate_player_list()
        self.menu = m.Menu()

    def show_in_console(self, message="", title=""):  # type: (str or list or None, str or None) -> None
        """
        Receives either str or list[str]
        Returns none
        """
        print("\n\n")
        if title != "":
            print("-----------------------------------\n" + title.upper() + "\n-----------------------------------\n")

        if message == "":
            return

        if isinstance(message, str):
            print(message)
        elif isinstance(message, list):
            for line in message:
                print(line)
        print("\n")

    def invalid_choice(self):
        """
        shows the choice is not valid
        """
        print("\n\nLe choix effectué n'est pas valide !\n")

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
                                      f"{self.menu.command_exit} : quitter le programme."],
                             title="tournoi")
        return input("")

    def prompt_player_list_selection(self):
        """
        Prompts user for :
        - using default player list
        - create new list of player
        - return to tournament selection
        - exiting the program

        Returns :
        - [COMMAND_ONE] to default player list
        - [COMMAND_TWO] to create new list of player
        - [COMMAND_RETURN] to return to tournament selection
        - [COMMAND_SAVE] to save the tournament actual state
        - [COMMAND_LOAD] to load a previously saved tournament
        - [COMMAND_EXIT] to exit program
        """
        self.show_in_console(message=["souhaitez-vous :",
                                      f"{self.menu.command_one} utiliser la liste de joueurs par défaut",
                                      f"{self.menu.command_two} créer une liste de joueurs",
                                      f"{self.menu.command_save} : {self.menu.command_description_save}",
                                      f"{self.menu.command_load} : {self.menu.command_description_load}",
                                      f"{self.menu.command_return} : {self.menu.command_description_return}",
                                      f"{self.menu.command_exit} : {self.menu.command_description_exit}"],
                             title="liste des joueurs")
        return input("")

    def get_player_list(self):
        """
        Returns player list with following shape :
        [Name1 FamilyName1 Birthdate1(AAAA/MM/DD), ...]
        """

        print("voici la liste des joueurs par défaut :\n")
        for player_info in self.player_list:
            print(str(player_info))

    def dummy_generate_player_list(self) -> list[str]:
        """
        player list for testing purpose
        """
        return [
            "Jeanne Thériault 1989/12/07",
            "Dexter Chesnay 1995/07/16",
            "Chandler Bisaillon 1969/02/15",
            "Guillaume Aoust 1994/10/12",
            "Christiane Laramée 1999/01/22",
            "Élise Lévesque 2004/03/19",
            "Orville Mireault 1984/10/06",
            "Étienne Salois 1992/12/06"
        ]

    def dummy_generate_scores(self):
        """
        Randomly generate players scores for this round.
        This is a dummy function (the scores should be determined by every games,
        instead of randomed for app building purpose).
        """

    def display_round_pairings(self, pairing_list):
        """
        gets list with uneven index being player "A"s and even players being players "B"s
        returns none
        """
        self.show_in_console(pairing_list)
