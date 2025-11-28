# Team_Selection.py
class TeamSelection:
    """
    Division に属する実際のチーム
    """

    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []           # 選手一覧

    def add_player(self, player):
        self.players.append(player)

    def __str__(self):
        return f"Team({self.team_name})"
