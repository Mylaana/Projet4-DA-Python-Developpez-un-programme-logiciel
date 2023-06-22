"""
Controller module
"""

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
        """
        Initialize the Controller object.

        Args:
        - model (m.Model): The Model object.
        - view (v.View): The View object.
        - debug (bool, optional): Debug mode flag. Defaults to False.
        """
        self.model: m.Model = model
        self.view: v.View = view
        self.menu = menu.Menu()
        self.debug = debug
        self.step_validated = False

    def rooter(self, choice: str, choice_dict: dict) -> bool:
        """
        Gets a string as choice (coming from view) and a dict like: dict[str]: function_name.
        Calls the function corresponding to choice if found.

        Args:
        - choice (str): used to select the related method to call from choice_dict.
        - choice_dict (dict): Dictionary containing the method to call.

        Returns:
        - (bool) True if found, False if not.
        """
        if choice not in choice_dict:
            self.view.invalid_choice()
            return False
        # runs the controller's function related to choice, see choice_dict

        return choice_dict[choice]()

    def exit_program(self, show_exit_message: bool = True) -> None:
        """
        Exit the program
        """
        if show_exit_message:
            self.view.show_in_console(title="fin du programme")

        self.model.data.update_all()
        sys.exit()

    def set_player_group(self, player_list: list, player_group: dict[int, dict]):
        """
        Set the player group.

        Args:
        - player_list (list): List of player IDs.
        - player_group (dict): Dictionary containing player information.

        Returns:
        - None.
        """
        self.model.player_list_id = player_list
        self.model.player_group = player_group

    def set_up_data_info(self):
        """
        Set up information in data object.

        Returns:
        - None.
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
        Load previously saved data

        Returns:
        - None.
        """
        self.model.load_data()
        self.step_validated = self.model.data.loaded_data["status"][self.menu.name_controller]

    def update_data(self):
        """
        Update data.

        Returns:
        - None.
        """
        self.model.update_data()

    def save_data(self):
        """
        Save data.

        Returns:
        - None.
        """
        self.model.save_data()

    def get_info_list_from_user(self, info_list: list[dict], title: str) -> list[dict]:
        """
        Prompt the user for a list of information.

        Args:
        - info_list (list[dict]): List of dictionaries containing information details.
        - title (str): Title of the prompt.

        Returns:
        - list[dict]: List of dictionaries with user-entered information.
        """
        return self.view.prompt_info_list(info_list=info_list, title=title)

    def check_info_list_result(self, info_list: list[dict]) -> bool:
        """
        Check if the user-entered information is valid.

        Args:
        - info_list (list[dict]): List of dictionaries containing information details.

        Returns:
        - (bool): True if the information is valid, False otherwise.
        """
        data_is_valid = True
        for result_line in info_list:
            if result_line["value"] is None:
                data_is_valid = False
                self.view.invalid_info_entered_empty(result_line["caption"])
                break

            if str(type(result_line["value"])) != str(result_line["type"]):
                data_is_valid = False
                self.view.invalid_info_entered_type(result_line["caption"])
                break

        return data_is_valid

    def get_prompt_dict_from_var(self, attribute, message: str) -> dict:
        """
        Create a prompt dictionary from a variable name.

        Args:
        - attribute: The variable value.
        - message (str): The prompt message.

        Returns:
        - (dict): A dictionary with keys 'caption', 'type', 'value', and 'default_value'.
        """
        return {
            "caption": str(message),
            "type": type(attribute),
            "value": None,
            "default_value": attribute
        }

    def report_selection(self) -> None:
        """
        Display a menu for report selection and execute the selected report.

        Returns:
        - None.
        """

        report_list = ["Liste de tous les joueurs",
                       "Liste de tous les tournois",
                       "Informations sur un tournoi",
                       "Lister les joueurs du tournoi actif",
                       "Lister les rounds/matchs du tournoi actif"]

        report_dict = {report_list[0]: self.model.data.report_player_list,
                       report_list[1]: self.model.data.report_tournament_list,
                       report_list[2]: self.report_tournament_info,
                       report_list[3]: self.model.data.report_active_tournament_player_list,
                       report_list[4]: self.model.data.report_rounds_and_match}

        report_title = {report_list[0]: "liste des joueurs",
                        report_list[1]: "liste des tournois",
                        report_list[2]: "informations sur le tournoi",
                        report_list[3]: "liste des joueurs du tournoi",
                        report_list[4]: "rounds et matchs"}

        prompt_list = report_list.copy()

        if self.model.data.data["status"]["player_list"] is False:
            prompt_list.remove(report_list[3])

        if (self.model.data.data["round"]["round_counter"] == 1 and
                self.model.data.data["round"]["current_round_step"] == 0):
            prompt_list.remove(report_list[4])

        report_selected = self.view.prompt_report_choice(prompt_list)
        self.view.display_report(
            report_dict[report_selected](), report_title[report_selected])

        return False

    def report_tournament_info(self) -> list:
        """
        Prompt the user to select a tournament.

        Returns:
        - list: List containing the tournament information to be displayed.
        """
        tournament_list = self.model.data.report_tournament_list()
        if tournament_list == []:
            return []

        tournament_name = self.view.prompt_report_tournament_name(
            tournament_list)
        return self.model.data.report_tournament_info(tournament_name=tournament_name)
