from Team import Team_selection


class Division:
    """
    Division の基底クラス
    （アメリカンリーグ/ナショナルリーグの各地区、NPBはMainが該当）
    """

    def __init__(self, division_name: str):
        self.name = division_name
        self.teams = []  # Teamオブジェクトのリスト

    def add_team(self, team: Team_selection):
        self.teams.append(team)

    def show(self):
        print(f"  [Division] {self.name}")
        for t in self.teams:
            t.show()

class east_division_national(Division):
    def __init__(self):
        super().__init__("National League East")


class west_division_national(Division):
    def __init__(self):
        super().__init__("National League West")


class central_division_national(Division):
    def __init__(self):
        super().__init__("National League Central")


class east_division_american(Division):
    def __init__(self):
        super().__init__("American League East")


class west_division_american(Division):
    def __init__(self):
        super().__init__("American League West")


class central_division_american(Division):
    def __init__(self):
        super().__init__("American League Central")
