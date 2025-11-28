# Division.py

class Division:
    """Division（地区）の基本構造。Team は後でセットされる。"""
    def __init__(self, name: str):
        self.name = name
        self.teams = []

    def add_team(self, team_obj):
        self.teams.append(team_obj)

    def list_teams(self):
        return [team.name for team in self.teams]

    def __str__(self):
        return f"Division: {self.name} | Teams: {', '.join(self.list_teams())}"


# ======================
# MLB - American League
# ======================

class AmericanLeagueWest(Division):
    def __init__(self):
        super().__init__("American League West")


class AmericanLeagueCentral(Division):
    def __init__(self):
        super().__init__("American League Central")


class AmericanLeagueEast(Division):
    def __init__(self):
        super().__init__("American League East")


# ======================
# MLB - National League
# ======================

class NationalLeagueWest(Division):
    def __init__(self):
        super().__init__("National League West")


class NationalLeagueCentral(Division):
    def __init__(self):
        super().__init__("National League Central")


class NationalLeagueEast(Division):
    def __init__(self):
        super().__init__("National League East")


# ======================
# NPB
# ======================

class CentralLeagueDivision(Division):
    """NPB セリーグ（1リーグを Division として扱う）"""
    def __init__(self):
        super().__init__("Central League Division")


class PacificLeagueDivision(Division):
    """NPB パリーグ（1リーグを Division として扱う）"""
    def __init__(self):
        super().__init__("Pacific League Division")
