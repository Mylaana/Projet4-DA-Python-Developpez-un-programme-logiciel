"""
view module
"""
from . import view as v


class ViewPlayer(v.View):
    """
    View class that handles user interface related to players in the tournament.
    """
    def prompt_player_list_selection(self):
        """
        Prompts the user for:
        - Using the default player list
        - Creating a new player list
        - Displaying a report
        - Exiting the program

        Returns:
        - [COMMAND_ONE] creating a list of player
        - [COMMAND_TWO] use the demo player list
        - [COMMAND_THREE] for displaying a report
        - [COMMAND_EXIT] for exiting the program
        """
        choice = self.prompt_choice_selection_defined_keys(
            title="liste des joueurs",
            choice_dict={self.menu.command_one: "créer une liste de joueurs",
                         self.menu.command_two: "[demo mode] utiliser la liste de joueurs par défaut",
                         self.menu.command_three: "afficher un rapport",
                         self.menu.command_exit: "quitter le programme."})

        return choice

    def prompt_player_number(self) -> int:
        """
        Prompts the user to enter the number of players to add to the tournament.

        Returns:
        - The number of players entered by the user.
        """
        self.clear_console()
        self.show_in_console("Combien voulez vous ajouter de joueur au tournoi ?",
                             "liste des joueurs - ajouter des joueurs")
        return input("")

    def dummy_generate_player_list(self) -> list[str]:
        """
        Generates a dummy player list for testing purposes.

        Returns:
        - A list of player dictionaries.
        """
        return [{"name": "Jeanne", "last_name": "Thériault", "birth_date": "1989/12/07"},
                {"name": "Dexter", "last_name": "Chesnay", "birth_date": "1995/07/16"},
                {"name": "Chandler", "last_name": "Bisaillon", "birth_date": "1969/02/15"},
                {"name": "Guillaume", "last_name": "Aoust", "birth_date": "1994/10/12"},
                {"name": "Christiane", "last_name": "Laramée", "birth_date": "1998/06/06/17"},
                {"name": "Élise", "last_name": "Lévesque", "birth_date": "2004/03/28"},
                {"name": "Orville", "last_name": "Mireault", "birth_date": "2003/02/24"},
                {"name": "Étienne", "last_name": "Salois", "birth_date": "1993/09/11"}]

    def invalid_player_number_minimum(self, minimum_number):
        """
        Displays an error message for an invalid minimum player number.

        Args:
        - minimum_number (int): The minimum number of players required for the tournament.
        """
        self.invalid_info_entered(f"il faut au minimum {minimum_number} joueurs pour ce tournoi !")

    def invalid_player_number_uneven(self):
        """
        Displays an error message for an invalid uneven player number.
        """
        self.invalid_info_entered("il faut un nombre de joueur pair pour ce tournoi !")
