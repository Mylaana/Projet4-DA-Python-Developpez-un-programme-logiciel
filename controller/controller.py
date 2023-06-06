"""
Controller module
"""


import sys
import time
from CommonClass import menu
sys.path.insert(0, '../CommonClass')


class Controller:
    """
    Controller class
    """
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.menu = menu.Menu()

        # initialize values of every menu'selection (status)
        self.selected_element = {}
        for navigation in self.menu.tree:
            self.selected_element[navigation] = False

    def rooter(self, choice: str, choice_dict: dict) -> bool:
        """
        Gets a string as choice (coming from view) and a dict like : dict[str]: function_name
        Call the function corresponding to choice if found.

        Returns Boolean : True if found, False if not
        """
        if choice not in choice_dict:
            self.view.invalid_choice()
            return False

        # runs the controller's function related to choice, see choice_dict
        choice_dict[choice]()
        return True

    def exit_program(self, show_exit_message: bool = True) -> None:
        """
        Exit program
        """
        if show_exit_message:
            self.view.show_in_console(title="fin du programme")

        sys.exit()

    def menu_cleaner(self, running_menu_name: str):
        """
        Gets the name of RUNNING MENU and sets his parent to false
        Cleans self variable and reset related status if needed
        """
        # sets the parent of running_menu_name menu selection value to false
        if running_menu_name != self.menu.navigation_tournament:
            self.selected_element[self.menu.tree_parent[running_menu_name]] = False

        # sets every child selection value to false if parent is set to false
        for parent, child in self.menu.tree_child.items():
            if not self.selected_element[parent]:
                self.selected_element[child] = False

    def select_tournament(self) -> bool:
        """
        Ask view if the user wants to create or load tournament.
        Roots view's return to related function.

        Returns boolean == choice in choice list and could be executed.
        """
        return self.rooter(choice=self.view.prompt_tournament_selection(),
                           choice_dict={self.menu.command_one: self.create_new_tournament,
                                        self.menu.command_two: self.load_existing_tournament,
                                        self.menu.command_exit: self.exit_program})

    def create_new_tournament(self):
        """
        Create new tournament from view's player list
        returns None
        """
        self.model.name = "Tournoi club du vieux Lyon"
        self.model.location = "Lyon - France"
        self.model.date_start = time.localtime()

        # self.model.player_list = self.view.get_player_list()

    def load_existing_tournament(self):
        """
        load an existing tournament
        """
        print("pas encore possbible")

    def load_dummy_default_tournament(self):
        """
        load an existing tournament
        """
        print("pas encore possbible")
