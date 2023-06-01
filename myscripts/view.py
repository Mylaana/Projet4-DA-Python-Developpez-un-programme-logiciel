"""
view module
"""


class View:
    """
    View class
    """
    def __init__(self):
        self.player_list = self.dummy_generate_player_list()

    def show_in_console(self, message="", title=""):  # type: (str or list or None, str or None) -> None
        """
        Receives either str or list[str]
        Returns none
        """
        print("\n\n")
        if title != "":
            print("-----------------------------------\n" + title.upper() + "\n-----------------------------------\n")

        if message == "":
            return

        if isinstance(message, str):
            print(message)
        elif isinstance(message, list):
            for line in message:
                print(line)
        print("\n")

    def invalid_choice(self):
        """
        shows the choice is not valid
        """
        print("\n\nLe choix effectué n'est pas valide !\n")

    def prompt_tournament_selection(self) -> str:
        """
        Prompts user for :
        - new tournament
        - load tournament
        - exiting the program

        Returns :
        - '1' to create new tournament
        - '2' to load tournament
        - 'q' to exit program
        """
        self.show_in_console(["souhaitez-vous :",
                              "'1' créer un nouveau tournoi",
                              "'2' charger un tournoi existant",
                              "'q' : quitter le programme."
                              ])
        return input("")

    def prompt_player_list_selection(self):
        """
        Prompts user for :
        - using default player list
        - create new list of player
        - return to tournament selection
        - exiting the program

        Returns :
        - '1' to default player list
        - '2' to create new list of player
        - 'r' to return to tournament selection
        - 'q' to exit program
        """
        self.show_in_console(message=["souhaitez-vous :",
                                      "'1' utiliser la liste de joueurs par défaut",
                                      "'2' créer une liste de joueurs",
                                      "'r' : retourner à la sélection de tournoi.",
                                      "'q' : quitter le programme."],
                             title="selection du tournoi")
        return input("")

    def get_player_list(self):
        """
        Returns player list with following shape :
        [Name1 FamilyName1 Birthdate1(AAAA/MM/DD), ...]
        """

        print("voici la liste des joueurs par défaut :")
        for player_info in self.player_list:
            print(str(player_info))

        default_player_list = input("\nvoulez vous utiliser la liste des joueurs par défaut ? (y/n)\n")

        if default_player_list == "y":
            print(r"c'est parti")
            return self.player_list
        else:
            print("tant pis")
            return None

    def dummy_generate_player_list(self) -> list[str]:
        """
        player list for testing purpose
        """
        return [
            "Jeanne Thériault 1989/12/07",
            "Dexter Chesnay 1995/07/16",
            "Chandler Bisaillon 1969/02/15",
            "Guillaume Aoust 1994/10/12",
            "Christiane Laramée 1999/01/22",
            "Élise Lévesque 2004/03/19",
            "Orville Mireault 1984/10/06",
            "Étienne Salois 1992/12/06"
        ]

    def dummy_calculate_scores(self):
        """
        Randomly generate players scores for this round.
        This is a dummy function (the scores should be determined by every games,
        instead of randomed for app building purpose).
        """
