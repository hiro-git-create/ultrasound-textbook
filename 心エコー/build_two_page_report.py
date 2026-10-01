import docx
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=40, bottom=40, left=60, right=60):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="CCCCCC", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def build_report():
    doc = Document()

    # 余白設定 (A4縦、余白12mm程度)
    for section in doc.sections:
        section.top_margin = Inches(0.45)
        section.bottom_margin = Inches(0.45)
        section.left_margin = Inches(0.5)
        section.right_margin = Inches(0.5)

    # デフォルトスタイル
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Yu Gothic'
    font.size = Pt(8)
    font.color.rgb = RGBColor(30, 30, 30)

    # ==========================================
    # PAGE 1: 基本報告書 (添付原本準拠)
    # ==========================================
    # ヘッダータイトル部
    t_top = doc.add_table(rows=1, cols=3)
    t_top.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_top.autofit = False
    set_table_borders(t_top, val="none")
    t_top.rows[0].cells[0].width = Inches(2.0)
    t_top.rows[0].cells[1].width = Inches(3.27)
    t_top.rows[0].cells[2].width = Inches(2.0)

    p_title = t_top.rows[0].cells[1].paragraphs[0]
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("心臓超音波検査報告書")
    r_title.font.size = Pt(16)
    r_title.font.bold = True

    p_date = t_top.rows[0].cells[2].paragraphs[0]
    p_date.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_date = p_date.add_run("実施日: 20   /   /   ")
    r_date.font.size = Pt(8.5)

    # 患者ヘッダー枠
    t_pat = doc.add_table(rows=5, cols=4)
    t_pat.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_pat, color="888888")
    col_w_pat = [Inches(1.2), Inches(2.5), Inches(1.1), Inches(2.47)]

    pat_rows_data = [
        [("患者ID: ", False), ("", False), ("病名:", True), ("", False)],
        [("フリガナ:", True), ("", False), ("", False), ("", False)],
        [("患者氏名:", True), ("", False), ("検査目的:", True), ("", False)],
        [("性別: 男 / 女   年齢:    歳", False), ("生年月日:      年   月   日", False), ("", False), ("", False)],
        [("身長:       cm    体重:       kg", False), ("BSA:         ㎡   依頼科/医:           科 /          ", False), ("病棟/外来:", True), ("入外: [ 入院 / 外来 ]", False)],
    ]
    for r_idx, row in enumerate(t_pat.rows):
        for c_idx, cell in enumerate(row.cells):
            cell.width = col_w_pat[c_idx]
            lbl, is_bold = pat_rows_data[r_idx][c_idx]
            cell.text = lbl
            p = cell.paragraphs[0]
            p.runs[0].font.size = Pt(7.5)
            if is_bold:
                p.runs[0].font.bold = True
            set_cell_margins(cell, top=30, bottom=30, left=50, right=50)

    # 3列ブロック（計測データ）
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

    # 3列のメインレイアウトテーブル（枠線なし）
    t_main = doc.add_table(rows=1, cols=3)
    t_main.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_main, val="none")
    col_w_main = [Inches(2.42), Inches(2.42), Inches(2.42)]
    for c_idx, cell in enumerate(t_main.rows[0].cells):
        cell.width = col_w_main[c_idx]
        set_cell_margins(cell, top=20, bottom=20, left=30, right=30)

    # --- 左列: Dimension & volume ---
    cell_c1 = t_main.rows[0].cells[0]
    t_c1 = cell_c1.add_table(rows=16, cols=3)
    set_table_borders(t_c1, color="B0B0B0")
    t_c1.rows[0].cells[0].merge(t_c1.rows[0].cells[1])
    t_c1.rows[0].cells[0].text = "【 Dimension & volume 】"
    t_c1.rows[0].cells[2].text = "基準値"
    set_cell_background(t_c1.rows[0].cells[0], "F1F5F9")
    set_cell_background(t_c1.rows[0].cells[2], "F1F5F9")
    t_c1.rows[0].cells[0].paragraphs[0].runs[0].font.bold = True
    t_c1.rows[0].cells[2].paragraphs[0].runs[0].font.bold = True

    c1_items = [
        ("RVD", "mm", ""),
        ("AOD", "mm", "(18～35)"),
        ("LAD", "mm", "(20～38)"),
        ("IVS", "mm", "(7～11)"),
        ("  motion", "", ""),
        ("LVPW", "mm", "(7～11)"),
        ("  motion", "", ""),
        ("LVDd", "mm", "(35～55)"),
        ("LVDs", "mm", "(22～44)"),
        ("EF", "%", "(55～83)"),
        ("FS", "%", "(>30)"),
        ("simpson EF", "%", "(>50)"),
        ("visual EF", "%", "(>50)"),
        ("LAV", "ml", ""),
        ("LAV(係数)", "ml/m²", "(16～34)"),
    ]
    for idx, item in enumerate(c1_items):
        row = t_c1.rows[idx+1]
        row.cells[0].width = Inches(1.1)
        row.cells[1].width = Inches(0.55)
        row.cells[2].width = Inches(0.77)
        row.cells[0].text = item[0]
        row.cells[1].text = f"    {item[1]}"
        row.cells[2].text = item[2]
        for c in row.cells:
            c.paragraphs[0].runs[0].font.size = Pt(7)
            set_cell_margins(c, top=20, bottom=20, left=30, right=30)

    # --- 中央列: LV inflow / TDI / PV flow ---
    cell_c2 = t_main.rows[0].cells[1]
    
    # LV inflow
    t_c2_1 = cell_c2.add_table(rows=5, cols=3)
    set_table_borders(t_c2_1, color="B0B0B0")
    t_c2_1.rows[0].cells[0].merge(t_c2_1.rows[0].cells[1])
    t_c2_1.rows[0].cells[0].text = "【 LV inflow 】"
    t_c2_1.rows[0].cells[2].text = "基準値"
    set_cell_background(t_c2_1.rows[0].cells[0], "F1F5F9")
    set_cell_background(t_c2_1.rows[0].cells[2], "F1F5F9")
    t_c2_1.rows[0].cells[0].paragraphs[0].runs[0].font.bold = True
    t_c2_1.rows[0].cells[2].paragraphs[0].runs[0].font.bold = True

    inflow_items = [
        ("E", "cm/s", "(54～92)"),
        ("A", "cm/s", "(52～88)"),
        ("E/A", "", ""),
        ("DcT", "ms", "(150～240)"),
    ]
    for idx, item in enumerate(inflow_items):
        row = t_c2_1.rows[idx+1]
        row.cells[0].text = item[0]
        row.cells[1].text = f"    {item[1]}"
        row.cells[2].text = item[2]
        for c in row.cells:
            c.paragraphs[0].runs[0].font.size = Pt(7)
            set_cell_margins(c, top=20, bottom=20, left=30, right=30)

    # TDI
    cell_c2.add_paragraph().paragraph_format.space_before = Pt(2)
    t_c2_2 = cell_c2.add_table(rows=6, cols=3)
    set_table_borders(t_c2_2, color="B0B0B0")
    t_c2_2.rows[0].cells[0].merge(t_c2_2.rows[0].cells[1])
    t_c2_2.rows[0].cells[0].text = "【 TDI 】"
    t_c2_2.rows[0].cells[2].text = "基準値"
    set_cell_background(t_c2_2.rows[0].cells[0], "F1F5F9")
    set_cell_background(t_c2_2.rows[0].cells[2], "F1F5F9")
    t_c2_2.rows[0].cells[0].paragraphs[0].runs[0].font.bold = True
    t_c2_2.rows[0].cells[2].paragraphs[0].runs[0].font.bold = True

    tdi_items = [
        ("Sep e'", "cm/s", "(7～16)"),
        ("Sep a'", "cm/s", ""),
        ("e'/a'", "", "(0.75～1.47)"),
        ("E/e'", "", "(4.5～9.0)"),
        ("lat e'", "cm/s", ""),
    ]
    for idx, item in enumerate(tdi_items):
        row = t_c2_2.rows[idx+1]
        row.cells[0].text = item[0]
        row.cells[1].text = f"    {item[1]}"
        row.cells[2].text = item[2]
        for c in row.cells:
            c.paragraphs[0].runs[0].font.size = Pt(7)
            set_cell_margins(c, top=20, bottom=20, left=30, right=30)

    # PV flow
    cell_c2.add_paragraph().paragraph_format.space_before = Pt(2)
    t_c2_3 = cell_c2.add_table(rows=6, cols=3)
    set_table_borders(t_c2_3, color="B0B0B0")
    t_c2_3.rows[0].cells[0].merge(t_c2_3.rows[0].cells[1])
    t_c2_3.rows[0].cells[0].text = "【 PV flow 】"
    t_c2_3.rows[0].cells[2].text = "基準値"
    set_cell_background(t_c2_3.rows[0].cells[0], "F1F5F9")
    set_cell_background(t_c2_3.rows[0].cells[2], "F1F5F9")
    t_c2_3.rows[0].cells[0].paragraphs[0].runs[0].font.bold = True
    t_c2_3.rows[0].cells[2].paragraphs[0].runs[0].font.bold = True

    pv_items = [
        ("S vel", "cm/s", "(41～62)"),
        ("D vel", "cm/s", "(28～50)"),
        ("S/D", "", ""),
        ("PVA vel", "cm/s", "(<35)"),
        ("PVA dur", "ms", "(<140)"),
    ]
    for idx, item in enumerate(pv_items):
        row = t_c2_3.rows[idx+1]
        row.cells[0].text = item[0]
        row.cells[1].text = f"    {item[1]}"
        row.cells[2].text = item[2]
        for c in row.cells:
            c.paragraphs[0].runs[0].font.size = Pt(7)
            set_cell_margins(c, top=20, bottom=20, left=30, right=30)

    # --- 右列: Aortic Valve / Mitral Valve / IVC / Pericardial ---
    cell_c3 = t_main.rows[0].cells[2]
    
    # Aortic Valve
    t_c3_1 = cell_c3.add_table(rows=6, cols=2)
    set_table_borders(t_c3_1, color="B0B0B0")
    t_c3_1.rows[0].cells[0].merge(t_c3_1.rows[0].cells[1])
    t_c3_1.rows[0].cells[0].text = "【 Aortic Valve 】"
    set_cell_background(t_c3_1.rows[0].cells[0], "F1F5F9")
    t_c3_1.rows[0].cells[0].paragraphs[0].runs[0].font.bold = True

    av_items = [
        ("Vel_max", "m/s"),
        ("PG_max", "mmHg"),
        ("AVA(Dop)", "cm²"),
        ("AVA(trace)", "cm²"),
        ("PG_mean", "mmHg"),
    ]
    for idx, item in enumerate(av_items):
        row = t_c3_1.rows[idx+1]
        row.cells[0].text = item[0]
        row.cells[1].text = f"       {item[1]}"
        for c in row.cells:
            c.paragraphs[0].runs[0].font.size = Pt(7)
            set_cell_margins(c, top=20, bottom=20, left=30, right=30)

    # Mitral Valve
    cell_c3.add_paragraph().paragraph_format.space_before = Pt(2)
    t_c3_2 = cell_c3.add_table(rows=6, cols=2)
    set_table_borders(t_c3_2, color="B0B0B0")
    t_c3_2.rows[0].cells[0].merge(t_c3_2.rows[0].cells[1])
    t_c3_2.rows[0].cells[0].text = "【 Mitral Valve 】"
    set_cell_background(t_c3_2.rows[0].cells[0], "F1F5F9")
    t_c3_2.rows[0].cells[0].paragraphs[0].runs[0].font.bold = True

    mv_items = [
        ("Vel_max", "m/s"),
        ("PG_max", "mmHg"),
        ("MVA(trace)", "cm²"),
        ("MVA(PHT)", "cm²"),
        ("PG_mean", "mmHg"),
    ]
    for idx, item in enumerate(mv_items):
        row = t_c3_2.rows[idx+1]
        row.cells[0].text = item[0]
        row.cells[1].text = f"       {item[1]}"
        for c in row.cells:
            c.paragraphs[0].runs[0].font.size = Pt(7)
            set_cell_margins(c, top=20, bottom=20, left=30, right=30)

    # IVC & Pericardial
    cell_c3.add_paragraph().paragraph_format.space_before = Pt(2)
    t_c3_3 = cell_c3.add_table(rows=4, cols=2)
    set_table_borders(t_c3_3, color="B0B0B0")
    t_c3_3.rows[0].cells[0].merge(t_c3_3.rows[0].cells[1])
    t_c3_3.rows[0].cells[0].text = "【 IVC & Pericardial effusion 】"
    set_cell_background(t_c3_3.rows[0].cells[0], "F1F5F9")
    t_c3_3.rows[0].cells[0].paragraphs[0].runs[0].font.bold = True

    t_c3_3.rows[1].cells[0].text = "呼気 / 吸気"
    t_c3_3.rows[1].cells[1].text = "   /    mm"
    t_c3_3.rows[2].cells[0].text = "呼吸性変動"
    t_c3_3.rows[2].cells[1].text = "       %"
    t_c3_3.rows[3].cells[0].text = "心嚢液(Effusion)"
    t_c3_3.rows[3].cells[1].text = "[ なし / 少量 / 多量 ]"
    for r in t_c3_3.rows[1:]:
        for c in r.cells:
            c.paragraphs[0].runs[0].font.size = Pt(7)
            set_cell_margins(c, top=20, bottom=20, left=30, right=30)

    # 弁膜症サマリー行
    doc.add_paragraph().paragraph_format.space_before = Pt(3)
    t_valv = doc.add_table(rows=2, cols=4)
    t_valv.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_valv, color="888888")
    t_valv.rows[0].cells[0].merge(t_valv.rows[0].cells[3])
    t_valv.rows[0].cells[0].text = "【 Valve regurgitation / stenosis 】"
    set_cell_background(t_valv.rows[0].cells[0], "F1F5F9")
    t_valv.rows[0].cells[0].paragraphs[0].runs[0].font.bold = True
    t_valv.rows[0].cells[0].paragraphs[0].runs[0].font.size = Pt(7.5)

    v_cols = [
        "【MV】 MR:   / MS:  ",
        "【AV】 AR:   / AS:  ",
        "【PV】 PR:   / PS:  \nendPG:    mmHg",
        "【TV】 TR:   / TS:  \nPG:    mmHg"
    ]
    for idx, c_text in enumerate(v_cols):
        cell = t_valv.rows[1].cells[idx]
        cell.width = Inches(1.81)
        cell.text = c_text
        cell.paragraphs[0].runs[0].font.size = Pt(7.5)
        set_cell_margins(cell, top=30, bottom=30, left=40, right=40)

    # 壁運動 (16/17 Segment スコア表)
    doc.add_paragraph().paragraph_format.space_before = Pt(3)
    t_wma = doc.add_table(rows=3, cols=2)
    t_wma.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_wma, color="888888")
    t_wma.rows[0].cells[0].width = Inches(5.27)
    t_wma.rows[0].cells[1].width = Inches(2.0)
    
    t_wma.rows[0].cells[0].text = "【 左室局所壁運動 (Wall Motion Score: 1-Norm, 2-Hypo, 3-Aki, 4-Dys, 5-Aneu) 】"
    t_wma.rows[0].cells[0].paragraphs[0].runs[0].font.bold = True
    t_wma.rows[0].cells[0].paragraphs[0].runs[0].font.size = Pt(7.5)
    set_cell_background(t_wma.rows[0].cells[0], "F1F5F9")
    
    t_wma.rows[0].cells[1].text = "壁運動分類基準"
    t_wma.rows[0].cells[1].paragraphs[0].runs[0].font.bold = True
    t_wma.rows[0].cells[1].paragraphs[0].runs[0].font.size = Pt(7.5)
    set_cell_background(t_wma.rows[0].cells[1], "F1F5F9")

    # 左側：セグメント記入表
    c_wma_l = t_wma.rows[1].cells[0]
    p_wl = c_wma_l.paragraphs[0]
    p_wl.text = (
        "Basal:   1.Ant[  ]   2.Ant-Sept[  ]   3.Inf-Sept[  ]   4.Inf[  ]   5.Inf-Lat[  ]   6.Ant-Lat[  ]\n"
        "Mid:     7.Ant[  ]   8.Ant-Sept[  ]   9.Inf-Sept[  ]  10.Inf[  ]  11.Inf-Lat[  ]  12.Ant-Lat[  ]\n"
        "Apical: 13.Ant[  ]  14.Sept[  ]      15.Inf[  ]      16.Lat[  ]  17.Apex[  ]\n"
        "※添付のBull's-eye・4腔・2腔・長軸断面図を参照"
    )
    if p_wl.runs:
        p_wl.runs[0].font.size = Pt(7)


    # 右側：スコア定義
    c_wma_r = t_wma.rows[1].cells[1]
    p_wr = c_wma_r.paragraphs[0]
    p_wr.text = (
        "1: Normal\n"
        "2: Mild Hypokinesis\n"
        "3: Hypokinesis\n"
        "4: Severe Hypokinesis\n"
        "5: Akinesis / Dyskinesis"
    )
    if p_wr.runs:
        p_wr.runs[0].font.size = Pt(7)

    for c in [c_wma_l, c_wma_r]:
        set_cell_margins(c, top=40, bottom=40, left=50, right=50)

    # 所見欄
    c_wma_bot = t_wma.rows[2].cells[0]
    c_wma_bot.merge(t_wma.rows[2].cells[1])
    c_wma_bot.text = (
        "所見 [検査所見並びに測定値の妥当性については判読医の承認が必要です]\n"
        "Chamber size      : \n"
        "LV contractility  : \n"
        "LV diastric func. : \n"
        "Asynergy          : \n"
        "総合コメント      : "
    )
    c_wma_bot.paragraphs[0].runs[0].font.size = Pt(7.5)
    set_cell_margins(c_wma_bot, top=40, bottom=40, left=50, right=50)

    # フッター署名欄
    doc.add_paragraph().paragraph_format.space_before = Pt(3)
    t_foot = doc.add_table(rows=1, cols=4)
    t_foot.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_foot, color="888888")
    t_foot.rows[0].cells[0].width = Inches(2.27)
    t_foot.rows[0].cells[1].width = Inches(1.5)
    t_foot.rows[0].cells[2].width = Inches(1.5)
    t_foot.rows[0].cells[3].width = Inches(2.0)

    t_foot.rows[0].cells[0].text = "国東市民病院"
    t_foot.rows[0].cells[0].paragraphs[0].runs[0].font.bold = True
    t_foot.rows[0].cells[0].paragraphs[0].runs[0].font.size = Pt(9)

    t_foot.rows[0].cells[1].text = "検査者: ________"
    t_foot.rows[0].cells[2].text = "診断医: ________"
    t_foot.rows[0].cells[3].text = "Page 1 / 2"
    for c in t_foot.rows[0].cells[1:]:
        c.paragraphs[0].runs[0].font.size = Pt(8)
    for c in t_foot.rows[0].cells:
        set_cell_margins(c, top=30, bottom=30, left=40, right=40)

    # ==========================================
    # PAGE 2: 詳細測定・血行動態・弁膜症精査
    # ==========================================
    doc.add_page_break()

    # Page 2 タイトル
    t_top2 = doc.add_table(rows=1, cols=3)
    t_top2.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_top2, val="none")
    t_top2.rows[0].cells[0].width = Inches(2.0)
    t_top2.rows[0].cells[1].width = Inches(3.27)
    t_top2.rows[0].cells[2].width = Inches(2.0)

    p_title2 = t_top2.rows[0].cells[1].paragraphs[0]
    p_title2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title2 = p_title2.add_run("心臓超音波検査報告書（詳細評価・血行動態）")
    r_title2.font.size = Pt(13)
    r_title2.font.bold = True

    p_p2_meta = t_top2.rows[0].cells[2].paragraphs[0]
    p_p2_meta.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_p2_meta.add_run("患者ID: ____________\n氏名: ____________")
    p_p2_meta.runs[0].font.size = Pt(8)

    # 1. 弁膜症詳細定量的評価テーブル
    p_h1 = doc.add_paragraph()
    p_h1.paragraph_format.space_before = Pt(4)
    p_h1.paragraph_format.space_after = Pt(2)
    r_h1 = p_h1.add_run("1. 弁膜症 詳細定量的評価 (Quantitative Valvular Assessment)")
    r_h1.font.bold = True
    r_h1.font.size = Pt(8.5)

    t_valv_detail = doc.add_table(rows=7, cols=5)
    t_valv_detail.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_valv_detail, color="888888")
    col_w_vd = [Inches(1.5), Inches(1.5), Inches(1.4), Inches(1.4), Inches(1.47)]
    vd_headers = ["対象弁", "計測項目", "計測値", "重症基準(目安)", "判定・形態所見"]
    for c_idx, cell in enumerate(t_valv_detail.rows[0].cells):
        cell.width = col_w_vd[c_idx]
        cell.text = vd_headers[c_idx]
        set_cell_background(cell, "F1F5F9")
        cell.paragraphs[0].runs[0].font.bold = True
        cell.paragraphs[0].runs[0].font.size = Pt(7.5)
        set_cell_margins(cell, top=30, bottom=30, left=40, right=40)

    vd_rows = [
        ["大動脈弁 (AS/AR)", "AVA (連続の式) / Vmax\nmean PG / DVI\nAR: PHT / VC", "   cm² /   m/s\n   mmHg /   \n   ms /   mm", "AVA < 1.0 cm²\nmeanPG ≥ 40 mmHg\nPHT < 200 ms", "[ なし / 軽度 / 中等度 / 重度 ]\n二尖弁 / 石灰化 [ - / + ]\nジェット: [ 中心性 / 偏位 ]"],
        ["僧帽弁 (MS/MR)", "MVA (PHT / プライニメトリ)\nmean PG\nMR: VC / EROA / RegVol", "   cm²\n   mmHg\n   mm /   cm² /   ml", "MVA ≤ 1.5 cm²\nmeanPG ≥ 5 mmHg\nVC ≥ 7mm / EROA≥0.4", "[ なし / 軽度 / 中等度 / 重度 ]\n逸脱: [ A1 A2 A3 / P1 P2 P3 ]\nテザリング / 腱索断裂"],
        ["三尖弁 (TS/TR)", "TR Vmax / TR-PG\nVC / 収縮期肝静脈逆流", "   m/s /   mmHg\n   mm / [ なし / あり ]", "TR Vmax > 2.8 m/s\nVC ≥ 7 mm (Severe)", "[ なし / 軽度 / 中等度 / 重度 ]\n弁輪拡大 / ペーシングリード"],
        ["肺動脈弁 (PS/PR)", "PR end-diastolic PG\nPS peak PG", "   mmHg\n   mmHg", "PR end-PG > 5 (PADP↑)\nPS peak > 64 (重症)", "[ なし / 軽度 / 中等度 / 重度 ]"],
        ["人工弁 (Prosthesis)", "種類 / 部位 / サイズ\npeak / mean PG / DVI", "   弁 (    mm)\n   /   mmHg /   ", "PPM疑い: [ - / + ]\n弁周囲逆流 (PVL): [ - / + ]", "開閉制限: [ なし / あり ]\nパンヌス / 血栓疑い: [ - / + ]"],
        ["感染性心内膜炎 (IE)", "疣贅 (Vegetation) 部位 / サイズ\n弁破壊・穿孔・膿瘍", "   弁 /   ×   mm\n[ なし / あり ]", "塞栓高リスク: > 10 mm", "可動性: [ 高 / 低 ]\n新規逆流悪化: [ なし / あり ]"],
    ]

    for r_idx, r_data in enumerate(vd_rows):
        row = t_valv_detail.rows[r_idx+1]
        for c_idx, cell in enumerate(row.cells):
            cell.width = col_w_vd[c_idx]
            cell.text = r_data[c_idx]
            cell.paragraphs[0].runs[0].font.size = Pt(7)
            set_cell_margins(cell, top=30, bottom=30, left=40, right=40)

    # 2. 右心系・肺高血圧 & 左室拡張能詳細
    p_h2 = doc.add_paragraph()
    p_h2.paragraph_format.space_before = Pt(4)
    p_h2.paragraph_format.space_after = Pt(2)
    r_h2 = p_h2.add_run("2. 右心機能・肺高血圧 & 拡張能・心室相互作用詳細")
    r_h2.font.bold = True
    r_h2.font.size = Pt(8.5)

    t_p2_split = doc.add_table(rows=1, cols=2)
    t_p2_split.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_p2_split, val="none")
    t_p2_split.rows[0].cells[0].width = Inches(3.63)
    t_p2_split.rows[0].cells[1].width = Inches(3.64)

    # 左側：右心系・肺高血圧
    c_rh = t_p2_split.rows[0].cells[0]
    t_rh = c_rh.add_table(rows=8, cols=3)
    set_table_borders(t_rh, color="888888")
    t_rh.rows[0].cells[0].merge(t_rh.rows[0].cells[2])
    t_rh.rows[0].cells[0].text = "【 右心機能・肺循環評価 】"
    set_cell_background(t_rh.rows[0].cells[0], "F1F5F9")
    t_rh.rows[0].cells[0].paragraphs[0].runs[0].font.bold = True
    t_rh.rows[0].cells[0].paragraphs[0].runs[0].font.size = Pt(7.5)

    rh_items = [
        ("三尖弁輪移動量 (TAPSE)", "     mm", "≥ 17 mm"),
        ("右室自由壁速度 (RV s')", "     cm/s", "≥ 9.5 cm/s"),
        ("右室面積変化率 (RV-FAC)", "     %", "≥ 35 %"),
        ("TR最大圧較差 (TR-PG)", "     mmHg", "≤ 31 mmHg"),
        ("推定右房圧 (RAP: IVC判定)", "     mmHg", "3 / 8 / 15 mmHg"),
        ("推定肺動脈圧 (ePASP)", "     mmHg", "≤ 35 mmHg"),
        ("肺動脈弁血流加速度時間(Act)", "     ms", "> 105 ms (ノッチ: -/+)"),
    ]
    for idx, item in enumerate(rh_items):
        row = t_rh.rows[idx+1]
        row.cells[0].width = Inches(1.8)
        row.cells[1].width = Inches(0.9)
        row.cells[2].width = Inches(0.93)
        row.cells[0].text = item[0]
        row.cells[1].text = item[1]
        row.cells[2].text = item[2]
        for c in row.cells:
            c.paragraphs[0].runs[0].font.size = Pt(7)
            set_cell_margins(c, top=20, bottom=20, left=30, right=30)

    # 右側：左室拡張能アルゴリズム
    c_df = t_p2_split.rows[0].cells[1]
    t_df = c_df.add_table(rows=8, cols=3)
    set_table_borders(t_df, color="888888")
    t_df.rows[0].cells[0].merge(t_df.rows[0].cells[2])
    t_df.rows[0].cells[0].text = "【 左室拡張能 & 充満圧評価 】"
    set_cell_background(t_df.rows[0].cells[0], "F1F5F9")
    t_df.rows[0].cells[0].paragraphs[0].runs[0].font.bold = True
    t_df.rows[0].cells[0].paragraphs[0].runs[0].font.size = Pt(7.5)

    df_items = [
        ("中隔 / 側壁 e'", "  /   cm/s", "中隔>7 / 側壁>10"),
        ("平均 E/e' 比", "    ", "≤ 14 (>14で充満圧↑)"),
        ("左房容積係数 (LAVI)", "     ml/m²", "> 34 ml/m²で拡大"),
        ("TR Vmax", "     m/s", "> 2.8 m/sで陽性"),
        ("肺静脈波 (Ar dur - A dur)", "     ms", "≥ 30 ms (LVEDP↑)"),
        ("Valsalva手技 E/A変化", "偽正常化解除", "ΔE/A ≥ 0.5"),
        ("拡張能判定グレード", "[ 正常 / G1弛緩低下 / G2偽正常 / G3拘束型 ]", ""),
    ]
    for idx, item in enumerate(df_items):
        row = t_df.rows[idx+1]
        row.cells[0].width = Inches(1.8)
        row.cells[1].width = Inches(0.9)
        row.cells[2].width = Inches(0.94)
        row.cells[0].text = item[0]
        row.cells[1].text = item[1]
        row.cells[2].text = item[2]
        for c in row.cells:
            c.paragraphs[0].runs[0].font.size = Pt(7)
            set_cell_margins(c, top=20, bottom=20, left=30, right=30)

    # 3. 特殊所見・心筋症・先天性・心嚢腔
    p_h3 = doc.add_paragraph()
    p_h3.paragraph_format.space_before = Pt(4)
    p_h3.paragraph_format.space_after = Pt(2)
    r_h3 = p_h3.add_run("3. 心筋症・短絡疾患・大動脈・その他の詳細所見")
    r_h3.font.bold = True
    r_h3.font.size = Pt(8.5)

    t_misc = doc.add_table(rows=4, cols=2)
    t_misc.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_misc, color="888888")
    t_misc.rows[0].cells[0].width = Inches(3.63)
    t_misc.rows[0].cells[1].width = Inches(3.64)

    misc_boxes = [
        ("心筋症・肥厚パターン (HCM, DCM, アミロイド等)", "肥大局在: [ 全周性 / 心室中隔 (ASH) / 心尖部 (Apical) ]   SAM: [ - / + ]\n心尖部動脈瘤: [ - / + ]   心筋輝度: [ 正常 / 顆粒状・粗荒 ]   心筋緻密化障害: [ - / + ]"),
        ("大動脈・解離・基部形態 (Aorta)", "Valsalva洞径:     mm   ST junction径:     mm   上行大動脈径:     mm\nフラップ/偽腔: [ なし / あり (Stanford A / B) ]   ULP/血腫: [ - / + ]"),
        ("先天性心疾患・短絡血流 (Shunt)", "ASD (心房中隔欠損) / PFO: [ なし / あり ] (欠損径:    mm / 右左短絡: - / +)\nVSD (心室中隔欠損): [ なし / あり ] (欠損部位: 周膜部 / 筋性部 / 漏斗部)\nPDA (動脈管開存) / その他奇形: [ なし / あり ]"),
        ("心嚢液・胸水・心腔内腫瘤/血栓", "心嚢液(PE): [ なし / 少量 / 中等量 / 大量 ] (右室拡張期虚脱/スウィング: - / +)\n胸水: [ なし / 左 / 右 / 両側 ]   血栓/腫瘍: [ なし / あり ] (部位:       サイズ:      )")
    ]
    for idx, (title, desc) in enumerate(misc_boxes):
        r_idx = idx // 2
        c_idx = idx % 2
        cell = t_misc.rows[r_idx].cells[c_idx]
        cell.text = f"【 {title} 】\n{desc}"
        cell.paragraphs[0].runs[0].font.size = Pt(7)
        set_cell_background(cell, "FAFAFA")
        set_cell_margins(cell, top=30, bottom=30, left=40, right=40)

    # 4. 2枚目 詳細考察・指導医コメント枠
    p_h4 = doc.add_paragraph()
    p_h4.paragraph_format.space_before = Pt(4)
    p_h4.paragraph_format.space_after = Pt(2)
    r_h4 = p_h4.add_run("4. 総合所見・治療方針への提言 (Clinical Recommendation & Summary)")
    r_h4.font.bold = True
    r_h4.font.size = Pt(8.5)

    t_detail_comm = doc.add_table(rows=1, cols=1)
    t_detail_comm.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_detail_comm, color="888888")
    c_dc = t_detail_comm.rows[0].cells[0]
    c_dc.width = Inches(7.27)
    c_dc.text = (
        "【詳細考察・前回比較・治療判定へのコメント】\n\n\n\n\n\n"
        "前回検査日 (    年   月   日) との比較:\n"
        "推奨追跡間隔 / 追加検査 (経食道エコー・心臓MRI・冠動脈CT等): "
    )
    c_dc.paragraphs[0].runs[0].font.size = Pt(7.5)
    set_cell_margins(c_dc, top=40, bottom=40, left=50, right=50)

    # Page 2 フッター
    doc.add_paragraph().paragraph_format.space_before = Pt(3)
    t_foot2 = doc.add_table(rows=1, cols=4)
    t_foot2.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_foot2, color="888888")
    t_foot2.rows[0].cells[0].width = Inches(2.27)
    t_foot2.rows[0].cells[1].width = Inches(1.5)
    t_foot2.rows[0].cells[2].width = Inches(1.5)
    t_foot2.rows[0].cells[3].width = Inches(2.0)

    t_foot2.rows[0].cells[0].text = "国東市民病院"
    t_foot2.rows[0].cells[0].paragraphs[0].runs[0].font.bold = True
    t_foot2.rows[0].cells[0].paragraphs[0].runs[0].font.size = Pt(9)

    t_foot2.rows[0].cells[1].text = "検査者: ________"
    t_foot2.rows[0].cells[2].text = "診断医: ________"
    t_foot2.rows[0].cells[3].text = "Page 2 / 2"
    for c in t_foot2.rows[0].cells[1:]:
        c.paragraphs[0].runs[0].font.size = Pt(8)
    for c in t_foot2.rows[0].cells:
        set_cell_margins(c, top=30, bottom=30, left=40, right=40)

    out_file = r"c:\Antigravity\超音波検査\心エコー\心臓超音波検査報告書_2枚組.docx"
    doc.save(out_file)
    print(f"File created at: {out_file}")

if __name__ == '__main__':
    build_report()
