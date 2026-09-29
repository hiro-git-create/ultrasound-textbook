import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="D3D3D3"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="6" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'<w:bottom w:val="single" w:sz="8" w:space="0" w:color="005691"/>'
        f'<w:right w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def create_sr_doc(output_path):
    doc = docx.Document()
    
    # Page setup - Margins (15mm)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.5)
        section.bottom_margin = Inches(0.5)
        section.left_margin = Inches(0.5)
        section.right_margin = Inches(0.5)
        
    # Title
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_run = title_p.add_run("心エコー検査 DICOM SR連携 推奨項目マスターリファレンス")
    title_run.font.name = "Meiryo"
    title_run.font.size = Pt(17)
    title_run.font.bold = True
    title_run.font.color.rgb = RGBColor(0, 70, 130) # Navy
    
    sub_p = doc.add_paragraph()
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub_run = sub_p.add_run("― 臨床ガイドライン（ASE 2025新基準 / EACVI / JSE）準拠・LARS対応 レポート自動化仕様書 ―")
    sub_run.font.name = "Meiryo"
    sub_run.font.size = Pt(10)
    sub_run.font.italic = True
    sub_run.font.color.rgb = RGBColor(70, 70, 70)
    
    # Overview Box
    p_box = doc.add_paragraph()
    p_box.paragraph_format.space_before = Pt(3)
    p_box.paragraph_format.space_after = Pt(6)
    run_box = p_box.add_run(
        "【概要と目的】\n"
        "超音波診断装置で計測した数値をDICOM SR（Structured Report: 構造化レポート）としてレポートシステム・電子カルテへ自動連携することにより、"
        "① 転記ミスの完全撲滅、② 検査時間の短縮、③ 最新ASE 2025拡張能アルゴリズム（LARS・E/e'等）や弁膜症重症度、BSA体表面積補正（LAVI, LVMI, SVi等）の完全自動判定を実現します。"
    )
    run_box.font.name = "Meiryo"
    run_box.font.size = Pt(9.0)
    run_box.font.color.rgb = RGBColor(20, 40, 60)
    
    def add_section_header(title_text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(10)
        h.paragraph_format.space_after = Pt(3)
        run = h.add_run(title_text)
        run.font.name = "Meiryo"
        run.font.size = Pt(11.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 90, 160)
        
    def create_custom_table(headers, rows_data, col_widths=None):
        table = doc.add_table(rows=len(rows_data) + 1, cols=len(headers))
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(table)
        
        # Header row
        hdr_cells = table.rows[0].cells
        for i, header_text in enumerate(headers):
            hdr_cells[i].text = header_text
            set_cell_background(hdr_cells[i], "005691") # Dark Blue
            set_cell_margins(hdr_cells[i], top=100, bottom=100, left=80, right=80)
            p = hdr_cells[i].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.name = "Meiryo"
                r.font.size = Pt(9.0)
                r.font.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
                
        # Data rows
        for row_idx, data in enumerate(rows_data):
            row_cells = table.rows[row_idx + 1].cells
            bg_color = "F4F8FA" if row_idx % 2 == 1 else "FFFFFF"
            for col_idx, text in enumerate(data):
                row_cells[col_idx].text = str(text)
                set_cell_background(row_cells[col_idx], bg_color)
                set_cell_margins(row_cells[col_idx], top=60, bottom=60, left=80, right=80)
                p = row_cells[col_idx].paragraphs[0]
                if col_idx in [2, 3]: # Unit, tag center
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                elif col_idx == 0:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for r in p.runs:
                    r.font.name = "Meiryo"
                    r.font.size = Pt(8.5)
                    r.font.color.rgb = RGBColor(40, 40, 40)
                    if col_idx == 1 and ("EF" in text or "LAVI" in text or "E/e'" in text or "LARS" in text or "SVi" in text):
                        r.font.bold = True
                        r.font.color.rgb = RGBColor(180, 20, 20)
                        
        if col_widths:
            for row in table.rows:
                for idx, width in enumerate(col_widths):
                    row.cells[idx].width = Inches(width)
        return table

    # 1. Left Ventricle
    add_section_header("1. 🫀 左室形態・収縮能（最優先ルーチン計測項目）")
    headers_1 = ["大分類", "SR連携推奨項目", "英語表記 / DICOMタグ", "単位", "臨床的意義・システム自動演算"]
    data_1 = [
        ["Mモード / 2D", "左室拡張末期径", "LVDd (LVEDD)", "mm", "左室拡大の評価・BSA補正値算出"],
        ["Mモード / 2D", "左室収縮末期径", "LVDs (LVESD)", "mm", "左室収縮末期容積・リモデリング評価"],
        ["Mモード / 2D", "心室中隔壁厚", "IVSTd (IVSd)", "mm", "壁肥厚・肥大型心筋症 (HCM) 判定"],
        ["Mモード / 2D", "左室後壁厚", "PWTd (LVPWd)", "mm", "求心性肥大の評価"],
        ["自動演算", "左室心筋重量係数", "LVMI (LV Mass Index)", "g/m²", "左室肥大 (LVH) 確定診断 (男>115, 女>95)"],
        ["自動演算", "相対的壁厚", "RWT (2×PWTd/LVDd)", "-", "求心性肥大 vs 遠心性肥大の分類 (基準>0.42)"],
        ["自動演算", "左室短縮率", "FS (%FS)", "%", "左室円周方向収縮能 (正常 28〜45%)"],
        ["Simpson法", "左室拡張末期容積", "LVEDV (EDV Biplane)", "mL", "容量負荷評価・BSA補正 (EDVI)"],
        ["Simpson法", "左室収縮末期容積", "LVESV (ESV Biplane)", "mL", "BSA補正 (ESVI)"],
        ["Simpson法", "左室駆出率 (最重要)", "LVEF (Biplane EF)", "%", "収縮能の国際基準 (HFrEF/HFmrEF/HFpEF分類)"],
        ["Simpson法", "1回拍出量 / 心拍出量", "SV / CO", "mL, L/min", "有効駆出量・心係数 (CI: L/min/m²) 算出"],
        ["自動演算", "1回拍出量係数 (重要)", "SVi (SV Index)", "mL/m²", "低流量判定 (<35 mL/m²: LF-LG AS, 低拍出状態)"]
    ]
    create_custom_table(headers_1, data_1, [1.2, 1.6, 1.6, 0.8, 2.3])

    # 2. Diastolic Function & LARS
    add_section_header("2. 🌊 左室拡張能評価（ASE 2025新基準 / LARS・E/e'・LAVI・TR）")
    p_dia = doc.add_paragraph()
    r_dia = p_dia.add_run(
        "【ASE 2025改訂アルゴリズム & LARS】\n"
        "① 平均 E/e' > 14  |  ② 中隔側 e' < 7 cm/s または 側壁側 e' < 10 cm/s  |  ③ TR Vmax > 2.8 m/s  |  ④ LAVI > 34 mL/m²\n"
        "★【新指標 LARS（左房リザーバーストレイン）】: LARS < 18% で充満圧上昇確定。LAVIが正常の早期HFpEFやグレーゾーン症例を決着させる最重要指標。\n"
        "※ AF（心房細動）症例では、E/e' ≧ 11 単独判定ロジックへ自動切り替え。"
    )
    r_dia.font.name = "Meiryo"
    r_dia.font.size = Pt(8.5)
    r_dia.font.bold = True
    r_dia.font.color.rgb = RGBColor(160, 50, 0)
    
    headers_2 = ["検査手技", "SR連携推奨項目", "英語表記 / DICOMタグ", "単位", "判定基準・自動連携メリット"]
    data_2 = [
        ["左房ストレイン", "左房リザーバーストレイン (新基準)", "LARS (LA Res. Strain)", "%", "充満圧上昇 (重度低下 < 18%, 軽度低下 < 24%, 正常 > 39%)"],
        ["左房ストレイン", "左房コンジット / ポンプストレイン", "LACS / LAAS", "%", "左房受動的導管機能 / 心房能動的収縮機能の評価"],
        ["TVI (流入血流)", "E波最高血流速度", "MV E vel (Peak E)", "cm/s", "拡張早期左室流入速度"],
        ["TVI (流入血流)", "A波最高血流速度", "MV A vel (Peak A)", "cm/s", "心房収縮期流入速度 (AF時は欠損)"],
        ["自動演算", "E/A比", "E/A ratio", "-", "弛緩障害型 (<0.8), 偽正常型, 拘束型 (>2.0)"],
        ["TVI (流入血流)", "E波減速時間", "MV DT", "ms", "左室コンプライアンス評価 (<160ms: 拘束型)"],
        ["組織ドプラ TDI", "中隔側 拡張早期弁輪速度", "Septal e'", "cm/s", "心筋局所弛緩能 (< 7.0 cm/s で低下)"],
        ["組織ドプラ TDI", "側壁側 拡張早期弁輪速度", "Lateral e'", "cm/s", "心筋局所弛緩能 (< 10.0 cm/s で低下)"],
        ["自動演算", "平均 E/e' 比 (最重要)", "Average E/e'", "-", "左房圧・左室充満圧の指標 (> 14 で上昇, AF時は ≧ 11)"],
        ["Biplane容積", "左房容積係数 (最重要)", "LAVI", "mL/m²", "慢性左房圧上昇 (> 34 mL/m² で拡大陽性)"],
        ["連続波ドプラ CW", "三尖弁逆流最高流速", "TR Vmax", "m/s", "肺動脈圧上昇スクリーニング (> 2.8 m/s で陽性)"],
        ["肺静脈血流 PW", "S波速度 / D波速度", "PV S vel / PV D vel", "cm/s", "S/D比による左房圧推定 (S < D: 左房圧上昇)"],
        ["肺静脈血流 PW", "心房逆流波持続時間差", "PV Ar dur - MV A dur", "ms", "Ar - A ≧ 30 ms で左室拡張末期圧 (LVEDP) 上昇"]
    ]
    create_custom_table(headers_2, data_2, [1.3, 1.8, 1.7, 0.7, 2.0])

    # 3. Valvular Disease
    add_section_header("3. 🎯 弁膜症の重症度・定量評価（AS / AR / MS / MR）")
    headers_3 = ["弁膜症", "SR連携推奨項目", "英語表記 / DICOMタグ", "単位", "重症度判定カットオフ値"]
    data_3 = [
        ["大動脈弁狭窄 AS", "大動脈弁最高血流速度", "AV Vmax (Peak Vel)", "m/s", "重症: ≧ 4.0 m/s"],
        ["大動脈弁狭窄 AS", "大動脈弁平均圧較差", "AV Mean PG", "mmHg", "重症: ≧ 40 mmHg"],
        ["大動脈弁狭窄 AS", "大動脈弁口面積 (連続の式)", "AVA (Continuity Eq)", "cm²", "重症: < 1.0 cm² (指数化 AVAi < 0.6 cm²/m²)"],
        ["大動脈弁狭窄 AS", "無次元速度指数", "DVI (LVOT VTI / AV VTI)", "-", "重症: < 0.25 (低流量低圧較差 LF-LG AS で極めて有用)"],
        ["大動脈弁逆流 AR", "圧半減時間", "AR PHT", "ms", "重症: < 200 ms (軽症: > 500 ms)"],
        ["僧帽弁逆流 MR", "PISA半径 / アライアンス速度", "PISA Radius / Aliasing Vel", "mm, cm/s", "定量的逆流評価の必須元データ"],
        ["僧帽弁逆流 MR", "有効逆流弁口面積 (EROA)", "MR EROA", "cm²", "重症: ≧ 0.40 cm² (二次性MRでは ≧ 0.20 cm²)"],
        ["僧帽弁逆流 MR", "逆流量 (Regurgitant Volume)", "MR RVol", "mL", "重症: ≧ 60 mL (二次性MRでは ≧ 30 mL)"],
        ["僧帽弁狭窄 MS", "平均圧較差 / 弁口面積", "MV Mean PG / MVA (PHT)", "mmHg, cm²", "重症: Mean PG ≧ 10 mmHg / MVA ≦ 1.5 cm²"]
    ]
    create_custom_table(headers_3, data_3, [1.3, 1.7, 1.7, 0.8, 2.0])

    # 4. Right Heart & IVC
    add_section_header("4. 🫁 右心系機能・肺高血圧・下大静脈（右心不全評価）")
    headers_4 = ["評価領域", "SR連携推奨項目", "英語表記 / DICOMタグ", "単位", "判定基準・カットオフ"]
    data_4 = [
        ["右室収縮能", "三尖弁輪収縮期移動距離", "TAPSE", "mm", "< 17 mm で右室収縮能低下"],
        ["右室収縮能", "組織ドプラ三尖弁輪収縮速度", "RV s' (TDI S')", "cm/s", "< 9.5 cm/s で右室収縮能低下"],
        ["右室収縮能", "右室面積変化率", "RV FAC", "%", "< 35 % で右室機能低下"],
        ["下大静脈 IVC", "下大静脈最大径 (呼気時)", "IVCd max", "mm", "> 21 mm で拡大 (右房圧上昇示唆)"],
        ["下大静脈 IVC", "IVC虚脱率 (吸気時虚脱)", "IVC Collapse Index", "%", "> 50 % で正常虚脱 (≦ 50% で虚脱不良)"],
        ["自動演算", "推定右房圧", "RAP (eRAP)", "mmHg", "IVC径と虚脱率より 3 / 8 / 15 mmHg 自動算出"],
        ["自動演算", "推定肺動脈収縮期圧", "PASP (TR-PG + RAP)", "mmHg", "> 35〜40 mmHg で肺高血圧症疑い"],
        ["予備バックアップ", "肺動脈弁拡張末期逆流速度", "PR end-diastolic vel", "m/s", "TR描出不良時の推定肺動脈拡張期圧 (PADP) 算出用"]
    ]
    create_custom_table(headers_4, data_4, [1.2, 1.7, 1.7, 0.8, 2.1])

    # 5. Aorta & Pericardium
    add_section_header("5. 📏 大血管・心膜腔計測")
    headers_5 = ["計測部位", "SR連携推奨項目", "英語表記 / DICOMタグ", "単位", "臨床的意義・拡大基準"]
    data_5 = [
        ["大動脈基部", "大動脈弁輪径", "Ao Annulus", "mm", "TAVI / 人工弁サイズ選択"],
        ["大動脈基部", "バルサルバ洞径", "Sinus of Valsalva", "mm", "> 40 mm で拡大 (大動脈基部拡張症)"],
        ["大動脈基部", "洞管接合部径", "ST Junction", "mm", "上行大動脈瘤・解離好発部"],
        ["大動脈基部", "上行大動脈径", "Ascending Aorta", "mm", "> 40 mm で拡大 (≧ 50mm 手術検討)"],
        ["心膜腔", "心嚢液深度 (拡張末期)", "Pericardial Effusion Depth", "mm", "少量 <10mm, 中等量 10-20mm, 大量 >20mm"]
    ]
    create_custom_table(headers_5, data_5, [1.2, 1.7, 1.7, 0.8, 2.1])

    # Operational Tips & IT Specifications
    add_section_header("💡 現場でのSR連携 運用・システム設計チェックポイント")
    p_tips = doc.add_paragraph()
    r_tips = p_tips.add_run(
        "1. 計測ラベルの選択厳守: フリーキャリパーではなく、必ず装置内蔵の専用ラベル（例: Ao Diam, MV E, Sep e', LARS 等）を選択して計測すること。\n"
        "2. Biplaneペアリング: 左室容積・左房容積（LAVI）は、A4CとA2Cの両方を同一検査内で測定完了することで、SR上で1つのBiplane容積として統合出力される。\n"
        "3. TR描出不良時のPRバックアップ: TRが得られない場合はPR end-diastolic velを記録し、肺動脈圧推定の欠損を防ぐ。\n"
        "4. 単位系スケーリングの整合性: エコー機側の出力単位（cm/s ⇄ m/s、mL ⇄ L）とレポートシステム側の受信単位の整合性を結合テストで必ず照合すること。\n"
        "5. 複数計測の代表値採用ルール: 不整脈や連続波ドプラ等で複数回計測した場合、レポート側で「平均値（Average）」を採用する設定に固定することを推奨する。"
    )
    r_tips.font.name = "Meiryo"
    r_tips.font.size = Pt(8.5)
    r_tips.font.color.rgb = RGBColor(30, 30, 30)

    doc.save(output_path)
    print(f"Successfully updated docx at {output_path}")

if __name__ == "__main__":
    local_path = r"c:\Antigravity\超音波検査\心エコーデジタル教科書\心エコー_DICOM_SR連携_推奨項目マスターリファレンス.docx"
    create_sr_doc(local_path)
