# PlayerRole.py

class PlayerRole:
    """選手の役割（Pitcher / Batter）の基底クラス"""
    def __init__(self, role_name: str):
        self.role_name = role_name

    def __str__(self):
        return f"Player Role: {self.role_name}"


class Pitcher(PlayerRole):
    """投手という役割のみ定義（詳細は Player_position が担当）"""
    def __init__(self):
        super().__init__("Pitcher")


class Batter(PlayerRole):
    """打者という役割のみ定義（守備位置などは Player_position が担当）"""
    def __init__(self):
        super().__init__("Batter")
