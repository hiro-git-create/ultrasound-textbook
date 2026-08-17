---
title: 02 完全左脚ブロック (CLBBB) と不完全左脚ブロック
tags: [心電図, 脚ブロック, CLBBB, Sgarbossa基準, 心筋梗塞, 心臓再同期療法, CRT]
aliases: [完全左脚ブロック, 不完全左脚ブロック, CLBBB, Left Bundle Branch Block, Sgarbossa criteria]
date_created: 2026-08-17
last_modified: 2026-08-17
reference_guideline: 日本不整脈心電学会 / JCS 2021年 ガイドライン フォーカスアップデート版 冠動脈疾患 / AHA・ACC・ESC
---

# 02 完全左脚ブロック (CLBBB) と不完全左脚ブロック

完全左脚ブロック（Complete Left Bundle Branch Block: CLBBB）は、刺激伝導系の左脚本幹または前枝・後枝双方の高度な伝導障害により、左室全体の脱分極が大幅に遅延する重篤な室内伝導障害です。左室心筋の広範な線維化、虚血性心疾患、拡張型心筋症、弁膜症（大動脈弁狭窄症等）などの器質的心疾患を背景に持つことが多く、心不全の増悪因子や急性冠症候群（ACS）の診断困難要因となります。

---

## 1. 刺激伝導系の解剖と電気生理学的メカニズム

```mermaid
graph TD
    His["\"ヒス束 (Bundle of His")"] --> LBBB_Site["\"左脚本幹 (Left Bundle Branch")<br>"※ブロック部位\""]
    His --> RBB["\"右脚 (Right Bundle Branch")<br>"(正常伝導")"]
    
    RBB --> Septum_Right["\"右室中隔側の早期興奮<br>(右から左へ脱分極ベクトル反転")"]
    Septum_Right --> RV["\"右室遊離壁の脱分極<br>(最初の0.04秒")"]
    
    LBBB_Site -.->|伝導途絶| Block["左室プルキンエ網伝導停止"]
    RV -->|中隔を横断・心室筋間伝播| LV_Septum["心室中隔の遅延貫通伝導"]
    LV_Septum --> LV_FreeWall["\"左室遊離壁の広範な遅延脱分極<br>(終末0.08〜0.12秒以上持続")"]
```

### 正常伝導とCLBBB伝導の決定的差異
1. **中隔脱分極の逆転**:
   - **正常**: 心室中隔は「左側から右側」へ脱分極するため、左側誘導（I, aVL, V5, V6）に小さな**中隔q波**が記録されます。
   - **CLBBB**: 右脚から興奮が始まるため、中隔脱分極は**「右側から左側」へ反転**します。このため、**左側誘導の中隔q波が完全に消失**します。
2. **左室遊離壁の遅延脱分極**:
   - 右室から心室中隔の作業心筋をゆっくり経由して左室へ興奮が伝わるため、QRS前半〜後半にかけて持続的に左後方に向かう巨大な起電力が発生します。
   - これが左側誘導（I, aVL, V5, V6）における幅広く頭頂部にノッチ（くびれ）を伴う単相性R波（M型波形）を形成し、右側胸部誘導（V1〜V3）では深いQS波またはrS波を形成します。

---

## 2. 心電図診断基準

```mermaid
graph LR
    LBBB_Check["左脚伝導障害の判定"] --> Width{"QRS幅の計測"}
    Width -->|QRS ≥ 0.12秒 (120ms)| CLBBB["\"完全左脚ブロック (CLBBB")"]
    Width -->|0.10秒 ≤ QRS < 0.12秒| ILBBB["\"不完全左脚ブロック (ILBBB")"]
    
    CLBBB --> Lead_Left["\"I, aVL, V5, V6:<br>① 中隔q波の完全消失<br>② 幅広く頭頂部ノッチのある単相性R波<br>③ 心室興奮時間 (VAT") > 0.06秒"]
    CLBBB --> Lead_Right["\"V1, V2, V3:<br>① 幅広く深いQS波 または rS波<br>② 二次性ST上昇・陽性T波 (Discordant")"]
```

### 完全左脚ブロック（CLBBB）の確定診断基準
| 誘導グループ | 特徴的心電図所見 | 判定基準・計測値 |
| :--- | :--- | :--- |
| **全体基準** | **QRS幅の著明な延長** | **QRS幅 ≥ 0.12 秒 (120 ms)** |
| **側壁誘導 (I, aVL, V5, V6)** | **中隔q波の消失** | 正常な生理的q波（幅<0.04s, 深さ<Rの1/4）が消失。 |
| | **幅広く結節（ノッチ）のあるR波** | M型波形（plateau/slurred R波）。 |
| | **心室興奮時間 (VAT) の延長** | **V5/V6で VAT > 0.06 秒 (60 ms)**。 |
| **前中隔誘導 (V1, V2, V3)** | **幅広いQS波 または 小さなr波を伴うrS波** | 初期のr波は非常に細く微小、S波は深く幅広い。 |
| **再分極過程 (ST-T)** | **二次性ST-T変化 (適切な不一致: Appropriate Discordance)** | QRS主波とST-Tの向きが**正反対**になる（V1-V3でST上昇・上向きT波、I/aVL/V5/V6でST低下・陰性T波）。 |

### 不完全左脚ブロック（ILBBB）の診断基準
- **QRS幅**: **0.10秒以上 0.12秒未満**（100〜119 ms）。
- **側壁誘導（I, aVL, V5, V6）**: 中隔q波が消失し、R波の立ち上がりが緩徐（VAT > 0.05s）。
- **臨床的意味**: 左室肥大（LVH）との境界病態であることが多く、左室負荷の進行とともに完全左脚ブロックへ移行することがあります。

---

## 3. CLBBB存在下における急性心筋梗塞（STEMI）の診断基準

> [!CAUTION]
> **CLBBBは従来のSTEMI診断基準を完全にマスクする！**
> CLBBBでは正常でもV1〜V3でST上昇（QRS反対方向）、V5〜V6でST低下（QRS反対方向）を認めます。したがって、**「通常のST上昇基準（≥1mm）」をCLBBBに適応すると誤診（過剰診断または見逃し）** につながります。

```mermaid
flowchart TD
    ChestPain["CLBBB + 急性胸痛"] --> Sgarbossa{"Sgarbossa & Modified Sgarbossa 判定"}
    
    Sgarbossa -->|A: 同方向性ST上昇 ≥1mm (V4-V6, I, aVL)| HighRisk["\"🚨 STEMI確定 (特異度 >98%")<br>"即時冠動脈造影 (CAG")"]
    Sgarbossa -->|B: V1-V3で同方向性ST低下 ≥1mm| HighRisk
    Sgarbossa -->|C: 不一致ST上昇 / S波振幅 比率 ≤ -0.25| HighRisk
    
    Sgarbossa -->|すべて陰性だが症状持続| SubSigns{"\"虚血微細サイン (Cabrera/Chapman")"}
    SubSigns -->|Cabrera徴候 または Chapman徴候 陽性| EchoCAG["\"心エコー (壁運動低下") / 冠動脈造影考慮"]
    SubSigns -->|陰性| Biomarker["トロポニン連続測定 / 冠動脈CT"]
```

### 1. Sgarbossa基準（スガルボッサ基準: 1996年）
| 項目 | 所見・判定条件 | 陽性時配点 | 特異度 |
| :--- | :--- | :---: | :---: |
| **① 同方向性 ST上昇 (Concordant ST elevation)** | QRS主波が上向きの誘導（I, aVL, V5, V6等）で **ST上昇 ≥ 1 mm (0.1 mV)** | **5点** | **98%** |
| **② 同方向性 ST低下 (Concordant ST depression)** | QRS主波が下向きの前中隔誘導（V1, V2, V3）で **ST低下 ≥ 1 mm (0.1 mV)** | **3点** | **96%** |
| **③ 過剰な不一致 ST上昇 (Excessively discordant ST elevation)** | QRS主波が下向きの誘導（V1〜V3等）で **ST上昇 ≥ 5 mm (0.5 mV)** | **2点** | 70〜80% |

> [!IMPORTANT]
> **Sgarbossaスコア 3点以上** で急性心筋梗塞（STEMI同等病態）と診断し、緊急カテーテル治療（PCI）の適応となります。

---

### 2. 改変Smith-Sgarbossa基準（Modified Smith-Sgarbossa Criteria）
従来の③（5mm基準）はQRS波の電位が高い場合に偽陽性となりやすいため、S波の深さに応じた比率で判定する基準へ改良されました。

$$\text{Modified Sgarbossa Ratio} = \frac{\text{不一致 ST上昇値 (mm)}}{\text{S波の振幅 (mm)}} \le -0.25 \quad (\text{または } \ge 25\%)$$

- **診断精度**: 感度 91%、特異度 90% と従来のSgarbossa基準より大幅に感度が向上しています。
- **解釈**: V1〜V3でS波の深さの25%以上のST上昇があれば、絶対値が5mm未満であっても急性前壁中隔梗塞と判定します。

---

### 3. 陳旧性心筋梗塞合併の補助徴候
- **Cabrera徴候 (Cabrera's sign)**: V3〜V5誘導の深いS波の上昇脚に **0.05秒（1.25mm）以上の明瞭なノッチ（くびれ）** を認める所見（前壁陳旧性心筋梗塞を示唆）。
- **Chapman徴候 (Chapman's sign)**: I, aVL, V6誘導の幅広いR波の上昇脚に明瞭なノッチを認める所見（側壁梗塞を示唆）。

---

## 4. 臨床的意義と心不全・CRT適応

```mermaid
graph TD
    CLBBB["CLBBBの病態進行"]
    CLBBB --> Dyssynchrony["\"心室同期不全 (Dyssynchrony")<br>"中隔の早期収縮 + 側壁の遅延収縮\""]
    Dyssynchrony --> Remodeling["\"左室リモデリング・僧帽弁閉鎖不全 (MR") 増悪"]
    Remodeling --> HFrEF["\"収縮不全型心不全 (HFrEF") の進行"]
    
    HFrEF --> CRT["\"⚡ 心臓再同期療法 (CRT-P / CRT-D") の適応検討<br>"・LVEF ≤ 35%<br>・NYHA II〜IV度<br>・QRS幅 ≥ 130〜150ms (CLBBBパターン: Class I")"]
```

> [!TIP]
> **CRT（両室ペーシング）におけるCLBBBの重要性**
> 心臓再同期療法（CRT）において、**CLBBBパターン（特にQRS幅 ≥ 150ms）** は最も高いレスポンダー率（治療反応性）を示します。非LBBB（CRBBBやIVCD）に比べて心不全入院・死亡率の劇的な改善が期待できます（JCSガイドライン Class I適応）。

---

## 5. レポート記載例

### 慢性期のCLBBB（心機能低下合併例）
```text
【心電図所見】
洞調律 72bpm、電気軸 -15°。
QRS幅 164ms、I, aVL, V5, V6誘導にて中隔q波の消失および頂部ノッチを伴う幅広R波を認める。
V1-V3誘導にて幅広いQS波、軽度の二次性ST上昇（S波振幅の15%未満）を認める。
明らかなConcordant ST変化（Sgarbossa基準陽性所見）は認めず。

【診断】
完全左脚ブロック (Complete Left Bundle Branch Block: CLBBB)
【推奨コメント】
高度な左室伝導障害および同期不全を示唆します。心エコーによる左室収縮能（EF）評価および器質的心疾患の精査を推奨します。
```

### CLBBBに急性前壁STEMIを疑う緊急レポート
```text
【心電図所見】
洞性頻脈 104bpm、QRS幅 156ms (CLBBBパターン)。
V2誘導においてS波深さ 12mm に対し ST上昇 +4.5mm (ST/S比 = 37.5% ≥ 25%: 改変Sgarbossa基準陽性)。
V5, V6誘導にて 1.5mmの同方向性ST上昇（Concordant ST elevation: Sgarbossa 5点）を認める。

【診断】
完全左脚ブロック (CLBBB) 合併 急性ST上昇型心筋梗塞 (前壁〜側壁STEMI疑い)
【至急対応コメント】
🚨 改変Smith-Sgarbossa基準を満たす超緊急心電図です。急性冠症候群（LAD閉塞）を強く疑います。直ちに循環器当直医へ連絡し、緊急カテーテル検査（CAG/PCI）の準備を開始してください。
```

---

## 関連リンク（Obsidian WikiLinks）
- [[01_完全右脚ブロック_CRBBB_と不完全右脚ブロック_IRBBB]] - 右脚ブロックとの対比
- [[04_2枝ブロック_3枝ブロックと室内伝導遅延_IVCD]] - 分枝ブロックと室内伝導遅延
- [[01_ST上昇型心筋梗塞_STEMI_責任冠動脈枝の同定と誘導局在]] - 冠動脈閉塞と局在診断
- [[02_心室頻拍_VT_単形性_多形性_鑑別診断_Brugada基準]] - Wide QRS頻拍におけるLBBBパターン鑑別
