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

    my_model = model.Model()
    my_controller = controller.Controller(my_model, None)
    my_view = view.View()
    my_controller.view = my_view

    while True:
        # select a tournament by either creating or loading one
        if my_controller.selected_element[my_controller.menu.navigation_tournament] is False:
            clear_console()
            my_controller.selected_element[
                my_controller.menu.navigation_tournament] = my_controller.select_tournament()
            continue

        if my_controller.selected_element[my_controller.menu.navigation_player_list] is False:
            clear_console()
            my_controller.selected_element[
                my_controller.menu.navigation_player_list] = my_controller.select_player_list()
            continue

        if my_controller.selected_element[my_controller.menu.navigation_round_first] is False:
            my_controller.selected_element[
                my_controller.menu.navigation_round_first] = my_controller.start_first_round()
            print("round 1")
            continue

        if my_controller.selected_element[my_controller.menu.navigation_round_subsequent] is False:
            my_controller.selected_element[
                my_controller.menu.navigation_round_subsequent] = my_controller.start_next_round()
            print("round")
            continue

        # end of tournament
        my_controller.view.show_in_console(title="fin du tournoi")

        my_controller.exit_program(show_exit_message=False)


if __name__ == "__main__":
    clear_console()
    main()
