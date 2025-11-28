# Stats_overall.py
from Stats_Games import GameBattingStats, GamePitchingStats


class SeasonBattingStats:
    """
    シーズン通算打撃成績
    """

    def __init__(self):
        self.PA = 0
        self.AB = 0
        self.H = 0
        self._2B = 0
        self._3B = 0
        self.HR = 0
        self.BB = 0
        self.HBP = 0
        self.SF = 0
        self.TB = 0

    def add_game(self, game: GameBattingStats):
        self.PA += game.PA
        self.AB += game.AB
        self.H += game.H
        self._2B += game._2B
        self._3B += game._3B
        self.HR += game.HR
        self.BB += game.BB
        self.HBP += game.HBP
        self.SF += game.SF
        self.TB += game.TB

    # ------- rate stats -------
    def avg(self):
        return self.H / self.AB if self.AB > 0 else 0.0

    def obp(self):
        denom = self.AB + self.BB + self.HBP + self.SF
        if denom == 0:
            return 0.0
        return (self.H + self.BB + self.HBP) / denom

    def slg(self):
        return self.TB / self.AB if self.AB > 0 else 0.0

    def ops(self):
        return self.obp() + self.slg()

    def to_dict(self):
        return {
            "PA": self.PA,
            "AB": self.AB,
            "H": self.H,
            "2B": self._2B,
            "3B": self._3B,
            "HR": self.HR,
            "BB": self.BB,
            "HBP": self.HBP,
            "SF": self.SF,
            "AVG": round(self.avg(), 3),
            "OBP": round(self.obp(), 3),
            "SLG": round(self.slg(), 3),
            "OPS": round(self.ops(), 3),
        }


class SeasonPitchingStats:
    """
    シーズン通算投手成績（簡略）
    """

    def __init__(self):
        self.IP = 0.0
        self.H = 0
        self.R = 0
        self.ER = 0
        self.BB = 0
        self.SO = 0
        self.HR = 0

    def add_game(self, game: GamePitchingStats):
        self.IP += game.IP
        self.H += game.H
        self.R += game.R
        self.ER += game.ER
        self.BB += game.BB
        self.SO += game.SO
        self.HR += game.HR

    def era(self):
        # 9 * ER / IP
        return 9 * self.ER / self.IP if self.IP > 0 else 0.0

    def whip(self):
        # (BB + H) / IP
        return (self.BB + self.H) / self.IP if self.IP > 0 else 0.0

    def k9(self):
        return 9 * self.SO / self.IP if self.IP > 0 else 0.0

    def to_dict(self):
        return {
            "IP": self.IP,
            "H": self.H,
            "R": self.R,
            "ER": self.ER,
            "BB": self.BB,
            "SO": self.SO,
            "HR": self.HR,
            "ERA": round(self.era(), 2),
            "WHIP": round(self.whip(), 2),
            "K9": round(self.k9(), 2),
        }
