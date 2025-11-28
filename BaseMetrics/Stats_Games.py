# Stats_games.py

class GameBattingStats:
    """
    1試合分の打撃成績
    """
    def __init__(self, PA=0, AB=0, H=0, _2B=0, _3B=0, HR=0, BB=0, HBP=0, SF=0):
        self.PA = PA        # 打席
        self.AB = AB        # 打数
        self.H = H          # 安打
        self._2B = _2B      # 二塁打
        self._3B = _3B      # 三塁打
        self.HR = HR        # 本塁打
        self.BB = BB        # 四球
        self.HBP = HBP      # 死球
        self.SF = SF        # 犠飛

    @property
    def TB(self):
        """塁打数"""
        return (self.H - self._2B - self._3B - self.HR) \
               + 2 * self._2B + 3 * self._3B + 4 * self.HR


class GamePitchingStats:
    """
    1試合分の投手成績（超シンプル版）
    """
    def __init__(self, IP=0.0, H=0, R=0, ER=0, BB=0, SO=0, HR=0):
        self.IP = IP    # 投球回
        self.H = H
        self.R = R
        self.ER = ER
        self.BB = BB
        self.SO = SO
        self.HR = HR
