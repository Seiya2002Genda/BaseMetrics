class Selection:
    """
    すべての階層構造をここで定義する“設計書クラス”
    チーム名は略さずフルネームで定義
    """

    def __init__(self):

        # ==========================================
        # MLB 要件定義（フル球団名）
        # ==========================================
        self.MLB = {
            "American League": {
                "East": [
                    "New York Yankees",
                    "Boston Red Sox",
                    "Toronto Blue Jays",
                    "Tampa Bay Rays",
                    "Baltimore Orioles",
                ],
                "Central": [
                    "Cleveland Guardians",
                    "Minnesota Twins",
                    "Chicago White Sox",
                    "Kansas City Royals",
                    "Detroit Tigers",
                ],
                "West": [
                    "Houston Astros",
                    "Texas Rangers",
                    "Seattle Mariners",
                    "Los Angeles Angels",
                    "Oakland Athletics",
                ]
            },

            "National League": {
                "East": [
                    "Atlanta Braves",
                    "New York Mets",
                    "Philadelphia Phillies",
                    "Miami Marlins",
                    "Washington Nationals",
                ],
                "Central": [
                    "Chicago Cubs",
                    "Milwaukee Brewers",
                    "Cincinnati Reds",
                    "Pittsburgh Pirates",
                    "St. Louis Cardinals",
                ],
                "West": [
                    "Los Angeles Dodgers",
                    "San Francisco Giants",
                    "San Diego Padres",
                    "Arizona Diamondbacks",
                    "Colorado Rockies",
                ]
            }
        }

        # ==========================================
        # NPB 要件定義（フル球団名）
        # ==========================================
        self.NPB = {
            "Central League": {
                "Main": [
                    "Yomiuri Giants",
                    "Yokohama DeNA BayStars",
                    "Hiroshima Toyo Carp",
                    "Hanshin Tigers",
                    "Chunichi Dragons",
                    "Tokyo Yakult Swallows",
                ]
            },

            "Pacific League": {
                "Main": [
                    "Orix Buffaloes",
                    "Fukuoka SoftBank Hawks",
                    "Saitama Seibu Lions",
                    "Chiba Lotte Marines",
                    "Hokkaido Nippon-Ham Fighters",
                    "Tohoku Rakuten Golden Eagles",
                ]
            }
        }
