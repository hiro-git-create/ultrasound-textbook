import os
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=80, bottom=80, left=120, right=120):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def create_echo_report_docx(output_path):
    doc = Document()
    
    # ページ余白（A4・やや狭め）
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.5)
        section.bottom_margin = Inches(0.5)
        section.left_margin = Inches(0.6)
        section.right_margin = Inches(0.6)
        
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Yu Gothic'
    font.size = Pt(9)
    font.color.rgb = RGBColor(30, 41, 59)

    # タイトル
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_run = title_p.add_run('超音波心臓構造・血行動態検査（心エコー）レポート')
    title_run.font.size = Pt(15)
    title_run.font.bold = True
    title_run.font.color.rgb = RGBColor(15, 23, 42)
    title_p.paragraph_format.space_after = Pt(6)

    def add_section_header(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(2)
        run = p.add_run(f'■ {title}')
        run.font.bold = True
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(30, 64, 175) # Deep Blue

    # 1. 基本情報テーブル
    add_section_header("基本情報")
    table_info = doc.add_table(rows=3, cols=4)
    table_info.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_info.autofit = False

    info_data = [
        [("患者ID", True), ("", False), ("氏名", True), ("", False)],
        [("生年月日/年齢", True), ("年  月  日 (  歳)  性別: 男 / 女", False), ("検査日時", True), ("20   年  月  日   : ", False)],
        [("身長/体重(BSA)", True), ("   cm /   kg (   ㎡)", False), ("血圧/脈拍", True), ("   /   mmHg /   bpm", False)],
    ]

    col_widths_info = [Inches(1.2), Inches(2.3), Inches(1.2), Inches(2.3)]
    for r_idx, row in enumerate(table_info.rows):
        for c_idx, cell in enumerate(row.cells):
            cell.width = col_widths_info[c_idx]
            text, is_hdr = info_data[r_idx][c_idx]
            cell.text = text
            p = cell.paragraphs[0]
            p.runs[0].font.size = Pt(8.5)
            if is_hdr:
                set_cell_background(cell, "F1F5F9")
                p.runs[0].font.bold = True
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)

    # 臨床診断・検査目的
    p_meta = doc.add_paragraph()
    p_meta.paragraph_format.space_before = Pt(3)
    p_meta.paragraph_format.space_after = Pt(2)
    run_meta = p_meta.add_run("依頼科/担当医: ____________科 / ____________ 医師    描出能: [ 良好 / 普通 / 不良 ]    検査技師: ____________\n臨床診断・検査目的: ")
    run_meta.font.size = Pt(8.5)

    # 2. 心エコー計測データ
    add_section_header("左室内径・壁厚・左室機能・大動脈/左房/右心系計測")
    table_meas = doc.add_table(rows=8, cols=5)
    table_meas.alignment = WD_TABLE_ALIGNMENT.CENTER
    meas_headers = ["項目", "略語", "計測値", "基準値（目安）", "評価・所見"]
    meas_data = [
        ["左室拡張末期径", "LVDd", "     mm", "37 - 52 mm", "正常 / 拡大"],
        ["左室収縮末期径", "LVDs", "     mm", "22 - 36 mm", "正常 / 拡大"],
        ["心室中隔厚", "IVSd", "     mm", "6 - 10 mm", "正常 / 肥大"],
        ["左室後壁厚", "LVPWd", "     mm", "6 - 10 mm", "正常 / 肥大"],
        ["左室駆出率 (Teich/Simp)", "LVEF", "     %", "≥ 52%(男) / ≥ 54%(女)", "正常 / 軽度 / 中等度 / 高度低下"],
        ["大動脈基部径 / 左房径", "AoD / LAD", "  /   mm", "Ao < 35 / LAD < 40", "正常 / 拡大"],
        ["左房容積係数", "LAVI", "   mL/㎡", "16 - 34 mL/㎡", "正常 / 軽度 / 中等度 / 高度拡大"],
    ]

    col_widths_meas = [Inches(1.8), Inches(1.1), Inches(1.1), Inches(1.6), Inches(1.6)]
    # Header row
    for c_idx, cell in enumerate(table_meas.rows[0].cells):
        cell.width = col_widths_meas[c_idx]
        cell.text = meas_headers[c_idx]
        set_cell_background(cell, "E2E8F0")
        p = cell.paragraphs[0]
        p.runs[0].font.bold = True
        p.runs[0].font.size = Pt(8.5)
        set_cell_margins(cell, top=50, bottom=50, left=60, right=60)

    for r_idx, row_data in enumerate(meas_data):
        for c_idx, cell in enumerate(table_meas.rows[r_idx+1].cells):
            cell.width = col_widths_meas[c_idx]
            cell.text = row_data[c_idx]
            p = cell.paragraphs[0]
            p.runs[0].font.size = Pt(8)
            set_cell_margins(cell, top=40, bottom=40, left=60, right=60)

    # 3. ドプラ・拡張能・肺循環
    add_section_header("ドプラ血流・左室拡張能・肺動脈圧")
    table_dop = doc.add_table(rows=5, cols=4)
    table_dop.alignment = WD_TABLE_ALIGNMENT.CENTER
    dop_headers = ["項目", "計測値", "基準値", "判定・特記事項"]
    dop_data = [
        ["Transmitral E / A / DT", "  /  cm/s (  ms)", "E/A: 0.8 - 2.0", "正常 / 弛緩低下 / 偽正常 / 拘束型"],
        ["僧帽弁輪速度 e' / 平均 E/e'", "   cm/s /    ", "E/e' ≤ 14", "正常 / 左室充満圧上昇疑い"],
        ["大動脈弁流速 (AV Vmax / meanPG)", "  m/s /   mmHg", "Vmax < 2.0 m/s", "狭窄なし / 軽度 / 中等度 / 重度"],
        ["TR Vmax / 推定RAP / ePASP", " m/s /  /  mmHg", "ePASP ≤ 35 mmHg", "PH確率: 低 / 中 / 高  IVC: 虚脱良好 / 不良"],
    ]
    col_widths_dop = [Inches(2.3), Inches(1.7), Inches(1.3), Inches(1.9)]
    for c_idx, cell in enumerate(table_dop.rows[0].cells):
        cell.width = col_widths_dop[c_idx]
        cell.text = dop_headers[c_idx]
        set_cell_background(cell, "E2E8F0")
        p = cell.paragraphs[0]
        p.runs[0].font.bold = True
        p.runs[0].font.size = Pt(8.5)
        set_cell_margins(cell, top=50, bottom=50, left=60, right=60)

    for r_idx, row_data in enumerate(dop_data):
        for c_idx, cell in enumerate(table_dop.rows[r_idx+1].cells):
            cell.width = col_widths_dop[c_idx]
            cell.text = row_data[c_idx]
            p = cell.paragraphs[0]
            p.runs[0].font.size = Pt(8)
            set_cell_margins(cell, top=40, bottom=40, left=60, right=60)

    # 4. 弁膜症評価
    add_section_header("弁膜症評価 (Valvular Disease)")
    table_valv = doc.add_table(rows=5, cols=3)
    table_valv.alignment = WD_TABLE_ALIGNMENT.CENTER
    valv_headers = ["弁", "逆流 (Regurgitation)", "狭窄 (Stenosis) / 形態所見"]
    valv_data = [
        ["大動脈弁 (AV)", "None / Trace / Mild / Moderate / Severe", "なし / 軽度 / 中等度 / 重度 (石灰化: なし/あり)"],
        ["僧帽弁 (MV)", "None / Trace / Mild / Moderate / Severe", "なし / 軽度 / 中等度 / 重度 (逸脱: 前尖/後尖)"],
        ["三尖弁 (TV)", "None / Trace / Mild / Moderate / Severe", "なし / 軽度 / 中等度 / 重度"],
        ["肺動脈弁 (PV)", "None / Trace / Mild / Moderate / Severe", "なし / 軽度 / 中等度 / 重度"],
    ]
    col_widths_valv = [Inches(1.5), Inches(2.7), Inches(3.0)]
    for c_idx, cell in enumerate(table_valv.rows[0].cells):
        cell.width = col_widths_valv[c_idx]
        cell.text = valv_headers[c_idx]
        set_cell_background(cell, "E2E8F0")
        p = cell.paragraphs[0]
        p.runs[0].font.bold = True
        p.runs[0].font.size = Pt(8.5)
        set_cell_margins(cell, top=50, bottom=50, left=60, right=60)

    for r_idx, row_data in enumerate(valv_data):
        for c_idx, cell in enumerate(table_valv.rows[r_idx+1].cells):
            cell.width = col_widths_valv[c_idx]
            cell.text = row_data[c_idx]
            p = cell.paragraphs[0]
            p.runs[0].font.size = Pt(8)
            set_cell_margins(cell, top=40, bottom=40, left=60, right=60)

    # 5. 壁運動 & その他所見 & 総合判定
    add_section_header("左室局所壁運動 (RWMA) & その他・総合判定")
    
    p_rwma = doc.add_paragraph()
    p_rwma.paragraph_format.space_before = Pt(2)
    p_rwma.paragraph_format.space_after = Pt(2)
    p_rwma_run = p_rwma.add_run("局所壁運動: [ 全周性良好(Normokinesis) / 壁運動異常あり ]\n異常部位: [ 前壁 / 心室中隔 / 下壁 / 側壁 / 心尖部 ]  性状: [ Hypo / A / Dys ]\n心嚢液: [ なし / 少量 / 中等量 / 大量 ]   心腔内血栓: [ なし / あり ]   奇形・短絡: [ なし / あり ]")
    p_rwma_run.font.size = Pt(8.5)

    table_conc = doc.add_table(rows=1, cols=1)
    table_conc.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_cell = table_conc.rows[0].cells[0]
    c_cell.width = Inches(7.2)
    c_cell.text = "【総合所見・コメント】\n\n\n\n\n"
    set_cell_background(c_cell, "F8FAFC")
    set_cell_margins(c_cell, top=100, bottom=100, left=100, right=100)
    c_cell.paragraphs[0].runs[0].font.size = Pt(8.5)
    c_cell.paragraphs[0].runs[0].font.bold = True

    doc.save(output_path)
    print(f"Successfully generated: {output_path}")

if __name__ == '__main__':
    target = r"c:\Antigravity\超音波検査\心エコー\心エコー検査レポート用紙.docx"
    create_echo_report_docx(target)
