import csv
import os


class SaveCSV_Pitcher:
    """
    投手成績をCSVに保存するクラス
    """

    def __init__(self, filepath: str = "pitcher_stats.csv"):
        self.filepath = filepath

        # ファイルが無ければヘッダー作成
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "Pitcher Name",
                    "IP (Innings Pitched)",
                    "ER (Earned Runs)",
                    "H (Hits Allowed)",
                    "BB (Walks Allowed)",
                    "SO (Strikeouts)",
                    "HR (Home Runs Allowed)",
                    "ERA (Earned Run Average)",
                    "WHIP (Walks + Hits / IP)",
                    "K/9 (Strikeouts per 9 Innings)",
                    "HR/9 (Home Runs per 9 Innings)"
                ])

    def save(self, stats):
        """
        stats: PitcherStats オブジェクト
        """
        with open(self.filepath, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                stats.name,
                stats.innings_pitched,
                stats.earned_runs,
                stats.hits_allowed,
                stats.walks_allowed,
                stats.strikeouts,
                stats.home_runs_allowed,
                stats.ERA(),
                stats.WHIP(),
                stats.K_per_9(),
                stats.HR_per_9()
            ])



class SaveCSV_Batter:
    """
    打者成績をCSVに保存するクラス
    """

    def __init__(self, filepath: str = "batter_stats.csv"):
        self.filepath = filepath

        if not os.path.exists(self.filepath):
            with open(self.filepath, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "Batter Name",
                    "AB (At Bats)",
                    "H (Hits)",
                    "2B (Doubles)",
                    "3B (Triples)",
                    "HR (Home Runs)",
                    "BB (Walks)",
                    "HBP (Hit By Pitch)",
                    "SF (Sacrifice Fly)",
                    "AVG (Batting Average)",
                    "OBP (On-base Percentage)",
                    "SLG (Slugging Percentage)",
                    "OPS (On-base Plus Slugging)"
                ])

    def save(self, stats):
        """
        stats: BatterStats オブジェクト
        """
        with open(self.filepath, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                stats.name,
                stats.at_bats,
                stats.hits,
                stats.doubles,
                stats.triples,
                stats.home_runs,
                stats.walks,
                stats.hit_by_pitch,
                stats.sacrifice_fly,
                stats.AVG(),
                stats.OBP(),
                stats.SLG(),
                stats.OPS()
            ])
