# Organization.py

class Organization:
    """スポーツ組織の基底クラス（MLB / NPB の親）"""
    def __init__(self, name: str):
        self.name = name
        self.leagues = {}

    def add_league(self, league_name: str, league_obj):
        self.leagues[league_name] = league_obj

    def get_league(self, league_name: str):
        return self.leagues.get(league_name)

    def list_leagues(self):
        return list(self.leagues.keys())

    def __str__(self):
        return f"Organization: {self.name} | Leagues: {', '.join(self.list_leagues())}"


class major_league_baseball(Organization):
    """Seiya の指示通り MLB をここで定義"""
    def __init__(self):
        super().__init__("Major League Baseball")

        # 後で League.py がこれを補完する
        self.add_league("American League", None)
        self.add_league("National League", None)


class nippon_professional_baseball(Organization):
    """Seiya の指示通り NPB をここで定義"""
    def __init__(self):
        super().__init__("Nippon Professional Baseball")

        # 後で League.py がこれを補完する
        self.add_league("Central League", None)
        self.add_league("Pacific League", None)
0