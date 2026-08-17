---
title: 03 左室肥大（LVH）の診断基準 Sokolow-Lyon・Cornell・電圧基準
tags: [心電図, 左室肥大, LVH, Sokolow-Lyon基準, Cornell基準, Cornell積, ストレインパターン, 高血圧, 心電図検定]
aliases: [左室肥大, LVH, ソコロフライオン基準, コーネル基準, コーネル積, 左室ストレイン]
date_created: 2026-08-17
last_modified: 2026-08-17
reference_guideline: 日本不整脈心電学会 / 日本高血圧学会(JSH2019/2024) / AHA・ACC・HRS Recommendations for the Standardization and Interpretation of the Electrocardiogram / 心電図検定公式基準
---

# 03 左室肥大（LVH）の診断基準 Sokolow-Lyon・Cornell・電圧基準

左室肥大（Left Ventricular Hypertrophy: LVH）は、高血圧、大動脈弁狭窄症（AS）、肥大型心筋症（HCM）などに伴い左室心筋量（Left Ventricular Mass: LVM）が増加した状態です。心電図上のLVH所見は、単なる心筋壁肥厚の検出にとどまらず、将来の**心血管イベント（脳卒中・心不全・心筋梗塞・心臓突然死）の極めて強力な独立した予後規定因子**です。

---

## 1. 左室肥大の電気生理学的メカニズム

```mermaid
graph TD
    LVH_Physiology["左室肥大の電気生理学的基盤"]
    LVH_Physiology --> Mass["\"① 心筋重量・断面積の増加<br>➔ 左後下方への総起電力増大<br>(V5/V6の巨大R波、V1/V2の深大S波")"]
    LVH_Physiology --> Delay["\"② 心室壁厚の増大<br>➔ 心内膜から外膜への伝導遅延<br>(VAT延長 > 0.05秒、QRS幅軽度増大")"]
    LVH_Physiology --> Strain["\"③ 心内膜側の相対的虚血・再分極遅延<br>➔ 左室ストレイン型ST-T変化<br>(V5/V6でのST低下＋非対称陰性T")"]
```

---

## 2. 主要な左室肥大（LVH）診断基準の完全対照表

心電図を用いたLVH診断には多数の基準が提唱されています。特異度が高い「Sokolow-Lyon基準」と、性差を考慮し感度に優れる「Cornell基準」の併用が標準的です。

| 診断基準名 | 算出フォーミュラ | LVH陽性カットオフ値 | 特徴・感度・特異度 |
| :--- | :--- | :--- | :--- |
| **① Sokolow-Lyon<br>胸部電圧基準**<br>【最頻出】 | $$\text{SV}_1 + \text{RV}_5 \text{ (または } \text{RV}_6\text{)}$$ | **$\ge 3.5\text{ mV}$ ($35\text{ mm}$)** | ・世界で最も普及<br>・特異度高（$\approx 90\%$）<br>・感度は低め（$20 \sim 40\%$）<br>・若年者で偽陽性多い |
| **② Sokolow-Lyon<br>肢誘導基準** | $$\text{RaVL}$$ | **$\ge 1.1\text{ mV}$ ($11\text{ mm}$)** | 高位側壁への起電力を反映 |
| **③ Cornell 電圧基準**<br>(コーネル基準) | $$\text{RaVL} + \text{SV}_3$$ | **男性: $\ge 2.8\text{ mV}$ ($28\text{ mm}$)**<br>**女性: $\ge 2.0\text{ mV}$ ($20\text{ mm}$)** | ・**性差を補正**<br>・感度・特異度のバランス優良<br>・肥満患者でも感度低下しにくい |
| **④ Cornell 電圧時間積**<br>(Cornell Product) | $$(\text{RaVL} + \text{SV}_3) \times \text{QRS幅}$$<br>*(※女性は電圧に $+0.6\text{mV}$ 加算)* | **$> 2440\text{ mm}\cdot\text{ms}$**<br>($> 244\text{ mV}\cdot\text{ms}$) | ・心エコー左室重量と最強の相関<br>・大規模治験（LIFE試験等）で採用 |
| **⑤ Gubner-Ungerleider** | $$\text{RI} + \text{SIII}$$ | **$\ge 2.5\text{ mV}$ ($25\text{ mm}$)** | 肢誘導のみで判定可能 |
| **⑥ 肢誘導最大R波** | $\text{RI} \ge 1.5\text{ mV}$ または $\text{RaVF} \ge 2.0\text{ mV}$ | 各カットオフ以上 | 肢誘導の高電位所見 |

---

## 3. 左室ストレインパターン（LV Strain Pattern: 二次性ST-T変化）

左室肥大に伴い、左側胸部誘導および高位側壁誘導に出現する特異的なST-T変化を「ストレインパターン（過負荷パターン）」と呼びます。

```mermaid
graph LR
    subgraph StrainMorphology["左室ストレインパターンの形態"]
        ST["\"下向き凸 (Downsloping") のST低下<br>"(J点からなだらかに沈み込む")"]
        T["\"非対称性 (Asymmetrical") 陰性T波<br>"(下降脚は緩やか、後半急速に基線へ復帰")"]
        Lead["出現誘導: I, aVL, V5, V6"]
    end
    ST --> T --> Lead
```

```mermaid
graph TD
    Diff["\"ストレイン型陰性T vs 虚血性陰性T (冠性T波") の鑑別"]
    Diff --> StrainT["\"左室ストレイン型 (LV Strain")<br>"・非対称性 (緩やかに下がり急に戻る")<br>"・高いR波に伴って出現<br>・I, aVL, V5, V6 に限局\""]
    Diff --> CoronaryT["\"虚血性・冠性T波 (Coronary T")<br>"・左右完全対称 (鋭利な矢尻状")<br>"・R波高に関係なく出現<br>・鏡面像や局所解剖に一致\""]
```

> [!IMPORTANT]
> **ストレインパターンの臨床的重要度**
> 単なる「電圧基準のみのLVH」に比べ、「**電圧基準 ＋ ストレインパターン**」を認めるLVHは、心筋線維化、左室拡張末期圧上昇、冠血流予備能低下が高度に進行しており、**心不全入院および心血管死リスクが約 3〜5 倍に跳ね上がります**。

---

## 4. Romhilt-Estes 点数システム（Point Score System）

電圧基準以外の多角的心電図パラメータを点数化した高精度診断法です（5点以上でLVH確定、4点でLVH疑い）。

| 評価項目 | 心電図所見 | 配点 |
| :--- | :--- | :--- |
| **1. 電圧基準** | ・四肢誘導で $R$ または $S \ge 2.0\text{ mV}$<br>・$\text{SV}_1$ または $\text{SV}_2 \ge 3.0\text{ mV}$<br>・$\text{RV}_5$ または $\text{RV}_6 \ge 3.0\text{ mV}$ | **3点** |
| **2. ST-T変化** | ・ジギタリス非内服時の左室ストレイン型ST-T変化<br>・*(※ジギタリス内服時は 1点)* | **3点** |
| **3. 左房負荷** | ・V1誘導で Morris指数陽性（終末陰性波 $\ge 1\text{mm} \times 0.04\text{s}$） | **3点** |
| **4. 電気軸** | ・左軸偏位（$\text{Axis} \le -30^\circ$） | **2点** |
| **5. QRS幅** | ・QRS幅 $\ge 0.09\text{ 秒}$（$90\text{ ms}$） | **1点** |
| **6. 心室興奮時間** | ・V5 または V6 で $\text{VAT} \ge 0.05\text{ 秒}$（$50\text{ ms}$） | **1点** |

---

## 5. 心電図検定・実務でのピットフォール（偽陽性と偽陰性）

```mermaid
graph TD
    Pitfalls["LVH診断におけるピットフォール"]
    Pitfalls --> FalsePos["\"偽陽性 (False Positive: 高電位だが肥大なし")<br>"・若年健常男性 (20〜30代")<br>"・痩身・胸壁の薄い患者<br>・アスリート心臓 (生理的増大")"]
    Pitfalls --> FalseNeg["\"偽陰性 (False Negative: 肥大あるのに低電圧")<br>"・高度肥満 (皮下脂肪による減衰")<br>"・肺気腫・COPD (過膨張空気による絶縁")<br>"・心嚢液貯留・胸水<br>・心アミロイドーシス\""]
```

> [!TIP]
> **若年男性におけるSokolow-Lyon基準の適用限界**
> 35歳未満（特に20代）の健常男性では、胸壁が薄く心臓と電極が近いため、正常であっても $\text{SV}_1 + \text{RV}_5 \ge 3.5\text{ mV}$ を容易に超えます。若年者では **Cornell電圧基準** を用いるか、**ストレイン型ST-T変化や左房負荷の随伴** を確認して総合判定します。

---

## 関連リンク・ナビゲーション
- 前の項目: [[02_心房負荷_右房負荷_左房負荷_両房負荷の心電図基準]]
- 次の項目: [[04_右室肥大_RVH_および両室肥大の心電図基準]]
- 基準値確認: [[00_心電図計測基準値_クイックリファレンス]]
- 関連疾患: [[02_QRS群の波形解析_幅_高さ_移行帯]], [[02_完全左脚ブロック_CLBBB_と不完全左脚ブロック]]
