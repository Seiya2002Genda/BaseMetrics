from Player_position import PlayerPosition


class Team_selection:
    """
    各チームの基本構造
    players: 投手・打者どちらも入る
    """

    def __init__(self, name: str):
        self.name = name
        self.players = []   # pitcher と batter の混合リスト

    # -------------------------------
    # プレイヤー登録
    # -------------------------------
    def add_player(self, player):
        self.players.append(player)

    # -------------------------------
    # プレイヤー表示
    # -------------------------------
    def show_players(self):
        print(f"\n===== Team: {self.name} =====")

        if not self.players:
            print("  No players registered.")
            return

        for p in self.players:

            # 名前
            name = p.name

            # ポジションコード
            pos_code = getattr(p, "position_code", None)

            if pos_code:
                full = PlayerPosition.get_full_name(pos_code)
                pos_str = f"{pos_code} / {full}"
            else:
                pos_str = "No Position Assigned"

            print(f"  - {name} [{pos_str}]")
