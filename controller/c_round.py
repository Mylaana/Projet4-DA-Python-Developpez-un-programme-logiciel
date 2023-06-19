"""
Controller module
"""


import sys
from View import v_round as v
from Model import m_round as m
from . import controller as c
sys.path.insert(0, '../View')
sys.path.insert(0, '../Model')
sys.path.insert(0, '../CommonClass')


class ControllerRound(c.Controller):
    """
    Controller class
    """
    def __init__(self, model: m.Round, view: v.ViewRound, debug: bool = False):
        super().__init__(model=model, view=view)
        self.model: m.Round = model
        self.view: v.ViewRound = view
        self.last_round_over = False
        self.debug = debug
        self.model.data_section_name = self.menu.navigation_round
        self.menu.name_controller = self.model.data_section_name

    def round_loop(self):
        """
        Loops while rounds need to be run
        Returns True when last round is over
        """
        while not self.model.round_counter > self.model.round_max_number:
            self.update_data()
            self.save_data()

            # creating new round with pairings
            if self.model.current_round_step == 0:
                self.clear_console()
                self.start_new_round()
                self.model.current_round_step = 1
                continue

            # displaying pairings and asking for round score method
            if self.model.current_round_step == 1:
                self.view.display_round_pairings(pairing_list=self.model.get_current_round_pairings(),
                                                 round_number=self.model.round_counter,
                                                 player_group=self.model.player_group)

                choice_dict = {self.menu.command_one: self.enter_score_results,
                               self.menu.command_two: self.set_random_scores,
                               self.menu.command_exit: self.exit_program}

                prompt_result = self.view.prompt_score_calculation_method()
                result = self.rooter(choice=prompt_result, choice_dict=choice_dict)
                if result:
                    self.model.current_round_step = 2

                continue

            if self.model.current_round_step == 2:
                self.display_scores()
                prompt_result = self.view.prompt_next_round()

                if prompt_result == self.menu.command_one:
                    self.finalize_round()

                if prompt_result == self.menu.command_exit:
                    self.exit_program()

                continue

        self.step_validated = True

        return self.step_validated

    def start_new_round(self) -> None:
        """
        gets none
        create new round
        returns none
        """
        self.model.create_new_round()

    def finalize_round(self):
        """
        gets none
        runs round finalization
        returns none
        """
        self.model.finalize_round()

    def enter_score_results(self):
        """
        prompts user for players' scores on the current round
        """
        print("pas encore possible")

        return False

    def set_random_scores(self):
        """
        generates random scores for the current round
        """
        self.model.set_random_scores()

        return True

    def display_scores_previous_round(self):
        """
        Calls display scores with previous round = true
        """
        self.display_scores(previous_round=True)

    def display_scores(self, previous_round: bool = False):
        """
        gets none
        display score and total score end of round
        Returns none
        """
        self.clear_console()

        # display round's score
        self.view.display_scores(
            score=self.model.current_round.player_score_round,
            round_number=self.model.round_counter,
            total_score=False,
            player_group=self.model.player_group)

        # display total score at end of round
        self.view.display_scores(
            score=self.model.current_round.player_score_total_end_of_round,
            round_number=self.model.round_counter,
            total_score=True,
            player_group=self.model.player_group)

    def load_existing_rounds(self):
        """
        load an existing tournament
        """
        self.model.load_data()
