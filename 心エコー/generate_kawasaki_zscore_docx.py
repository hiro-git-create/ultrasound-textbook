import os
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

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_cell_border(cell, **kwargs):
    """
    kwargs: top, bottom, left, right
    values: dict(sz=12, val='single', color='CBD5E1')
    """
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}/>')
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        edge_data = kwargs.get(edge)
        if edge_data:
            b_elm = parse_xml(f'<w:{edge} {nsdecls("w")} w:val="{edge_data.get("val","single")}" w:sz="{edge_data.get("sz","4")}" w:space="0" w:color="{edge_data.get("color","CBD5E1")}"/>')
            tcBorders.append(b_elm)
    tcPr.append(tcBorders)

def build_kawasaki_zscore_doc(output_path):
    doc = Document()
    
    # ページ余白 (A4)
    for section in doc.sections:
        section.top_margin = Inches(0.7)
        section.bottom_margin = Inches(0.7)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # 基本フォント設定
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Yu Gothic'
    font.size = Pt(9.5)
    font.color.rgb = RGBColor(30, 41, 59) # Slate 800

    # ドキュメントタイトル
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(2)
    r_title = p_title.add_run('川崎病・小児心エコーにおけるZスコア総合マニュアル')
    r_title.font.size = Pt(17)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(15, 23, 42)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(14)
    r_sub = p_sub.add_run('〜冠動脈・心腔計測の臨床的根拠、国内推奨式、および小児科医カンファレンス実践対話ガイド〜')
    r_sub.font.size = Pt(10.5)
    r_sub.font.color.rgb = RGBColor(71, 85, 105)

    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(f'■ {text}')
        r.font.size = Pt(12)
        r.font.bold = True
        r.font.color.rgb = RGBColor(26, 54, 93) # Navy Blue

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(f'▶ {text}')
        r.font.size = Pt(10.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(30, 64, 175) # Royal Blue

    def add_bullet(p, bold_prefix, text):
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.left_indent = Inches(0.2)
        r1 = p.add_run(f'• {bold_prefix}：')
        r1.font.bold = True
        r2 = p.add_run(text)

    # 1. エグゼクティブ・サマリー（結論）
    add_h1("1. エグゼクティブ・サマリー（結論と推奨式一覧）")
    
    table_sum = doc.add_table(rows=4, cols=4)
    table_sum.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_sum.autofit = False
    
    col_widths = [Inches(1.8), Inches(2.3), Inches(1.5), Inches(1.3)]
    headers = ["評価対象", "国内標準・第一推奨算出式", "計測基準手法", "国内シェア・位置づけ"]
    
    hdr_cells = table_sum.rows[0].cells
    for i, h_text in enumerate(headers):
        hdr_cells[i].width = col_widths[i]
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h_text)
        r.font.bold = True
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(255, 255, 255)
        set_cell_background(hdr_cells[i], "1E3A8A")
        set_cell_margins(hdr_cells[i], 120, 120, 120, 120)

    sum_data = [
        ("川崎病 冠動脈\n(LMCA/LAD/LCx/RCA)", "Z Score Project 式 (LMS法)\n/ 小林式 (Kobayashi et al.)", "2D Inner-to-inner\n(拡張末期)", "国内シェア第1位\n(JSPCCS/川崎病学会推奨)"),
        ("心腔・基部計測\n(LVDd, LAD, Ao, 弁輪等)", "Pettersen et al. (JASE 2008)\n(または日本人小児基準)", "2D Inner-to-inner\n(ASE小児ガイドライン)", "世界・国内デファクト\n(各社エコー装置標準)"),
        ("体表面積 (BSA)\n(全Zスコア共通)", "Haycock 式\n(Ht^0.3964 × Wt^0.5378 × 0.024265)", "身長・体重実測", "全式共通の絶対条件\n(DuBois式は乳児で不可)")
    ]

    for row_idx, row in enumerate(sum_data):
        cells = table_sum.rows[row_idx + 1].cells
        bg_col = "F8FAFC" if row_idx % 2 == 0 else "FFFFFF"
        for col_idx, text in enumerate(row):
            cells[col_idx].width = col_widths[col_idx]
            p = cells[col_idx].paragraphs[0]
            if col_idx in [2, 3]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(text)
            r.font.size = Pt(8.5)
            set_cell_background(cells[col_idx], bg_col)
            set_cell_margins(cells[col_idx], 80, 80, 100, 100)
            set_cell_border(cells[col_idx], bottom=dict(sz=4, val='single', color='E2E8F0'))

    # 2. なぜZスコアが必要なのか（絶対径基準の破綻）
    add_h1("2. なぜZスコアが必要なのか？（厚生省絶対径基準の破綻と根拠）")
    
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    p.add_run('小児領域では体重2kg〜60kg超まで体格が劇的に変化するため、大人のような固定カットオフ値は通用しません。従来の1984年厚生省基準（3mm/4mm/8mm）には以下の致命的リスクが存在します。')

    p1 = doc.add_paragraph()
    add_bullet(p1, "乳幼児における過小評価（偽陰性の危険）", "生後1〜6か月の乳児の正常LAD径は平均1.2〜1.5mmです。もし3.0mmに達していた場合、旧厚生省基準では「正常〜軽度拡大」と見逃されますが、乳児にとっては正常の2倍以上であり、Zスコア換算では Z > +5.0〜+8.0（中等度〜巨大動脈瘤）に相当します。適切な抗血栓療法が遅れる致命的リスクが生じます。")

    p2 = doc.add_paragraph()
    add_bullet(p2, "年長児における過剰診断（偽陽性の弊害）", "学童期（10歳以上）では正常冠動脈径自体が2.5〜3.0mm近くあります。絶対径3.0mmだけで「動脈瘤」と過剰診断される不利益を排除できます。")

    p3 = doc.add_paragraph()
    add_bullet(p3, "体表面積（BSA）計算式の重要性", "小林式やPettersen式の前提は「Haycock式」です。成人用DuBois式を1歳児（75cm, 10kg）に用いると、BSAが0.464 m²から0.437 m²へと約5.65%過小評価され、Zスコアが跳ね上がって判定がズレます。装置設定の統一が必須です。")

    # 決定論的検証テーブル
    add_h2("体格別 冠動脈径とZスコアの実算比較表")
    table_calc = doc.add_table(rows=4, cols=6)
    table_calc.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_calc.autofit = False
    col_w2 = [Inches(1.0), Inches(1.1), Inches(1.1), Inches(1.0), Inches(1.2), Inches(1.5)]
    h2_titles = ["年齢", "身長/体重", "Haycock BSA", "LAD実測径", "旧厚生省判定", "Zスコア判定 (小林式)"]
    
    for i, t in enumerate(h2_titles):
        c = table_calc.rows[0].cells[i]
        c.width = col_w2[i]
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(t)
        r.font.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)
        set_cell_background(c, "334155") # Slate 700
        set_cell_margins(c, 80, 80, 80, 80)

    calc_rows = [
        ("生後6か月", "66cm / 7.5kg", "0.377 m²", "3.0 mm", "正常〜境界域", "Z ≒ +6.5 (中等度瘤: 重症)"),
        ("1歳", "75cm / 10.0kg", "0.464 m²", "3.2 mm", "境界域", "Z ≒ +5.1 (中等度動脈瘤)"),
        ("5歳", "110cm / 18.0kg", "0.740 m²", "3.2 mm", "境界域", "Z ≒ +2.1 (軽度拡大にとどまる)")
    ]

    for r_idx, r_data in enumerate(calc_rows):
        cells = table_calc.rows[r_idx + 1].cells
        bg_col = "F1F5F9" if r_idx % 2 == 0 else "FFFFFF"
        for c_idx, val in enumerate(r_data):
            cells[c_idx].width = col_w2[c_idx]
            p = cells[c_idx].paragraphs[0]
            if c_idx in [0, 2, 3, 4]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.size = Pt(8.5)
            if c_idx == 5:
                r.font.bold = True
                if "重症" in val or "中等度" in val:
                    r.font.color.rgb = RGBColor(185, 28, 28) # Red
            set_cell_background(cells[c_idx], bg_col)
            set_cell_margins(cells[c_idx], 60, 60, 80, 80)
            set_cell_border(cells[c_idx], bottom=dict(sz=4, val='single', color='CBD5E1'))

    # 3. 最新ガイドライン分類基準（JCS/JSPCCS 2020）
    add_h1("3. 最新ガイドライン冠動脈病変分類（JCS/JSPCCS 2020年改訂版）")
    table_g = doc.add_table(rows=6, cols=4)
    table_g.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_g.autofit = False
    g_widths = [Inches(1.5), Inches(1.5), Inches(1.5), Inches(2.4)]
    g_headers = ["病変分類", "Zスコア基準", "絶対径条件", "臨床的意義・治療管理方針"]
    
    for i, h_text in enumerate(g_headers):
        c = table_g.rows[0].cells[i]
        c.width = g_widths[i]
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h_text)
        r.font.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)
        set_cell_background(c, "1E3A8A")
        set_cell_margins(c, 80, 80, 80, 80)

    g_data = [
        ("正常 (No involvement)", "Z < 2.0", "なし", "冠動脈内径の有意な拡大なし。IVIGへの反応を追跡。"),
        ("拡大 (Dilation only)", "2.0 ≤ Z < 2.5", "なし", "軽度・一過性拡大。血管周囲輝度亢進の併発に注意。"),
        ("小動脈瘤 (Small)", "2.5 ≤ Z < 5.0", "絶対径 < 4.0 mm", "明らかな冠動脈瘤。アスピリン継続、退縮と内膜肥厚観察。"),
        ("中等度動脈瘤 (Medium)", "5.0 ≤ Z < 10.0", "かつ 絶対径 < 8.0 mm", "血栓・将来の狭窄リスク高。抗血小板強化、頻回エコー。"),
        ("巨大動脈瘤 (Giant)", "Z ≥ 10.0", "または 絶対径 ≥ 8.0 mm", "破裂・血栓閉塞の超高リスク。アスピリン＋ワルファリン併用必須。")
    ]

    for r_idx, r_val in enumerate(g_data):
        cells = table_g.rows[r_idx + 1].cells
        bg_col = "FEF2F2" if r_idx == 4 else ("FFFBEB" if r_idx == 3 else ("FFFFFF" if r_idx % 2 == 0 else "F8FAFC"))
        for c_idx, val in enumerate(r_val):
            cells[c_idx].width = g_widths[c_idx]
            p = cells[c_idx].paragraphs[0]
            if c_idx in [1, 2]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.size = Pt(8.5)
            if r_idx == 4 and c_idx in [0, 1]:
                r.font.bold = True
                r.font.color.rgb = RGBColor(185, 28, 28)
            set_cell_background(cells[c_idx], bg_col)
            set_cell_margins(cells[c_idx], 60, 60, 80, 80)
            set_cell_border(cells[c_idx], bottom=dict(sz=4, val='single', color='E2E8F0'))

    # 4. 心腔計測Zスコアの臨床的知見
    add_h1("4. 心腔計測（Chamber）Zスコアの知見（汎心筋炎・大動脈炎の早期検出）")
    p_ch = doc.add_paragraph()
    p_ch.paragraph_format.space_before = Pt(2)
    p_ch.paragraph_format.space_after = Pt(4)
    p_ch.add_run('川崎病は冠動脈瘤だけでなく、本質的に「汎心筋炎（Pancarditis）」です。冠動脈瘤が出現する前の超急性期（第1〜4病日）から、心腔Zスコアを用いることで重症病態をいち早く捉えることができます。')

    table_ch = doc.add_table(rows=5, cols=4)
    table_ch.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_ch.autofit = False
    ch_widths = [Inches(1.8), Inches(1.3), Inches(1.5), Inches(2.3)]
    ch_headers = ["計測部位", "正常基準値", "異常判定閾値", "川崎病における臨床的病態と意義"]

    for i, h_text in enumerate(ch_headers):
        c = table_ch.rows[0].cells[i]
        c.width = ch_widths[i]
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h_text)
        r.font.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)
        set_cell_background(c, "0F766E") # Teal 700
        set_cell_margins(c, 80, 80, 80, 80)

    ch_data = [
        ("左室拡張末期径\n(LVDd)", "-2.0 ≤ Z ≤ +2.0", "Z > +2.0", "急性期心筋炎（Carditis）の合併。収縮不全（FS < 28%）やショック症候群（KDSS）のリスク。"),
        ("左房前後径 / 容積\n(LAD / LA vol)", "-2.0 ≤ Z ≤ +2.0", "Z > +2.0", "急性期弁膜炎に伴う僧帽弁逆流（MR）や、左室拡張末期圧上昇（容量負荷・心不全）を反映。"),
        ("大動脈基部・バルサルバ洞\n(Sinus of Valsalva / Ao)", "-2.0 ≤ Z ≤ +2.0", "Z > +2.0", "大動脈炎（Aortitis）・基部一過性拡張。弁輪拡大に伴うARや、IVIG不応・重症化の早期予測因子。"),
        ("心室中隔 / 後壁厚\n(IVSd / LVPWd)", "-2.0 ≤ Z ≤ +2.0", "Z > +2.0", "急性期心筋間質浮腫に伴う一過性の壁肥厚。炎症の活動性を反映。")
    ]

    for r_idx, r_val in enumerate(ch_data):
        cells = table_ch.rows[r_idx + 1].cells
        bg_col = "F0FDFA" if r_idx % 2 == 0 else "FFFFFF"
        for c_idx, val in enumerate(r_val):
            cells[c_idx].width = ch_widths[c_idx]
            p = cells[c_idx].paragraphs[0]
            if c_idx in [1, 2]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.size = Pt(8.5)
            set_cell_background(cells[c_idx], bg_col)
            set_cell_margins(cells[c_idx], 60, 60, 80, 80)
            set_cell_border(cells[c_idx], bottom=dict(sz=4, val='single', color='CCFBF1'))

    # 5. 心エコー計測の厳格な技術的根拠
    add_h1("5. 心エコー計測の厳格な技術的根拠（Inner-to-Innerと心電図同期）")
    p_tech1 = doc.add_paragraph()
    add_bullet(p_tech1, "Inner-to-Inner（内膜内縁間）計測の徹底", "冠動脈周囲の炎症に伴う高輝度エコー（Perivascular brightness）や外膜を含めず、対側の内膜内縁間を血管走行に直角に計測します。ゲインを上げすぎると側方音束幅増大（ブルーミング）により内腔が塗りつぶされて過小評価されます。ダイナミックレンジは45〜55dBに絞ります。")

    p_tech2 = doc.add_paragraph()
    add_bullet(p_tech2, "拡張末期フレーム（ECG同期）でのフリーズ", "小児の高心拍（120〜150 bpm）によるブレを抑えるため、心電図同期下の拡張末期（R波直後、または大動脈弁閉鎖後）で計測します。")

    p_tech3 = doc.add_paragraph()
    add_bullet(p_tech3, "高周波プローブとアコースティックズーム", "乳児（<10kg）は8〜12MHz高周波セクタまたはマイクロコンベックスを選択し、アコースティックズーム（RES）を用いてROIの走査線密度を高めて計測します。")

    # 6. 小児科Drとの対話・カンファレンストーク集
    add_h1("6. 小児科Drとの対話・カンファレンス実践トークスクリプト")
    
    add_h2("シーンA：乳児初回評価（絶対径は小さく見えるがZスコアが高い）")
    p_sa = doc.add_paragraph()
    p_sa.paragraph_format.left_indent = Inches(0.2)
    p_sa.paragraph_format.space_before = Pt(2)
    p_sa.paragraph_format.space_after = Pt(4)
    r_sa1 = p_sa.add_run('技師: ')
    r_sa1.font.bold = True
    p_sa.add_run('「先生、生後7か月（BSA 0.36 m²）の〇〇ちゃんのエコー結果です。LAD近位部の実測径は 2.2 mm ですが、小林式Zスコアで計算すると Z = +2.8（小型動脈瘤）の域に入っています。さらに、血管周囲の浮腫を反映した Perivascular brightness（輝度亢進）が明瞭に見られます。絶対径だけ見ると2mm台ですが、月齢補正するとすでに瘤形成が疑われますので、画像をマークしておきました。」\n')
    r_sa2 = p_sa.add_run('Drの反応例: ')
    r_sa2.font.bold = True
    r_sa2.font.color.rgb = RGBColor(30, 64, 175)
    p_sa.add_run('「2.2mmだから大丈夫かと思ったけれど、Zスコアだと+2.8もあるんだね。周囲の輝度亢進もあるなら、IVIG治療の反応を厳重にフォローしよう。」')

    add_h2("シーンB：急性期心筋炎合併の報告（LVDd拡大と収縮能低下）")
    p_sb = doc.add_paragraph()
    p_sb.paragraph_format.left_indent = Inches(0.2)
    p_sb.paragraph_format.space_before = Pt(2)
    p_sb.paragraph_format.space_after = Pt(4)
    r_sb1 = p_sb.add_run('技師: ')
    r_sb1.font.bold = True
    p_sb.add_run('「第4病日の〇〇ちゃんですが、冠動脈径はLAD 1.8mm（Z=+1.4）と正常内にとどまっています。しかし、左室拡張末期径（LVDd）が 31.8 mm、Pettersen式Zスコアで +2.85 と著明に拡大しており、FSも 23.8% まで低下しています。軽度MRと微量心嚢液も認め、急性期心筋炎（Carditis）を強く疑う所見です。」\n')
    r_sb2 = p_sb.add_run('Drの反応例: ')
    r_sb2.font.bold = True
    r_sb2.font.color.rgb = RGBColor(30, 64, 175)
    p_sb.add_run('「冠動脈だけでなくLVDd Zスコアが+2.8超で心筋炎を合併しているのか！IVIG中の循環動態と心不全兆候を厳重にモニタリングするよ。」')

    add_h2("シーンC：当院のレポート表記基準を提案するトーク（決定打）")
    p_sc = doc.add_paragraph()
    p_sc.paragraph_format.left_indent = Inches(0.2)
    p_sc.paragraph_format.space_before = Pt(2)
    p_sc.paragraph_format.space_after = Pt(4)
    r_sc1 = p_sc.add_run('技師: ')
    r_sc1.font.bold = True
    p_sc.add_run('「先生、当院でのZスコア運用ですが、学会推奨に基づき、冠動脈は日本人小児データに基づく『Z Score Project（LMS法）/ 小林式』、心腔・大動脈基部はエコー装置の世界標準である『Pettersen式（2D Inner-to-inner）』、体表面積は『Haycock式』で統一してよろしいでしょうか？ レポート上にも計算エンジン名を明記して運用いたします。」\n')
    r_sc2 = p_sc.add_run('Drの反応例: ')
    r_sc2.font.bold = True
    r_sc2.font.color.rgb = RGBColor(30, 64, 175)
    p_sc.add_run('「学会ガイドラインと装置の標準に揃えてもらえるなら一番安心だね。その方針でレポートを出してください。」')

    # 保存
    doc.save(output_path)
    print(f"Successfully generated docx at: {output_path}")

if __name__ == '__main__':
    target = r"c:\Antigravity\超音波検査\心エコー\川崎病_心エコーZスコア総合マニュアル_臨床対話ガイド.docx"
    build_kawasaki_zscore_doc(target)
