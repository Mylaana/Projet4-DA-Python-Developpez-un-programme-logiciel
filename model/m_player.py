
"""
Player and player list model
"""


class Player:
    """
    player class
    """
    def __init__(self, player_id: int, name: str = "", family_name: str = "", birth_date: str = ""):
        self.name = name
        self.last_name = family_name
        self.birth_date = birth_date
        self.player_id = player_id

    def get_player_info(self):
        """
        returns player info as a string
        """
        return "name : " + self.name + "  last name : " + self.last_name


class PlayerList:
    """
    player list
    """
    def __init__(self):
        """
        stores player list with a dictionnaty :
        Key = id, value = class Player
        """
        self.player_group = {}
        self.player_list_id = []

    def set_player_group(self, player_info_list: list) -> list:
        """
        get a list like :
        'Name FamilyName Birthdate',
        'Name FamilyName Birthdate',

        generate a dict
        returns none
        """
        # reset player group
        self.player_group = {}
        player_counter = 1

        for player_info in player_info_list:
            player = Player(player_id=player_counter)
            player.name = player_info["name"]
            player.last_name = player_info["name"]
            player.birth_date = player_info["name"]

            self.add_player_to_group(player)

    def add_player_to_group(self, player: Player) -> None:
        """
        stores player in dict
        gets a player class argument
        returns none
        """
        self.player_group[len(self.player_group) + 1] = player
        self.player_list_id.append(len(self.player_group))
