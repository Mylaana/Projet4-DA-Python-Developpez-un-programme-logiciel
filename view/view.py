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
        self.player_list = []
        self.menu = m.Menu()

    def show_in_console(self, message="", title=""):  # type: (str or list or None, str or None) -> None
        """
        Receives either str or list[str]
        Returns none
        """
        # print("\n\n")
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
