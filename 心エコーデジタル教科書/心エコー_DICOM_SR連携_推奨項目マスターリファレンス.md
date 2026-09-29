---
title: 心エコー DICOM SR連携 推奨項目マスターリファレンス (アルティメット完全版)
tags: [心エコー, DICOM_SR, 構造化レポート, 2Dストレイン, GLS, 心毒性, CTRCD, 心アミロイドーシス, Apical_Sparing, RV_FWS, LARS, 弁狭窄, 弁逆流, Qp_Qs, PVR, dP_dt, 医療IT]
aliases: [心エコーSR連携アルティメット版, DICOM_SR連携マスター, エコーレポート自動化, ストレイン, GLS, CTRCD, アミロイドーシス]
date_created: 2026-09-29
last_modified: 2026-09-29
reference_guideline: ASE 2025新基準 / ESC 2022 Cardio-Oncology / EACVI / 日本心エコー図学会 (JSE)
---

# 🫀 心エコー検査 DICOM SR連携 推奨項目マスターリファレンス (アルティメット完全版)
― 2Dストレイン（GLS/心毒性CTRCD/心アミロイドーシスApical Sparing/RV FWS）・全4弁狭窄・全4弁逆流・Qp/Qs・PVR網羅仕様書 ―

> [!NOTE] 概要と目的
> 超音波診断装置で測定した数値をDICOM SR（Structured Report: 構造化レポート）としてレポートシステム・電子カルテへ自動連携することにより、
> ① 転記ミスの完全撲滅、② 検査時間の大幅短縮、
> ③ **【2Dスペックルストレイン】GLS、抗がん剤心毒性（CTRCD: 相対低下>15%）、心アミロイドーシス（心尖部温存比率 Apical Sparing Ratio > 1.0）、右室自由壁ストレイン（RV FWS）**、
> ④ **【全4弁狭窄症 AS / MS / TS / PS】＆【全4弁逆流症 AR / MR / TR / PR】**の連続の式・PISA・VC幅・EROA・逆流量・圧較差、
> ⑤ **【先進血行動態】**Qp/Qs（シャント率）・PVR（肺血管抵抗）・左室 dP/dt・RV-PAカップリング、
> ⑥ **【最新ASE 2025拡張能】**LARS（左房リザーバーストレイン）・E/e'の完全自動判定を実現します。

---

## 1. 🎯 2Dストレイン評価（GLS / 心毒性CTRCD / 心アミロイドーシス / 右室FWS）

> [!IMPORTANT]
> ### ストレイン解析の臨床判定基準
> ・**正常GLS**: **|GLS| > 18〜20%**（低下: > -16%）
> ・**心毒性 (CTRCD)**: ベースライン比で **GLS 相対低下 > 15%** で無症候性心毒性（Subclinical CTRCD）確定
> ・**心アミロイドーシス (Apical Sparing)**: **心尖部 / (基部+中部) 比 > 1.0**（Cherry-on-top sign）＆ **EF/|GLS| > 4.1** で特異度極めて高
> ・**右室自由壁 (RV FWS)**: **|RV FWS| > 20〜23%** が正常。肺高血圧・右室機能不全の強力な予後予測指標

| ストレイン分類 | SR連携推奨項目 | 英語表記 / DICOMタグ | 単位 | 判定基準・自動演算ロジック |
| :--- | :--- | :--- | :---: | :--- |
| **左室長軸ストレイン** | **左室グローバル縦方向歪み** | `LV GLS (Average)` | % | 正常: \|GLS\| > 18〜20% (低下: > -16%) |
| **左室長軸ストレイン** | 3断面個別GLS (4C/2C/3C) | `GLS A4C / A2C / A3C` | % | 各断面の歪み計測データ (ブルズアイ描画元) |
| **腫瘍循環器・心毒性** | **心毒性判定 (CTRCD相対低下率)** | `ΔGLS Relative Change` | % | ベースライン比で > 15% 低下で無症候性心毒性確定 |
| **心アミロイドーシス** | **心尖部温存比率 (Apical Sparing)** | `Apical Sparing Ratio (RELAPS)` | - | 心尖部 / (基部+中部) > 1.0 で心アミロイドーシス示唆 |
| **心アミロイドーシス** | **EF to GLS 比** | `LVEF / |GLS| ratio` | - | EF/\|GLS\| > 4.1 でアミロイドーシス (EF保たれGLS著減) |
| **心筋同期不全** | ピーク歪み時間分散 (同期不全) | `PSD (Peak Strain Dispersion)` | ms | > 55〜65 ms で心室性不整脈・突然死リスク増大 |
| **右室ストレイン** | **右室自由壁縦方向歪み (最重要)** | `RV FWS (Free Wall Strain)` | % | 正常: \|RV FWS\| > 20〜23% (中隔除外の純右室機能) |
| **右室ストレイン** | 右室全体縦方向歪み (4腔像) | `RV 4CH Strain (GLS)` | % | 中隔を含む右室全体ストレイン (正常: \|GLS\| > 20%) |
| **左房ストレイン** | **左房リザーバーストレイン (新基準)** | `LARS (LA Res. Strain)` | % | 充満圧上昇 (重度 < 18%, 軽度 < 24%, 正常 > 39%) |
| **左房ストレイン** | 左房コンジット / ポンプ歪み | `LACS / LAAS` | % | 左房受動導管機能 / 心房能動収縮機能の評価 |

---

## 2. 🫀 左室形態・収縮能 ＆ 拡張能評価（ASE 2025 / E/e'・LAVI・TR）

| 計測区分 | SR連携推奨項目 | 英語表記 / DICOMタグ | 単位 | 臨床的意義・システム自動演算 |
| :--- | :--- | :--- | :---: | :--- |
| **Mモード / 2D** | 左室拡張末期径 / 収縮末期径 | `LVDd / LVDs` | mm | 左室径・容量負荷評価・BSA補正値算出 |
| **Mモード / 2D** | 心室中隔壁厚 / 後壁厚 | `IVSTd / PWTd` | mm | 壁肥厚・HCM・アミロイドーシス心筋肥厚評価 |
| **自動演算** | **左室心筋重量係数 / 相対的壁厚** | `LVMI / RWT` | g/m², - | 左室肥大 (LVH) 確定 (男>115, 女>95), 求心性 (RWT>0.42) |
| **Simpson法** | 左室拡張末期 / 収縮末期容積 | `LVEDV / LVESV` | mL | 容量負荷評価・BSA補正 (EDVI, ESVI) |
| **Simpson法** | **左室駆出率 (最重要)** | `LVEF (Biplane EF)` | % | 心機能分類 (HFrEF / HFmrEF / HFpEF) |
| **Simpson法** | **1回拍出量係数 (SVi)** | `SVi (SV Index)` | mL/m² | 低流量判定 (<35 mL/m²: LF-LG AS, 低拍出状態) |
| **TVI (流入血流)** | E波 / A波最高速度 / E/A比 | `MV E / MV A / E/A` | cm/s, - | 拡張早期/心房収縮期流入速度 (AF時はA波欠損) |
| **TVI (流入血流)** | E波減速時間 (DT) | `MV DT` | ms | 左室コンプライアンス評価 (<160ms: 拘束型) |
| **組織ドプラ TDI** | **中隔 / 側壁 e' ＆ 平均 E/e'** | `Septal e' / Lat e' / E/e'` | cm/s, - | 局所弛緩能 (中隔<7, 側壁<10)・充満圧指標 (>14, AF時≧11) |
| **Biplane容積** | **左房容積係数 (LAVI)** | `LAVI` | mL/m² | 慢性左房圧上昇 (> 34 mL/m² で拡大陽性) |
| **MR連続波 CW** | **左室収縮期圧上昇率 (dP/dt)** | `LV dP/dt` | mmHg/s | MR波形1-3m/s時間より算出。正常>1200, 低下<1000 |

---

## 3. 🔒 全弁膜狭窄症の完全定量・重症度評価（AS / MS / TS / PS）

| 対象弁狭窄 | SR連携推奨項目 | 英語表記 / DICOMタグ | 単位 | 重症度判定カットオフ値 (ASE/ESC基準) |
| :--- | :--- | :--- | :---: | :--- |
| **大動脈弁狭窄 AS** | **大動脈弁最高血流速度** | `AV Vmax` (Peak Vel) | m/s | 重症: ≧ 4.0 m/s (中等症: 3.0〜4.0 m/s) |
| **大動脈弁狭窄 AS** | **大動脈弁平均圧較差 / 最大PG** | `AV Mean PG / AV Max PG` | mmHg | 重症: Mean PG ≧ 40 mmHg (Max PG ≧ 64 mmHg) |
| **大動脈弁狭窄 AS** | **大動脈弁口面積 (連続の式)** | `AVA` (Continuity Eq) | cm² | 重症: < 1.0 cm² (体表面積補正 AVAi < 0.6 cm²/m²) |
| **大動脈弁狭窄 AS** | **無次元速度指数 (DVI)** | `DVI` (LVOT VTI / AV VTI) | - | 重症: < 0.25 (低流量低圧較差 LF-LG AS で極めて有用) |
| **大動脈弁狭窄 AS** | 大動脈弁加速時間 / 駆出時間比 | `AV AcT / (AcT / ET)` | ms, - | 重症: AcT ≧ 100 ms, AcT/ET > 0.35 (弁開放遅延) |
| **僧帽弁狭窄 MS** | **僧帽弁平均圧較差 / 最大流速** | `MV Mean PG / MV Peak E` | mmHg, m/s | 重症: Mean PG ≧ 10 mmHg (中等症: 5〜10 mmHg) |
| **僧帽弁狭窄 MS** | 僧帽弁圧半減時間 (PHT) | `MV PHT` | ms | 重症: ≧ 220 ms (MVA = 220 / PHT) |
| **僧帽弁狭窄 MS** | **僧帽弁口面積 (PHT法 / トレース)** | `MVA (PHT) / MVA (Plan)` | cm² | 重症: ≦ 1.0 cm² (臨床的有意狭窄: ≦ 1.5 cm²) |
| **僧帽弁狭窄 MS** | 連続の式僧帽弁口面積 | `MVA (Continuity Eq)` | cm² | AR合併等でPHT信頼性低下時の確定評価 |
| **僧帽弁狭窄 MS** | **Wilkinsエコースコア (4項目)** | `Wilkins Score` (Total) | 点 | 弁尖肥厚・可動性・石灰化・下部病変 (PTMC適応 ≦ 8点) |
| **三尖弁狭窄 TS** | **三尖弁平均圧較差 / 圧半減時間** | `TV Mean PG / TV PHT` | mmHg, ms | 重症: Mean PG ≧ 5 mmHg / PHT ≧ 190 ms |
| **三尖弁狭窄 TS** | **三尖弁口面積 (PHT法 / 連続の式)** | `TVA (PHT) / TVA (Cont)` | cm² | 重症: ≦ 1.0 cm² (TVA = 190 / TV PHT) |
| **肺動脈弁狭窄 PS** | **肺動脈弁最高血流速度 / 最大PG** | `PV Vmax / PV Max PG` | m/s, mmHg | 重症: Vmax > 4.0 m/s / Max PG ≧ 64 mmHg (中等症: 36〜64) |
| **肺動脈弁狭窄 PS** | **肺動脈弁平均圧較差** | `PV Mean PG` | mmHg | 重症: ≧ 35 mmHg |

---

## 4. 🎯 全弁膜逆流症の完全定量・半定量評価（AR / MR / TR / PR）

| 対象弁逆流 | SR連携推奨項目 | 英語表記 / DICOMタグ | 単位 | 重症度判定カットオフ値 (ASE/ESC基準) |
| :--- | :--- | :--- | :---: | :--- |
| **大動脈弁逆流 AR** | **Vena Contracta 幅 (VC)** | `AR VC width` | mm | 重症: > 6.0 mm (軽症: < 3.0 mm) |
| **大動脈弁逆流 AR** | 圧半減時間 (PHT) | `AR PHT` | ms | 重症: < 200 ms (軽症: > 500 ms) |
| **大動脈弁逆流 AR** | **有効逆流弁口面積 (EROA)** | `AR EROA` | cm² | 重症: ≧ 0.30 cm² (軽症: < 0.10 cm²) |
| **大動脈弁逆流 AR** | **逆流量 (Regurgitant Volume)** | `AR RVol` | mL | 重症: ≧ 60 mL (軽症: < 30 mL) |
| **大動脈弁逆流 AR** | 下行大動脈拡張期逆流終末速度 | `AR Holodiastolic (EDV)` | cm/s | 重症: 下行大動脈全拡張期逆流 ＆ EDV > 20 cm/s |
| **僧帽弁逆流 MR** | **Vena Contracta 幅 (VC)** | `MR VC width` | mm | 重症: ≧ 7.0 mm (軽症: < 3.0 mm) |
| **僧帽弁逆流 MR** | PISA半径 / アライアンス速度 | `PISA Radius / Aliasing` | mm, cm/s | 定量的逆流評価 (PISA法) の必須元データ |
| **僧帽弁逆流 MR** | **有効逆流弁口面積 (EROA)** | `MR EROA` | cm² | 重症: ≧ 0.40 cm² (二次性MRでは ≧ 0.20 cm²) |
| **僧帽弁逆流 MR** | **逆流量 (Regurgitant Volume)** | `MR RVol` | mL | 重症: ≧ 60 mL (二次性MRでは ≧ 30 mL) |
| **僧帽弁逆流 MR** | 肺静脈逆流波 (収縮期逆流) | `PV Systolic reversal` | - | 重症: 肺静脈血流で収縮期逆流 (S波の陰転化) |
| **三尖弁逆流 TR** | **三尖弁逆流最高流速 / 最大PG** | `TR Vmax / TR max PG` | m/s, mmHg | 肺動脈圧推定の基幹 (Vmax > 2.8 m/s でPH疑い) |
| **三尖弁逆流 TR** | **TR Vena Contracta 幅 (VC)** | `TR VC width` | mm | 重症: ≧ 7.0 mm (Massive 14-20, Torrential ≧21) |
| **三尖弁逆流 TR** | **TR PISA EROA / 逆流量** | `TR EROA / TR RVol` | cm², mL | 重症: EROA ≧ 0.40 cm² / RVol ≧ 45 mL |
| **三尖弁逆流 TR** | 肝静脈収縮期逆流波 | `Hepatic vein reversal` | - | 重症: 肝静脈波形での収縮期逆流 (Blunting/Reversal) |
| **肺動脈弁逆流 PR** | **PR peak vel / end-diastolic vel** | `PR peak vel / PRed vel` | m/s | 平均肺動脈圧 (mPAP) ＆ 拡張期圧 (PADP) 推定 |
| **肺動脈弁逆流 PR** | PR 圧半減時間 (PHT) | `PR PHT` | ms | 重症: < 100 ms で急峻な減衰 (Severe PR) |
| **肺動脈弁逆流 PR** | PR Index (持続時間比) | `PR Index (dur / Diastole)` | - | 重症: < 0.77 (拡張期の早期に血流途絶) |

---

## 5. 🫁 先進血行動態指標（Qp/Qs・PVR・RV-PAカップリング）＆ 右心系・大血管

| 演算・形態領域 | SR連携推奨項目 | 英語表記 / DICOMタグ | 単位 | 計算ロジック・臨床判断基準 |
| :--- | :--- | :--- | :---: | :--- |
| **シャント率 (Qp/Qs)** | **肺体血流比 (Qp/Qs)** | `Qp/Qs ratio` | - | ASD/VSD/PDA。RVOT/LVOTの径・VTIより算出 (>1.5 閉鎖適応) |
| **肺血管抵抗 (PVR)** | **肺血管抵抗 (Abbas推定式)** | `PVR (Wood Units)` | Wood U | 10×(TR Vmax/RVOT VTI)+0.16 (正常<2.0, >3.0 前毛細管性PH) |
| **右室PA連関** | **TAPSE / PASP 比 (カップリング)** | `TAPSE/PASP ratio` | mm/mmHg | 右室後負荷不整合。正常 > 0.55, 予後不良 < 0.36 |
| **右室収縮能** | **TAPSE / RV s' / RV FAC** | `TAPSE / RV s' / RV FAC` | mm, cm/s, % | TAPSE<17mm, s'<9.5cm/s, FAC<35% で右室機能低下 |
| **右室心筋機能** | 右室 Tei Index (MPI) | `RV Tei Index (MPI)` | - | 組織ドプラで > 0.54 (パルスで > 0.43) で機能低下 |
| **下大静脈 IVC** | 下大静脈最大径 / 虚脱率 | `IVCd max / IVC Collapse` | mm, % | > 21 mm ＆ 虚脱率 < 50% で右房圧上昇 (RAP 15mmHg) |
| **自動演算** | **推定右房圧 / 推定肺動脈収縮期圧** | `RAP / PASP (TR-PG + RAP)` | mmHg | RAP: 3/8/15 mmHg, PASP > 35〜40 mmHg で肺高血圧 |
| **大動脈基部** | 弁輪 / Valsalva / STJ / 上行径 | `Ao Annulus/Sinus/STJ/Asc` | mm | Valsalva / 上行 > 40 mm で拡大 (≧ 50mm 手術検討) |
| **心膜腔** | 心嚢液深度 (拡張末期) | `Pericardial Effusion Depth` | mm | 少量 <10mm, 中等量 10-20mm, 大量 >20mm |

---

## 💡 現場でのSR連携 運用・システム設計チェックポイント

1. **ストレイン解析のベンダー独立性**: GE (EchoPAC), Philips (AutoSTRAIN), Canon (Wall Motion Tracking) 等でGLSやBulls-eyeのタグ定義が異なるため、DICOM SRのTID 5200 User-defined strainタグのマッピングを必ず確認すること。
2. **CTRCD心毒性監視のベースライン連携**: 過去のベースラインGLSと比較し、相対低下率 (Baseline - Current)/Baseline > 15% を自動算出するアラートロジックをレポートシステムへ実装すること。
3. **心アミロイドーシス Apical Sparing の自動算出**: 心尖部（4セグメント）平均歪み ÷ (基部6セグメント + 中部6セグメント平均歪み) > 1.0 のフラグ付けで特異的検出を自動化。
4. **弁狭窄・逆流・血行動態の整合性**: LVOT/RVOTペアリング（Qp/Qs）、TR Vmax＋RVOT VTI（PVR）、連続の式（AVA/MVA/TVA）がワンストップで欠損なく連動するプリセットを固定する。
5. **単位系スケーリング整合性**: cm/s ⇄ m/s、mL ⇄ L のスケールバグを結合テストで排除し、不整脈時は複数心拍平均 (Average) を採用すること。
