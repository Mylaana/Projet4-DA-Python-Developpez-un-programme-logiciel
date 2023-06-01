"""
Controller module
"""
# import time
# from . import event_handler as event
import sys
from . import view as v
from . import model as m


class Controller:
    """
    Controller class
    """

    # these elements helps adding a hierarchy in console's choice for navigation purpose
    # menu names
    _MENU_NAME_TOURNAMENT = "tournament"
    _MENU_NAME_PLAYER_LIST = "player_list"
    _MENU_NAME_ROUND = "round"

    # Creating menu tree
    _MENU_TREE = (_MENU_NAME_TOURNAMENT,
                  _MENU_NAME_PLAYER_LIST,
                  _MENU_NAME_ROUND)
    
    # key = child : value = parent
    _MENU_TREE_CHILD = {}
    # key = parent : value = child
    _MENU_TREE_PARENT = {}

    # filling _MENU_TREE_PARENT and _MENU_TREE_CHILD
    parent = None
    for item in _MENU_TREE:
        child = parent
        parent = item
        if child is not None:
            _MENU_TREE_CHILD[child] = parent
            _MENU_TREE_PARENT[parent] = child

    # basic menu commands
    _MENU_COMMAND_RETURN = "r"
    _MENU_COMMAND_EXIT = "q"

    def __init__(self, model: m.Model, view: v.View):
        """
        self.model = m.Model(
                            name="Tournoi club du vieux Lyon",
                            location="Lyon - France",
                            date_start=time.localtime(),
                            round_number=4
                            )
        """
        self.model = model
        self.view = view

        # stocks the status (value) of every selection
        self.selected_element = {self._MENU_NAME_TOURNAMENT: False,
                                 self._MENU_NAME_PLAYER_LIST: False
                                 }

    def kernel(self) -> None:
        """
        the almighty kernel
        """
        while True:
            # select a tournament by either creating or loading one
            if self.selected_element[self._MENU_NAME_TOURNAMENT] is False:
                self.selected_element[self._MENU_NAME_TOURNAMENT] = self.select_tournament()
                continue

            if self.selected_element[self._MENU_NAME_PLAYER_LIST] is False:
                self.selected_element[self._MENU_NAME_PLAYER_LIST] = self.select_player_list()
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
        Gets the name of RUNNING MENU
        Cleans self variable and reset related status if needed
        """
        # sets the parent menu selection value to false
        if running_menu_name != self._MENU_NAME_TOURNAMENT:
            self.selected_element[self._MENU_TREE_PARENT[running_menu_name]] = False

        # sets every child selection value to false if parent is set to false
        for parent, child in self._MENU_TREE_CHILD.items():
            if not self.selected_element[parent]:
                self.selected_element[child] = False

    def select_tournament(self) -> bool:
        """
        Ask view if the user wants to create or load tournament.
        Roots view's return to related function.

        Returns boolean == choice in choice list and could be executed.
        """
        return self.rooter(choice=self.view.prompt_tournament_selection(),
                           choice_dict={"1": self.create_new_tournament,
                                        "2": self.load_existing_tournament,
                                        "q": self.exit_program})

    def select_player_list(self) -> bool:
        """
        Ask view for player list
        Roots view's return to related function.
        Returns boolean == choice in choice list and could be executed.
        """
        prompt_result = self.view.prompt_player_list_selection()
        if prompt_result == "r":
            self.menu_cleaner(self._MENU_NAME_PLAYER_LIST)
            return False

        return self.rooter(choice=prompt_result,
                           choice_dict={"1": self.create_new_tournament,
                                        "2": self.load_existing_tournament,
                                        "q": self.exit_program})

    def create_new_tournament(self):
        """
        Create new tournament from view's player list
        returns None
        """
        self.model.player_list = self.view.get_player_list()

    def load_existing_tournament(self):
        """
        load an existing tournament
        """
        print("pas encore possbible")
