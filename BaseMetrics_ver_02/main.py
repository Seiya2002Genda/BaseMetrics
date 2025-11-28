from Organization import Organization
from PlayerRole import pitcher, batter
from Player_position import PlayerPosition
from Stats import PitcherStats, BatterStats
from SaveCSV import SaveCSV_Pitcher, SaveCSV_Batter


def choose(title, options: list):
    print(f"\n===== {title} を選択してください =====")
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")
    while True:
        try:
            idx = int(input("番号 → "))
            if 1 <= idx <= len(options):
                return options[idx - 1]
        except ValueError:
            pass
        print("無効な入力です。再入力してください。")


def main():
    print("=== BaseMetrics System ===")

    org = Organization()

    # -------------------------
    # 1. MLB / NPB 選択
    # -------------------------
    org_type = choose("組織 (Organization)", ["MLB", "NPB"])

    if org_type == "MLB":
        league_obj = org.MLB
    else:
        league_obj = org.NPB

    # -------------------------
    # 2. League 選択
    # -------------------------
    league_name = choose("リーグ (League)", list(league_obj.leagues.keys()))
    league = league_obj.leagues[league_name]

    # -------------------------
    # 3. Division 選択
    # -------------------------
    division_name = choose("ディビジョン (Division)", list(league.divisions.keys()))
    division = league.divisions[division_name]

    # -------------------------
    # 4. Team 選択
    # -------------------------
    team_names = [team.name for team in division.teams]
    team_name = choose("チーム (Team)", team_names)

    # 該当 Team オブジェクト取得
    selected_team = next(t for t in division.teams if t.name == team_name)

    # -------------------------
    # 5. Player の名前入力
    # -------------------------
    player_name = input("\n選手名を入力してください → ").strip()

    # -------------------------
    # 6. Position 選択
    # -------------------------
    pos_name = choose("ポジション (Position)", PlayerPosition.get_all_positions())

    # 自動で pitcher / batter を振り分け
    if PlayerPosition.is_pitcher(pos_name):
        player_obj = pitcher(player_name)
        stats_obj = PitcherStats(player_name)
        is_pitcher = True
    else:
        player_obj = batter(player_name)
        stats_obj = BatterStats(player_name)
        is_pitcher = False

    # Team に登録
    selected_team.add_player(player_obj)

    # -------------------------
    # 7. Stats 入力
    # -------------------------
    print("\n=== 成績入力 ===")
    if is_pitcher:
        ip = float(input("投球回 (IP) → "))
        er = int(input("自責点 (ER) → "))
        h = int(input("被安打 (H) → "))
        bb = int(input("与四球 (BB) → "))
        so = int(input("奪三振 (SO) → "))
        hr = int(input("被本塁打 (HR) → "))

        stats_obj.add_innings(ip)
        stats_obj.add_earned_runs(er)
        for _ in range(h):
            stats_obj.add_hit_allowed()
        for _ in range(bb):
            stats_obj.add_walk_allowed()
        for _ in range(so):
            stats_obj.add_strikeout()
        for _ in range(hr):
            stats_obj.add_home_run_allowed()

    else:  # batter
        ab = int(input("打数 (AB) → "))
        hit = int(input("安打 (H) → "))
        doubles = int(input("二塁打 (2B) → "))
        triples = int(input("三塁打 (3B) → "))
        hr = int(input("本塁打 (HR) → "))
        bb = int(input("四球 (BB) → "))
        hbp = int(input("死球 (HBP) → "))
        sf = int(input("犠飛 (SF) → "))

        for _ in range(ab):
            stats_obj.add_at_bat()
        for _ in range(hit):
            stats_obj.add_hit()
        for _ in range(doubles):
            stats_obj.add_double()
        for _ in range(triples):
            stats_obj.add_triple()
        for _ in range(hr):
            stats_obj.add_home_run()
        for _ in range(bb):
            stats_obj.add_walk()
        for _ in range(hbp):
            stats_obj.add_hit_by_pitch()
        for _ in range(sf):
            stats_obj.add_sac_fly()

    # -------------------------
    # 8. 結果表示
    # -------------------------
    print("\n===== 結果 =====")
    selected_team.show_players()
    stats_obj.show()

    # -------------------------
    # 9. CSV 保存
    # -------------------------
    if is_pitcher:
        SaveCSV_Pitcher().save(stats_obj)
    else:
        SaveCSV_Batter().save(stats_obj)

    print("\nCSV 保存完了！")


if __name__ == '__main__':
    main()
