"""
Controller module
"""
import time
from . import view as v
from . import model as m
from . import event_handler as event


class Controller:
    """
    Controller class
    """
    def __init__(self):

        self.model = m.Model(
                            name="Tournoi club du vieux Lyon",
                            location="Lyon - France",
                            date_start=time.localtime(),
                            round_number=4
                            )

        self.view = v.View()

        # test on event
        choix = {"1": self.message1, "2": self.message2}
        event.wait_for_event(
                    message=["veuillez choisir :",
                             "1 pour afficher le message 1",
                             "2 pour afficher le message 2"],
                    choice_possibilities=choix,
                    quit_additionnal_option=True)

    def create_new_tournament(self):
        """
        Create new tournament from view's player list
        returns None
        """
        self.model.player_list = self.view.get_player_list()

    def message1(self):
        print("message 1 dskjhfqlsdkj")

    def message2(self):
        print("message 2 123456789")
