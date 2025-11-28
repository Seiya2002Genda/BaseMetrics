class League:
    """
    MLB / NPB の各リーグを表現する基底クラス。
    Division（地区）を保持する。
    """
    def __init__(self, league_name: str):
        self.name = league_name
        self.divisions = {}   # {division_name: Divisionオブジェクト}

    def add_division(self, division_obj):
        self.divisions[division_obj.name] = division_obj

    def show(self):
        print(f"[League] {self.name}")
        for division in self.divisions.values():
            division.show()

class american_league(League):
    def __init__(self):
        super().__init__("American League")


class national_league(League):
    def __init__(self):
        super().__init__("National League")


class pacific_league(League):
    def __init__(self):
        super().__init__("Pacific League")


class central_league(League):
    def __init__(self):
        super().__init__("Central League")
