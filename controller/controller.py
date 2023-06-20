"""
Controller module
"""

import os
import sys
from Model import model as m
from View import view as v
from CommonClass import menu
sys.path.insert(0, '../CommonClass')


class Controller:
    """
    Controller class
    """
    def __init__(self, model: m.Model, view: v.View, debug: bool = False):
        self.model: m.Model = model
        self.view: v.View = view
        self.menu = menu.Menu()
        self.debug = debug
        self.step_validated = False

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

        return choice_dict[choice]()

    def exit_program(self, show_exit_message: bool = True) -> None:
        """
        Exit program
        """
        if show_exit_message:
            self.view.show_in_console(title="fin du programme")

        self.model.data.update_all()
        sys.exit()

    def menu_cleaner(self, running_menu_name: str):  # DELETE
        """
        Gets the name of RUNNING MENU and sets his parent to false
        Cleans self variable and reset related status if needed
        """
        # sets the parent of running_menu_name menu selection value to false
        """
        if running_menu_name != self.menu.navigation_tournament:
            self.selected_element[self.menu.tree_parent[running_menu_name]] = False

        # sets every child selection value to false if parent is set to false
        for parent, child in self.menu.tree_child.items():
            if not self.selected_element[parent]:
                self.selected_element[child] = False
        """
    def set_player_group(self, player_list: list, player_group: dict[int, dict]):
        """
        gets a list of player id
        pass the list to model
        returns none
        """
        self.model.player_list_id = player_list
        self.model.player_group = player_group

    def set_up_data_info(self):
        """
        gets none
        set up information in data object
        returns none
        """

        # links the controller to the controller list in data object for load/save/update ..._all functions
        self.model.data.controller_list.append(self)
        self.model.data_section_name = self.menu.name_controller
        self.model.data.data["status"][self.menu.name_controller] = False
        model_attributes = {}
        for attribute, values in vars(self.model).items():
            if attribute not in self.model.data_excluded:
                model_attributes[attribute] = values

        self.model.data.data[self.menu.name_controller] = model_attributes

    def load_data(self):
        """
        gets none
        loads previously saved data
        returns none
        """
        self.model.load_data()
        self.step_validated = self.model.data.loaded_data["status"][self.menu.name_controller]

    def update_data(self):
        """
        gets none
        calls model.update_data
        returns none
        """
        self.model.update_data()

    def save_data(self):
        """
        gets none
        calls model.update_data
        returns none
        """
        self.model.save_data()

    def get_info_list_from_user(self, info_list: list[dict], title: str) -> list[dict]:
        """
        gets a list of dict, each dict containing :
        value name
        value type

        returns bool if list is filled and valid
        """
        return self.view.prompt_info_list(info_list=info_list, title=title)

    def get_prompt_dict_from_var(self, attribute, message: str) -> dict:
        """
        gets a variable name
        returns a dictionnary like :
        "name" : variable_name
        "type" : type(variable)
        "value" : None
        """
        return {
            "caption": str(message),
            "type": type(attribute),
            "value": None,
            "default_value": attribute
        }

    def get_model_attribute_as_printable_list(self) -> list:  # DELETE
        """
        gets none
        return model's formated info as list like  [attribute_name : value]
        """

        message = [f"{attribute} : {value}" for attribute, value in vars(self.model).items()
                   if attribute not in self.model.data_excluded]

        return message
