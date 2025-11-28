class PlayerPosition:
    """全ポジションの正式名称管理クラス"""

    # 投手 (Pitcher)
    PITCHER_POSITIONS = [
        "Starting Pitcher (SP)",
        "Relief Pitcher (RP)",
        "Closing Pitcher (CP)"
    ]

    # 野手 (Batter / Fielder)
    BATTER_POSITIONS = [
        "Catcher (C)",
        "First Baseman (1B)",
        "Second Baseman (2B)",
        "Third Baseman (3B)",
        "Shortstop (SS)",
        "Left Fielder (LF)",
        "Center Fielder (CF)",
        "Right Fielder (RF)",
        "Designated Hitter (DH)"
    ]

    @classmethod
    def get_all_positions(cls) -> list:
        """main.py で全ポジション一覧を取得するため"""
        return cls.PITCHER_POSITIONS + cls.BATTER_POSITIONS

    @classmethod
    def is_pitcher(cls, pos_name: str) -> bool:
        """投手かどうか判定する"""
        return pos_name in cls.PITCHER_POSITIONS
