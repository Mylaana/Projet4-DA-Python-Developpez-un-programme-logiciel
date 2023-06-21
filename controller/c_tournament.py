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
        super().__init__(model=model, view=view)
        self.view: v.ViewTournament = view
        self.model: m.Tournament = model
        self.debug = debug
        self.model.data_section_name = self.menu.navigation_tournament
        self.menu.name_controller = self.model.data_section_name
        self.step_validated = False

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
        gets None
        Returns bool
        """
        while True:
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
        gets none
        returns bool
        """
        self.model.name = "Tournoi club local"
        self.model.location = "a coté de la mairie"
        self.model.date_start = time.localtime()
        self.model.description = "ouvert à tous"

        return True

    def load_existing_tournament(self):
        """
        load an existing tournament
        """
        # gets file name to load
        self.model.data.file_name = self.view.prompt_tournament_load(self.model.data.get_file_list()) + ".json"

        self.model.data.load_tournament()
        self.model.data.load_all()
        self.model.data.update_all()
        self.model.data.save_data()

        if self.step_validated is False:
            self.view.invalid_no_data_found()
        else:
            self.view.display_loading_status(data_loaded=self.model.data.data)

        return self.step_validated
