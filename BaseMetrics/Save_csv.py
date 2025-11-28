# Save_csv.py
import csv


def save_stats_list(stats_list, filename):
    """
    BatterStats / PitcherStats のリストを CSV 保存
    stats_list: to_dict() を持つオブジェクトのリスト
    """
    if not stats_list:
        return

    # 1件目のキーをヘッダに使う
    header = list(stats_list[0].to_dict().keys())

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for s in stats_list:
            writer.writerow(s.to_dict())
