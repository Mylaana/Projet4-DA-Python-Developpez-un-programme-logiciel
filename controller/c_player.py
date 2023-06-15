"""
Controller module
"""


import sys
from View import v_player as v
from Model import m_player as m
from . import controller as c
sys.path.insert(0, '../View')
sys.path.insert(0, '../Model')
sys.path.insert(0, '../CommonClass')


class ControllerPlayer(c.Controller):
    """
    Controller class
    """
    def __init__(self, model: m.PlayerList, view: v.ViewPlayer, debug: bool = False):
        super().__init__(model=model, view=view)
        self.view: v.ViewPlayer = view
        self.model: m.PlayerList = model
        self.debug = debug
        self.model.data_section_name = self.menu.navigation_player_list
        self.menu.name_controller = self.model.data_section_name

    def select_player_list(self) -> bool:
        """
        Ask view for player list
        Roots view's return to related function.
        Returns boolean == choice in choice list and could be executed.
        """
        prompt_result = self.view.prompt_player_list_selection()
        if prompt_result == self.menu.command_return:
            self.menu_cleaner(self.menu.navigation_player_list)
            return False

        return self.rooter(choice=prompt_result,
                           choice_dict={self.menu.command_one: self.create_player_group,
                                        self.menu.command_two: self.load_dummy_default_player_list,
                                        self.menu.command_exit: self.exit_program})

    def create_player_group(self):
        """
        Create new tournament from view's player list
        returns None
        """
        player_list = self.view.prompt_player_group_creation()
        if player_list:
            return True

    def load_existing_player_list(self):
        """
        load an existing tournament
        """
        self.model.load_data()

    def load_dummy_default_player_list(self):
        """
        load an existing tournament
        """
        self.model.set_player_group(self.view.dummy_generate_player_list())
        return True

    def get_player_list_id(self) -> list:
        """
        gets none
        returns a player id list
        """
        return self.model.player_list_id

    def get_player_group(self) -> dict[int, dict]:
        """
        gets none
        returns a player id list
        """
        return self.model.player_group
