"""
main module
"""

import os
from Controller import c_tournament
from Controller import c_player
from Controller import c_round
from View import v_tournament
from View import v_player
from View import v_round
from Model import m_tournament
from Model import m_player
from Model import m_round
from CommonClass import data


def clear_console():
    """
    clear console
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """
    main function
    """
    DEBUG = True  # pylint: disable=C0103
    clear_console()

    # initialize MVC relations
    model_tournament: m_tournament.Tournament = m_tournament.Tournament()
    view_tournament = v_tournament.ViewTournament()
    controller_tournament = c_tournament.ControllerTournament(model_tournament, view_tournament, DEBUG)

    model_round_list: m_round.Round = m_round.Round()
    view_round = v_round.ViewRound()
    controller_round = c_round.ControllerRound(model_round_list, view_round, DEBUG)

    model_player_list = m_player.PlayerList()
    view_player = v_player.ViewPlayer()
    controller_player = c_player.ControllerPlayer(model_player_list, view_player, DEBUG)

    # initialize data object
    # controller_tournament.model.data.create_json()  # DELETE
    controller_tournament.model.data: data.Data = data.Data()
    controller_player.model.data: data.Data = controller_tournament.model.data
    controller_round.model.data: data.Data = controller_tournament.model.data

    controller_tournament.model.data.model_list.append(controller_tournament.model)
    controller_player.model.data.model_list.append(controller_player.model)
    controller_round.model.data.model_list.append(controller_round.model)

    while True:
        # update tournament section status
        controller_tournament.model.data.data["status"][
            controller_tournament.menu.navigation_tournament] = controller_tournament.selected_element[
                controller_tournament.menu.navigation_tournament]
        controller_player.model.data.data["status"][
            controller_player.menu.navigation_player_list] = controller_player.selected_element[
                controller_player.menu.navigation_player_list]

        controller_tournament.model.update_data()
        controller_player.model.update_data()
        controller_round.model.update_data()

        # select a tournament by either creating or loading one
        if controller_tournament.selected_element[controller_tournament.menu.navigation_tournament] is False:
            controller_tournament.selected_element[
                controller_tournament.menu.navigation_tournament] = controller_tournament.select_tournament()

            # forces the minimum player number to two times the number of round
            controller_player.model.minimum_player_number = controller_tournament.model.round_number * 2

            if controller_tournament.load and controller_tournament.selected_element[
                                                controller_tournament.menu.navigation_tournament]:
                controller_tournament.load = False
                controller_player.load_existing_player_list()
                controller_round.load_existing_rounds()
                print("loading all")

            continue

        controller_tournament.model.data.save_data()

        if controller_player.selected_element[controller_player.menu.navigation_player_list] is False:
            # clear_console()
            controller_player.selected_element[
                controller_player.menu.navigation_player_list] = controller_player.select_player_list()

            # pass player_list_id and player_group for models that needs it
            if controller_player.selected_element[controller_player.menu.navigation_player_list] is True:
                controller_tournament.set_player_group(player_list=controller_player.get_player_list_id(),
                                                       player_group=controller_player.get_player_group())
                controller_round.set_player_group(player_list=controller_player.get_player_list_id(),
                                                  player_group=controller_player.get_player_group())

            continue

        if controller_round.selected_element[controller_round.menu.navigation_round] is False:
            controller_round.selected_element[
                controller_round.menu.navigation_round] = controller_round.round_loop()

        # end of tournament
        controller_tournament.view.show_in_console(title="fin du tournoi")
        controller_tournament.model.data.data["status"]["finished"] = True
        controller_round.model.data.data["status"][
            controller_round.menu.navigation_round] = controller_round.selected_element[
                controller_round.menu.navigation_round]
        controller_tournament.model.data.save_data()

        controller_tournament.exit_program(show_exit_message=False)


if __name__ == "__main__":
    clear_console()
    main()
