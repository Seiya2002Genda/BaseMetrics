# 🏟️ BaseMetrics — Baseball Analytics Core Engine  
### *Designed & Engineered by Seiya Genda*  
MLB / NPB の正式な組織構造を OOP で再現し、成績管理・計算・CSV 出力まで行う「野球分析エンジン（現行版）」。  
将来的には Web 化・3D 可視化・物理シミュレーションまで統合する拡張版の開発を計画している。

---

# 📌 Overview

**BaseMetrics（現行版）**  
- MLB / NPB の階層構造（Organization → League → Division → Team）を OOP で完全再現  
- 選手（pitcher / batter）管理  
- ポジションは正式名称＋略称に対応  
- 投手・打者の主要指標（ERA / WHIP / OPS など）を計算  
- CSV 保存  
- すべてを CLI 入力で操作可能  

**BaseMetrics（将来計画）**  
BaseMetrics は今後、以下を統合した **Web 版・3D 分析プラットフォーム**へ発展予定：

- Flask による Web UI  
- Three.js による 3D 球場モデル  
- 打球物理シミュレーション  
- 投球位置の 3D 可視化  
- Out カウントの視覚的 UI  
- MySQL 永続化  
- AI による打球予測・投球クラスタリング  
- LUMISTIA との分析統合  

これにより **「次世代型ベースボール分析エンジン」** に進化する計画である。

---

# 📂 Project Structure

---
BaseMetrics/
│
├── core/
│ ├── Organization.py
│ ├── League.py
│ ├── Division.py
│ ├── Team.py
│ ├── PlayerRole.py
│ ├── Player_position.py
│ ├── Stats.py
│ └── SaveCSV.py
│
├── main.py # CLI 入力式の実行アプリ
│
└── (将来的に追加) app.py, templates/, static/ # Flask Web化予定


---

# 🧩 OOP Architecture



Organization
├── MLB (major_league_baseball)
│ ├── American League
│ │ ├── East Division
│ │ ├── Central Division
│ │ └── West Division
│ └── National League
│ ├── East Division
│ ├── Central Division
│ └── West Division
│
└── NPB (nippon_professional_baseball)
├── Pacific League
└── Central League


各 Division は正式名称・正確な階層で管理。

Team → Player → Position → Stats  
という構造で動作する。

---

# 🧢 Team & Player System

### ✔ Team.py  
- 正式名称のチーム名（略称禁止）  
- 複数の選手を保持  
- `add_player()` と `show_players()` を実装  

### ✔ PlayerRole.py  
- `pitcher(name)`  
- `batter(name)`  

### ✔ Player_position.py  
正式名称＋略称の全ポジションを網羅：

#### Pitchers
- Starting Pitcher (SP)  
- Relief Pitcher (RP)  
- Closing Pitcher (CP)

#### Batters
- Catcher (C)  
- First Baseman (1B)  
- Second Baseman (2B)  
- Third Baseman (3B)  
- Shortstop (SS)  
- Left Fielder (LF)  
- Center Fielder (CF)  
- Right Fielder (RF)  
- Designated Hitter (DH)

提供メソッド：  
- `get_all_positions()`  
- `is_pitcher(pos)`  

---

# 📊 Stats Engine

## ✔ PitcherStats

| 指標 | 公式名 |
|------|--------|
| IP | Innings Pitched |
| ER | Earned Runs |
| H | Hits Allowed |
| BB | Walks |
| SO | Strikeouts |
| HR | Home Runs Allowed |
| ERA | Earned Run Average |
| WHIP | (BB+H)/IP |
| K/9 | Strikeouts per 9 |
| HR/9 | Home Runs per 9 |

## ✔ BatterStats

| 指標 | 公式名 |
|------|--------|
| AB | At Bats |
| H | Hits |
| 2B | Doubles |
| 3B | Triples |
| HR | Home Runs |
| BB | Walks |
| HBP | Hit By Pitch |
| SF | Sac Fly |
| AVG | Batting Average |
| OBP | On Base % |
| SLG | Slugging % |
| OPS | OBP + SLG |

---

# 💾 CSV Export

- `SaveCSV_Pitcher()`  
- `SaveCSV_Batter()`  

成績を自動で CSV に保存。

---

# 🎮 CLI Version (main.py)

ユーザーが以下をすべて入力可能：

1. MLB / NPB  
2. League  
3. Division  
4. Team  
5. Player 名  
6. ポジション（正式名称選択）  
7. 投手 / 打者を自動判定  
8. 成績入力  
9. 結果表示  
10. CSV 保存  

現行版 BaseMetrics の操作 UI。

---

# 🌐 Future Plan — Flask Web Application（将来機能）

BaseMetrics は今後、  
**Flask を使って Web アプリ化**する計画。

予定されている UI：

- 選手一覧テーブル  
- 選手追加フォーム  
- 成績入力画面  
- OPS・ERA のライブ分析  
- Out カウントランプ（●●○）  
- 投手・打者の成績ビューア  
- 打球と投球の 3D 可視化画面  

API 構成案：



/api/add_player
/api/add_stats
/api/get_team
/api/get_player


---

# 🟡 Future Plan — Out Count Visualization（将来機能）

MLB スコアボード式アウト表示を Web で実現：



● ● ○ ← OUT 2


HTML × CSS × JavaScript でランプ式 UI を構築。

---

# 🟠 Future Plan — 3D Hit Simulation（将来機能）

打球の飛行を **物理シミュレーション**で正確に可視化。

利用するパラメータ：

- Exit Velocity  
- Launch Angle  
- Spray Angle  
- Spin（Backspin / Sidespin）  
- 空気抵抗（Drag）  
- Magnus 効果  
- 重力  

物理式例：



Fd = 1/2 * ρ * v² * Cd * A
Fm = S (v × ω)


Three.js で球場内を飛ぶボールを 3D アニメーション表示する計画。

---

# 🔴 Future Plan — 3D Pitch Location Tracking（将来機能）

投手の投球軌跡を Web 上で 3D 表示：

- リリース位置（x,y,z）
- キャッチャーミット位置
- 球速・球種
- ボールの曲がり（変化量）

Three.js の 3D 曲線を使用。

---

# 🏟 Future Plan — 3D Stadium Model（将来機能）

Seiya が収集した  
**MLB 全30球場 / NPB 全12球場の正確な外野フェンス距離**  
を Three.js モデルとして再現する計画。

- 左翼 / 左中間 / 中堅 / 右中間 / 右翼距離  
- フェンス高さ  
- フィールド形状  
- 観客席（簡易モデル）  

---

# 🗄️ Future Plan — MySQL Integration

データを永続化するため  
将来的には MySQL + SQLAlchemy を導入：

- 選手  
- チーム  
- 成績  
- 打球記録  
- 投球記録  

LUMISTIA の分析エンジンとも統合予定。

---

# 🚀 Vision

BaseMetrics は  
**「野球 × AI × 物理 × Web × データ解析」**  
を統合した **次世代型ベースボール分析エコシステム**へ進化する。

目標：

✔ 打球飛距離予測 AI  
✔ 投手リリース点クラスタリング  
✔ OPS / ERA の自動解析  
✔ Realtime 3D Visualization  
✔ LUMISTIA との統合  
✔ 世界で唯一の個人開発プロ野球分析システム  

---

# 👤 Author

**Seiya Genda**  
University of Nebraska at Kearney  
Double Major: Computer Science × Marketing  
Creator of LUMISTIA / ClassMake / BaseMetrics  

世界唯一の「野球 × AI × 物理 × Web」統合システムを開発中。

