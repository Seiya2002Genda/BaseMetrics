from Player_position import PlayerPosition


class pitcher:
    """
    Pitcher class
    投手の基本情報のみ（ポジション管理は Player_position へ委譲）
    """

    def __init__(self, name: str):
        self.name = name
        self.position_code = None       # SP / RP / CP
        self.pitch_types = []
        self.fastball_velocity = None

    def set_position(self, code: str):
        if PlayerPosition.is_pitcher_role(code):
            self.position_code = code
        else:
            raise ValueError(f"Invalid pitcher role: {code}")

    def add_pitch_type(self, pitch_name: str):
        self.pitch_types.append(pitch_name)

    def show(self):
        print(f"[Pitcher] {self.name}")

        if self.position_code:
            full_pos = PlayerPosition.get_full_name(self.position_code)
            print(f"  Position: {self.position_code} ({full_pos})")
        else:
            print("  Position: Not Assigned")

        print(f"  Pitch Types: {self.pitch_types}")
        print(f"  Velocity: {self.fastball_velocity}")


class batter:
    """
    Batter class
    打者の基本情報のみ（ポジション管理は Player_position へ委譲）
    """

    def __init__(self, name: str):
        self.name = name
        self.position_code = None       # SS / CF / RF / 1B / DH etc.
        self.bat_side = None            # R / L / Switch

    def set_position(self, code: str):
        if PlayerPosition.is_batter_position(code):
            self.position_code = code
        else:
            raise ValueError(f"Invalid batter position: {code}")

    def show(self):
        print(f"[Batter] {self.name}")

        if self.position_code:
            full_pos = PlayerPosition.get_full_name(self.position_code)
            print(f"  Position: {self.position_code} ({full_pos})")
        else:
            print("  Position: Not Assigned")

        print(f"  Batting Side: {self.bat_side}")
