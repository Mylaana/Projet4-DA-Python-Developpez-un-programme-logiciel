"""
Controller module
"""
# import time
# from . import event_handler as event
from . import view as v
from . import model as m


class Controller:
    """
    Controller class
    """
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

    def program_start(self):
        """
        Starting the view prompts
        """
        self.view.start()

    def create_new_tournament(self):
        """
        Create new tournament from view's player list
        returns None
        """
        the_list = self.view.get_player_list()
        self.model.player_list = the_list

    def load_existing_tournament(self):
        """
        load an existing tournament
        """
        print("pas encore possbible")
