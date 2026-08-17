---
title: 02 発作性上室性頻拍 (PSVT) AVNRTとAVRTの鑑別
tags: [心電図, 不整脈, PSVT, AVNRT, AVRT, 上室性頻拍, 迷走神経刺激, アデノシン, カテーテルアブレーション]
aliases: [発作性上室性頻拍, PSVT, AVNRT, AVRT, 房室結節リエントリー性頻拍, 房室回帰性頻拍, Supraventricular Tachycardia]
date_created: 2026-08-17
last_modified: 2026-08-17
reference_guideline: 日本不整脈心電学会 / JCS 2020年 不整脈薬物治療ガイドライン / JCS 2024年 不整脈非薬物治療ガイドライン / AHA・ACC・HRS
---

# 02 発作性上室性頻拍 (PSVT) AVNRTとAVRTの鑑別

発作性上室性頻拍（Paroxysmal Supraventricular Tachycardia: PSVT）は、突然発症・突然停止する規則的な頻拍（心拍数 150〜220 bpm、通常 Narrow QRS）の総称です。その約90%以上を**房室結節リエントリー性頻拍（AVNRT）**と**房室回帰性頻拍（AVRT）**の2大疾患が占めます。両者の電気生理学的機序を理解し、体表心電図から見分けることはカテーテルアブレーション等の治療戦略において決定的に重要です。

---

## 1. AVNRT vs AVRT の電気生理学的メカニズム

```mermaid
graph TD
    subgraph AVNRT ["房室結節リエントリー性頻拍 (AVNRT)"]
        AVN_Node["房室結節内の二重伝導路"]
        AVN_Node --> Slow["\"遅延伝導路 (Slow pathway")<br>"伝導速度: 遅い / 不応期: 短い (順行")"]
        Slow --> Fast["\"高速伝導路 (Fast pathway")<br>"伝導速度: 速い / 不応期: 長い (逆行")"]
        Fast --> Slow
        Fast -.->|ほぼ同時に興奮| Atria_Ventr["\"心房と心室が『同時に』脱分極<br>⇒ P波はQRS内に埋没 または 直後 (RP < 70ms")"]
    end
    
    subgraph AVRT ["房室回帰性頻拍 (AVRT: 順行性)"]
        AV_Circuit["\"房室結節 ＋ 副伝導路 (Kent束")"]
        AV_Circuit --> Node_Down["\"房室結節を順行下降 (Narrow QRS")"]
        Node_Down --> Ventricle["心室全体を脱分極"]
        Ventricle --> Kent_Up["Kent束を逆行上昇"]
        Kent_Up --> Atrium["\"心房を逆行脱分極<br>⇒ P波はQRSから離れて出現 (RP > 70ms")"]
        Atrium --> Node_Down
    end
```

---

## 2. 心電図上の重要鑑別所見：Pseudo r' と Pseudo s

### ① AVNRT（Typical: Slow-Fast型、約90%）の決定的サイン
心房と心室がほぼ同時に興奮するため、逆行性P波はQRS波の終末部にわずかに重なります。
- **V1誘導の Pseudo r'（偽性r'波）**: QRS終末部に小さな上向きの突起（r'波様）が出現。洞調律時の心電図と比較すると、頻拍時のみに認められるのが特徴。
- **下壁誘導（II, III, aVF）の Pseudo s（偽性s波）**: QRS終末部に小さな下向きのくびれ（s波様）が出現。
- **RP'時間**: **$< 70$ ms**（極めて短い）。

```mermaid
graph LR
    AVNRT_ECG["\"AVNRT (Slow-Fast型") の特徴"]
    AVNRT_ECG --> V1["\"V1: 偽性r'波 (Pseudo r'")"]
    AVNRT_ECG --> Inf["\"II, III, aVF: 偽性s波 (Pseudo s")"]
    AVNRT_ECG --> RP["\"RP'時間 < 70ms (QRSとP波が重なる")"]
```

---

### ② AVRT（順行性: Orthodromic AVRT、約95%）の決定的サイン
刺激が「心室全体を興奮させた後にKent束を通って心房に戻る」ため、逆行性P波はQRS波から明確に離れて出現します。
- **ST-T部分の逆行性P波**: QRS終了後、ST部分やT波の初期に明瞭な陰性P波（下壁誘導）を認める。
- **RP'時間**: **$> 70$ ms（通常 100〜150 ms以上）**。
- **ST低下**: 頻拍中に広範な誘導（V4〜V6等）で著名な下降性ST低下を伴いやすい。
- **QRS電気的交互脈（Electrical Alternans）**: 1拍ごとにQRS波の高さが交互に変動する現象（AVRTで高頻度）。

---

## 3. AVNRT vs AVRT 徹底鑑別比較表

| 鑑別項目 | 房室結節リエントリー性頻拍 (AVNRT) | 房室回帰性頻拍 (AVRT: 順行性) |
| :--- | :--- | :--- |
| **リエントリー回路** | 房室結節内部の二重伝導路（マイクロ） | 房室結節 ＋ Kent束 ＋ 心房・心室（マクロ） |
| **RP'間隔** | **超短縮（$< 70$ ms）** | **延長（$> 70$ ms、通常 $> 100$ ms）** |
| **逆行性P波の視認** | **QRS内に埋没、または終末部に微小突出** | **ST部分・T波初期に明瞭に視認可能** |
| **V1誘導の形態** | **Pseudo r'（偽性r'波）陽性** | 通常はPseudo r'なし |
| **下壁誘導の形態** | **Pseudo s（偽性s波）陽性** | 明瞭な陰性P波（逆行性） |
| **ST低下の合併** | 軽度またはなし | **著明なST低下を高頻度に合併** |
| **QRS電気的交互脈** | まれ | **しばしば認める（高心拍時）** |
| **洞調律時の心電図** | 正常 | **WPW症候群のデルタ波**（顕性WPWの場合）[[03_WPW症候群と副伝導路_Kent束局在診断]] |
| **発症年齢** | 中高年・女性に多い | 若年者〜青壮年に多い |

---

## 4. PSVTの急性期停止アルゴリズムと根治治療

```mermaid
flowchart TD
    Detect["\"PSVT発作 (Narrow QRS Regular 頻拍 150-220bpm")"] --> Instab{"\"血行動態不安定？<br>(意識消失, 血圧低下 <90, ショック, 急性肺水腫")"}
    
    Instab -->|Yes (不安定)| SyncDC["\"🚨 同期電気的除細動 (Cardioversion: 50〜100J")"]
    
    Instab -->|No (安定)| Vagal["\"① 迷走神経刺激手技<br>・改変Valsalva手技 (息こらえ後下肢挙上: 成功率40%")<br>"・頸動脈洞マッサージ (禁忌: 血管雑音・プラーク")"]
    
    Vagal --> Success1{"停止した？"}
    Success1 -->|Yes| Done["発作停止・洞調律復帰"]
    Success1 -->|No| ATP["\"② ATP (アデホス") 急速静注 (10〜20mg) ＋ 生食フラッシュ<br>"※気管支喘息には禁忌\""]
    
    ATP --> Success2{"停止した？"}
    Success2 -->|Yes| Done
    Success2 -->|No| CCB["\"③ Ca拮抗薬 (ベラパミル 5mg 静注") または β遮断薬"]
    
    Done --> Cure["\"【根治治療】カテーテルアブレーション (成功率 >95〜98%")<br>"・AVNRT: 遅延伝導路 (Slow pathway") 焼灼<br>"・AVRT: 副伝導路 (Kent束") 焼灼"]
```

> [!TIP]
> **改変Valsalva手技（Modified Valsalva Maneuver）のやり方**
> 半座位で40mmHgの圧で15秒間息こらえ（Valsalva）をさせた直後に、仰臥位に倒して両下肢を45度挙上して15秒維持する手技。従来のValsalva法（成功率17%）に比べ、**成功率が43%以上へ劇的に向上**します。

---

## 5. レポート記載例

### AVNRT（Typical Slow-Fast型）のレポート
```text
【心電図所見】
心拍数 176bpm、規則的な Narrow QRS 頻拍 (QRS幅 80ms)。
V1誘導においてQRS終末部に尖鋭な偽性r'波 (Pseudo r')、II, III, aVF誘導において偽性s波 (Pseudo s) を認める。
RP'間隔は 40ms 未満と極めて短縮しており、P波はQRS終末部にほぼ埋没している。

【診断】
発作性上室性頻拍 (PSVT: 房室結節リエントリー性頻拍 Typical AVNRT)
【コメント】
迷走神経刺激法（改変Valsalva手技）またはATP急速静注による停止を推奨します。頻回再発例にはカテーテルアブレーション（遅延伝導路焼灼）が第一選択の根治治療となります。
```

### AVRT（順行性・Kent束逆行伝導）のレポート
```text
【心電図所見】
心拍数 190bpm、規則的な Narrow QRS 頻拍。
QRS終了後 120ms (RP'間隔 120ms > 70ms) のST部分に明瞭な逆行性陰性P波（II, aVF誘導）を認める。
V4-V6誘導にて 2mmの下降性ST低下、およびQRS電気的交互脈 (Electrical alternans) を伴う。

【診断】
発作性上室性頻拍 (PSVT: 房室回帰性頻拍 順行性AVRT)
【コメント】
副伝導路（Kent束）を介するマクロリエントリー頻拍です。洞調律復帰後にデルタ波の有無（WPW症候群）を確認し、電気生理検査・カテーテルアブレーションをご検討ください。
```

---

## 関連リンク（Obsidian WikiLinks）
- [[03_WPW症候群と副伝導路_Kent束局在診断]] - Kent束の局在とWPW症候群
- [[01_上室期外収縮_PAC_と変行伝導]] - PSVTの誘発契機となるPAC
- [[04_心房細動_AF_と心房粗動_AFL_心房頻拍_AT]] - その他の上室性頻脈性不整脈
- [[02_心室頻拍_VT_単形性_多形性_鑑別診断_Brugada基準]] - Wide QRS頻拍との鑑別
