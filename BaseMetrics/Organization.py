# Organization.py
class Organization:
    """
    MLB / NPB など組織全体
    ここからリーグ（TeamLeague）を追加していく
    """

    def __init__(self, name):
        self.name = name              # "MLB" or "NPB"
        self.leagues = []             # American / National / Central / Pacific

    def add_league(self, league):
        self.leagues.append(league)

    def __str__(self):
        return f"Organization({self.name})"
