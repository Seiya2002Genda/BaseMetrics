class Inning:
    """
    1イニングを表現するクラス
    攻撃側・守備側、得点、アウト、投球数などを管理
    """

    def __init__(self, inning_number: int, top: bool):
        """
        inning_number: 1,2,3...
        top: True = 表(top), False = 裏(bottom)
        """
        self.inning_number = inning_number
        self.top = top

        self.runs = 0  # 得点
        self.hits = 0  # 安打数
        self.errors = 0  # 失策
        self.pitch_count = 0  # 投球数
        self.outs = 0  # アウトカウント

        self.events = []  # イニング内の打席記録（必要に応じて追加）

    def add_run(self, n: int = 1):
        self.runs += n

    def add_hit(self):
        self.hits += 1

    def add_error(self):
        self.errors += 1

    def add_pitch(self, n: int = 1):
        self.pitch_count += n

    def add_out(self):
        if self.outs < 3:
            self.outs += 1

    def add_event(self, event: str):
        """
        イベント記録
        例: 'Single', 'Home Run', 'Strikeout', 'Walk'
        """
        self.events.append(event)

    def is_finished(self) -> bool:
        return self.outs >= 3

    def show(self):
        inning_side = "TOP" if self.top else "BOTTOM"
        print(f"--- Inning {self.inning_number} {inning_side} ---")
        print(f" Runs: {self.runs}")
        print(f" Hits: {self.hits}")
        print(f" Errors: {self.errors}")
        print(f" Pitches: {self.pitch_count}")
        print(f" Outs: {self.outs}")
        if self.events:
            print(" Events:")
            for e in self.events:
                print(f"   - {e}")
