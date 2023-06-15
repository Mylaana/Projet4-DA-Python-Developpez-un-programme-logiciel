
"""
Player and player list model
"""
from . import model as m


class Player:
    """
    player class
    """
    def __init__(self, player_id: int, name: str = "", family_name: str = "",
                 birth_date: str = ""):
        self.name = name
        self.last_name = family_name
        self.birth_date = birth_date
        self.player_id = player_id

    def get_player_info(self):
        """
        returns player info as a string
        """
        return "name : " + self.name + "  last name : " + self.last_name


class PlayerList(m.Model):
    """
    player list
    """
    def __init__(self):
        """
        stores player list with a dictionnaty :
        Key = id, value = class Player
        """
        super().__init__()
        self.player_group: dict[int, dict] = {}
        self.player_list_id = []
        self.minimum_player_number: int = 0

    def set_player_group(self, player_info_list: list) -> list:
        """
        get a list of dict :
        'Name FamilyName Birthdate',
        'Name FamilyName Birthdate',
        returns none
        """
        # reset player group
        self.player_group = {}

        # adds every player to de player group dict
        for player_info in player_info_list:
            self.add_player_to_group(player_info)

    def add_player_to_group(self, player: dict) -> None:
        """
        stores player in dict
        gets a player class argument
        returns none
        """
        self.player_group[len(self.player_group) + 1] = player
        self.player_list_id.append(len(self.player_group))
