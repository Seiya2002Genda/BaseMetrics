# Stats.py

class PitcherStats:
    """投手の成績を集計するクラス"""

    def __init__(self):
        self.pitches = 0          # 投球数
        self.strikes = 0          # ストライク数
        self.balls = 0            # ボール数
        self.hits_allowed = 0     # 被安打
        self.runs_allowed = 0     # 失点
        self.pitch_speeds = []    # 球速リスト

    def update_from_inning(self, pitcher_events: list):
        """Inning から渡された投手成績(dict)のリストを集計"""
        for event in pitcher_events:

            if "pitch" in event:
                self.pitches += 1

                if event["pitch"] == "Strike":
                    self.strikes += 1
                elif event["pitch"] == "Ball":
                    self.balls += 1

            if "speed" in event:
                self.pitch_speeds.append(event["speed"])

            if "result" in event and event["result"] == "Hit":
                self.hits_allowed += 1

            if "runs" in event:
                self.runs_allowed += event["runs"]

    def average_speed(self):
        if not self.pitch_speeds:
            return 0
        return sum(self.pitch_speeds) / len(self.pitch_speeds)

    def summary(self):
        return {
            "pitches": self.pitches,
            "strikes": self.strikes,
            "balls": self.balls,
            "hits_allowed": self.hits_allowed,
            "runs_allowed": self.runs_allowed,
            "average_speed": self.average_speed()
        }


class BatterStats:
    """打者の成績を集計するクラス"""

    def __init__(self):
        self.PA = 0        # 打席数
        self.H = 0         # 安打
        self.HR = 0        # 本塁打
        self.RBI = 0       # 打点
        self.BB = 0        # 四球
        self.SO = 0        # 三振
        self.R = 0         # 得点

    def update_from_inning(self, batter_events: list):
        """Inning から渡された打者成績(dict)のリストを集計"""
        for event in batter_events:
            self.PA += 1

            result = event.get("result", "")

            if result == "Hit":
                self.H += 1
            if result == "HomeRun":
                self.HR += 1
                self.H += 1
            if result == "Walk":
                self.BB += 1
            if result == "Strikeout":
                self.SO += 1

            self.RBI += event.get("RBI", 0)
            self.R += event.get("Run", 0)

    def summary(self):
        return {
            "PA": self.PA,
            "H": self.H,
            "HR": self.HR,
            "RBI": self.RBI,
            "BB": self.BB,
            "SO": self.SO,
            "R": self.R
        }


class GameStats:
    """1試合の総合成績（ラインスコア対応）"""

    def __init__(self, game):
        self.game = game
        self.linescore_home = []
        self.linescore_away = []
        self.total_home = 0
        self.total_away = 0

    def calculate(self):
        """イニングの得点を集計してラインスコアを作成"""
        self.linescore_home = []
        self.linescore_away = []
        self.total_home = 0
        self.total_away = 0

        for inn in self.game.innings:
            self.linescore_home.append(inn.runs_bottom)   # ホーム＝裏
            self.linescore_away.append(inn.runs_top)      # アウェイ＝表
            self.total_home += inn.runs_bottom
            self.total_away += inn.runs_top

    def summary(self):
        """現実の野球でも使われるラインスコア形式で出力（完全揃え版）"""

        # 1〜9回の数字
        innings_header = " ".join(f"{i}" for i in range(1, len(self.linescore_home) + 1))

        # それぞれのイニングスコア
        away_scores = " ".join(str(r) for r in self.linescore_away)
        home_scores = " ".join(str(r) for r in self.linescore_home)

        # 合計
        R_home = self.total_home
        R_away = self.total_away

        # H, E（現状は 0）
        H_home = H_away = 0
        E_home = E_away = 0

        # -----------------------------
        # ★ チーム名の幅をそろえる（最大30文字）
        # -----------------------------
        TEAM_COL_WIDTH = 30  # ← 長い名前でもここで揃う

        home_name = self.game.home_team.name.ljust(TEAM_COL_WIDTH)
        away_name = self.game.away_team.name.ljust(TEAM_COL_WIDTH)

        result = (
            "=================== 試合結果 ===================\n\n"
            f"{' ' * TEAM_COL_WIDTH} {innings_header}    R  H  E\n"
            "---------------------------------------------------------\n"
            f"{home_name} {home_scores}    {R_home}  {H_home}  {E_home}\n"
            f"{away_name} {away_scores}    {R_away}  {H_away}  {E_away}\n"
            "---------------------------------------------------------"
        )

        return result


class TeamStats:
    """チームの通算成績"""

    def __init__(self, team):
        self.team = team
        self.total_runs_scored = 0
        self.total_runs_allowed = 0

    def update_from_game(self, game_stats: GameStats):
        """GameStats から成績を受け取る"""

        summary = game_stats.summary()

        # Home
        if summary["home_team"] == self.team.name:
            self.total_runs_scored += game_stats.total_home
            self.total_runs_allowed += game_stats.total_away

        # Away
        elif summary["away_team"] == self.team.name:
            self.total_runs_scored += game_stats.total_away
            self.total_runs_allowed += game_stats.total_home

    def summary(self):
        return {
            "team": self.team.name,
            "total_runs_scored": self.total_runs_scored,
            "total_runs_allowed": self.total_runs_allowed
        }
