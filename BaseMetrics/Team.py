# Team.py
class TeamDatabase:
    """
    MLB / NPB の全公式チームデータをまとめて管理するクラス
    main.py はここからチームを取得する
    """

    NPB_TEAMS = {
        "Central League": [
            "Yomiuri Giants",
            "Hanshin Tigers",
            "Hiroshima Carp",
            "Chunichi Dragons",
            "Yokohama DeNA BayStars",
            "Tokyo Yakult Swallows"
        ],

        "Pacific League": [
            "Orix Buffaloes",
            "SoftBank Hawks",
            "Chiba Lotte Marines",
            "Rakuten Eagles",
            "Nippon-Ham Fighters",
            "Seibu Lions"
        ]
    }

    MLB_TEAMS = {
        ("American League", "East"): [
            "New York Yankees", "Boston Red Sox", "Toronto Blue Jays",
            "Baltimore Orioles", "Tampa Bay Rays"
        ],
        ("American League", "Central"): [
            "Minnesota Twins", "Chicago White Sox", "Cleveland Guardians",
            "Detroit Tigers", "Kansas City Royals"
        ],
        ("American League", "West"): [
            "Houston Astros", "Seattle Mariners", "Texas Rangers",
            "Los Angeles Angels", "Oakland Athletics"
        ],

        ("National League", "East"): [
            "Atlanta Braves", "New York Mets", "Philadelphia Phillies",
            "Miami Marlins", "Washington Nationals"
        ],
        ("National League", "Central"): [
            "Chicago Cubs", "Milwaukee Brewers", "St. Louis Cardinals",
            "Pittsburgh Pirates", "Cincinnati Reds"
        ],
        ("National League", "West"): [
            "Los Angeles Dodgers", "San Diego Padres", "San Francisco Giants",
            "Arizona Diamondbacks", "Colorado Rockies"
        ]
    }

    @staticmethod
    def get_teams(org, league, division=None):
        """
        組織 / リーグ / ディビジョンからチームリストを返す関数
        """
        if org == "NPB":
            return TeamDatabase.NPB_TEAMS.get(league, [])

        elif org == "MLB":
            key = (league, division)
            return TeamDatabase.MLB_TEAMS.get(key, [])

        return []
