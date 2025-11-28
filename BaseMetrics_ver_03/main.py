# main.py

from Organization import major_league_baseball, nippon_professional_baseball
from League import AmericanLeague, NationalLeague, PacificLeague, CentralLeague
from Division import (
    AmericanLeagueEast, AmericanLeagueCentral, AmericanLeagueWest,
    NationalLeagueEast, NationalLeagueCentral, NationalLeagueWest,
    CentralLeagueDivision, PacificLeagueDivision
)
from Team import TEAM_DATABASE
from PlayerRole import Pitcher, Batter
from Player_position import PitcherPosition, BatterPosition
from StartingLineup import StartingLineup
from Games import Game
from Inning import Inning
from Stats import GameStats
import csv


# ======================================================
# CSV 保存
# ======================================================
def save_player_csv(name, age, nationality, handed, role):
    filename = "player_information.csv"
    header = ["name", "age", "nationality", "handed", "role"]

    try:
        with open(filename, "x", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(header)
    except FileExistsError:
        pass

    with open(filename, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([name, age, nationality, handed, role])


# ======================================================
# MLB / NPB チームをフィルタする関数  ← ★追加
# ======================================================
def filter_teams_by_organization(org_choice):
    mlb = []
    npb = []

    for div_name, tlist in TEAM_DATABASE.items():

        if "American League" in div_name or "National League" in div_name:
            mlb.extend(tlist)
        else:
            npb.extend(tlist)

    return mlb if org_choice == "1" else npb


# ======================================================
# チーム選択
# ======================================================
def select_team(title, teams):
    print(f"\n--- {title} ---")
    for i, t in enumerate(teams, 1):
        print(f"{i}. {t.name}")

    while True:
        try:
            num = int(input("番号 → "))
            if 1 <= num <= len(teams):
                return teams[num - 1]
        except:
            pass
        print("無効な番号です。")


# ======================================================
# main
# ======================================================
def main():
    print("===== BaseMetrics System =====")

    # --------------------------------------------------
    # プレイヤー情報
    # --------------------------------------------------
    if input("選手情報を登録しますか？ (y/n): ").lower() == "y":
        name = input("名前: ")
        age = int(input("年齢: "))
        nationality = input("国籍: ")
        handed = input("利き手 (Right/Left/Switch): ")
        role = input("役割 (Pitcher/Batter): ")
        save_player_csv(name, age, nationality, handed, role)
        print("保存しました。")

    # --------------------------------------------------
    # 組織 (MLB / NPB)
    # --------------------------------------------------
    print("\n===== 組織を選択 =====")
    print("1. MLB\n2. NPB")
    org_choice = input("番号 → ")

    if org_choice == "1":
        org = major_league_baseball()
    else:
        org = nippon_professional_baseball()

    # --------------------------------------------------
    # リーグ (MLB or NPB)
    # --------------------------------------------------
    print("\n===== リーグを選択 =====")
    if org_choice == "1":
        print("1. American League\n2. National League")
        lg = input("番号 → ")
        league = AmericanLeague() if lg == "1" else NationalLeague()
    else:
        print("1. Pacific League\n2. Central League")
        lg = input("番号 → ")
        league = PacificLeague() if lg == "1" else CentralLeague()

    # --------------------------------------------------
    # Division
    # --------------------------------------------------
    print("\n===== ディビジョンを選択 =====")

    if org_choice == "1":  # MLB
        print("1. East\n2. Central\n3. West")
        dv = input("番号 → ")

        if isinstance(league, AmericanLeague):
            division = [AmericanLeagueEast, AmericanLeagueCentral, AmericanLeagueWest][int(dv) - 1]()
        else:
            division = [NationalLeagueEast, NationalLeagueCentral, NationalLeagueWest][int(dv) - 1]()
    else:  # NPB
        division = CentralLeagueDivision() if lg == "2" else PacificLeagueDivision()

    # --------------------------------------------------
    # チーム（Division 内）
    # --------------------------------------------------
    div_key = division.name
    division_teams = TEAM_DATABASE[div_key]

    selected_team = select_team("チームを選択してください", division_teams)
    print(f"\n→ 選択されたチーム: {selected_team.name}")

    # --------------------------------------------------
    # 役割 / ポジション
    # --------------------------------------------------
    print("\n===== 選手の役割 =====")
    print("1. Pitcher\n2. Batter")
    rp = input("番号 → ")

    if rp == "1":
        role = Pitcher()
        pos = input("ポジション (Starter / Reliever / Closer): ")
        position = PitcherPosition(role, pos)
    else:
        role = Batter()
        pos = input("ポジション ('Catcher', 'First Base', 'Second Base', 'Third Base', 'Shortstop', 'Left Field', 'Center Field', 'Right Field', 'Designated Hitter'): ")
        position = BatterPosition(role, pos)

    # --------------------------------------------------
    # スタメン登録
    # --------------------------------------------------
    lineup = StartingLineup()
    if input("\nスタメン登録しますか？ (y/n): ").lower() == "y":
        pname = input("選手名: ")
        lineup.add_player(pname, position)
        print("→ 登録完了")

    # --------------------------------------------------
    # Home / Away（MLB or NPB のチームだけ） ← ★修正
    # --------------------------------------------------
    print("\n===== Home / Away チームを選択 =====")

    filtered_team_list = filter_teams_by_organization(org_choice)  # ← ★ここ重要

    home_team = select_team("Home Team", filtered_team_list)
    away_team = select_team("Away Team", filtered_team_list)

    game = Game(home_team, away_team, lineup, lineup)

    # --------------------------------------------------
    # イニング入力
    # --------------------------------------------------
    print("\n===== 9イニングの得点を入力 =====")
    for i in range(1, 10):
        print(f"\n--- {i}回 ---")
        inn = Inning(i)
        inn.add_run_top(int(input("表の得点: ")))
        inn.add_run_bottom(int(input("裏の得点: ")))
        game.add_inning(inn)

    # --------------------------------------------------
    # スコア表示
    # --------------------------------------------------
    gs = GameStats(game)
    gs.calculate()

    print("\n===== 試合結果 =====")
    print(gs.summary())

    # --------------------------------------------------
    # CSV 保存
    # --------------------------------------------------
    with open("season_game.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Game Result"])
        writer.writerow([gs.summary()])

    print("\nCSV 保存完了: season_game.csv")


if __name__ == "__main__":
    main()
