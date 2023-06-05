"""
Controller module
"""


import sys
import time
from myclass import class_menu
from myscripts import view as v
from myscripts import model as m

sys.path.insert(0, '../myclass')
sys.path.insert(0, '../myscripts')


class Controller:
    """
    Controller class
    """
    def __init__(self, model: m.Model, view: v.View):
        self.model = model
        self.view = view
        self.menu = class_menu.Menu()

        # initialize values of every menu'selection (status)
        self.selected_element = {}
        for navigation in self.menu.tree:
            self.selected_element[navigation] = False
        print(self.selected_element)

    def kernel(self) -> None:
        """
        the almighty kernel
        """
        while True:
            # select a tournament by either creating or loading one
            if self.selected_element[self.menu.navigation_tournament] is False:
                self.selected_element[self.menu.navigation_tournament] = self.select_tournament()
                continue

            if self.selected_element[self.menu.navigation_player_list] is False:
                self.selected_element[self.menu.navigation_player_list] = self.select_player_list()
                continue

            if self.selected_element[self.menu.navigation_round] is False:
                self.selected_element[self.menu.navigation_round] = self.select_player_list()
                continue

            # exit program if reached, preventing infinite loop
            self.view.show_in_console(title="BOUCLE INFINIE -> fin du programme")

            self.exit_program(show_exit_message=False)

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
            print("Fin du programme")
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
                                        self.menu.command_three: self.load_dummy_default_player_list,
                                        self.menu.command_exit: self.exit_program})

    def select_player_list(self) -> bool:
        """
        Ask view for player list
        Roots view's return to related function.
        Returns boolean == choice in choice list and could be executed.
        """
        prompt_result = self.view.prompt_player_list_selection()
        if prompt_result == "r":
            self.menu_cleaner(self.menu.navigation_player_list)
            return False

        return self.rooter(choice=prompt_result,
                           choice_dict={self.menu.command_one: self.create_player_list,
                                        self.menu.command_two: self.load_dummy_default_player_list,
                                        self.menu.command_exit: self.exit_program})

    def create_new_tournament(self):
        """
        Create new tournament from view's player list
        returns None
        """
        self.model.name = "Tournoi club du vieux Lyon"
        self.model.location = "Lyon - France"
        self.model.date_start = time.localtime()

        self.model.player_list = self.view.get_player_list()

    def load_existing_tournament(self):
        """
        load an existing tournament
        """
        print("pas encore possbible")

    def create_player_list(self):
        """
        Create new tournament from view's player list
        returns None
        """
        self.model.name = "Tournoi club du vieux Lyon"
        self.model.location = "Lyon - France"
        self.model.date_start = time.localtime()

        self.model.player_list = self.view.get_player_list()

    def load_existing_player_list(self):
        """
        load an existing tournament
        """
        print("pas encore possbible")

    def load_dummy_default_tournament(self):
        """
        load an existing tournament
        """
        print("pas encore possbible")

    def load_dummy_default_player_list(self):
        """
        load an existing tournament
        """
        print("pas encore possbible")

    def select_round(self):
        """
        round selection
        """
        self.model.create_new_round()
