# SaveCSV.py

import csv


# ========================================
# 基本となる CSV 書き込みユーティリティ
# ========================================

def write_csv(filename: str, headers: list, rows: list):
    """汎用CSV書き込み。rows は list of dict を想定"""
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


# ========================================
# 1. Pitcher Information 保存
# ========================================

class SaveCSV_Pitcher_Information:
    def save(self, filename: str, pitcher_info: dict):
        """
        pitcher_info expected:
        {
            "Darvish": {"age": 37, "handed": "Right", "nationality": "Japan", "role": "Pitcher"}
        }
        """
        rows = []
        for name, info in pitcher_info.items():
            row = {"name": name}
            row.update(info)
            rows.append(row)

        headers = list(rows[0].keys()) if rows else []
        write_csv(filename, headers, rows)


# ========================================
# 2. Batter Information 保存
# ========================================

class SaveCSV_Batter_Information:
    def save(self, filename: str, batter_info: dict):
        rows = []
        for name, info in batter_info.items():
            row = {"name": name}
            row.update(info)
            rows.append(row)

        headers = list(rows[0].keys()) if rows else []
        write_csv(filename, headers, rows)


# ========================================
# 3. Pitcher Stats 保存
# ========================================

class SaveCSV_Pitcher_Stats:
    def save(self, filename: str, pitcher_stats_summary: dict):
        """
        pitcher_stats_summary example:
        {
            "pitches": 95,
            "strikes": 62,
            "balls": 33,
            "hits_allowed": 5,
            "runs_allowed": 2,
            "average_speed": 148.5
        }
        """
        headers = list(pitcher_stats_summary.keys())
        rows = [pitcher_stats_summary]
        write_csv(filename, headers, rows)


# ========================================
# 4. Batter Stats 保存
# ========================================

class SaveCSV_Batter_Stats:
    def save(self, filename: str, batter_stats_summary: dict):
        headers = list(batter_stats_summary.keys())
        rows = [batter_stats_summary]
        write_csv(filename, headers, rows)


# ========================================
# 5. Day/Night Game 保存
# ========================================

class SaveCSV_day_night_game:
    def save(self, filename: str, game_stats: dict):
        """
        game_stats example:
        {
            "inning": 1,
            "top_runs": 0,
            "bottom_runs": 2,
            "top_batters": [...],
            "bottom_batters": [...],
        }
        """
        # バッターやピッチャーの詳細がリストの場合は文字列に変換
        processed = {}
        for key, val in game_stats.items():
            if isinstance(val, list):
                processed[key] = str(val)
            else:
                processed[key] = val

        headers = list(processed.keys())
        rows = [processed]
        write_csv(filename, headers, rows)


# ========================================
# 6. Season Game（GameStats 全試合分の集計）保存
# ========================================

class SaveCSV_season_game:
    def save(self, filename: str, list_of_game_summaries: list):
        """
        list_of_game_summaries example:
        [
            {"home_team": "Dodgers", "away_team": "Giants", "home_runs": 5, "away_runs": 3},
            {"home_team": "Dodgers", "away_team": "Padres", "home_runs": 2, "away_runs": 4}
        ]
        """
        if not list_of_game_summaries:
            return

        headers = list(list_of_game_summaries[0].keys())
        rows = list_of_game_summaries
        write_csv(filename, headers, rows)
