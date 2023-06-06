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
    def __init__(self, model: m.Tournament, view: v.View):
        super().__init__(model=model, view=view)

        # initialize values of every menu'selection (status)
        self.selected_element = {}
        for navigation in self.menu.tree:
            self.selected_element[navigation] = False

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
