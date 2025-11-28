# Inning.py

class Inning:
    """1イニングを表すクラス（表裏のラン・選手成績を管理）"""

    def __init__(self, inning_number: int):
        self.inning_number = inning_number

        # 表・裏の得点
        self.runs_top = 0
        self.runs_bottom = 0

        # 打者の成績リスト（1打席ごとの記録を入れる）
        self.batters_top = []
        self.batters_bottom = []

        # 投手の成績（ボール/ストライク数・被安打など）
        self.pitchers_top = []
        self.pitchers_bottom = []

    # -----------------------------
    # ラン（得点）管理
    # -----------------------------
    def add_run_top(self, runs: int = 1):
        self.runs_top += runs

    def add_run_bottom(self, runs: int = 1):
        self.runs_bottom += runs

    # -----------------------------
    # 打者成績
    # batter_stats: dict 形式を推奨
    # {'player': 'Ohtani', 'result': 'HR', 'RBI': 2}
    # -----------------------------
    def add_batter_top(self, batter_stats: dict):
        self.batters_top.append(batter_stats)

    def add_batter_bottom(self, batter_stats: dict):
        self.batters_bottom.append(batter_stats)

    # -----------------------------
    # 投手成績
    # pitcher_stats: dict
    # {'player': 'Darvish', 'pitch': 'Strike', 'speed': 152}
    # -----------------------------
    def add_pitcher_top(self, pitcher_stats: dict):
        self.pitchers_top.append(pitcher_stats)

    def add_pitcher_bottom(self, pitcher_stats: dict):
        self.pitchers_bottom.append(pitcher_stats)

    # -----------------------------
    # このイニングのまとめ
    # -----------------------------
    def get_summary(self):
        return {
            "inning": self.inning_number,
            "top_runs": self.runs_top,
            "bottom_runs": self.runs_bottom,
            "top_batters": self.batters_top,
            "bottom_batters": self.batters_bottom,
            "top_pitchers": self.pitchers_top,
            "bottom_pitchers": self.pitchers_bottom
        }

    def __str__(self):
        return f"Inning {self.inning_number}: Top {self.runs_top} - Bottom {self.runs_bottom}"
