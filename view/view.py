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
        clear console
        """
        if self.debug:
            return
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_in_console(self, message="", title=""):  # type: (str or list or None, str or None) -> None
        """
        Receives either str or list[str]
        Returns none
        """
        # print("\n\n")
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
        print("\n")

    def display_error_message(self, error_title: str = "", error_message: str = ""):
        """
        gets error message as string
        returns none
        """
        self.show_in_console(title=error_title, message=error_message)
        input("")

    def invalid_choice(self):
        """
        shows the choice is not valid
        """
        self.display_error_message("Le choix effectué n'est pas valide !")

    def invalid_info_entered(self, message: str = ""):
        """
        shows the choice is not valid
        """
        self.display_error_message("Les informations entrées ne sont pas valide !", message)

    def invalid_info_entered_type(self, message: str = ""):
        """
        shows the choice is not valid
        """
        self.display_error_message(error_title="Les informations entrées ne sont pas valide !",
                                   error_message=f"{message} n'est pas du bon type")

    def invalid_info_entered_empty(self, message: str = ""):
        """
        shows the choice is not valid
        """
        self.display_error_message(error_title="Les informations entrées ne sont pas valide !",
                                   error_message=f"{message} n'a pas été rempli")

    def invalid_info_entered_number_needed(self):
        """
        shows the choice is not valid
        """
        self.display_error_message("Veuillez entrer un nombre !")

    def prompt_info_list(self, info_list: list[dict], title) -> list[dict]:
        """
        gets list
        returns list
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
        gets list of tournament names
        return tournament name as string
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
        gets list
        returns none
        """
        self.clear_console()
        self.show_in_console(message=report_result, title="rapport - " + report_title)
        input("appuyez sur entrée")
