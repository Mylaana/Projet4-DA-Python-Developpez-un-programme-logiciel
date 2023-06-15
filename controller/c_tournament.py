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
        self.model.name = "Tournoi club du vieux Lyon"
        self.model.location = "Lyon - France"
        self.model.date_start = time.localtime()
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
            message = self.get_tournament_info()

        self.view.display_loading_status(message=message)

        return self.step_validated

    def load_dummy_default_tournament(self):
        """
        load an existing tournament
        """
        input("dummy pas encore possbible")

    def get_tournament_info(self) -> list:
        """
        gets none
        return model's formated info as list like  [attribute_name : value]
        """

        message = [f"{attribute} : {value}" for attribute, value in vars(self.model).items()
                   if attribute not in self.model.data_excluded]

        return message
