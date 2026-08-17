---
title: 心室頻拍 VT 単形性 多形性 鑑別診断 Brugada基準
tags: [不整脈, 心室頻拍, VT, Wide QRS, Brugada基準, Vereckei基準, 房室解離, 心電図検定]
aliases: [Ventricular Tachycardia, VT, Brugada Criteria, Vereckei Criteria, Wide Complex Tachycardia, WCT]
date_created: 2026-08-17
last_modified: 2026-08-17
reference_guideline: 日本不整脈心電学会 / 2020年改訂版不整脈薬物治療ガイドライン(JCS/JHRS) / AHA・ACC・HRS Wide Complex Tachycardia鑑別基準
---

# 心室頻拍（VT）：単形性・多形性・Wide QRS鑑別アルゴリズム（Brugada基準・Vereckei基準）

心室頻拍（Ventricular Tachycardia: **VT**）は、ヒス束分岐部より下位の心室興奮伝導系または心室筋から発生する頻脈性不整脈であり、臨床的には心拍数 > 100 bpm（通常 120〜250 bpm）で心室性期外収縮が3拍以上連続するものと定義されます。
臨床現場で遭遇する **Wide QRS頻拍（Wide Complex Tachycardia: WCT、QRS幅 ≥ 120ms）** の約80%はVTであり、上室性頻拍（SVT）に変行伝導を伴ったもの（約15%）やWPW症候群に伴う逆方向性頻拍（約5%）との鑑別が生命予後を直結して左右します。

---

## 1. 心室頻拍の分類と臨床像

### 1) 持続時間による分類
- **非持続性心室頻拍（Non-sustained VT: NSVT）**: 3拍以上連続し、**30秒未満** で自然停止するもの（血行動態破綻を伴わない）。
- **持続性心室頻拍（Sustained VT: SVT）**: **30秒以上持続** するか、または30秒未満であっても血圧低下・意識障害など血行動態の破綻を伴い緊急治療（カルディオバージョン等）を要するもの。

### 2) 波形形態による分類
- **単形性心室頻拍（Monomorphic VT）**: 同一誘導においてQRS波形が拍ごとに均一。陳旧性心筋梗塞（OMI）などの心筋瘢痕周囲リエントリー、特発性VT（RVOT/中隔）に多い。
- **多形性心室頻拍（Polymorphic VT）**: 同一誘導においてQRS波形・軸が拍ごとに連続的に変化する。急性心筋虚血、心筋炎、またはQT延長に伴う **Torsades de Pointes（TdP）** が代表的。

---

## 2. Wide QRS頻拍におけるVT示唆の決定的心電図サイン

Wide QRS頻拍に遭遇した際、以下の所見が1つでも認められれば **VTの特異度はほぼ100%** です。

```mermaid
flowchart TD
    WCT["\"Wide QRS頻拍 (QRS ≥ 120ms, HR > 100bpm")"] --> Sign1["\"① 房室解離 (AV Dissociation") / 捕捉拍 (Capture) / 融合拍 (Fusion)"]
    WCT --> Sign2["\"② 極度の軸偏位 (Northwest Axis: -90°〜±180°")"]
    WCT --> Sign3["\"③ 胸部誘導の一致現象 (Precordial Concordance")"]
    WCT --> Sign4["\"④ QRS幅の極端な拡大 (LBBB様 > 160ms, RBBB様 > 140ms")"]
```

### 1) 房室解離（Atrioventricular Dissociation: AV Dissociation）
- 心室の興奮（速いレート）と心房の洞性興奮（遅いレート）が完全に独立して作動している状態。
- **独立したP波**: ワイドなQRS波やST-T波の中に、無関係な周期でP波が埋没・出現する。
- **心室捕捉拍（Capture Beat）**: 洞結節からの興奮がたまたま不応期を脱した房室結節を通過し、心室を正常伝導系経由で脱分極させた拍（幅の狭い正常QRSが1拍だけ混入する）。
- **融合収縮拍（Fusion Beat / Dressler beat）**: 洞性興奮とVTの異所性興奮が心室内で同時に衝突し、正常QRSとVT-QRSの中間形態の波形を形成する。

### 2) 極度の軸偏位（Northwest Axis / 極度の右上軸偏位）
- 電気軸が **-90° 〜 ±180°**（I誘導が陰性、aVF誘導が陰性、**aVR誘導で上向き主波**）。
- 正常なヒス・プルキンエ伝導系では興奮が心尖部から心基部・右上へ向かうことは稀であり、心室固有心筋から逆行性に広がるVTに極めて特異的。

### 3) 胸部誘導の一致現象（Precordial Concordance）
- **陽性一致（Positive Concordance）**: V1〜V6のすべての誘導でQRSが単相性の上向き（R型）。
- **陰性一致（Negative Concordance）**: V1〜V6のすべての誘導でQRSが単相性の下向き（QS型）。

---

## 3. Brugadaアルゴリズム（Brugada Criteria）

Pedro Brugadaら（1991年）によって提唱された、Wide QRS頻拍鑑別の世界標準4ステップアルゴリズムです。感度98.7%、特異度96.5%を誇ります。

```mermaid
flowchart TD
    Step1{"\"Step 1: 全胸部誘導 (V1-V6") に<br/>RSパターンが全く存在しないか？<br/>(すべてR単相 または すべてQS/QR)"}
    Step1 -- Yes --> VT1["\"VTと診断 (感度良好")"]
    Step1 -- No (RSが存在する) --> Step2{"\"Step 2: RSパターンを持つ誘導で<br/>RS時間 (R波開始〜S波最深点") が<br/>> 100ms (2.5小マス) の誘導があるか？"}
    
    Step2 -- Yes --> VT2["VTと診断"]
    Step2 -- No --> Step3{"\"Step 3: 房室解離 (AV Dissociation") の<br/>所見が存在するか？"}
    
    Step3 -- Yes --> VT3["\"VTと診断 (特異度100%")"]
    Step3 -- No --> Step4{"\"Step 4: V1/V2およびV6の波形が<br/>VT形態基準 (Morphology criteria") を満たすか？"}
    
    Step4 -- Yes --> VT4["VTと診断"]
    Step4 -- No --> SVT["\"SVT (変行伝導伴う") と診断"]
```

### 【Step 4の形態基準（Morphology Criteria）詳細】

| パターン | 誘導 | VTを示唆する波形（Morphology） | 変行伝導SVTを示唆する波形 |
| :--- | :---: | :--- | :--- |
| **右脚ブロック型 (RBBB-like)**<br>*(V1で陽性主波)* | **V1** | ・単相性R波、qR型、QR型<br>・二峰性R波で**左側の山が高い（左耳 > 右耳: "Rabbit ear sign"）** | ・二峰性R波で**右側の山が高い（rsR'型）** |
| | **V6** | ・$R/S < 1$（S波が深い）<br>・QS型、QR型 | ・$R/S > 1$（R波優位） |
| **左脚ブロック型 (LBBB-like)**<br>*(V1で陰性主波)* | **V1/V2** | ・初期R波の幅が広い（**$R \text{幅} \ge 30\text{ms} = 0.03\text{s}$**）<br>・S波の立ち下がり遅延（**$S \text{の最深点まで} \ge 60\text{ms}$**）<br>・S波下行脚にノッチがある（Josephson's sign） | ・鋭く細いr波（$r < 30\text{ms}$）<br>・急峻なS波立ち下がり（$< 60\text{ms}$） |
| | **V6** | ・qR型、QR型、またはQS型 | ・幅広く明瞭な単相性R波（q波なし） |

---

## 4. Vereckei aVRアルゴリズム（Vereckei Criteria）

Andras Vereckeiら（2008年）が開発した、**aVR誘導単独** を用いた簡便かつ迅速な4ステップ診断法です。胸部誘導の電極付け間違いや判読困難例でも高い診断精度を発揮します。

```mermaid
flowchart TD
    V1{"\"Step 1: aVR誘導で初期に<br/>単相性R波 (Initial R") があるか？"} -->|Yes| VT_V1["VT"]
    V1 -->|No| V2{"Step 2: aVR誘導で初期r波または<br/>初期q波の幅が > 40ms か？"}
    
    V2 -->|Yes| VT_V2["VT"]
    V2 -->|No| V3{"\"Step 3: 主に陰性のQRSの下行脚に<br/>ノッチ (Notch on descending limb") があるか？"}
    
    V3 -->|Yes| VT_V3["VT"]
    V3 -->|No| V4{"Step 4: 心室脱分極速度比<br/>vi / vt ≤ 1 か？"}
    
    V4 -->|Yes (vi ≤ vt)| VT_V4["\"VT (初期伝導遅延")"]
    V4 -->|No (vi > vt)| SVT_V["SVT with aberrancy"]
```

> [!NOTE]
> **$v_i / v_t$ 比の原理**
> - **$v_i$（初期電位変化量）**: QRS開始から最初の40ms（1小マス）での縦方向の電位変化（mV）。
> - **$v_t$（終末電位変化量）**: QRS終了点から直前40msでの縦方向の電位変化（mV）。
> - **$v_i / v_t \le 1$**: 初期の伝導が心室固有心筋を介するため遅く、後半に伝導系に乗るためVTを示唆。
> - **$v_i / v_t > 1$**: 刺激伝導系を介して初期脱分極が急速に生じるため変行伝導伴うSVTを示唆。

---

## 5. 特殊な特発性心室頻拍の鑑別

器質的心疾患を伴わない若年者に生じる特発性VT（Idiopathic VT）は、予後良好で特異的な薬物反応性を示します。

| 疾患名 | 起源部位 | 心電図波形特徴 | 特異的治療薬 |
| :--- | :--- | :--- | :--- |
| **右室流出路心室頻拍<br>(RVOT-VT)** | 右室流出路 (中隔側/自由壁) | ・**LBBB様波形**（V1で深いS波）<br>・**下方軸**（II, III, aVFで高電位R波） | ATP (アデノシン), β遮断薬 |
| **特発性左室中隔VT<br>(Belhassen型VT / Fascicular VT)** | 左室後乳頭筋近傍<br>(左脚後枝プルキンエ線維) | ・**RBBB様波形**（V1でrsR'または高電位R）<br>・**左軸偏位**（上方軸: II, III, aVFで陰性）<br>・比較的幅の狭いQRS（0.12〜0.14s） | **ベラパミル（ワソラン®）著効**<br>*(※注: 通常の虚血性VTへのベラパミル投与は血圧虚脱を招くため禁忌)* |

---

## 6. 急性期治療戦略とマネジメント

> [!IMPORTANT]
> **Wide QRS頻拍における臨床原則**
> 1. **血行動態不安定（血圧低下、意識消失、胸痛、急性肺水腫）** ➔ 躊躇なく **同期下カルディオバージョン（電気的除細動: 100〜200J）** を施行。
> 2. **鑑別に迷った場合** ➔ **「VTである」と仮定して治療** を行う（SVTと誤認してベラパミルやジルチアゼムを投与すると、VT患者では心原性ショック・心停止に至るため極めて危険）。

```mermaid
flowchart TD
    WCT_Pt["Wide QRS頻拍患者の来院"] --> Hemodynamics{"\"血行動態は安定しているか？<br/>(意識・血圧・ショック徴候")"}
    
    Hemodynamics -- 不安定 --> SyncDC["\"即時 同期下電気的除細動<br/>(Cardioversion: 100-200J")"]
    Hemodynamics -- 安定 --> Alg["12誘導心電図記録 ➔ Brugada / Vereckei基準で鑑別"]
    
    Alg -->|VTと判定 または 鑑別不能| DrugVT["\"抗不整脈薬静注<br/>(アミオダロン, ニフェカラント, リドカイン, プロカインアミド")"]
    Alg -->|確実なSVT (変行伝導)| DrugSVT["迷走神経刺激 ➔ ATP急速静注 ➔ Ca拮抗薬"]
```

---

## 7. 電子カルテ記載用レポートテンプレート

```text
【心電図所見】
・調律: Wide QRS頻拍 (Heart Rate: 165 bpm, レギュラー)
・QRS幅: 155 ms (著明な拡大)
・電気軸: 極度の右上軸偏位 (Northwest axis: I陰性, aVF陰性, aVR陽性)
・胸部誘導所見: V1-V6 全胸部誘導で陰性一致 (Negative concordance: 全誘導QS型)
・房室関係: II誘導およびV1誘導にてQRSと無関係に出現する独立した解離P波を認める (房室解離: AV dissociation)。
・Brugadaアルゴリズム判定: Step 1陽性 (RSパターン欠如) ➔ 心室頻拍 (VT) と判定。

【総合判定】
単形性持続性心室頻拍 (Monomorphic Ventricular Tachycardia)

【対応・推奨】
血行動態モニター装着、除細動器スタンバイ。血圧低下・意識障害出現時は即時同期下電気的除細動。安定時はアミオダロン静注等の薬物治療および緊急冠動脈精査・基礎心疾患評価を推奨。
```
