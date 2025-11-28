# Games.py

class Game:
    """1試合の基本クラス（ホーム・アウェイ・スタメン・イニング）"""

    def __init__(self, home_team, away_team, home_lineup=None, away_lineup=None):
        self.home_team = home_team
        self.away_team = away_team

        # StartingLineup オブジェクト
        self.home_lineup = home_lineup
        self.away_lineup = away_lineup

        # Inningオブジェクトを入れる枠（Inning.py が作る）
        self.innings = []

    def add_inning(self, inning_obj):
        """Inning.py で作る inning オブジェクトを追加"""
        self.innings.append(inning_obj)

    def list_innings(self):
        """イニング番号一覧"""
        return [i.inning_number for i in self.innings]

    def show_game_info(self):
        """試合情報を出力（main.py のデバッグ用）"""
        print("===== Game Info =====")
        print(f"Home Team : {self.home_team.name}")
        print(f"Away Team : {self.away_team.name}")

        if self.home_lineup:
            print("Home Lineup:")
            for p in self.home_lineup.list_players():
                print(" -", p)

        if self.away_lineup:
            print("Away Lineup:")
            for p in self.away_lineup.list_players():
                print(" -", p)

        print("=====================")

    def __str__(self):
        return f"Game: {self.away_team.name} vs {self.home_team.name}"
