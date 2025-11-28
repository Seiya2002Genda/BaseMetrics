# PlayerInformation.py

class PlayerDatabase:
    """選手情報をメモリ上で保持する独立データベース"""
    def __init__(self):
        self.players = {}

    def exists(self, name: str):
        return name in self.players

    def add(self, name: str, info: dict):
        self.players[name] = info

    def edit(self, name: str, new_info: dict):
        self.players[name] = new_info

    def delete(self, name: str):
        if name in self.players:
            del self.players[name]

    def search(self, name: str):
        return self.players.get(name, None)

    def list_all(self):
        return self.players


# ====================================================
# AddInformation
# ====================================================

class AddInformation:
    """選手情報を追加するクラス"""

    def __init__(self, database: PlayerDatabase):
        self.db = database

    def add_player(self, name: str, age: int, nationality: str, handed: str, role: str):
        if self.db.exists(name):
            raise ValueError("この選手はすでに登録されています。")

        info = {
            "age": age,
            "nationality": nationality,
            "handed": handed,
            "role": role
        }

        self.db.add(name, info)


# ====================================================
# EditInformation
# ====================================================

class EditInformation:
    """登録済みの選手情報を編集"""

    def __init__(self, database: PlayerDatabase):
        self.db = database

    def edit_player(self, name: str, new_age=None, new_nationality=None, new_handed=None, new_role=None):
        if not self.db.exists(name):
            raise ValueError("選手が見つかりません。")

        current = self.db.search(name)

        updated = {
            "age": new_age if new_age is not None else current["age"],
            "nationality": new_nationality if new_nationality is not None else current["nationality"],
            "handed": new_handed if new_handed is not None else current["handed"],
            "role": new_role if new_role is not None else current["role"]
        }

        self.db.edit(name, updated)


# ====================================================
# DeleteInformation
# ====================================================

class DeleteInformation:
    """選手情報を削除"""

    def __init__(self, database: PlayerDatabase):
        self.db = database

    def delete_player(self, name: str):
        if not self.db.exists(name):
            raise ValueError("選手が存在しません。")
        self.db.delete(name)


# ====================================================
# SearchInformation
# ====================================================

class SearchInformation:
    """選手情報検索"""

    def __init__(self, database: PlayerDatabase):
        self.db = database

    def search_player(self, name: str):
        return self.db.search(name)
