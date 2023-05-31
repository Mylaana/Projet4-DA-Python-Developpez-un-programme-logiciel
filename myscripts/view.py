"""
view module
"""
from . import event_handler as event
# from . import controller as c


class View:
    """
    View class
    """
    def __init__(self, controller):
        self.player_list = self.dummy_generate_player_list()
        self.controller = controller

    def start(self):
        """
        Starting function
        """
        event.wait_for_event(
            message=["souhaitez-vous :",
                     "'1' créer un nouveau tournoi",
                     "'2' charger un tournoi existant"
                     ],
            choice_possibilities={
                "1": self.controller.create_new_tournament,
                "2": self.controller.load_existing_tournament
                },
            quit_additionnal_option=True)

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

    def dummy_generate_player_list(self):
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
