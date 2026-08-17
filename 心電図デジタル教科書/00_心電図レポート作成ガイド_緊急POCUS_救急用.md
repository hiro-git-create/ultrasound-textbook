---
title: 心電図レポート作成ガイド 緊急POCUS・救急用
tags: [心電図, 救急, 当直, POCUS, ACS, 緊急レポート, STEMI]
aliases: [ECG Emergency Report, 救急心電図レポート]
date_created: 2026-08-17
last_modified: 2026-08-17
---

# 🚨 緊急POCUS・救急・当直用 心電図速攻レポート

当直帯・救急外来（ER）・集中治療室（ICU）において、ショック、急性胸痛、意識障害、致死的不整脈を数秒〜1分以内で判定し、緊急カテ隊コールや循環器オンコールへ伝達するための速攻レポートテンプレートです。

---

## 1. 緊急コール用 30秒要約フォーマット（SBAR形式）

```text
【緊急心電図アラート / ER SBAR】
■ Situation (状況): [ 急性胸痛 / 心原性ショック / 失神・意識障害 ]
■ Background (背景): [ 年齢・性別 / 基礎疾患 / 心電図記録時刻:   :   ]
■ Assessment (心電図評価):
  1. 調律: [ 洞調律 / VT / VF / Complete AVB / Rapid AF ]
  2. ST-T変化: 
     - [  ] STEMI疑い: [ 誘導: V1-V4(前壁) / II,III,aVF(下壁) / I,aVL,V5-V6(側壁) ]
     - [  ] Reciprocal change: [ 誘導:                    ]
     - [  ] STEMI等価物: [ Wellens sign / de Winter / aVR ST上昇+広範ST低下 / Sgarbossa陽性CLBBB ]
  3. 緊急電解質・中毒徴候: [ テント状T波(高K) / QTc延長(>500ms) / Brugada Type1 ]
■ Recommendation (要請・方針):
  - [ 緊急心臓カテーテル検査 (Primary PCI) 招集要請 ]
  - [ 除細動 (DC 200J) / ペーシング / 硫酸Mg静注 / グルコン酸カルシウム投与 ]
```

---

## 2. 疾患別 緊急速攻レポートテンプレート

### ① 急性心筋梗塞（STEMI）
```text
【緊急心電図所見: 急性ST上昇型心筋梗塞 (STEMI)】
・記録時刻: 202X/XX/XX XX:XX
・所見: 
  - [ II, III, aVF ] で J点より [ 2.5 ] mm のST上昇あり。
  - [ I, aVL ] で鏡面像 (Reciprocal ST低下) を認める。
  - 右側胸部誘導(V4R)でST上昇あり (右室梗塞合併)。
・推定責任病変: 右冠動脈 (RCA #1-#2)
・対応: Primary PCI適応。循環器当直コール、アスピリン・P2Y12阻害薬投与準備。
```

### ② 致死的不整脈・Wide QRS頻拍（VT vs SVT with aberrancy）
```text
【緊急心電図所見: Wide QRS頻脈 (Wide Complex Tachycardia)】
・心拍数: 180bpm、QRS幅: 160ms (広大)。
・判定基準: 
  - 房室解離 (AV dissociation) 陽性 / Fusion beatあり
  - Brugadaアルゴリズム: 全胸部誘導でRSパターンなし (Concordance)
・診断: 単形性心室頻拍 (Monomorphic VT)
・対応: 血行動態不安定 (ショック) → 直ちに同期下カルディオバージョン (100J) 施行準備。
```

### ③ 完全房室ブロック・徐脈性ショック
```text
【緊急心電図所見: 完全房室ブロック (3度AVB)】
・所見: P波レート 80bpm、QRSレート 32bpm。PP間隔とRR間隔が完全に解離。
・補充調律: Wide QRS (心室性補充調律)
・症状: 血圧 78/45 mmHg、ふらつき・意識障害あり。
・対応: 経皮ペーシング (TCP) 装着開始、アトロピン 0.5mg静注、イソプロテレノール準備、緊急一時的ペーシングリード挿入依頼。
```

---

## 3. 緊急アラートサイン・見落とし厳禁一覧

```mermaid
graph TD
    ChestPain["急性胸痛 / ショック"] --> STCheck{"ST上昇あるか?"}
    STCheck -- YES --> STEMI["\"典型STEMI<br>(直ちにカテ隊コール")"]
    STCheck -- NO --> Equivalent{"STEMI等価物チェック"}
    Equivalent -- "aVR上昇 + 広範ST低下" --> LMT["\"主幹部(LMT") / 3枝病変"]
    Equivalent -- "V1-V3 上向き凹ST + 対称性高尖T" --> deWinter["\"de Winterサイン (LAD近位部完全閉塞")"]
    Equivalent -- "胸痛消失時のV2-V3 二相性/深大陰性T" --> Wellens["\"Wellens症候群 (LAD重症狭窄")"]
    Equivalent -- "LBBB存在下のST変化" --> Sgarbossa["\"Sgarbossa基準陽性 (LBBB+AMI")"]
```
