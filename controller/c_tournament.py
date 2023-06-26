"""
Controller module
"""


import sys
import time
from View import v_tournament as v
from Model import m_tournament as m
from . import controller as c
sys.path.insert(0, '../View')
sys.path.insert(0, '../Model')
sys.path.insert(0, '../CommonClass')


class ControllerTournament(c.Controller):
    """
    Controller class
    """
    def __init__(self, model: m.Tournament, view: v.ViewTournament, debug: bool = False):
        """
        Initialize the ControllerTournament object.

        Args:
        - model (m.Tournament): The Tournament model object.
        - view (v.ViewTournament): The ViewTournament object.
        - debug (bool, optional): Debug mode flag. Defaults to False.
        """
        super().__init__(model=model, view=view)
        self.view: v.ViewTournament = view
        self.model: m.Tournament = model
        self.debug = debug
        self.model.data_section_name = self.menu.navigation_tournament
        self.menu.name_controller = self.model.data_section_name
        self.step_validated = False

    def select_tournament(self) -> bool:
        """
        Ask the view if the user wants to create or load a tournament.
        Calls the related function.

        Returns:
        - (bool) The choice in the choice list and whether it can be executed.
        """
        self.view.clear_console()
        return self.rooter(choice=self.view.prompt_tournament_selection(),
                           choice_dict={self.menu.command_one: self.create_new_tournament,
                                        self.menu.command_two: self.load_existing_tournament,
                                        self.menu.command_three: self.report_selection,
                                        self.menu.command_exit: self.exit_program})

    def create_new_tournament(self):
        """
        Roots the user choice to the appropriate tournament creation method.

        Returns:
        - None.
        """
        self.view.clear_console()
        result = self.rooter(choice=self.view.prompt_tournament_creation_mode(),
                             choice_dict={self.menu.command_one: self.get_tournament_info,
                                          self.menu.command_two: self.dummy_create_tournament,
                                          self.menu.command_exit: self.exit_program})

        self.model.data.create_json(self.model.name + f" {self.model.date_start.tm_year}"
                                    f" {self.model.date_start.tm_mon} {self.model.date_start.tm_mday}")

        return result

    def get_tournament_info(self):
        """
        Get information for creating a tournament.

        Returns:
        - (bool) True if successful.
        """
        while True:
            self.view.clear_console()
            prompt_list = []
            prompt_list.append(self.get_prompt_dict_from_var(
                attribute=self.model.name, message="nom du tournoi"))
            prompt_list.append(self.get_prompt_dict_from_var(
                attribute=self.model.location, message="emplacement"))
            prompt_list.append(self.get_prompt_dict_from_var(
                attribute=self.model.round_number, message="nombre de round"))
            prompt_list.append(self.get_prompt_dict_from_var(
                attribute=self.model.description, message="description"))

            result = self.get_info_list_from_user(info_list=prompt_list.copy(), title="tournoi - creation tournoi")

            # check for info list content being conform
            data_is_valid = self.check_info_list_result(result)

            # exit loop if everything conform
            if data_is_valid:
                break

        self.model.name = result[0]["value"]
        self.model.location = result[1]["value"]
        self.model.round_number = result[2]["value"]
        self.model.description = result[3]["value"]
        self.model.date_start = time.localtime()

        return True

    def dummy_create_tournament(self):
        """
        Create a dummy tournament.

        Returns:
        -(bool) True if successful.
        """
        self.model.name = "Tournoi club local"
        self.model.location = "a coté de la mairie"
        self.model.date_start = time.localtime()
        self.model.description = "ouvert à tous"

        return True

    def load_existing_tournament(self) -> bool:
        """
        Load an existing tournament.

        Returns:
        - (bool): True if successful.
        """

        # gets file name to load
        tournament_list = self.model.data.get_file_list()
        if tournament_list == []:
            self.view.invalid_no_tournament_found_in_data()
            return self.step_validated

        self.model.data.file_name = self.view.prompt_tournament_load(self.model.data.get_file_list()) + ".json"

        self.model.data.load_tournament()

        # locks the data object if loaded tournament is already finished
        if self.model.data.data["status"]["finished"]:
            self.model.data.data_locked = True
            self.model.data.data = self.model.data.loaded_data.copy()
            return

        self.model.data.load_all()
        self.model.data.update_all()
        self.model.data.save_data()
        self.view.display_loading_status(data_loaded=self.model.data.data)

        return self.step_validated

    def set_tournament_finished(self):
        """
        Set the tournament as finished.

        Returns:
        - None.
        """
        self.model.data.data["status"]["finished"] = True
        self.model.date_end = time.localtime()
        self.model.update_data()
        self.model.save_data()
        self.model.data.data_locked = True

    def tournament_finished(self):
        """
        Handle the post tournament finished menu.

        Returns:
        - None.
        """
        self.view.clear_console()
        return self.rooter(choice=self.view.prompt_tournament_finished(),
                           choice_dict={self.menu.command_one: self.report_selection,
                                        self.menu.command_exit: self.exit_program})
