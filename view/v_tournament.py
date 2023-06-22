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
        Prompts the user for tournament selection.

        Returns:
        Command value as str
        """
        choice = self.prompt_choice_selection_defined_keys(
            title="tournoi",
            choice_dict={self.menu.command_one: "créer un nouveau tournoi",
                         self.menu.command_two: "charger un tournoi existant",
                         self.menu.command_three: "afficher un rapport",
                         self.menu.command_exit: "quitter le programme."})

        return choice

    def display_loading_status(self, data_loaded: dict) -> None:
        """
        Displays the loading status of the tournament.

        Args:
        - data_loaded: Dictionary containing the loaded data

        Returns:
        None
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

        self.show_in_console(message=message, title="tournoi - tournoi chargé")
        self.display_input_press_enter()

    def prompt_tournament_creation_mode(self) -> str:
        """
        Prompts the user for the tournament creation mode.

        Returns:
        Command value as str
        """
        choice = self.prompt_choice_selection_defined_keys(
            title="tournoi - creation du tournoi",
            choice_dict={self.menu.command_one: "entrer les informations du tournoi",
                         self.menu.command_two: "[demo mode] utiliser les informations par défaut",
                         self.menu.command_exit: "quitter le programme."})

        return choice

    def prompt_tournament_load(self, tournament_list) -> str:
        """
        Prompts the user to load an existing tournament.

        Args:
        - tournament_list: List of tournament names

        Returns:
        Tournament name as string
        """
        return self.prompt_choice_selection_from_list(
            title="tournoi - chargement d'un tournoi existant",
            choice_list=tournament_list,
            message_before_choice="Veuillez entrer le nombre correspondant au tournoi à charger :")

    def prompt_tournament_finished(self):
        """
        Prompts the user for choice, after tournament completion.

        Returns:
        Command value as str
        """
        choice = self.prompt_choice_selection_defined_keys(
            title="tournoi terminé",
            choice_dict={self.menu.command_one: "afficher un rapport",
                         self.menu.command_exit: "quitter le programme."})

        return choice

    def invalid_no_data_found(self):
        """
        Displays an error message when no data is found.

        Returns:
        None
        """
        self.show_in_console(title="Erreur de chargement",
                             message="Pas de donnée à charger dans ce fichier")
