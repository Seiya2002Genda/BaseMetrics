# StartingLineup.py

class StartingLineup:
    """スターティングラインナップを管理するクラス"""

    def __init__(self):
        # lineup は dict構造で保持
        # { "PlayerName": PlayerPositionインスタンス }
        self.lineup = {}

    def add_player(self, player_name: str, player_position):
        """
        main.py で YES と答えたら呼ばれる想定
        player_position は PitcherPosition または BatterPosition
        """
        self.lineup[player_name] = player_position

    def remove_player(self, player_name: str):
        """スタメンから選手を削除"""
        if player_name in self.lineup:
            del self.lineup[player_name]

    def get_player_position(self, player_name: str):
        """特定選手のポジションを取得"""
        return self.lineup.get(player_name)

    def list_players(self):
        """スタメン一覧を表示用に返す"""
        return list(self.lineup.keys())

    def show_lineup(self):
        """スタメン全表示（デバッグ用）"""
        print("=== Starting Lineup ===")
        for player_name, position in self.lineup.items():
            print(f"{player_name} : {position}")

    def clear(self):
        """スタメン全消去（試合前リセット用）"""
        self.lineup.clear()

    def __len__(self):
        return len(self.lineup)
