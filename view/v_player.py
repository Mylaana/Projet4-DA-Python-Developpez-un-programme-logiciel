"""
view module
"""
from . import view as v


class ViewPlayer(v.View):
    """
    View class
    """
    def prompt_player_list_selection(self):
        """
        Prompts user for :
        - using default player list
        - create new list of player
        - return to tournament selection
        - exiting the program

        Returns :
        - [COMMAND_ONE] to default player list
        - [COMMAND_TWO] to create new list of player
        - [COMMAND_RETURN] to return to tournament selection
        - [COMMAND_SAVE] to save the tournament actual state
        - [COMMAND_LOAD] to load a previously saved tournament
        - [COMMAND_EXIT] to exit program
        """
        self.show_in_console(message=["souhaitez-vous :",
                                      f"{self.menu.command_one} : créer une liste de joueurs",
                                      f"{self.menu.command_two} : [demo mode] utiliser la liste de joueurs par défaut",
                                      "",
                                      f"{self.menu.command_save} : {self.menu.command_description_save}",
                                      f"{self.menu.command_load} : {self.menu.command_description_load}",
                                      f"{self.menu.command_return} : {self.menu.command_description_return}",
                                      f"{self.menu.command_exit} : {self.menu.command_description_exit}"],
                             title="liste des joueurs")
        return input("")

    def prompt_player_group_creation(self) -> list[dict[str, str]]:
        """
        gets none
        return a player list of dict with informations :
        [{name : 'player name', last_name : 'player last name', birth_date : 'DD/MM/YYYY'}]
        """
        player_list = []
        list_complete = False
        while not list_complete:
            result = self.prompt_new_player()
            if result == self.menu.command_two:
                break

            player = self.get_new_player_info()
            self.show_in_console(f"confirmez-vous vouloir ajouter le joueur suivant : {player} \n 1 : oui \n2 : non")
            validate_player = input("")
            if validate_player == 1:
                player_list.append(player)

        return player_list

    def prompt_new_player(self):
        """
        prompt user if he wants new player or if he's done
        """
        while True:
            self.show_in_console(message=["souhaitez-vous :",
                                          f"{self.menu.command_one} : ajouter un nouveau joueur",
                                          f"{self.menu.command_two} : ne plus ajouter de joueurs"])
            result = input("")
            if result == self.menu.command_one:
                return self.menu.command_one
            elif result == self.menu.command_two:
                return self.menu.command_two
            else:
                self.invalid_choice()

    def get_new_player_info(self) -> dict:
        """
        gets None
        returns dict
        """
        player = {}
        player["name"] = input("enter player name :")
        player["last_name"] = input("enter player last name :")
        player["birth_date"] = input("enter player birth date :")

        return player

    def get_player_list(self):
        """
        Returns player list with following shape :
        [Name1 FamilyName1 Birthdate1(AAAA/MM/DD), ...]
        """

        print("voici la liste des joueurs par défaut :\n")
        for player_info in self.player_list:
            print(str(player_info))

    def dummy_generate_player_list(self) -> list[str]:
        """
        player list for testing purpose
        """
        return [{"name": "Jeanne", "last_name": "Thériault", "birth_date": "1989/12/07"},
                {"name": "Dexter", "last_name": "Chesnay", "birth_date": "1995/07/16"},
                {"name": "Chandler", "last_name": "Bisaillon", "birth_date": "1969/02/15"},
                {"name": "Guillaume", "last_name": "Aoust", "birth_date": "1994/10/12"},
                {"name": "Christiane", "last_name": "Laramée", "birth_date": "06/17/1998"},
                {"name": "Élise", "last_name": "Lévesque", "birth_date": "03/28/2004"},
                {"name": "Orville", "last_name": "Mireault", "birth_date": "02/24/2003"},
                {"name": "Étienne", "last_name": "Salois", "birth_date": "09/11/1993"}]
