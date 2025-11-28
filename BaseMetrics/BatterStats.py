# BatterStats.py
from Stats_Overall import SeasonBattingStats
from Stats_Games import GameBattingStats


class BatterStats:
    """
    打者としてのシーズン成績管理
    """

    def __init__(self, player):
        self.player = player
        self.season_stats = SeasonBattingStats()

    def add_game_stats(self, game_stats: GameBattingStats):
        self.season_stats.add_game(game_stats)

    def to_dict(self):
        d = self.season_stats.to_dict()
        d["Player"] = self.player.name
        d["Position"] = self.player.position
        return d

    def __str__(self):
        s = self.season_stats
        return (f"{self.player.name} AVG:{s.avg():.3f} "
                f"OBP:{s.obp():.3f} SLG:{s.slg():.3f} OPS:{s.ops():.3f}")
