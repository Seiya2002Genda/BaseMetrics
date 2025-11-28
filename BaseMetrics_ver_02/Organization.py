from Selection import Selection
from League import League
from Division import Division
from Team import Team_selection


class major_league_baseball:
    def __init__(self, selection: Selection):
        self.name = "Major League Baseball"
        self.leagues = {}

        # Selection の MLB 構造を読み込む
        for league_name, divisions in selection.MLB.items():

            # League クラス生成
            league_obj = League(league_name)

            # Division 生成
            for division_name, teams in divisions.items():

                division_obj = Division(division_name)

                # Team 生成
                for team_fullname in teams:
                    division_obj.add_team(Team_selection(team_fullname))

                league_obj.add_division(division_obj)

            self.leagues[league_name] = league_obj


class nippon_professional_baseball:
    def __init__(self, selection: Selection):
        self.name = "Nippon Professional Baseball"
        self.leagues = {}

        # Selection の NPB 構造を読み込む
        for league_name, divisions in selection.NPB.items():

            league_obj = League(league_name)

            for division_name, teams in divisions.items():

                division_obj = Division(division_name)

                for team_fullname in teams:
                    division_obj.add_team(Team_selection(team_fullname))

                league_obj.add_division(division_obj)

            self.leagues[league_name] = league_obj


class Organization:
    """
    すべての球団データを保持する “親玉（root）”
    MLB / NPB は Selection を読み込み自動構築される
    """

    def __init__(self):
        selection = Selection()

        # MLB と NPB を生成
        self.MLB = major_league_baseball(selection)
        self.NPB = nippon_professional_baseball(selection)

    # Universally readable access
    def show_all(self):
        print("===== MLB =====")
        for league in self.MLB.leagues.values():
            league.show()

        print("\n===== NPB =====")
        for league in self.NPB.leagues.values():
            league.show()
