"""
Controller module
"""
# import time
from . import event_handler as event
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

        event.wait_for_event(
                    message=["souhaitez-vous :", 
                             "'1' créer un nouveau tournoi",
                             "'2' charger un tournoi existant"
                             ],
                    choice_possibilities={
                        "1": self.create_new_tournament,
                        "2": self.load_existing_tournament
                        },
                    quit_additionnal_option=True)

    def create_new_tournament(self):
        """
        Create new tournament from view's player list
        returns None
        """
        self.model.player_list = self.view.get_player_list()

    def load_existing_tournament(self):
        """
        load an existing tournament
        """
        print("pas encore possbible")
