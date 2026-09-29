---
title: 心エコー DICOM SR連携 推奨項目マスターリファレンス (完全版)
tags: [心エコー, DICOM_SR, 構造化レポート, 拡張能, LARS, 弁膜逆流定量, Qp_Qs, PVR, dP_dt, RV_PAカップリング, 生理検査連携, 医療IT]
aliases: [心エコーSR連携完全版, DICOM_SR連携マスター, エコーレポート自動化, QpQs, PVR, 全弁逆流]
date_created: 2026-09-29
last_modified: 2026-09-29
reference_guideline: ASE 2025新基準 / EACVI / 日本心エコー図学会 (JSE)
---

# 🫀 心エコー検査 DICOM SR連携 推奨項目マスターリファレンス (完全版)
― 全弁逆流定量（AR/MR/TR/PR）・シャント率（Qp/Qs）・血行動態（PVR, dP/dt, RV-PA）・LARS対応 生理検査レポート自動化仕様書 ―

> [!NOTE] 概要と目的
> 超音波診断装置で測定した数値をDICOM SR（Structured Report: 構造化レポート）としてレポートシステム・電子カルテへ自動転送することにより、
> ① 転記ミスの完全撲滅、② 検査時間の大幅短縮、③ **4弁すべての逆流症定量（PISA/VC/EROA/RVol/PHT）**、
> ④ **シャント率（Qp/Qs）・肺血管抵抗（PVR）・左室収縮性（dP/dt）・右室肺動脈カップリング（TAPSE/PASP）**、
> ⑤ 最新ASE 2025拡張能新基準（LARS・E/e'等）の完全自動判定を実現します。

---

## 1. 🫀 左室形態・収縮能 ＆ 特殊血行動態指標（dP/dt）

| 計測区分 | SR連携推奨項目 | 英語表記 / DICOMタグ | 単位 | 臨床的意義・システム自動演算 |
| :--- | :--- | :--- | :---: | :--- |
| **Mモード / 2D** | 左室拡張末期径 / 収縮末期径 | `LVDd / LVDs` | mm | 左室径・容量負荷評価・BSA補正値算出 |
| **Mモード / 2D** | 心室中隔壁厚 / 後壁厚 | `IVSTd / PWTd` | mm | 壁肥厚・HCM・求心性肥大の評価 |
| **自動演算** | **左室心筋重量係数** | `LVMI` (LV Mass Index) | g/m² | 左室肥大 (LVH) 確定診断 (男>115, 女>95) |
| **自動演算** | 相対的壁厚 / 左室短縮率 | `RWT / FS` | -, % | 求心性vs遠心性肥大分類 (RWT>0.42), 円周収縮能 |
| **Simpson法** | 左室拡張末期 / 収縮末期容積 | `LVEDV / LVESV` | mL | 容量負荷評価・BSA補正 (EDVI, ESVI) |
| **Simpson法** | **左室駆出率 (最重要)** | `LVEF` (Biplane EF) | % | 心機能分類 (HFrEF / HFmrEF / HFpEF) |
| **Simpson法** | 1回拍出量 / 心拍出量 / SVi | `SV / CO / SVi` | mL, L/min, mL/m² | 有効拍出量・心係数 (CI)・低流量判定 (<35 mL/m²) |
| **MR連続波 CW** | **左室収縮期圧上昇率 (dP/dt)** | `LV dP/dt` | mmHg/s | MR波形1-3m/s時間より算出。正常>1200, 低下<1000 |

---

## 2. 🌊 左室拡張能評価（ASE 2025新基準 / LARS・E/e'・LAVI・TR）

> [!IMPORTANT]
> ### ASE 2025改訂アルゴリズム & LARS
> ① **平均 E/e' > 14**
> ② **中隔側 e' < 7 cm/s または 側壁側 e' < 10 cm/s**
> ③ **TR Vmax > 2.8 m/s**
> ④ **LAVI > 34 mL/m²**
> ★ **【新指標 LARS（左房リザーバーストレイン）】**: **LARS < 18%**（重度低下）または **< 24%**（軽度低下）で左室充満圧（LAP/PCWP）上昇確定。LAVIが正常な早期HFpEFやグレーゾーン症例を決着させる最新キーマーカー。
> ※ AF（心房細動）症例では通常判定から **「E/e' ≧ 11」 単独判定ロジック** へ自動切り替え。

| 検査手技 | SR連携推奨項目 | 英語表記 / DICOMタグ | 単位 | 判定基準・自動連携メリット |
| :--- | :--- | :--- | :---: | :--- |
| **左房ストレイン** | **左房リザーバーストレイン (新基準)** | `LARS` (LA Res. Strain) | % | 充満圧上昇確定 (重度低下 <18%, 軽度低下 <24%, 正常 >39%) |
| **左房ストレイン** | 左房コンジット / ポンプストレイン | `LACS / LAAS` | % | 受動的導管機能 / 心房能動的収縮機能の評価 |
| **TVI (流入血流)** | E波最高血流速度 / A波最高血流速度 | `MV E vel / MV A vel` | cm/s | 拡張早期 / 心房収縮期流入速度 (AF時はA波欠損) |
| **自動演算** | **E/A比 / E波減速時間 (DT)** | `E/A ratio / MV DT` | -, ms | 弛緩障害型 (<0.8), 拘束型 (>2.0, DT<160ms) |
| **組織ドプラ TDI** | **中隔側 / 側壁側 e' 速度** | `Septal e' / Lateral e'` | cm/s | 局所弛緩能低下 (中隔 < 7.0, 側壁 < 10.0 cm/s) |
| **自動演算** | **平均 E/e' 比 (最重要)** | `Average E/e'` | - | 左房圧・充満圧指標 (> 14 で上昇, AF時は ≧ 11) |
| **Biplane容積** | **左房容積係数 (最重要)** | `LAVI` | mL/m² | 慢性左房圧上昇 (> 34 mL/m² で拡大陽性) |
| **連続波ドプラ CW** | **三尖弁逆流最高流速** | `TR Vmax` | m/s | 肺動脈圧上昇スクリーニング (> 2.8 m/s で陽性) |
| **肺静脈血流 PW** | S/D比 ＆ Ar-A持続時間差 | `PV S/D / (Ar dur - A dur)` | -, ms | S < D: 左房圧上昇 / Ar-A ≧ 30ms: LVEDP上昇 |

---

## 3. 🎯 全弁膜逆流症の完全定量・半定量評価（AR / MR / TR / PR）

| 対象弁 | SR連携推奨項目 | 英語表記 / DICOMタグ | 単位 | 重症度判定カットオフ値 (ASE/ESC基準) |
| :--- | :--- | :--- | :---: | :--- |
| **大動脈弁逆流 AR** | **Vena Contracta 幅 (VC)** | `AR VC width` | mm | 重症: > 6.0 mm (軽症: < 3.0 mm) |
| **大動脈弁逆流 AR** | 圧半減時間 (PHT) | `AR PHT` | ms | 重症: < 200 ms (軽症: > 500 ms) |
| **大動脈弁逆流 AR** | **有効逆流弁口面積 (EROA)** | `AR EROA` | cm² | 重症: ≧ 0.30 cm² (軽症: < 0.10 cm²) |
| **大動脈弁逆流 AR** | **逆流量 (Regurgitant Volume)** | `AR RVol` | mL | 重症: ≧ 60 mL (軽症: < 30 mL) |
| **大動脈弁逆流 AR** | 下行大動脈拡張期逆流終末速度 | `AR Holodiastolic flow (EDV)` | cm/s | 重症: 下行大動脈全拡張期逆流 ＆ EDV > 20 cm/s |
| **僧帽弁逆流 MR** | **Vena Contracta 幅 (VC)** | `MR VC width` | mm | 重症: ≧ 7.0 mm (軽症: < 3.0 mm) |
| **僧帽弁逆流 MR** | PISA半径 / アライアンス速度 | `PISA Radius / Aliasing Vel` | mm, cm/s | 定量的逆流評価 (PISA法) の必須元データ |
| **僧帽弁逆流 MR** | **有効逆流弁口面積 (EROA)** | `MR EROA` | cm² | 重症: ≧ 0.40 cm² (二次性MRでは ≧ 0.20 cm²) |
| **僧帽弁逆流 MR** | **逆流量 (Regurgitant Volume)** | `MR RVol` | mL | 重症: ≧ 60 mL (二次性MRでは ≧ 30 mL) |
| **僧帽弁逆流 MR** | 肺静脈逆流波 (収縮期逆流) | `PV Systolic flow reversal` | - | 重症: 肺静脈血流で収縮期逆流 (S波の陰転化) |
| **三尖弁逆流 TR** | **三尖弁逆流最高流速 / 最大PG** | `TR Vmax / TR max PG` | m/s, mmHg | 肺動脈圧推定の基幹 (Vmax > 2.8 m/s でPH疑い) |
| **三尖弁逆流 TR** | **TR Vena Contracta 幅 (VC)** | `TR VC width` | mm | 重症: ≧ 7.0 mm (Massive 14-20, Torrential ≧21) |
| **三尖弁逆流 TR** | **TR PISA EROA / 逆流量** | `TR EROA / TR RVol` | cm², mL | 重症: EROA ≧ 0.40 cm² / RVol ≧ 45 mL |
| **三尖弁逆流 TR** | 肝静脈収縮期逆流波 | `Hepatic vein flow reversal` | - | 重症: 肝静脈波形での収縮期逆流 (Blunting/Reversal) |
| **肺動脈弁逆流 PR** | **PR peak vel / end-diastolic vel** | `PR peak vel / PRed vel` | m/s | 平均肺動脈圧 (mPAP) ＆ 拡張期圧 (PADP) 推定 |
| **肺動脈弁逆流 PR** | PR 圧半減時間 (PHT) | `PR PHT` | ms | 重症: < 100 ms で急峻な減衰 (Severe PR) |
| **肺動脈弁逆流 PR** | PR Index (持続時間比) | `PR Index (PR dur / Diastole)` | - | 重症: < 0.77 (拡張期の早期に血流途絶) |

---

## 4. 🫁 先進血行動態指標（Qp/Qs・PVR・RV-PAカップリング・AS狭窄）

> [!TIP]
> ### 先進演算指標の計算ロジック
> ・**Qp/Qs** = $(RVOT面積 \times RVOT\ VTI) / (LVOT面積 \times LVOT\ VTI)$ ➔ **$> 1.5$ でシャント閉鎖術適応**
> ・**PVR (Wood units)** = $10 \times (TR\ Vmax / RVOT\ VTI) + 0.16$ ➔ **$> 3.0\text{ Wood units}$ で前毛細管性肺高血圧**
> ・**RV-PA Coupling** = $TAPSE / PASP\ (\text{mm/mmHg})$ ➔ **$< 0.36$ で右室非代償・予後不良**

| 演算領域 | SR連携推奨項目 | 英語表記 / DICOMタグ | 単位 | 計算ロジック・臨床判断基準 |
| :--- | :--- | :--- | :---: | :--- |
| **シャント率 (Qp/Qs)** | **肺体血流比 (Qp/Qs)** | `Qp/Qs ratio` | - | ASD/VSD/PDAの評価。正常 1.0, > 1.5 で閉鎖適応 |
| **Qp/Qs 基礎データ** | 右室流出道径 / RVOT VTI | `RVOT diam / RVOT VTI` | mm, cm | Qp (肺血流量) 算出のための必須計測 |
| **Qp/Qs 基礎データ** | 左室流出道径 / LVOT VTI | `LVOT diam / LVOT VTI` | mm, cm | Qs (体血流量) 算出のための必須計測 |
| **肺血管抵抗 (PVR)** | **肺血管抵抗 (Abbas推定式)** | `PVR (Wood Units)` | Wood U | 正常 < 2.0, > 3.0 で前毛細管性肺高血圧 (毛細血管病変) |
| **右室PA連関** | **TAPSE / PASP 比 (カップリング)** | `TAPSE/PASP ratio` | mm/mmHg | 右室後負荷不整合の指標。正常 > 0.55, 予後不良 < 0.36 |
| **大動脈弁狭窄 AS** | **大動脈弁最高血流 / 平均圧較差** | `AV Vmax / AV Mean PG` | m/s, mmHg | 重症AS: Vmax ≧ 4.0 m/s / Mean PG ≧ 40 mmHg |
| **大動脈弁狭窄 AS** | **大動脈弁口面積 (連続の式) / DVI** | `AVA / DVI (LVOT/AV VTI)` | cm², - | 重症AS: AVA < 1.0 cm² (AVAi < 0.6 cm²/m²), DVI < 0.25 |
| **僧帽弁狭窄 MS** | 僧帽弁平均圧較差 / 弁口面積 | `MV Mean PG / MVA (PHT)` | mmHg, cm² | 重症MS: Mean PG ≧ 10 mmHg / MVA ≦ 1.5 cm² |

---

## 5. 📏 右室機能・下大静脈・大動脈基部計測

| 評価領域 | SR連携推奨項目 | 英語表記 / DICOMタグ | 単位 | 判定基準・カットオフ |
| :--- | :--- | :--- | :---: | :--- |
| **右室収縮能** | **三尖弁輪収縮期移動距離** | `TAPSE` | mm | < 17 mm で右室収縮能低下 |
| **右室収縮能** | 組織ドプラ三尖弁輪収縮速度 | `RV s'` (TDI S') | cm/s | < 9.5 cm/s で右室収縮能低下 |
| **右室収縮能** | 右室面積変化率 | `RV FAC` | % | < 35 % で右室機能低下 |
| **右室心筋機能** | 右室 Tei Index (MPI) | `RV Tei Index (MPI)` | - | 組織ドプラで > 0.54 (パルスで > 0.43) で機能低下 |
| **下大静脈 IVC** | 下大静脈最大径 / 虚脱率 | `IVCd max / IVC Collapse` | mm, % | > 21 mm ＆ 虚脱率 < 50% で右房圧上昇 (RAP 15mmHg) |
| **自動演算** | **推定右房圧 / 推定肺動脈収縮期圧** | `RAP / PASP (TR-PG + RAP)` | mmHg | RAP: 3/8/15 mmHg, PASP > 35〜40 mmHg で肺高血圧 |
| **大動脈基部** | 弁輪 / Valsalva / STJ / 上行径 | `Ao Annulus/Sinus/STJ/Asc` | mm | Valsalva / 上行 > 40 mm で拡大 (≧ 50mm 手術検討) |
| **心膜腔** | 心嚢液深度 (拡張末期) | `Pericardial Effusion Depth` | mm | 少量 <10mm, 中等量 10-20mm, 大量 >20mm |

---

## 💡 現場でのSR連携 運用・システム設計チェックポイント

1. **計測ラベルの選択厳守**: フリーキャリパーではなく、必ず装置内蔵の専用ラベル（例: Ao Diam, MV E, Sep e', LARS, RVOT diam, PISA 等）を選択して計測すること。
2. **シャント率 (Qp/Qs) のペアリング**: RVOT径・RVOT VTI、および LVOT径・LVOT VTI の4項目が揃って初めてQp/Qsが完全自動算出される。
3. **肺血管抵抗 (PVR) の自動計算**: TR Vmax と RVOT VTI が測定されていれば、レポートシステム側でWood単位を自動計算可能。
4. **全弁逆流定量の完全網羅**: AR/MR/TR/PRのVC幅・PISA・PHT・血流逆転波形をSR連携し、弁膜症重症度を客観的数値で完全担保する。
5. **単位系スケーリングの整合性**: エコー機側の出力単位（cm/s ⇄ m/s、mL ⇄ L）とレポートシステム側の受信単位の整合性を結合テストで必ず照合すること。
6. **複数計測の代表値採用ルール**: 不整脈や連続波ドプラ等で複数回計測した場合、レポート側で「平均値（Average）」を採用する設定に固定することを推奨する。
