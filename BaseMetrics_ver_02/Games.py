class Season_overall:
    """
    1シーズン全体を管理するクラス
    各試合(day_night_game)を蓄積する
    """

    def __init__(self):
        self.games = []  # day_night_game オブジェクトを保持

    def add_game(self, game):
        self.games.append(game)

    def total_games(self):
        return len(self.games)

    def show(self):
        print("=== Season Overall ===")
        for g in self.games:
            g.show()


class day_night_game:
    """
    デーゲーム / ナイトゲーム 1試合を表すクラス
    ballpark とスコア・日付などを保持できる
    """

    def __init__(self, date: str, is_day_game: bool, ballpark):
        self.date = date
        self.is_day_game = is_day_game
        self.ballpark = ballpark
        self.score = None  # 必要なら後で set_score() で設定

    def set_score(self, home: int, away: int):
        self.score = (home, away)

    def show(self):
        g_type = "DAY GAME" if self.is_day_game else "NIGHT GAME"
        print(f"  [{g_type}] {self.date} @ {self.ballpark.name}")
        if self.score is not None:
            print(f"     Score  Home {self.score[0]} - Away {self.score[1]}")


class ballpark:
    """
    球場データクラス
    ballpark("Yokohama Stadium", "Yokohama")
    """

    def __init__(self, name: str, location: str = None):
        self.name = name
        self.location = location

    def show(self):
        print(f"Ballpark: {self.name} ({self.location})")
