"""
Controller module
"""
# import time
# from . import event_handler as event
import sys
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
        self.tournament_selected = False

    def kernel(self) -> None:
        """
        the almighty kernel
        """

        while True:
            # select a tournament by either creating or loading one
            if self.tournament_selected is False:
                self.tournament_selected = self.select_tournament()
                continue

            # exit program if reached, preventing infinite loop
            print("\n\n-----------------------------------" +
                  "\nBOUCLE INFINIE -> fin du programme" +
                  "\n-----------------------------------")

            self.exit_program(show_exit_message=False)

    def rooter(self, choice: str, choice_dict: dict) -> bool:
        """
        Gets a string as choice (coming from view) and a dict like : dict[str]: function_name
        Call the function corresponding to choice if found.

        Returns Boolean : True if found, False if not
        """
        if choice not in choice_dict:
            self.view.invalid_choice()
            return False

        choice_dict[choice]()
        return True

    def exit_program(self, show_exit_message: bool = True) -> None:
        """
        Exit program
        """
        if show_exit_message:
            print("Fin du programme")
        sys.exit()

    def select_tournament(self) -> bool:
        """
        Ask view if the user wants to create or load tournament.
        Roots view's return to related function.

        Returns boolean == choice in choice list and could be executed.
        """
        return self.rooter(choice=self.view.prompt_tournament_selection(),
                           choice_dict={"1": self.create_new_tournament,
                                        "2": self.load_existing_tournament,
                                        "q": self.exit_program})

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
