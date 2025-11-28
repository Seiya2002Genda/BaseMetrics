# Team.py

class Team:
    """チームの基本クラス"""
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"{self.name}"


# ===================================
# MLB - American League
# ===================================

AL_EAST_TEAMS = [
    Team("New York Yankees"),
    Team("Boston Red Sox"),
    Team("Toronto Blue Jays"),
    Team("Tampa Bay Rays"),
    Team("Baltimore Orioles")
]

AL_CENTRAL_TEAMS = [
    Team("Cleveland Guardians"),
    Team("Minnesota Twins"),
    Team("Detroit Tigers"),
    Team("Kansas City Royals"),
    Team("Chicago White Sox")
]

AL_WEST_TEAMS = [
    Team("Houston Astros"),
    Team("Texas Rangers"),
    Team("Seattle Mariners"),
    Team("Los Angeles Angels"),
    Team("Oakland Athletics")
]


# ===================================
# MLB - National League
# ===================================

NL_EAST_TEAMS = [
    Team("Atlanta Braves"),
    Team("Philadelphia Phillies"),
    Team("New York Mets"),
    Team("Washington Nationals"),
    Team("Miami Marlins")
]

NL_CENTRAL_TEAMS = [
    Team("Chicago Cubs"),
    Team("St. Louis Cardinals"),
    Team("Milwaukee Brewers"),
    Team("Cincinnati Reds"),
    Team("Pittsburgh Pirates")
]

NL_WEST_TEAMS = [
    Team("Los Angeles Dodgers"),
    Team("San Diego Padres"),
    Team("San Francisco Giants"),
    Team("Arizona Diamondbacks"),
    Team("Colorado Rockies")
]


# ===================================
# NPB - セントラルリーグ
# ===================================

NPB_CENTRAL_TEAMS = [
    Team("Yomiuri Giants"),
    Team("Hanshin Tigers"),
    Team("Chunichi Dragons"),
    Team("Hiroshima Toyo Carp"),
    Team("Tokyo Yakult Swallows"),
    Team("Yokohama DeNA BayStars")
]


# ===================================
# NPB - パシフィックリーグ
# ===================================

NPB_PACIFIC_TEAMS = [
    Team("Orix Buffaloes"),
    Team("Fukuoka SoftBank Hawks"),
    Team("Saitama Seibu Lions"),
    Team("Chiba Lotte Marines"),
    Team("Hokkaido Nippon-Ham Fighters"),
    Team("Tohoku Rakuten Golden Eagles")
]


# ===================================
# Division（Division.py）に渡すための辞書データベース
# ===================================

TEAM_DATABASE = {
    "American League East": AL_EAST_TEAMS,
    "American League Central": AL_CENTRAL_TEAMS,
    "American League West": AL_WEST_TEAMS,

    "National League East": NL_EAST_TEAMS,
    "National League Central": NL_CENTRAL_TEAMS,
    "National League West": NL_WEST_TEAMS,

    "Central League Division": NPB_CENTRAL_TEAMS,
    "Pacific League Division": NPB_PACIFIC_TEAMS
}
