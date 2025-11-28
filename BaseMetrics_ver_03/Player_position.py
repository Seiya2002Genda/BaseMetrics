# Player_position.py

from PlayerRole import Pitcher, Batter


class PlayerPosition:
    """ポジションの基底クラス（Pitcher/Batter で共通化）"""
    def __init__(self, role, position_name: str):
        self.role = role              # Pitcher または Batter のインスタンス
        self.position_name = position_name

    def __str__(self):
        return f"{self.role.role_name} - {self.position_name}"


# ================================
# 投手の詳細ポジション
# ================================

class PitcherPosition(PlayerPosition):
    """先発 / 中継ぎ / 抑えを管理"""

    ALLOWED_POSITIONS = ["Starter", "Reliever", "Closer"]

    def __init__(self, role: Pitcher, pos_type: str):
        if pos_type not in self.ALLOWED_POSITIONS:
            raise ValueError(f"PitcherPosition must be one of {self.ALLOWED_POSITIONS}")

        super().__init__(role, pos_type)


# ================================
# 打者の詳細ポジション
# ================================

class BatterPosition(PlayerPosition):
    """捕手・内野・外野・DH を管理"""

    ALLOWED_POSITIONS = [
        "Catcher", "First Base", "Second Base",
        "Third Base", "Shortstop",
        "Left Field", "Center Field", "Right Field",
        "Designated Hitter"
    ]

    def __init__(self, role: Batter, pos_type: str):
        if pos_type not in self.ALLOWED_POSITIONS:
            raise ValueError(f"BatterPosition must be one of {self.ALLOWED_POSITIONS}")

        super().__init__(role, pos_type)
