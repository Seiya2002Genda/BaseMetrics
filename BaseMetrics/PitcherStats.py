# PitcherStats.py
from Stats_Overall import SeasonPitchingStats
from Stats_Games import GamePitchingStats


class PitcherStats:
    """
    投手としてのシーズン成績管理
    """

    def __init__(self, player):
        self.player = player
        self.season_stats = SeasonPitchingStats()

    def add_game_stats(self, game_stats: GamePitchingStats):
        self.season_stats.add_game(game_stats)

    def to_dict(self):
        d = self.season_stats.to_dict()
        d["Player"] = self.player.name
        d["Position"] = self.player.position
        return d

    def __str__(self):
        s = self.season_stats
        return (f"{self.player.name} IP:{s.IP:.1f} ERA:{s.era():.2f} "
                f"WHIP:{s.whip():.2f} K9:{s.k9():.2f}")
