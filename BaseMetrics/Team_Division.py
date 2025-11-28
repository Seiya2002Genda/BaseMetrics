# Team_Division.py
class TeamDivision:
    """
    リーグ内の Division（West / Central / East）
    """

    def __init__(self, division_name):
        self.division_name = division_name
        self.selections = []        # チーム選択へ進む

    def add_selection(self, selection):
        self.selections.append(selection)

    def __str__(self):
        return f"Division({self.division_name})"
