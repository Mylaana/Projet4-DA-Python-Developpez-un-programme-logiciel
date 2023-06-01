"""
Notes / idées en vrac :

Structure des fichiers JSON :
1 fichier pour la liste des joueurs
1 fichier par résultat de tournoi ?

Controller :
-Le controlleur pourrait gérer plusieurs formats de tournoi :
    genre un tournoi ESL, ou un tournoi a simple élimination

Vue :

"""

import os
from myscripts import controller
from myscripts import view
from myscripts import model


def clear_console():
    """
    clear console
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """
    main function
    """
    clear_console()
    my_model = model.Model()
    my_controller = controller.Controller(my_model, None)
    my_view = view.View()
    my_controller.view = my_view
    my_controller.kernel()


if __name__ == "__main__":
    main()
