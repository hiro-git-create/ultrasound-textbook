---
title: 01 上室期外収縮 (PAC) と変行伝導
tags: [心電図, 不整脈, PAC, 上室期外収縮, 変行伝導, Ashman現象, 心室期外収縮鑑別]
aliases: [上室期外収縮, 心房期外収縮, PAC, APC, SVPC, 変行伝導, 室内変行伝導, Ashman現象]
date_created: 2026-08-17
last_modified: 2026-08-17
reference_guideline: 日本不整脈心電学会 / JCS / AHA・ACC・HRS Recommendations for the Standardization and Interpretation of the Electrocardiogram
---

# 01 上室期外収縮 (PAC) と変行伝導

上室期外収縮（Premature Atrial Contraction: PAC / 心房期外収縮: APC）は、洞結節以外の心房組織または房室接合部から発生する早期の異所性興奮です。日常臨床で最も頻繁に遭遇する良性不整脈ですが、心室内の不応期にぶつかることで**「変行伝導（Aberrant Conduction）」**をきたして心室期外収縮（PVC）と酷似したWide QRSを呈したり、**「非伝導性PAC（Blocked PAC）」**となって洞停止や房室ブロックと誤認されるなど、高度な鑑別診断技術を要します。

---

## 1. 上室期外収縮（PAC）の成因と心電図基本特徴

```mermaid
graph TD
    SA["\"洞結節 (SA node")"] 
    Atrium_Focus["\"心房異所性焦点 (Ectopic Focus")<br>"・自動能亢進 / マイクロリエントリー\""]
    
    Atrium_Focus -->|洞性周期より早期に出現| Pprime["\"異所性P'波 (先行P'波")<br>"洞性P波と異なる形状・極性\""]
    
    Pprime --> AVN["\"房室結節 (AV node")"]
    AVN --> HisPurkinje["\"ヒス-プルキンエ系 (正常伝導")"]
    HisPurkinje --> NarrowQRS["\"通常の狭いQRS群 (Narrow QRS")"]
    
    Pprime --> Reset["洞結節へ逆行・リセット"]
    Reset --> IncompletePause["\"【非代償性休止期】<br>(先行PP + 後続PP < 洞性PP × 2")"]
```

### PACの心電図判定基準
1. **予定された洞性拍動より早期に出現**する。
2. **異所性P'波（先行P'波）**:
   - 洞性P波と極性・形態が異なる（下部心房起源ではII, III, aVFで陰性P'波）。
   - 先行するT波の終末部に重なり、T波の変形・尖鋭化として視認されることが多い。
3. **QRS波の形態**: 通常は洞調律時と同一の正常幅（Narrow QRS $< 0.10$秒）。
4. **非代償性休止期（Incomplete Compensatory Pause）**:
   - 異所性興奮が洞結節を逆行性にリセットするため、**期外収縮を挟む2周期（$P-P' + P'-P$）の長さが、正常洞性周期の2倍より短く**なります。

---

## 2. 非伝導性上室期外収縮（Blocked PAC）

PACの発生タイミングが極めて早期である場合、房室結節がまだ前拍の**絶対不応期**にあるため、刺激が心室へ伝導できず**「P'波のみが出現し、後続のQRS波が完全に脱落」**します。

```mermaid
graph LR
    Early_PAC["超早期の異所性P'波"] --> Refractory["房室結節の不応期に衝突"]
    Refractory --> Block["心室へ伝導せずブロック"]
    Block --> ECG["\"【心電図所見】<br>T波の頂部に小さな結節(P'波") ＋ QRS脱落による突然の休止期"]
```

> [!WARNING]
> **洞停止や2度房室ブロックとの誤診に注意！**
> QRSが突然脱落した休止期を見た際、**「直前のT波の形」を注意深く観察**してください。正常なT波と比べて形が尖っていたり、くびれ（ノッチ）がある場合は、T波の中に隠れた**Blocked PAC（非伝導性PAC）**です。洞停止やMobitz II型房室ブロックと誤診して不要なペースメーカ適応と判断しないよう極めて重要です。

---

## 3. 心室内変行伝導（Aberrant Conduction）とAshman現象

PACが房室結節を通過して心室へ到達した際、**脚の一方（多くは右脚）がまだ「相対不応期」から回復していない場合**、刺激は回復している脚側（左脚）のみを通過します。その結果、**脚ブロックパターン（多くは完全右脚ブロック様）の幅広いQRS波（Wide QRS）** となります。

```mermaid
graph TD
    PAC["早期の上室性刺激"] --> AVN["房室結節を通過"]
    AVN --> Bundles{"脚の不応期の差"}
    Bundles -->|右脚: 不応期が長い| RBB_Ref["\"右脚はまだ不応期 (ブロック")"]
    Bundles -->|左脚: 不応期が短い| LBB_OK["\"左脚は回復 (伝導可能")"]
    
    RBB_Ref & LBB_OK --> Result["【右脚ブロック型変行伝導】<br>V1で rsR' / Wide QRS波の形成"]
```

### Ashman現象（アッシュマン現象）
- **生理学的原理**: 心室（特に脚）の不応期の長さは、**「その直前の心周期（RR間隔）の長さに比例」**します。
  - 直前のRR間隔が**長い** $\rightarrow$ 脚の不応期が**長くなる**。
  - 直前のRR間隔が**短い** $\rightarrow$ 脚の不応期が**短くなる**。
- **発生パターン**: **「Long-Short周期」**（長いRR間隔の直後に、短い連結期で拍動が入り込む）の時に、右脚の不応期が延長しているため最も容易に変行伝導（Wide QRS）が発生します。心房細動（AF）中に頻発します。

---

## 4. PAC変行伝導 vs 心室期外収縮（PVC）の徹底鑑別表

```mermaid
flowchart TD
    WideQRS["早期に出現した Wide QRS 波"] --> CheckP{"先行する異所性P'波あり？"}
    
    CheckP -->|明確なP'波あり| Aberration["\"上室期外収縮の変行伝導 (Aberration")"]
    CheckP -->|P'波なし / T波変形なし| CheckV1{"V1誘導の波形形態"}
    
    CheckV1 -->|典型的な rsR' (右耳が高い)| Aberration
    CheckV1 -->|単相性R, qR, または 左耳が高い| PVC["\"心室期外収縮 (PVC")"]
    
    CheckV1 --> CheckPause{"休止期の長さ"}
    CheckPause -->|非代償性休止期 (リセット)| Aberration
    CheckPause -->|完全代償性休止期 (2倍)| PVC
```

| 鑑別項目 | 上室期外収縮の変行伝導 (Aberration) | 心室期外収縮 (PVC) |
| :--- | :--- | :--- |
| **先行P'波** | **あり**（直前のT波に重なるP'波） | **なし**（逆行性P波がQRS後に出ることはある） |
| **QRS初期ベクトル** | **正常洞調律と同一**（最初の0.02〜0.04秒が細い） | **正常洞調律と全く異なる**（立ち上がりから太い） |
| **V1誘導形態** | **典型的な rsR'、rSR'**（ウサギの耳）<br>※右耳（R'）が左耳（r）より高い | **単相性R波、qR波、または二峰性で左耳が高い**（Marriottサイン陽性） |
| **V6誘導形態** | 小さなq波 ＋ 幅広い終末部S波（qRs） | 幅広い単相性S波、QS波、またはq波なし |
| **休止期の性質** | **非代償性休止期**（洞結節がリセット） | **完全代償性休止期**（洞性周期の正確に2倍） |
| **先行RR間隔** | **Ashman現象**（Long-Short周期）で出やすい | 一定の連結期（Fixed coupling）で出やすい |

---

## 5. レポート記載例

### 一般的な上室期外収縮（PAC）
```text
【心電図所見】
洞調律 66bpm。
第3拍目および第7拍目に、早期に出現する異所性P'波（下壁誘導で二峰性）および後続の正常Narrow QRS波を認める。
期外収縮後は非代償性休止期を形成。

【診断】
上室期外収縮 (Premature Atrial Contraction: PAC / 散発性)
【コメント】
自覚症状が軽微であれば病的意義は乏しく、経過観察で問題ありません。
```

### 非伝導性PAC（Blocked PAC）
```text
【心電図所見】
洞調律 60bpm。
第4拍目のT波頂部に早期の異所性P'波の重なり（T波変形）を認め、後続のQRS波が脱落して 1.8秒間の休止期を認める。

【診断】
非伝導性上室期外収縮 (Blocked PAC / Non-conducted PAC)
【コメント】
洞停止や2度房室ブロックではなく、早期PACの房室結節不応期衝突による良性のQRS脱落です。ペースメーカ植込み等の適応外です。
```

---

## 関連リンク（Obsidian WikiLinks）
- [[01_完全右脚ブロック_CRBBB_と不完全右脚ブロック_IRBBB]] - 右脚ブロックの波形特徴
- [[02_発作性上室性頻拍_PSVT_AVNRTとAVRTの鑑別]] - PACから誘発される頻拍
- [[04_心房細動_AF_と心房粗動_AFL_心房頻拍_AT]] - Ashman現象とAF
- [[01_心室期外収縮_PVC_Lown分類と重症度判定]] - PVCの診断とLown分類
