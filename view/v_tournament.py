"""
view module
"""
from . import view as v


class ViewTournament(v.View):
    """
    View class
    """
    def prompt_tournament_selection(self) -> str:
        """
        Prompts user for :
        - new tournament
        - load tournament
        - exiting the program

        Returns :
        - [COMMAND_ONE] to create new tournament
        - [COMMAND_TWO] to load tournament
        - [COMMAND_SAVE] to save the tournament actual state
        - [COMMAND_LOAD] to load a previously saved tournament
        - [COMMAND_EXIT] to exit program
        """
        self.show_in_console(message=["souhaitez-vous :",
                                      f"{self.menu.command_one} créer un nouveau tournoi",
                                      f"{self.menu.command_two} charger un tournoi existant",
                                      f"{self.menu.command_three} afficher un rapport",
                                      "",
                                      f"{self.menu.command_exit} : quitter le programme."],
                             title="tournoi")
        return input("")

    def display_loading_status(self, data_loaded: dict) -> None:
        """
        gets a message to display as dict
        returns none
        """
        self.clear_console()
        message = []

        if "tournament" in data_loaded:
            message.append(f"tournoi : {data_loaded['tournament']['name']}")
            message.append(f"emplacement : {data_loaded['tournament']['location']}")
            message.append(f"nombre de rounds total : {data_loaded['tournament']['round_number']}")
            message.append(f"description : {data_loaded['tournament']['description']}")

        if "player_list" in data_loaded:
            message.append("")
            for key, value in data_loaded["player_list"]["player_group"].items():
                message.append(f"Joueur{key} : {value['name']} {value['last_name']}")

        self.show_in_console(message=message, title="loading status")
        self.display_input_press_enter()

    def prompt_tournament_creation_mode(self) -> str:
        """
        Prompts user for information
        Returns command value as str
        """
        choice = self.prompt_choice_selection(
            title="tournoi - creation du tournoi",
            choice_dict={self.menu.command_one: "entrer les informations du tournoi",
                         self.menu.command_two: "[demo mode] utiliser les informations par défaut",
                         self.menu.command_exit: "quitter le programme."},)

        return choice

    def prompt_tournament_load(self, tournament_list) -> str:
        """
        gets list of tournament names
        return tournament name as string
        """

        choice_dict = {}
        for index, tournament in enumerate(tournament_list):
            tournament_list[index] = f"{index + 1}: {tournament}"
            choice_dict[str(index + 1)] = tournament

        tournament_list.insert(0, "Veuillez entrer le nombre correspondant au tournoi à charger :")
        while True:
            self.clear_console()
            self.show_in_console(message=tournament_list,
                                 title="tournoi - chargement d'un tournoi existant")

            choice = str(input(""))

            if choice in choice_dict:
                break

            self.invalid_info_entered()

        return choice_dict[choice]

    def invalid_no_data_found(self):
        """
        gets none
        returns none
        """
        self.show_in_console(title="Erreur de chargement",
                             message="Pas de donnée à charger dans ce fichier")
