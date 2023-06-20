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
        return self.rooter(choice=self.view.prompt_tournament_creation_mode(),
                           choice_dict={self.menu.command_one: self.get_tournament_info,
                                        self.menu.command_two: self.dummy_create_tournament,
                                        self.menu.command_exit: self.exit_program})

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
            data_is_valid = True
            for result_line in result:
                if result_line["value"] is None:
                    data_is_valid = False
                    error_message = result_line["caption"] + " n'a pas été rempli"
                    break

                if str(type(result_line["value"])) != str(result_line["type"]):
                    data_is_valid = False
                    error_message = result_line["caption"] + " n'est pas du bon type"
                    break

            if not data_is_valid:
                self.view.invalid_info_entered(error_message)
            else:
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
        self.model.name = "Tournoi club du vieux Lyon"
        self.model.location = "Lyon - France"
        self.model.date_start = time.localtime()
        self.model.description = "tournoi par temps bleu"

        return True

    def load_existing_tournament(self):
        """
        load an existing tournament
        """
        self.model.data.load_file()
        self.model.data.load_all()
        self.model.data.update_all()
        self.model.data.save_data()

        if self.step_validated is False:
            message = "pas de donnée à charger dans ce tournoi, veuillez en créer un nouveau"
        else:
            message = self.get_model_attribute_as_printable_list()

        self.view.display_loading_status(message=message)

        return self.step_validated
