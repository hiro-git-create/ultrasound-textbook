---
title: 03 ST部・T波・U波の生理と形態変化
tags: [心電図, ST上昇, ST低下, T波, U波, 冠性T波, 巨大陰性T波, J点, 虚血性心疾患, 心電図検定]
aliases: [ST-T変化, J点, 冠性T波, テント状T波, 巨大陰性T波, 陰性U波]
date_created: 2026-08-17
last_modified: 2026-08-17
reference_guideline: 日本不整脈心電学会 / AHA・ACC・HRS Recommendations for the Standardization and Interpretation of the Electrocardiogram / ESC Fourth Universal Definition of Myocardial Infarction / 心電図検定公式基準
---

# 03 ST部・T波・U波の生理と形態変化

ST部分、T波、U波は、**心室作業心筋の再分極（活動電位の回復過程）**を反映する波形領域です。心室再分極過程は冠動脈虚血、心筋肥大・過負荷、電解質異常（K, Ca, Mg）、中枢神経病変、薬剤影響に対して極めて鋭敏に反応します。ST偏位のミリ単位の計測とT波・U波の微細な形態変化を体系的に読影するスキルは、救急・循環器診療の根幹です。

---

## 1. 心室再分極の生理学と波形の対応

```mermaid
graph TD
    subgraph CellLevel["心室筋細胞活動電位"]
        Phase2["\"Phase 2: プラトー相<br>(Ca2+流入 ≒ K+流出")<br>"細胞間電位差 ≈ 0\""]
        Phase3["\"Phase 3: 急速再分極相<br>(IKr / IKs 流出優位")<br>"外膜側 ➔ 内膜側へ回復\""]
        Phase3End["Phase 3終末〜Purkinje再分極"]
    end
    
    subgraph ECGLevel["体表面心電図"]
        STseg["\"ST部分 (J点〜T波開始")<br>"正常は等電位線 (基線")"]
        Twave["\"T波 (心室再分極波")<br>"QRSと同方向 (Concordant")"]
        Uwave["\"U波 (T波直後の小陽性波")"]
    end
    
    Phase2 --> STseg
    Phase3 --> Twave
    Phase3End --> Uwave
```

---

## 2. J点（J-point）の定義とST偏位の計測法

- **J点（Junction point）**: QRS群の終止点とST部分の開始点の変曲点（つなぎ目）。
- **基準基線（Baseline）**: **PRセグメントの終末部（QRS開始直前）**を基準線（$0\text{ mV}$）とする（心拍数上昇時はTPセグメントも参考）。
- **ST計測点**: 原則として **J点そのもの** で計測。運動負荷試験や頻脈時は **J点から 60〜80 ms 後（J+60ms / J+80ms）** の電位を計測。

```mermaid
graph LR
    QRSend["\"QRS終了点 = J点 (J-point")"] --> STstart["STセグメント"]
    STstart --> Twavestart["T波 立ち上がり"]
    Baseline["\"PRセグメント終末部 (基準線 0mV")"] -.->|"電位差を計測"| QRSend
```

---

## 3. ST上昇（ST Elevation）の形態分類と鑑別

ST上昇を認めた場合、その「上昇形態（コンベックス型、コンケーブ型等）」と「出現誘導の広がり」から原因疾患を即座に鑑別します。

```mermaid
graph TD
    STE["ST上昇の形態分類"]
    STE --> Convex["\"① 上向き凸 (Convex / 弓状 / Tombstone")<br>"🫀 急性心筋梗塞 (STEMI")<br>"局所誘導 + 鏡面像 (Reciprocal")"]
    STE --> Concave["\"② 上向き凹 (Concave / 鞍状")<br>"🔥 急性心膜炎 (広範全誘導 + PR低下")<br>"🌿 早期再分極パターン (良性J波")"]
    STE --> Coved["\"③ Coved型 / Saddle-back型<br>⚡ Brugada症候群 (V1〜V2で≥2mm")"]
    STE --> Persistent["④ 慢性持続性ST上昇<br>🧱 陳旧性心筋梗塞後の左室瘤"]
```

| 形態パターン | 波形特徴 | 鑑別疾患 | 随伴する決定的心電図所見 |
| :--- | :--- | :--- | :--- |
| **上向き凸<br>(Convex型)** | ST部が山なりに盛り上がり、T波と融合（墓石様: Tombstone）。 | **急性ST上昇型心筋梗塞 (STEMI)** | ・責任冠動脈領域に一致した局所誘導のST上昇<br>・対向誘導の**鏡面像（Reciprocal ST低下）** |
| **上向き凹<br>(Concave型)** | ST部がお椀状・鞍状に窪んで立ち上がる。 | **急性心膜炎 (Acute Pericarditis)** | ・aVRとV1を除く**ほぼ全誘導での広範なST上昇**<br>・**PR部分の低下（PR depression）**<br>・鏡面像としてのST低下はなし（aVRを除く） |
| **早期再分極<br>(Early Repol.)** | QRS終末部にJ波（ノッチ/スラー）を伴う凹型ST上昇。 | **良性早期再分極 (BER)**<br>早期再分極症候群 (ERS) | ・若年男性・アスリートに好発<br>・V3〜V5で明瞭、経時変化なし |
| **Coved型 / Saddle-back型** | 下降傾斜する高いST上昇（$\ge 2\text{mm}$）と陰性T波。 | **Brugada症候群** | ・右側胸部誘導（V1〜V3）に限定<br>・高位肋間記録で顕在化 |
| **持続性ST上昇** | 心筋梗塞後数ヶ月以上経過してもST上昇が残存。 | **左室瘤 (LV Aneurysm)** | ・陳旧性梗塞の異常Q波（QS型）を伴う<br>・心エコーで局所奇異運動を確認 |

---

## 4. ST低下（ST Depression）の形態分類と鑑別

ST低下は、心筋内膜側の虚血や心室壁への圧負荷を鋭敏に示します。

```mermaid
graph TD
    STD["ST低下の形態分類"]
    STD --> Downsloping["\"① 下降性 (Downsloping")<br>"虚血重症度高, 左室ストレイン\""]
    STD --> Horizontal["\"② 水平性 (Horizontal")<br>"心筋虚血の典型 (NSTEMI / 労作性狭心症")"]
    STD --> Upsloping["\"③ 上向性 (Upsloping")<br>"頻脈時生理的 (J点低下") vs de Winter"]
    STD --> Scooped["\"④ 盆状 (Scooped / 舟底状")<br>"ジギタリス効果 (Digitalis effect")"]
```

| 形態パターン | 虚血特異度 | 心電図所見と臨床的意義 |
| :--- | :--- | :--- |
| **水平性 ST低下<br>(Horizontal)** | **高 (High)** | J点からST部が水平に $0.1\text{ mV}$（$1\text{ mm}$）以上低下。**労作性狭心症・NSTEMI**の典型的虚血所見。 |
| **下降性 ST低下<br>(Downsloping)** | **極めて高** | STが右下がりに低下し陰性T波へ移行。重症多枝病変虚血、または肥大心の**ストレイン型（Strain pattern）**。 |
| **上向性 ST低下<br>(Upsloping)** | **低 (通常)** | 洞性頻脈等でJ点のみ沈み込み、急角度で基線へ戻る（J-point depression: 生理的）。<br>※ただし **de Winterサイン**（V1-V4で上向性ST低下＋巨大対称性直立T波）はLAD急性完全閉塞を示す緊急STEMI等価物！ |
| **盆状 ST低下<br>(Scooped型)** | 特異的 | サルバドール・ダリの口髭様（Salvador Dalí's mustache）に滑らかに窪む。**ジギタリス（ジゴキシン）内服中**の心電図変化。 |

---

## 5. T波の形態異常と鑑別診断

正常T波は、I, II, V3〜V6で常に直立（陽性）で、**「立ち上がりは緩やかで、後半はやや急に基線に戻る（非対称性: Asymmetric）」**のが特徴です。

```mermaid
graph LR
    subgraph TAbnormal["T波の形態異常"]
        Tent["\"テント状T波<br>(高K血症 / 超急性期MI")"]
        Coronary["\"冠性T波 (左右対称陰性T")<br>"(亜急性期MI / Wellens")"]
        GiantNeg["\"巨大陰性T波 (≥10mm")<br>"(心尖部HCM / くも膜下出血")"]
        Flat["\"平低T波 / 二峰性T波<br>(低K血症 / 心筋炎")"]
    end
```

### (1) テント状T波（Peaked / Tent-like T wave）
- **特徴**: 基部が狭く、針のように鋭利に尖った高い対称性陽性T波。
- **鑑別**:
  - **高カリウム血症（Hyperkalemia）**: 全誘導で出現。K値の上昇に伴い増高（[[01_高カリウム血症_テント状T波から正弦波まで_低K血症]]）。
  - **超急性期心筋梗塞（Hyperacute T wave）**: 局所誘導に出現。基部が幅広く拡大し、数分〜数十分でST上昇へ移行。

### (2) 冠性T波（Coronary T wave: 対称性陰性T波）
- **特徴**: 左右完全対称で深い「矢尻状」の陰性T波（Symmetrical inverted T wave）。
- **臨床的意義**:
  - 急性心筋梗塞の亜急性期（再灌流後）。
  - **Wellens症候群（Type B）**: 前胸部誘導（V2〜V4）で深い対称性陰性T波を呈し、左前下行枝（LAD）近位部の重症狭窄（Imminent MI）を告げる。

### (3) 巨大陰性T波（Giant Negative T wave）
- **定義**: T波の深さが **$1.0\text{ mV}$（$10\text{ mm}$）以上** に達する極度に深い陰性T波。

> [!IMPORTANT]
> **巨大陰性T波の3大鑑別疾患**
> 1. **心尖部肥大型心筋症（Apical HCM / Yamaguchi症候群）**:
>    - 左側胸部誘導（V4〜V6）で巨大陰性T波 ＋ 左室高電位。心エコー・MRIで心尖部の「スペードのエース様」心筋肥厚を認める。
> 2. **頭蓋内病変（くも膜下出血: SAH / 脳出血: CVA T wave）**:
>    - 激しい交感神経嵐（Catecholamine storm）による心筋障害。著明な **QT延長** を伴う広範な巨大陰性T波。
> 3. **たこつぼ心筋症（Takotsubo Cardiomyopathy）**:
>    - 広範な前胸部誘導でのST上昇に続いて出現する巨大陰性T波とQT延長。

---

## 6. U波の生理と臨床的異常

U波はT波の直後（心周期の拡張初期）に出現する小さな低振幅波（通常 $<0.2\text{ mV}$）です。

```mermaid
graph TD
    UwaveTypes["U波の臨床的評価"]
    UwaveTypes --> NormalU["\"正常U波: T波と同極性 (陽性")<br>"振幅はT波の5〜25% (V2〜V4で最大")"]
    UwaveTypes --> ProminentU["\"巨大U波 (Prominent U wave")<br>"⚡ 低カリウム血症 (U波高 > T波高")<br>"T-U融合による偽性QT延長\""]
    UwaveTypes --> InvertedU["\"陰性U波 (Negative U wave")<br>"🚨 重症心筋虚血 (LAD狭窄")<br>"🚨 左室圧過負荷 (重症高血圧 / AS")"]
```

> [!WARNING]
> **「陰性U波」の臨床的重大性**
> 通常U波は陽性波ですが、**下向きに反転した「陰性U波」は極めて特異度の高い病的サイン**です。
> 安静時心電図や運動負荷試験中に胸部誘導（V4〜V6）で陰性U波を認めた場合、**左前下行枝（LAD）の有意狭窄（心筋虚血）**または**重症高血圧による著明な左室拡張末期圧上昇**を強く示唆します。

---

## 関連リンク・ナビゲーション
- 前の項目: [[02_QRS群の波形解析_幅_高さ_移行帯]]
- 次の項目: [[04_QT時間とQTc補正計算式_Bazett_Fridericia_Framingham]]
- 基準値確認: [[00_心電図計測基準値_クイックリファレンス]]
- 関連疾患: [[01_ST上昇型心筋梗塞_STEMI_責任冠動脈枝の同定と誘導局在]], [[02_非ST上昇型心筋梗塞_NSTEMI_不安定狭心症_冠攣縮]], [[01_高カリウム血症_テント状T波から正弦波まで_低K血症]], [[04_急性心膜炎_心筋炎_たこつぼ心筋症_肺塞栓_S1Q3T3]]
