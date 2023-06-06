"""
Menu class module
"""


class Menu:
    """
    Menu class
    """
    # these elements helps adding a hierarchy in console's choice for navigation purpose
    # menu names
    _MENU_NAME_TOURNAMENT = "tournament"
    _MENU_NAME_PLAYER_LIST = "player_list"
    _MENU_NAME_ROUND_FIRST = "first_round"
    _MENU_NAME_ROUND_SUBSEQUENT = "subsequent_round"

    # Creating menu tree
    _MENU_TREE = (_MENU_NAME_TOURNAMENT,
                  _MENU_NAME_PLAYER_LIST,
                  _MENU_NAME_ROUND_FIRST,
                  _MENU_NAME_ROUND_SUBSEQUENT)

    # key = child : value = parent
    _MENU_TREE_CHILD = {}
    # key = parent : value = child
    _MENU_TREE_PARENT = {}

    # filling _MENU_TREE_PARENT and _MENU_TREE_CHILD
    parent = None
    for item in _MENU_TREE:
        child = parent
        parent = item
        if child is not None:
            _MENU_TREE_CHILD[child] = parent
            _MENU_TREE_PARENT[parent] = child

    # basic menu commands
    _MENU_COMMAND_RETURN = "r"
    _MENU_COMMAND_EXIT = "q"
    _MENU_COMMAND_ONE = "1"
    _MENU_COMMAND_TWO = "2"
    _MENU_COMMAND_THREE = "3"

    def __init__(self):
        self.navigation_tournament = self._MENU_NAME_TOURNAMENT
        self.navigation_player_list = self._MENU_NAME_PLAYER_LIST
        self.navigation_round_first = self._MENU_NAME_ROUND_FIRST
        self.navigation_round_subsequent = self._MENU_NAME_ROUND_SUBSEQUENT

        self.tree = self._MENU_TREE
        self.tree_child = self._MENU_TREE_CHILD
        self.tree_parent = self._MENU_TREE_PARENT

        self.command_exit = self._MENU_COMMAND_EXIT
        self.command_return = self._MENU_COMMAND_RETURN
        self.command_one = self._MENU_COMMAND_ONE
        self.command_two = self._MENU_COMMAND_TWO
        self.command_three = self._MENU_COMMAND_THREE
