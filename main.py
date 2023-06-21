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


def main():
    """
    main function
    """
    DEBUG = False  # pylint: disable=C0103

    # initialize MVC relations
    model_tournament: m_tournament.Tournament = m_tournament.Tournament()
    view_tournament = v_tournament.ViewTournament(DEBUG)
    controller_tournament = c_tournament.ControllerTournament(model_tournament, view_tournament, DEBUG)

    model_round_list: m_round.Round = m_round.Round()
    view_round = v_round.ViewRound(DEBUG)
    controller_round = c_round.ControllerRound(model_round_list, view_round, DEBUG)

    model_player_list = m_player.PlayerList()
    view_player = v_player.ViewPlayer(DEBUG)
    controller_player = c_player.ControllerPlayer(model_player_list, view_player, DEBUG)

    # initialize data object
    # controller_tournament.model.data.create_json()  # DELETE
    database = data.Data()
    controller_tournament.model.data: data.Data = database
    controller_player.model.data: data.Data = database
    controller_round.model.data: data.Data = database

    controller_tournament.set_up_data_info()
    controller_player.set_up_data_info()
    controller_round.set_up_data_info()
    # controller_round.model.save_data()

    controller_tournament.view.clear_console()

    while True:
        # update data section status
        controller_tournament.model.data.data["status"][
            controller_tournament.menu.name_controller] = controller_tournament.step_validated
        controller_player.model.data.data["status"][
            controller_player.menu.name_controller] = controller_player.step_validated

        # select a tournament by either creating or loading one
        if controller_tournament.step_validated is False:

            controller_tournament.step_validated = controller_tournament.select_tournament()

            # forces the minimum player number to two times the number of round
            controller_player.model.minimum_player_number = controller_tournament.model.round_number * 2

            continue

        controller_tournament.model.update_data()
        controller_player.model.update_data()
        controller_round.model.update_data()
        database.save_data()

        controller_tournament.view.show_in_console(
            controller_tournament.model.data.report_active_tournament_player_list(),
            title="report - active player")

        controller_tournament.view.show_in_console(
            message=controller_tournament.model.data.report_rounds_and_match(),
            title="report - rounds & match")

        if controller_player.step_validated is False:
            controller_tournament.view.clear_console()

            controller_player.step_validated = controller_player.select_player_list()

            # pass player_list_id and player_group for models that needs it
            if controller_player.step_validated:
                controller_tournament.set_player_group(player_list=controller_player.get_player_list_id(),
                                                       player_group=controller_player.get_player_group())
                controller_round.set_player_group(player_list=controller_player.get_player_list_id(),
                                                  player_group=controller_player.get_player_group())

                controller_player.model.update_data()
                controller_tournament.model.data.save_player_base()

            continue

        if controller_round.step_validated is False:
            controller_round.step_validated = controller_round.round_loop()

        # end of tournament
        controller_tournament.view.show_in_console(title="fin du tournoi")
        controller_tournament.model.data.data["status"]["finished"] = True
        controller_tournament.model.data.save_data()

        controller_tournament.exit_program(show_exit_message=False)


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
