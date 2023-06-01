"""
view module
"""


class View:
    """
    View class
    """
    def __init__(self):
        self.player_list = self.dummy_generate_player_list()

    def show_in_console(self, message):
        """
        Receives either str or list[str]
        Returns none
        """
        if isinstance(message, str):
            print("\n\n" + message + "\n")
        elif isinstance(message, list):
            for line in message:
                print(line)

    def prompt_tournament_selection(self) -> str:
        """
        Starting function, prompts user for :
        - new tournament
        - load tournament

        Returns :
        - '1' for new tournament
        - '2' for load tournament
        - 'q' for exit program
        """

        message = ["souhaitez-vous :",
                   "'1' créer un nouveau tournoi",
                   "'2' charger un tournoi existant",
                   "'q' : quitter le programme."
                   ]
        self.show_in_console(message)
        return input("")

    def invalid_choice(self):
        """
        shows the choice is not valid
        """
        print("\n\nLe choix effectué n'est pas valide !\n")

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
