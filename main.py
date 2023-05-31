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


def clear_console():
    """
    clear console
    """
    os.system('cls' if os.name == 'nt' else 'clear')


clear_console()
my_controller = controller.Controller()
print("end of treatment")
