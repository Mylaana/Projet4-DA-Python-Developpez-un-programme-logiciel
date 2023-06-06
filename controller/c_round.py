"""
Controller module
"""


import sys
from View import v_round as v
from Model import m_round as m
from . import controller as c
sys.path.insert(0, '../View')
sys.path.insert(0, '../Model')
sys.path.insert(0, '../CommonClass')


class ControllerRound(c.Controller):
    """
    Controller class
    """
    def __init__(self, model: m.RoundList, view: v.View):
        super().__init__(model=model, view=view)

        # initialize values of every menu'selection (status)
        self.selected_element = {}
        for navigation in self.menu.tree:
            self.selected_element[navigation] = False

    def start_first_round(self):
        """
        first round generation
        """
        self.model.create_new_round()
        self.view.display_round_pairings(self.model.get_current_round_pairings())
        return True

    def start_next_round(self):
        """
        any following round
        """
        result = self.model.create_new_round()
        self.view.display_round_pairings(self.model.get_current_round_pairings())
        return result
