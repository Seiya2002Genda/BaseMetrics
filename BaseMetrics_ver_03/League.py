# League.py

class League:
    """リーグの基本構造（Division を後からセットする）"""
    def __init__(self, name: str):
        self.name = name
        self.divisions = {}

    def add_division(self, division_name: str, division_obj):
        self.divisions[division_name] = division_obj

    def get_division(self, division_name: str):
        return self.divisions.get(division_name)

    def list_divisions(self):
        return list(self.divisions.keys())

    def __str__(self):
        return f"League: {self.name} | Divisions: {', '.join(self.list_divisions())}"


class AmericanLeague(League):
    """アメリカンリーグ"""
    def __init__(self):
        super().__init__("American League")
        # Division.py によって後で divisions がセットされる


class NationalLeague(League):
    """ナショナルリーグ"""
    def __init__(self):
        super().__init__("National League")
        # Division は後でセット


class CentralLeague(League):
    """セントラルリーグ（NPB）"""
    def __init__(self):
        super().__init__("Central League")
        # Division は後でセット（NPBは1リーグだが階層統一のため同じ形式）


class PacificLeague(League):
    """パシフィックリーグ（NPB）"""
    def __init__(self):
        super().__init__("Pacific League")
        # Division は後でセット（NPBは1リーグだが形式統一）
