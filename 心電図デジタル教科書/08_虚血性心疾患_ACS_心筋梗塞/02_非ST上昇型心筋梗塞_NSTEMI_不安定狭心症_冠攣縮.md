---
title: 非ST上昇型心筋梗塞 NSTEMI 不安定狭心症 冠攣縮
tags: [虚血性心疾患, ACS, NSTEMI, 不安定狭心症, 冠攣縮性狭心症, Wellens症候群, de_Winterサイン, 心電図検定]
aliases: [Non-ST-Elevation Myocardial Infarction, NSTEMI, Unstable Angina, UA, Vasospastic Angina, Wellens Syndrome, de Winter sign]
date_created: 2026-08-17
last_modified: 2026-08-17
reference_guideline: 日本循環器学会(JCS) 急性冠症候群ガイドライン / ESC NSTE-ACS Guidelines / AHA・ACC非ST上昇型ACSガイドライン
---

# 非ST上昇型ACS（NSTEMI / 不安定狭心症）・冠攣縮・STEMI等価物（Wellens・de Winter）

非ST上昇型急性冠症候群（Non-ST-Elevation Acute Coronary Syndrome: **NSTE-ACS**）は、冠動脈の不完全閉塞や側副血行路を介した不完全な血流低下により生じる **心内膜下虚血（Subendocardial Ischemia）** を病態とし、心筋バイオマーカー（トロポニン）上昇を伴う **NSTEMI** と、バイオマーカー陰性の **不安定狭心症（Unstable Angina: UA）** に大別されます。
また、一見すると明らかなST上昇を呈さないものの、冠動脈主幹部やLAD近位部の急性完全閉塞を示す **STEMI等価物（STEMI Equivalents: Wellens症候群、de Winterサイン、広範ST低下+aVR上昇）** を瞬時に見抜くことが極めて重要です。

---

## 1. NSTE-ACSの基本的虚血性心電図所見

心内膜下虚血では、心室壁の深部（内膜側）のみに再分極遅延と電位差が生じるため、心電図上は **ST低下** または **T波陰転化** として表れます。

```mermaid
flowchart TD
    Ischemia["\"心内膜下虚血 (Subendocardial Ischemia")"] --> Pattern1["\"① 水平成 ST低下 (Horizontal ST Depression")"]
    Ischemia --> Pattern2["\"② 下降性 ST低下 (Downsloping ST Depression")"]
    Ischemia --> Pattern3["\"③ 陰性T波 / 冠性T波 (T-Wave Inversion")"]
    Ischemia --> Pattern4["\"④ 一過性ST-T変化 (胸痛発作時のみ出現・寛解時に正常化")"]
```

### 1) ST低下の形態分類と虚血特異性
- **水平成ST低下（Horizontal）**: J点からST部が水平に走行。**心筋虚血の特異度が最も高い**（≥ 0.05 mV = 0.5mm で有意）。
- **下降性ST低下（Downsloping）**: ST部が右下がりに傾斜。心筋虚血や左室肥大・ストレインパターンで高頻度（高リスク）。
- **上行性ST低下（Upsloping）**: J点は低下しているが急峻に基線へ向かって右上がりに立ち上がる。頻脈や自律神経緊張でも見られるため、虚血診断基準は厳格（J点より80ms後のST点が ≥ 0.15 mV低下している場合のみ虚血考慮）。

| ST変化パターン | 虚血特異性 | 診断基準 (連続する2誘導以上) |
| :--- | :---: | :--- |
| **水平成 ST低下** | **極めて高い (★★★★★)** | **J点低下 ≥ 0.05 mV (0.5 mm)** |
| **下降性 ST低下** | **高い (★★★★☆)** | **J点低下 ≥ 0.05 mV (0.5 mm)** |
| **冠性T波 (対称性深い陰性T)** | **高い (★★★★☆)** | **陰性T波の深さ ≥ 0.1 mV (1 mm)** |
| **上行性 ST低下** | 低い〜中等度 (★★☆☆☆) | J点後80msで ≥ 0.15 mV低下 |

---

## 2. 見落とし厳禁のSTEMI等価物（High-Risk ECG Patterns）

通常の自動解析心電図で「ST上昇なし」「非特異的ST変化」と誤読されやすいものの、**左前下行枝（LAD）近位部や左冠動脈主幹部（LMCA）の致命的急性閉塞・重症病変** を示す3大クリティカルパターンです。

### 1) Wellens症候群（Wellens' Syndrome / LAD近位部重症狭窄）
- **病態**: LAD近位部の90〜99%重症狭窄。急性心筋梗塞の前駆状態（Impending Anterior Wall MI）。
- **特徴的臨床経過**: **「胸痛が寛解・消失した無痛期」** に12誘導心電図に特徴的T波変化が出現する（胸痛発作中は正常化または軽微なST上昇）。
- **心電図パターン**:
  - **Type A（約25%）**: **V2, V3（〜V4）誘導における二相性T波（Biphasic T-wave: 陽性から急峻に陰性へ移行）**。
  - **Type B（約75%）**: **V2, V3（〜V5）誘導における深く左右対称な陰性T波（Deep, symmetric inverted T-waves: -5mm以上にも及ぶ）**。
  - 異常Q波は存在せず、ST上昇はあっても1mm未満。
- **対応方針**: **緊急心臓カテーテル検査（CAG）の絶対適応**。**運動負荷心電図検査は広範な心筋梗塞を誘発するため絶対禁忌**。

```mermaid
flowchart LR
    A["\"胸痛発作中: 一過性狭窄 (心電図は正常〜軽微ST変化")"] --> B["胸痛消失・再開通: Wellensパターン出現"]
    B --> C["\"Type A: V2-V3 二相性T波 (+/-")"]
    B --> D["Type B: V2-V3 深い対称性陰性T波"]
    C & D --> E["数日〜数週以内に広範前壁STEMI発症の最高リスク ➔ 緊急CAG"]
```

---

### 2) de Winterサイン（de Winter T-Wave Pattern / 急性LAD完全閉塞の2%）
- **病態**: LAD近位部の急性完全閉塞であるにもかかわらず、典型的なST上昇を呈さないSTEMI等価物。
- **心電図特徴**:
  1. **V1〜V6（特にV2-V4）誘導におけるJ点の 1〜3 mm のST低下**
  2. **上行性ST低下に続いて急峻に立ち上がる、背が高く左右対称な増高T波（Tall, prominent, symmetric T-waves）**
  3. **aVR誘導における 0.5〜1.0 mm のST上昇（Reciprocal ST elevation）**
  4. QRS幅は正常または軽度延長、明らかな異常Q波は伴わない。
- **対応方針**: **通常のSTEMIと全く同様に、直ちに緊急Primary PCI（カテ室直行）** を施行。

---

### 3) 広範ST低下 ＋ aVR誘導のST上昇（LMCA閉塞・3枝病変）
- **病態**: 左冠動脈主幹部（Left Main Coronary Artery: LMCA）閉塞、または重症3枝病変による左室全体の広範な心内膜下虚血（Global Subendocardial Ischemia）。
- **心電図特徴**:
  1. **6誘導以上（特に I, II, aVL, V4-V6）にわたるびまん性の著明な水平成/下降性ST低下**
  2. **aVR誘導における ST上昇（≥ 0.5〜1.0 mm）**
  3. **$\text{ST}\uparrow_{\text{aVR}} \ge \text{ST}\uparrow_{\text{V1}}$**（aVRのST上昇がV1のST上昇を上回る）。
- **臨床的意義**: 心原性ショックや心停止への急速進行リスクが極めて高く、緊急血行再建（PCIまたは緊急CABG）が必要。

---

## 3. 冠攣縮性狭心症（Vasospastic Angina: VSA / 異型狭心症）

```mermaid
flowchart TD
    VSA["\"冠動脈平滑筋の局所的一過性攣縮 (Spasm")"] --> Complete["\"一過性の全層性虚血 (Transmural")"]
    Complete --> ECG["【発作中】責任領域の一過性ST上昇 + 対向性ST低下"]
    ECG --> Relieve["ニトログリセリン舌下投与 / Ca拮抗薬"]
    Relieve --> Back["\"【発作寛解後】ST上昇は完全に基線復帰 (陰性T波が残存することあり")"]
```

- **病態**: 動脈硬化病変の有無に関わらず、冠動脈平滑筋の過剰な収縮（スパスム）により一過性に血流が途絶する。
- **臨床特徴**: **夜間・早朝の安静時胸痛**、喫煙・飲酒・寒冷・ストレスが誘因。
- **心電図特徴**:
  - **発作中**: 狭窄部位に一致した **一過性の明瞭なST上昇**（時に巨大単相性曲線）。
  - **発作寛解後**: ST上昇は数分〜数十分で速やかに消失・正常化。
  - **治療**: 発作時ニトログリセリン、予防として **Ca拮抗薬（ジルチアゼム、ベニジピン等）**、禁煙徹底。※β遮断薬単独投与はα受容体優位による攣縮悪化リスクのため原則禁忌。

---

## 4. NSTE-ACSと鑑別疾患のまとめ

| 病態・疾患名 | 代表的心電図所見 | 冠動脈病態 | 緊急度・治療 |
| :--- | :--- | :--- | :--- |
| **NSTEMI / 不安定狭心症** | 水平成ST低下、冠性陰性T波 | 不完全閉塞、プラーク不安定化 | 早期CAG、抗血小板・抗凝固療法 |
| **Wellens症候群 (Type A/B)** | V2-V3 二相性T波 / 深い陰性T波 | LAD近位部 90-99%狭窄 | **準緊急CAG（負荷試験絶対禁忌）** |
| **de Winterサイン** | V1-V6 上行ST低下 + 高尖T波、aVR ST上昇 | LAD近位部 急性完全閉塞 | **最緊急 Primary PCI（STEMI同等）** |
| **広範ST低下 + aVR上昇** | 6誘導以上のST低下 + aVR ST上昇 | 主幹部(LMCA) / 3枝重症病変 | **最緊急 CAG/PCI/CABG** |
| **冠攣縮性狭心症 (VSA)** | 発作時の一過性ST上昇 ➔ 寛解時正常化 | 冠動脈平滑筋スパスム | Ca拮抗薬、ニトロ、禁煙 |

---

## 5. 電子カルテ記載用レポートテンプレート

```text
【心電図所見】
・調律: 洞調律 (Heart Rate: 64 bpm)
・QRS波: 幅 85 ms、明らかな異常Q波なし。
・ST-T所見: 
  - V2, V3誘導にて深い左右対称性の陰性T波 (T波深さ: -6.5mm) を認める。
  - V4誘導にて平低T波〜軽度陰性T波。
  - ST部分の明らかな上昇なし (Wellens症候群 Type Bパターン)。
・臨床文脈: 直前までの胸痛が軽快・消失したタイミングで記録された波形。

【総合判定】
Wellens症候群 Type B（左前下行枝近位部重症狭窄の疑い、Impending AMI）

【対応・推奨】
前壁心筋梗塞発症の極めて高いハイリスク病態です。運動負荷試験は絶対禁忌とし、直ちに冠動脈カテーテル検査(CAG)による血行再建を検討してください。
```
