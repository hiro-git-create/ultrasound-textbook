---
title: ST上昇型心筋梗塞 STEMI 責任冠動脈枝の同定と誘導局在
tags: [虚血性心疾患, ACS, 心筋梗塞, STEMI, 責任血管, 冠動脈解剖, LAD, RCA, LCx, 局在診断]
aliases: [ST-Elevation Myocardial Infarction, STEMI, Culprit Artery, 責任冠動脈, ST上昇, 冠動脈解剖]
date_created: 2026-08-17
last_modified: 2026-08-17
reference_guideline: 日本循環器学会(JCS) 急性冠症候群ガイドライン / ESC STEMI Guidelines / 第4次心筋梗塞ユニバーサル定義
---

# ST上昇型心筋梗塞（STEMI）：責任冠動脈枝の同定アルゴリズムと12誘導局在診断

ST上昇型心筋梗塞（ST-Elevation Myocardial Infarction: **STEMI**）は、冠動脈の急性プラーク破綻および血栓性完全閉塞によって心筋の全層性虚血（Transmural Ischemia）が生じる最緊急疾患です。
標準12誘導心電図（および追加の右側胸部誘導・背部誘導）から **「梗塞部位（局在）」** と **「責任冠動脈枝（Culprit Artery: LAD, RCA, LCx）および閉塞レベル（近位部 vs 末梢部）」** を正確に推定することは、緊急カテーテル治療（Primary PCI）における治療戦略決定や合併症予防（心原性ショック、致死性不整脈、房室ブロック、右室梗塞など）に直結します。

---

## 1. STEMIの心電図診断基準（第4次普遍的定義）

J点（QRSとST部分の接合部）における新規のST上昇が、**連続する2つ以上の誘導** で以下を満たす場合にSTEMIと診断します。

| 誘導部位 | 対象患者基準 | ST上昇カットオフ値（J点基準） |
| :--- | :--- | :--- |
| **V2, V3 誘導** | **40歳未満の男性** | **≥ 2.5 mm（0.25 mV）** |
| | **40歳以上の男性** | **≥ 2.0 mm（0.20 mV）** |
| | **すべての年齢の女性** | **≥ 1.5 mm（0.15 mV）** |
| **その他の誘導**<br>(肢誘導, V1, V4-V6) | **全年齢・男女共通** | **≥ 1.0 mm（0.10 mV）** |
| **右側胸部誘導 (V3R, V4R)** | 男女共通（右室梗塞疑い時） | **≥ 0.5 mm（0.05 mV）**（30歳未満男性は ≥ 1.0 mm） |
| **後壁・背部誘導 (V7, V8, V9)** | 男女共通（後壁梗塞疑い時） | **≥ 0.5 mm（0.05 mV）** |

---

## 2. 梗塞局在・心臓壁と対応する誘導・冠動脈対照表

```mermaid
flowchart TD
    Heart["心筋梗塞の局在"] --> Ant["\"前壁・中隔 (V1-V4") ➔ LAD (左前下行枝)"]
    Heart --> Lat["\"高位側壁 (I, aVL") / 側壁 (V5, V6) ➔ LCx (左回旋枝) または Diagonal枝"]
    Heart --> Inf["\"下壁 (II, III, aVF") ➔ RCA (右冠動脈 85%) / LCx (15%)"]
    Heart --> Post["\"後壁 (V7-V9, V1-V3鏡面像") ➔ LCx または RCA末梢 (4PD)"]
    Heart --> RV["\"右室 (V3R, V4R") ➔ RCA近位部閉塞"]
```

| 梗塞部位 | ST上昇誘導 | 責任冠動脈 (Culprit Artery) | 鏡面像 (Reciprocal ST低下) |
| :--- | :---: | :--- | :---: |
| **前壁中隔 (Anteroseptal)** | **V1, V2, V3** | **LAD**（左前下行枝: 中隔枝・対角枝） | なし、または II, III, aVF |
| **広範前壁 (Extensive Anterior)** | **V1〜V6, I, aVL** | **LAD 近位部**（本幹主幹部） | **II, III, aVF** |
| **前側壁 (Anterolateral)** | **V4〜V6, I, aVL** | **LAD**（末梢）または **LCx**（鈍縁枝 OM） | II, III, aVF |
| **高位側壁 (High Lateral)** | **I, aVL** | **LCx** または **LAD 第1対角枝 (D1)** | **II, III, aVF, V1-V2** |
| **下壁 (Inferior)** | **II, III, aVF** | **RCA**（約85%）または **LCx**（約15%） | **I, aVL, V1-V3** |
| **右室梗塞 (Right Ventricular)** | **V3R, V4R**（+ V1） | **RCA 近位部**（右室枝分枝前） | なし |
| **真性後壁 (Posterior)** | **V7, V8, V9**<br>*(V1-V3でR波増高+水平ST低下)* | **LCx** または **RCA**（後下行枝 4PD） | **V1, V2, V3（ミラー像）** |

---

## 3. 責任冠動脈枝（LAD / RCA / LCx）の詳細鑑別アルゴリズム

### 1) 前壁STEMIにおけるLAD閉塞レベルの同定（S1・D1基準）

左前下行枝（LAD）の閉塞部位が第1中隔枝（S1）および第1対角枝（D1）の手前（Proximal）か後（Distal）かによって、救済すべき心筋量とショックリスクが大きく異なります。

```mermaid
flowchart TD
    AntSTEMI["\"前壁STEMI (V1-V4 ST上昇")"] --> CheckS1{"aVR誘導で ST上昇 ≥ 0.5mm<br>かつ aVR ST上昇 ≥ V1 ST上昇？"}
    
    CheckS1 -- Yes --> ProxLAD["\"LAD超近位部閉塞 (S1手前")<br/>・完全右脚ブロック (CRBBB) 合併高頻度<br/>・極めて広範な梗塞・心原性ショックリスク"]
    CheckS1 -- No --> CheckD1{"\"I, aVL誘導で ST上昇<br>かつ 下壁誘導 (II, III, aVF") で ST低下？"}
    
    CheckD1 -- Yes --> MidLAD1["\"LAD近位部閉塞 (D1手前 / S1後")"]
    CheckD1 -- No (下壁ST上昇または変化なし) --> DistLAD["\"LAD末梢部閉塞 (D1・S1後")<br/>・心尖部を回り込む長いLADの場合<br/>下壁誘導でもST上昇することがある (Wrap-around LAD)"]
```

- **S1（第1中隔枝）手前閉塞のサイン**:
  1. **aVR誘導のST上昇**（$\ge 0.5\text{mm}$、かつ $\text{ST}\uparrow_{\text{aVR}} \ge \text{ST}\uparrow_{\text{V1}}$）
  2. 新規の **完全右脚ブロック（CRBBB）** 合併（中隔伝導路の虚血）
  3. V5誘導でのST低下
- **D1（第1対角枝）手前閉塞のサイン**:
  1. **I, aVL誘導のST上昇**（側壁高位の虚血）
  2. **III, aVF誘導の明瞭なReciprocal ST低下**

---

### 2) 下壁STEMIにおける責任血管鑑別（RCA vs LCx）

下壁STEMI（II, III, aVF ST上昇）に遭遇した場合、85%が右冠動脈（RCA）、15%が左回旋枝（LCx）閉塞です。

```mermaid
flowchart TD
    InfSTEMI["\"下壁STEMI (II, III, aVF ST上昇")"] --> Step1{"ST上昇の高さの比較<br/>III誘導のST上昇 > II誘導のST上昇 か？"}
    
    Step1 -- Yes (III > II) --> Step2{"肢誘導ST変化の比較<br/>aVL ST低下 > aVR ST低下 か？"}
    Step2 -- Yes --> RCA["\"責任血管: 右冠動脈 (RCA")"]
    
    Step1 -- No (II ≥ III) --> Step3{"\"側壁誘導 (I, aVL, V5-V6") で<br/>ST上昇を伴うか？"}
    Step3 -- Yes --> LCx["\"責任血管: 左回旋枝 (LCx")"]
    
    Step2 -- No --> CheckLead1{"I誘導の極性: ST低下ならRCA、ST平坦/上昇ならLCx"}
```

| 判定基準項目 | 右冠動脈 (RCA) 閉塞を示唆 | 左回旋枝 (LCx) 閉塞を示唆 |
| :--- | :--- | :--- |
| **ST上昇の優位性** | **Lead III > Lead II** | **Lead II ≥ Lead III** |
| **aVL誘導のST変化** | **著明なST低下（aVL低下 > aVR低下）** | ST変化なし、または **ST上昇** |
| **I誘導のST変化** | **ST低下** | **等電位 または ST上昇** |
| **側壁誘導 (V5-V6)** | ST変化なし、または軽度ST上昇 | **明瞭なST上昇** |
| **右側胸部 (V4R)** | **ST上昇 ≥ 0.5mm（右室梗塞合併）** | ST変化なし |

---

## 4. 見落とし厳禁の特殊なSTEMI病態

### 1) 右室梗塞（Right Ventricular Infarction）
- **病態**: RCA近位部閉塞により下壁とともに右室自由壁が壊死。右室収縮不全により左室への前負荷が激減し、著明な低血圧・ショックをきたす。
- **心電図特徴**:
  - 下壁STEMIに伴い、**V3R, V4Rで ST上昇 ≥ 0.5mm（V4Rが最も高感度）**。
  - V1誘導のST上昇 > V2誘導のST上昇、または V1でST上昇かつV2でST低下。
- **臨床禁忌事項**: **硝酸薬（ニトログリセリン）や利尿薬の投与は絶対禁忌**（前負荷が虚脱し急激な心停止・ショックを誘発するため、急速輸液が第一選択）。

### 2) 真性後壁梗塞（Posterior MI）
- **病態**: 左室後壁（基底部）の全層性虚血。標準12誘導では直接対向する電極がないため、前胸部誘導（V1-V3）に「裏返しの波形」として投影される。
- **標準12誘導での間接所見（ミラー像 / Mirror Image）**:
  1. **V1〜V3誘導の著明な水平性ST低下**
  2. **V1〜V3誘導の高いR波（$R/S > 1$、R波幅 ≥ 0.04s）**
  3. **V1〜V3誘導の直立高尖T波**
- **確定診断**: **背部誘導（V7, V8, V9）を記録し、ST上昇 ≥ 0.5mm を確認**。

---

## 5. 電子カルテ記載用レポートテンプレート

```text
【心電図所見】
・調律: 洞調律 (Heart Rate: 82 bpm)
・ST部所見: 
  - II, III, aVF誘導にて著明なST上昇 (III: 3.5mm, II: 2.0mm, aVF: 3.0mm, III > II)。
  - I, aVL誘導にて顕著な鏡面像ST低下 (Reciprocal ST depression: aVL -2.5mm)。
  - V4R誘導にて 1.5mm のST上昇を認める。
・責任病変推定: 右冠動脈近位部 (proximal RCA, Seg. 1-2) 急性閉塞による急性下壁・右室心筋梗塞 (STEMI)。

【総合判定】
急性ST上昇型心筋梗塞 (Acute Inferior and Right Ventricular STEMI)

【対応・指示】
直ちに冠動脈インターベンション(Primary PCI)チームを招集、カテ室へ緊急搬送。
※右室梗塞合併のため硝酸薬・利尿薬は投与禁止、血圧低下時は細胞外液急速負荷を優先。
```
