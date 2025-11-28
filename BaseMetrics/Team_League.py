# Team_League.py
from Organization import Organization

class TeamLeague(Organization):
    """
    組織（MLB/NPB）に属するリーグ（American, National, Central, Pacific）
    """

    def __init__(self, org_name, league_name):
        super().__init__(org_name)     # MLB or NPB を継承
        self.league_name = league_name # "American League" など
        self.divisions = []            # West / Central / East

    def add_division(self, division):
        self.divisions.append(division)

    def __str__(self):
        return f"{self.name} - League({self.league_name})"
