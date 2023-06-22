
"""
Player and player list model
"""
from . import model as m


class PlayerList(m.Model):
    """
    Player list model class.
    """
    def __init__(self):
        """
        Initialize the player list model.

        Attributes:
        - player_group (dict[int, dict]): A dictionary to store player information. Key: player ID,
        Value: player dictionary.
        - player_list_id (list[int]): A list to store the IDs of players.
        - minimum_player_number (int): The minimum number of players required.
        """
        super().__init__()
        self.player_group: dict[int, dict] = {}
        self.player_list_id = []
        self.minimum_player_number: int = 0

    def set_player_group(self, player_info_list: list[dict]) -> None:
        """
        Set the player group based on the provided player information list.

        Args:
        - player_info_list (list[dict]): A list of player information dictionaries.
          Each dictionary should contain the following keys:
          - 'name': The name of the player.
          - 'family_name': The family name of the player.
          - 'birth_date': The birth date of the player.

        Returns:
        - None
        """
        # reset player group
        self.player_group = {}

        # adds every player to de player group dict
        for player_info in player_info_list:
            self.add_player_to_group(player_info)

    def add_player_to_group(self, player: dict) -> None:
        """
        Add a player to the player group.

        Args:
        - player (dict): A dictionary containing the player information.
          It should have the following keys:
          - 'name': The name of the player.
          - 'family_name': The family name of the player.
          - 'birth_date': The birth date of the player.

        Returns:
        - None
        """
        self.player_group[len(self.player_group) + 1] = player
        self.player_list_id.append(len(self.player_group))
