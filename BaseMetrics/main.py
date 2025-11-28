# main.py

from Organization import Organization
from Team_League import TeamLeague
from Team_Division import TeamDivision
from Team_Selection import TeamSelection
from Player import Player
from PlayerRole import PlayerRole
from BatterStats import BatterStats
from PitcherStats import PitcherStats
from Stats_Games import GameBattingStats, GamePitchingStats
from Save_csv import save_stats_list
from Team import TeamDatabase


def choose_from_list(title, options):
    print(f"\n===== {title} を選択してください =====")
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")

    while True:
        try:
            num = int(input("番号を入力 → "))
            if 1 <= num <= len(options):
                return options[num - 1]
            else:
                print("番号が範囲外です。")
        except ValueError:
            print("数字で入力してください。")


def input_non_empty(message):
    v = input(message).strip()
    while v == "":
        print("空欄は不可です。")
        v = input(message).strip()
    return v


def select_team_structure():
    # =============================
    # ① 組織
    # =============================
    org = choose_from_list("組織（Organization）", ["NPB", "MLB"])

    # =============================
    # ② リーグ
    # =============================
    leagues = (
        ["Central League", "Pacific League"] if org == "NPB"
        else ["American League", "National League"]
    )
    league = choose_from_list("リーグ（League）", leagues)

    # =============================
    # ③ ディビジョン
    # =============================
    if org == "NPB":
        division = "NPB Division"  # 仮固定
        print(f"\nNPBはディビジョンなし → {division} に設定")
    else:
        division = choose_from_list("ディビジョン（Division）", ["East", "Central", "West"])

    # =============================
    # ④ チーム（Team.pyから自動ロード）
    # =============================
    teams = TeamDatabase.get_teams(org, league, division)
    team = choose_from_list("チーム（Team）", teams)

    return org, league, division, team


def main():
    print("===== 野球データ入力システム =====")

    # 組織 → リーグ → ディビジョン → チーム
    org_name, league_name, division_name, team_name = select_team_structure()

    org = Organization(org_name)
    league = TeamLeague(org.name, league_name)
    division = TeamDivision(division_name)
    team = TeamSelection(team_name)

    org.add_league(league)
    league.add_division(division)
    division.add_selection(team)

    # 選手登録
    num_players = int(input_non_empty("登録する選手数を入力: "))

    batter_stats_list = []
    pitcher_stats_list = []

    for i in range(num_players):
        print(f"\n===== {i+1}人目の選手 =====")
        name = input_non_empty("選手名: ")
        position = input_non_empty("ポジション（P, LF など）: ")

        player = Player(name, position)
        team.add_player(player)

        role = PlayerRole(player).get_role()
        print(f"→ 役割: {role}")

        # ===== 打者 =====
        if role == "Batter":
            print("\n--- 打者成績入力（1試合分） ---")

            PA  = int(input_non_empty("PA（打席数）: "))
            AB  = int(input_non_empty("AB（打数）: "))
            H   = int(input_non_empty("H（安打数）: "))
            _2B = int(input_non_empty("2B（二塁打）: "))
            _3B = int(input_non_empty("3B（三塁打）: "))
            HR  = int(input_non_empty("HR（本塁打）: "))
            BB  = int(input_non_empty("BB（四球）: "))
            HBP = int(input_non_empty("HBP（死球）: "))
            SF  = int(input_non_empty("SF（犠飛）: "))

            # ---- 1試合分データを GameBattingStats にまとめる ----
            game = GameBattingStats(
                PA, AB, H, _2B, _3B, HR, BB, HBP, SF
            )

            # ---- 選手ごとのシーズン成績へ追加 ----
            stats = BatterStats(player)
            stats.add_game_stats(game)

            batter_stats_list.append(stats)

        # ===== 投手 =====
        else:
            print("\n--- 投手成績入力（1試合分） ---")

            IP = float(input_non_empty("IP（投球回）: "))
            H  = int(input_non_empty("H（被安打）: "))
            R  = int(input_non_empty("R（失点）: "))
            ER = int(input_non_empty("ER（自責点）: "))
            BB = int(input_non_empty("BB（与四球）: "))
            SO = int(input_non_empty("SO（三振）: "))
            HR = int(input_non_empty("HR（被本塁打）: "))

            # ---- 1試合分データを GamePitchingStats にまとめる ----
            game = GamePitchingStats(
                IP, H, R, ER, BB, SO, HR
            )

            # ---- 選手ごとのシーズン成績へ追加 ----
            stats = PitcherStats(player)
            stats.add_game_stats(game)

            pitcher_stats_list.append(stats)


    # 保存
    if batter_stats_list:
        save_stats_list(batter_stats_list, "batter_stats.csv")
        print("\n打者成績を保存 → batter_stats.csv")

    if pitcher_stats_list:
        save_stats_list(pitcher_stats_list, "pitcher_stats.csv")
        print("投手成績を保存 → pitcher_stats.csv")

    # 最終出力
    print("\n===== 結果表示 =====")
    for b in batter_stats_list:
        print(b)

    for p in pitcher_stats_list:
        print(p)


if __name__ == "__main__":
    main()
