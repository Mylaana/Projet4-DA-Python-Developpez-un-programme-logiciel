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
from Controller import c_tournament
from View import v_tournament
from Model import m_tournament


def clear_console():
    """
    clear console
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """
    main function
    """
    my_model = m_tournament.Model()
    my_view = v_tournament.View()
    controller_tournament = c_tournament.Controller(my_model, my_view)

    while True:
        # select a tournament by either creating or loading one
        if controller_tournament.selected_element[controller_tournament.menu.navigation_tournament] is False:
            clear_console()
            controller_tournament.selected_element[
                controller_tournament.menu.navigation_tournament] = controller_tournament.select_tournament()
            continue

        if controller_tournament.selected_element[controller_tournament.menu.navigation_player_list] is False:
            clear_console()
            controller_tournament.selected_element[
                controller_tournament.menu.navigation_player_list] = controller_tournament.select_player_list()
            continue

        if controller_tournament.selected_element[controller_tournament.menu.navigation_round_first] is False:
            controller_tournament.selected_element[
                controller_tournament.menu.navigation_round_first] = controller_tournament.start_first_round()
            print("round 1")
            continue

        if controller_tournament.selected_element[controller_tournament.menu.navigation_round_subsequent] is False:
            controller_tournament.selected_element[
                controller_tournament.menu.navigation_round_subsequent] = controller_tournament.start_next_round()
            print("round")
            continue

        # end of tournament
        controller_tournament.view.show_in_console(title="fin du tournoi")

        controller_tournament.exit_program(show_exit_message=False)


if __name__ == "__main__":
    clear_console()
    main()
