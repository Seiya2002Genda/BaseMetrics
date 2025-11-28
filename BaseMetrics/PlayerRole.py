# Player_Role.py
class PlayerRole:
    """
    Player のポジションをもとに "Pitcher" または "Batter" を判定
    """

    PITCHER_POS = ["P", "SP", "RP"]

    def __init__(self, player):
        self.player = player

    def get_role(self):
        if self.player.position in self.PITCHER_POS:
            return "Pitcher"
        return "Batter"

    def __str__(self):
        return f"{self.player.name} is {self.get_role()}"
