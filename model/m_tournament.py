"""
model dedicated module
"""


class Tournament:
    """
    Model = tournament class
    """
    def __init__(self):
        self.name = ""
        self.location = ""
        self.date_start = ""
        self.date_end = ""
        self.player_list_id: list[int] = None
        self.description = ""
