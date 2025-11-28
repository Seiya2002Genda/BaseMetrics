# Player.py
class Player:
    """
    チームに所属する選手の基本情報
    """

    def __init__(self, name, position):
        self.name = name
        self.position = position     # "P", "C", "1B", "SS", "LF", etc.

    def __str__(self):
        return f"Player({self.name}, {self.position})"
