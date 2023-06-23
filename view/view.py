"""
view module
"""
import os
import sys
from CommonClass import menu as m
sys.path.insert(0, '../CommonClass')


class View:
    """
    View class
    """
    def __init__(self, debug: bool):
        self.player_list = []
        self.menu = m.Menu()
        self.debug = debug

    def clear_console(self):
        """
        Clears the console.
        """
        if self.debug:
            return
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_in_console(self, message="", title="", carriage_return_end_message: bool = True):
        """
        Displays a message in the console.

        Args:
        - message: Message to display (str or list[str])
        - title: Title for the message (str)
        - carriage_return_end_message: Whether to add a carriage return at the end of the message (bool)

        Returns:
        - None
        """
        if title != "":
            print("-------------------------------------------------\n" + title.upper() +
                  "\n-------------------------------------------------\n")

        if message == "":
            return

        if isinstance(message, str):
            print(message)
        elif isinstance(message, list):
            for line in message:
                print(line)
        if carriage_return_end_message:
            print("\n")

    def display_error_message(self, error_title: str = "", error_message: str = ""):
        """
        Displays an error message.

        Args:
        - error_title: Title of the error message (str)
        - error_message: Error message to display (str)

        Returns:
        - None
        """
        self.show_in_console(title=error_title, message=error_message, carriage_return_end_message=False)
        self.display_input_press_enter()

    def invalid_choice(self):
        """
        Displays an error message for an invalid choice.
        """
        self.display_error_message(error_message="Le choix effectué n'est pas valide !")

    def invalid_info_entered(self, message: str = ""):
        """
        Displays an error message for invalid information entered.
        """
        self.display_error_message("Les informations entrées ne sont pas valide !", message)

    def invalid_info_entered_type(self, message: str = ""):
        """
        Displays an error message for invalid information type entered.
        """
        self.display_error_message(error_title="Les informations entrées ne sont pas valide !",
                                   error_message=f"{message} n'est pas du bon type")

    def invalid_info_entered_empty(self, message: str = ""):
        """
        Displays an error message for empty information entered.
        """
        self.display_error_message(error_title="Les informations entrées ne sont pas valide !",
                                   error_message=f"{message} n'a pas été rempli")

    def invalid_info_entered_number_needed(self):
        """
        Displays an error message for a number needed to be entered.
        """
        self.display_error_message("Veuillez entrer un nombre !")

    def invalid_no_tournament_found_in_data(self) -> None:
        """
        Displays an error message when no tournament is found in the data.
        """
        self.clear_console()
        self.display_error_message(
            error_title="TOURNOI",
            error_message="Aucun tournoi sauvegardé !")

    def prompt_info_list(self, info_list: list[dict], title) -> list[dict]:
        """
        Prompts the user for a list of information.

        Args:
        - info_list: List of information (list[dict])
        - title: Title for the prompt (str)

        Returns:
        Updated list of information (list[dict])
        """
        for line in info_list:
            self.clear_console()
            message = ["Liste des informations à entrer :"]
            for line_message in info_list:
                if line_message["value"] is None:
                    value = ""
                else:
                    value = ": " + str(line_message["value"])
                message.append(line_message["caption"] + value)
            self.show_in_console(message=message, title=title)

            prompt_message = f"Veuillez saisir [{line['caption']}]"
            if str(line["default_value"]) != "":
                prompt_message = prompt_message + f" (valeur par défaut={line['default_value']})"

            line["value"] = input(f"{prompt_message}:\n")
            if str(line["value"]) == "":
                line["value"] = str(line["default_value"])

            # if the value is numeric, converts it to the expected type
            if str(line["type"]) not in [str(int), str(float)]:
                continue
            if not line["value"].replace(".", "").replace(",", "").isdigit():
                continue

            if str(line["type"]) == str(int):
                line["value"] = int(line["value"].replace(",", "."))
            elif str(line["type"]) == str(float):
                line["value"] = float(line["value"].replace(",", "."))

        return info_list

    def prompt_report_choice(self, report_list: list) -> str:
        """
        Prompts the user for a report choice.

        Args:
        - report_list: List of report names (list)

        Returns:
        Selected report name as string
        """
        self.clear_console()
        choice_dict = {}
        for index, report in enumerate(report_list):
            report_list[index] = f"{index + 1}: {report}"
            choice_dict[str(index + 1)] = report

        report_list.insert(0, "Veuillez sélectionner un rapport :")

        while True:
            self.clear_console()
            self.show_in_console(message=report_list,
                                 title="rapport")

            choice = str(input(""))

            if choice in choice_dict:
                break

            self.invalid_info_entered()

        return choice_dict[choice]

    def display_report(self, report_result, report_title):
        """
        Displays a report.

        Args:
        - report_result: List of report results (list)
        - report_title: Title of the report (str)

        Returns:
        - None
        """
        self.clear_console()
        if report_result == []:
            report_result = ["Aucune information à afficher."]
        self.show_in_console(message=report_result, title="rapport - " + report_title)
        self.display_input_press_enter()

    def prompt_report_tournament_name(self, tournament_list: list) -> str:
        """
        Prompts the user for a tournament name for the report.

        Args:
        - tournament_list: List of tournament names (list)

        Returns:
        - Selected tournament name as string
        """
        message = ["Liste des tournois sauvegardés :"]
        tournament_dict = {}

        for index, value in enumerate(tournament_list):
            tournament_dict[str(index + 1)] = value
            message.append(f"{index + 1}: {value}")

        while True:
            self.clear_console()
            self.show_in_console(message=message, title="rapport - information sur le tournoi")
            choice = input("\n\nveuillez entrer le numéro correspondant au tournoi :\n")

            if str(choice) in tournament_dict:
                break

            self.invalid_choice()

        return tournament_dict[str(choice)]

    def prompt_choice_selection_defined_keys(
            self, title: str, choice_dict: dict, message_before_choice: str = "") -> str:
        """
        Prompts the user for a choice selection from a defined set of keys.

        Args:
        - title: Title for the menu (str)
        - choice_dict: Dictionary with key=str(key to press), value=text to display (dict)
        - message_before_choice: Optional message to display before the choice listed (str)

        Returns:
        - Key pressed as str
        """
        if message_before_choice != "":
            message_list = [message_before_choice]
        else:
            message_list = ["Souhaitez-vous:"]

        for key, value in choice_dict.items():
            message_list.append(f"{key}: {value}")

        while True:
            self.clear_console()
            self.show_in_console(title=title, message=message_list)

            choice = input("\n\n Veuillez taper votre choix puis appuyer sur 'entrée':\n")

            if choice in choice_dict:
                break

            self.invalid_choice()

        return choice

    def prompt_choice_selection_from_list(
            self, title: str, choice_list: list, message_before_choice: str = "") -> str:
        """
        Prompts the user for a choice selection from a list of options.

        Args:
        - title: Title for the menu (str)
        - choice_list: List of options with value=text to display (list)
        - message_before_choice: Optional message to display before the choice listed (str)

        Returns:
        - Key pressed as str
        """
        choice_dict = {}
        for index, values in enumerate(choice_list):
            choice_dict[str(index + 1)] = values

        choice = self.prompt_choice_selection_defined_keys(title=title,
                                                           choice_dict=choice_dict,
                                                           message_before_choice=message_before_choice)

        return choice_dict[choice]

    def display_input_press_enter(self) -> None:
        """
        Displays a message to prompt the user to press enter.

        Returns:
        - None
        """
        input("Veuillez appuyer sur entrée pour continuer.")
