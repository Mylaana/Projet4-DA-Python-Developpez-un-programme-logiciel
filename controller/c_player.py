"""
Controller module
"""


import sys
from View import v_player as v
from Model import m_player as m
from . import controller as c
sys.path.insert(0, '../View')
sys.path.insert(0, '../Model')
sys.path.insert(0, '../CommonClass')


class ControllerPlayer(c.Controller):
    """
    Controller player class
    """
    def __init__(self, model: m.PlayerList, view: v.ViewPlayer, debug: bool = False):
        """
        Initialize the ControllerPlayer object.

        Args:
        - model (m.PlayerList): The PlayerList model object.
        - view (v.ViewPlayer): The ViewPlayer object.
        - debug (bool, optional): Debug mode flag. Defaults to False.
        """
        super().__init__(model=model, view=view)
        self.view: v.ViewPlayer = view
        self.model: m.PlayerList = model
        self.debug = debug
        self.model.data_section_name = self.menu.navigation_player_list
        self.menu.name_controller = self.model.data_section_name

    def select_player_list(self) -> bool:
        """
        Ask view for player list
        Calls the related function.

        Returns:
        - (bool) if the related function was successful.
        """
        prompt_result = self.view.prompt_player_list_selection()

        return self.rooter(choice=prompt_result,
                           choice_dict={self.menu.command_one: self.create_player_group,
                                        self.menu.command_two: self.load_dummy_default_player_list,
                                        self.menu.command_three: self.report_selection,
                                        self.menu.command_exit: self.exit_program})

    def create_player_group(self) -> bool:
        """
        Create a list of player using view's output.

        Returns:
        - (bool) True if successful
        """
        while True:
            player_number = self.view.prompt_player_number()
            if not player_number.isdigit():
                self.view.invalid_info_entered_number_needed()
                continue

            player_number = int(player_number)

            if player_number < self.model.minimum_player_number:
                self.view.invalid_player_number_minimum(self.model.minimum_player_number)
                continue

            if player_number % 2 != 0:
                self.view.invalid_player_number_uneven()
                continue

            break

        # generates an empty player list and prompt user for entering every player info
        while True:
            prompt_list = []

            for player_id in range(1, player_number + 1):
                # player name
                prompt_list.append(self.get_prompt_dict_from_var(
                    attribute="name" + str(player_id),
                    message="Nom joueur " + str(player_id)))

                # player last name
                prompt_list.append(self.get_prompt_dict_from_var(
                    attribute="last_name" + str(player_id),
                    message="Nom famille joueur " + str(player_id)))

                # player birthday
                prompt_list.append(self.get_prompt_dict_from_var(
                    attribute="birth_date" + str(player_id),
                    message="Date de naissance joueur " + str(player_id)))

            result = self.get_info_list_from_user(info_list=prompt_list.copy(),
                                                  title="liste des joueurs : ajouter des joueurs")

            # check for info list content being conform
            data_is_valid = self.check_info_list_result(result)

            # exit loop if everything conform
            if data_is_valid:
                break

        player_list = []
        info_counter = 1
        for line in result:
            if info_counter == 1:
                player_dict = {}
                player_dict["name"] = line["value"]
                info_counter += 1
                continue

            elif info_counter == 2:
                player_dict["last_name"] = line["value"]
                info_counter += 1
                continue

            elif info_counter == 3:
                player_dict["birth_date"] = line["value"]
                player_list.append(player_dict.copy())
                info_counter = 1
                continue

        self.model.set_player_group(player_list)
        return True

    def load_existing_player_list(self):
        """
        load data into model.

        Returns:
        - None.
        """
        self.model.load_data()

    def load_dummy_default_player_list(self) -> bool:
        """
        set model's player group from view's dummy player list.

        Returns:
        - (bool) True if successful.
        """
        self.model.set_player_group(self.view.dummy_generate_player_list())
        return True

    def get_player_list_id(self) -> list:
        """
        Returns:
        - (list) of player ID from model.
        """
        return self.model.player_list_id

    def get_player_group(self) -> dict[int, dict]:
        """
        Returns:
        - (dict) player_group containing all players informations from model.
        """
        return self.model.player_group
