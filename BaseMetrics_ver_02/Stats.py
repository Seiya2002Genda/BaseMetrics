class PitcherStats:
    """
    Pitcher Statistics (投手成績)
    - Earned Run Average (ERA)
    - Walks plus Hits per Inning Pitched (WHIP)
    - Strikeouts per 9 Innings (K/9)
    - Home Runs per 9 Innings (HR/9)
    """

    def __init__(self, pitcher_name: str):
        self.name = pitcher_name

        # Raw stats
        self.innings_pitched = 0.0        # IP
        self.earned_runs = 0              # ER
        self.hits_allowed = 0             # H
        self.walks_allowed = 0            # BB
        self.strikeouts = 0               # SO
        self.home_runs_allowed = 0        # HR

    # --- Adders ---
    def add_innings(self, innings: float):
        self.innings_pitched += innings

    def add_earned_runs(self, runs: int):
        self.earned_runs += runs

    def add_hit_allowed(self):
        self.hits_allowed += 1

    def add_walk_allowed(self):
        self.walks_allowed += 1

    def add_strikeout(self):
        self.strikeouts += 1

    def add_home_run_allowed(self):
        self.home_runs_allowed += 1

    # --- Calculations ---
    def ERA(self):
        """Earned Run Average (ERA)"""
        if self.innings_pitched == 0:
            return 0.00
        return round((self.earned_runs * 9) / self.innings_pitched, 2)

    def WHIP(self):
        """Walks plus Hits per Inning Pitched (WHIP)"""
        if self.innings_pitched == 0:
            return 0.00
        return round((self.walks_allowed + self.hits_allowed) / self.innings_pitched, 2)

    def K_per_9(self):
        """Strikeouts per 9 Innings (K/9)"""
        if self.innings_pitched == 0:
            return 0.00
        return round((self.strikeouts * 9) / self.innings_pitched, 2)

    def HR_per_9(self):
        """Home Runs per 9 Innings (HR/9)"""
        if self.innings_pitched == 0:
            return 0.00
        return round((self.home_runs_allowed * 9) / self.innings_pitched, 2)

    def show(self):
        print(f"[PitcherStats] {self.name}")
        print(f"  IP (Innings Pitched): {self.innings_pitched}")
        print(f"  ER (Earned Runs): {self.earned_runs}")
        print(f"  H (Hits Allowed): {self.hits_allowed}")
        print(f"  BB (Walks Allowed): {self.walks_allowed}")
        print(f"  SO (Strikeouts): {self.strikeouts}")
        print(f"  HR (Home Runs Allowed): {self.home_runs_allowed}")
        print(f"  ERA (Earned Run Average): {self.ERA()}")
        print(f"  WHIP (Walks + Hits / IP): {self.WHIP()}")
        print(f"  K/9 (Strikeouts per 9): {self.K_per_9()}")
        print(f"  HR/9 (Home Runs per 9): {self.HR_per_9()}")


class BatterStats:
    """
    Batter Statistics (打者成績)
    - Batting Average (AVG)
    - On-base Percentage (OBP)
    - Slugging Percentage (SLG)
    - On-base Plus Slugging (OPS)
    """

    def __init__(self, batter_name: str):
        self.name = batter_name

        # Raw stats
        self.at_bats = 0           # AB
        self.hits = 0              # H
        self.doubles = 0           # 2B
        self.triples = 0           # 3B
        self.home_runs = 0         # HR
        self.walks = 0             # BB
        self.hit_by_pitch = 0      # HBP
        self.sacrifice_fly = 0     # SF

    # --- Adders ---
    def add_at_bat(self):
        self.at_bats += 1

    def add_hit(self):
        self.hits += 1

    def add_double(self):
        self.hits += 1
        self.doubles += 1

    def add_triple(self):
        self.hits += 1
        self.triples += 1

    def add_home_run(self):
        self.hits += 1
        self.home_runs += 1

    def add_walk(self):
        self.walks += 1

    def add_hbp(self):
        self.hit_by_pitch += 1

    def add_sac_fly(self):
        self.sacrifice_fly += 1

    # --- Calculations ---
    def AVG(self):
        """Batting Average (AVG)"""
        if self.at_bats == 0:
            return 0.000
        return round(self.hits / self.at_bats, 3)

    def OBP(self):
        """On-base Percentage (OBP)"""
        denom = self.at_bats + self.walks + self.hit_by_pitch + self.sacrifice_fly
        if denom == 0:
            return 0.000
        return round((self.hits + self.walks + self.hit_by_pitch) / denom, 3)

    def SLG(self):
        """Slugging Percentage (SLG)"""
        singles = self.hits - self.doubles - self.triples - self.home_runs
        total_bases = (
            1 * singles +
            2 * self.doubles +
            3 * self.triples +
            4 * self.home_runs
        )
        if self.at_bats == 0:
            return 0.000
        return round(total_bases / self.at_bats, 3)

    def OPS(self):
        """On-base Plus Slugging (OPS)"""
        return round(self.OBP() + self.SLG(), 3)

    def show(self):
        print(f"[BatterStats] {self.name}")
        print(f"  AB (At Bats): {self.at_bats}")
        print(f"  H (Hits): {self.hits}")
        print(f"  2B (Doubles): {self.doubles}")
        print(f"  3B (Triples): {self.triples}")
        print(f"  HR (Home Runs): {self.home_runs}")
        print(f"  BB (Walks): {self.walks}")
        print(f"  HBP (Hit By Pitch): {self.hit_by_pitch}")
        print(f"  SF (Sac Fly): {self.sacrifice_fly}")
        print(f"  AVG (Batting Average): {self.AVG()}")
        print(f"  OBP (On-base %): {self.OBP()}")
        print(f"  SLG (Slugging %): {self.SLG()}")
        print(f"  OPS: {self.OPS()}")
