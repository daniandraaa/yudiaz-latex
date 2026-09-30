import docx
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

doc = docx.Document()

for s in doc.sections:
    s.top_margin = Inches(1.18)
    s.bottom_margin = Inches(1.18)
    s.left_margin = Inches(1.38)
    s.right_margin = Inches(1.18)

def format_p(p, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, line_spacing=1.5):
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing

def add_heading_1(text):
    p = doc.add_paragraph()
    format_p(p, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12, line_spacing=1.5)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(14)
    run.font.bold = True
    return p

def add_heading_2(text):
    p = doc.add_paragraph()
    format_p(p, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=6, line_spacing=1.5)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.bold = True
    return p

def add_body(text, indent=True):
    p = doc.add_paragraph()
    format_p(p, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, line_spacing=1.5)
    if indent:
        p.paragraph_format.first_line_indent = Inches(0.4)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    return p

# 1. COVER PAGE
p_title = doc.add_paragraph()
format_p(p_title, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)
r = p_title.add_run("LAPORAN BULANAN\nBULAN JULI TAHUN 2026\nMAGANG\nIT Core Charging\nPT XLSMART Telecom Sejahtera Tbk\nMonitoring Kegiatan Program MBKM di Universitas Telkom")
r.font.name = 'Times New Roman'
r.font.size = Pt(14)
r.font.bold = True

for _ in range(3):
    doc.add_paragraph()

p_by = doc.add_paragraph()
format_p(p_by, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)
r_by = p_by.add_run("oleh:\n")
r_by.font.name = 'Times New Roman'
r_by.font.size = Pt(12)
r_name = p_by.add_run("Daniandra Prayudisty Ilham\n103012300052")
r_name.font.name = 'Times New Roman'
r_name.font.size = Pt(13)
r_name.font.bold = True

for _ in range(4):
    doc.add_paragraph()

p_foot = doc.add_paragraph()
format_p(p_foot, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0)
r_foot = p_foot.add_run("S1 Informatika\nFakultas Informatika\nUniversitas Telkom\n2026")
r_foot.font.name = 'Times New Roman'
r_foot.font.size = Pt(12)
r_foot.font.bold = True

doc.add_page_break()

# 2. LEMBAR PENGESAHAN
add_heading_1("LEMBAR PENGESAHAN\nIT Core Charging\nDi PT XLSMART Telecom Sejahtera Tbk")
p_peng = doc.add_paragraph()
format_p(p_peng, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)
r_peng = p_peng.add_run("Disusun Oleh:\nDaniandra Prayudisty Ilham / 103012300052\n\nDisetujui dan disahkan sebagai Laporan Bulanan\nBulan Juli Tahun 2026 Magang MBKM")
r_peng.font.name = 'Times New Roman'
r_peng.font.size = Pt(12)

for _ in range(3):
    doc.add_paragraph()

t_sign = doc.add_table(rows=1, cols=2)
t_sign.alignment = WD_TABLE_ALIGNMENT.CENTER
t_sign.autofit = False
cell_l = t_sign.cell(0, 0)
cell_r = t_sign.cell(0, 1)

p_l = cell_l.paragraphs[0]
format_p(p_l, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=0)
r_l = p_l.add_run("Bandung, 15 September 2026\nMengetahui,\nPembimbing Lapangan,\n\n\n\n\n\nLukman Satria\nIT Core Charging")
r_l.font.name = 'Times New Roman'
r_l.font.size = Pt(12)

p_r = cell_r.paragraphs[0]
format_p(p_r, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=0)
r_r = p_r.add_run("Bandung, 15 September 2026\nMenyusun,\nMahasiswa,\n\n\n\n\n\nDaniandra Prayudisty Ilham\nNIM: 103012300052")
r_r.font.name = 'Times New Roman'
r_r.font.size = Pt(12)

doc.add_page_break()

# 3. RINGKASAN LAPORAN
add_heading_1("Ringkasan Laporan")
add_body("Bulan Juli 2026 merupakan bulan pertama bagi penulis dalam menjalankan kegiatan Praktik Kerja Magang MBKM secara penuh di unit IT Core Charging PT XLSMART Telecom Sejahtera Tbk. Penulis menangani pengujian fungsionalitas, validasi hierarki paket, serta verifikasi kelayakan rilis produk broadband Fixed Wireless Access (FWA) dan Fiber To The Home (FTTH), khususnya dalam ekosistem XL SATU.")
add_body("Kegiatan awal pada bulan ini diawali dengan pembekalan arsitektur industri, pemahaman konsep produk telekomunikasi (seperti produk Business As Usual / BAU, relasi dependency, pemisahan antara Technical Product dan Commercial Product), serta penyiapan perangkat kerja keamanan dan jaringan melalui Saviynt Identity Management dan konfigurasi VPN korporat. Memasuki fase operasional teknis, penulis bertanggung jawab dalam penyusunan skenario pengujian, eksekusi pengujian tiket produk komersial (antara lain FTTH Addon Upsell Speedbooster, skema diskon dan changeplan, integrasi bundling OTT Catchplay SVOD/TVOD, promo Tebus Murah, hingga penawaran khusus FWA Pilot), validasi alur order entry dan CPC Manager, serta verifikasi mekanisme penagihan berulang (recurring billing). Sepanjang bulan Juli 2026, seluruh 23 hari kerja terlaksana secara penuh di kantor (Work From Office / WFO) dengan pemenuhan target pengujian tiket rilis sesuai standar mutu yang ditetapkan oleh unit IT Core Charging.")

doc.add_page_break()

# 4. KATA PENGANTAR
add_heading_1("Kata Pengantar")
add_body("Puji dan syukur penulis panjatkan ke hadirat Allah SWT atas limpahan rahmat, hidayah, serta kekuatan-Nya, sehingga penulis dapat menyelesaikan Laporan Bulanan Magang MBKM untuk periode Bulan Juli Tahun 2026 di PT XLSMART Telecom Sejahtera Tbk dengan tepat waktu. Laporan ini disusun sebagai bagian dari evaluasi dan pemantauan berkala pelaksanaan program Magang Bersertifikat Kampus Merdeka (MBKM) di Universitas Telkom.")
add_body("Laporan ini menyajikan secara rinci aktivitas teknis harian, analisis capaian kerja, pemetaan kendala yang dihadapi, serta solusi yang diimplementasikan selama penulis menjalankan peran di unit IT Core Charging. Penulis menyadari bahwa kelancaran dan keberhasilan pelaksanaan program magang ini tidak terlepas dari bimbingan, arahan, dan dukungan dari berbagai pihak. Oleh karena itu, penulis ingin menyampaikan rasa terima kasih dan apresiasi yang sebesar-besarnya kepada:")

p_list = doc.add_paragraph()
format_p(p_list, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6)
r_list = p_list.add_run(
    "1. Allah SWT atas karunia dan kelancaran yang senantiasa dilimpahkan dalam setiap tahapan pekerjaan.\n"
    "2. Orang tua dan keluarga tercinta yang senantiasa memberikan doa, perhatian, dan motivasi tanpa henti.\n"
    "3. Bapak Lukman Satria, selaku Pembimbing Lapangan di unit IT Core Charging PT XLSMART Telecom Sejahtera Tbk, atas kesempatan, bimbingan teknis, serta arahan strategis yang sangat berharga selama pelaksanaan magang.\n"
    "4. Seluruh mentor, rekan engineer, dan staf di unit IT Core Charging yang telah menyambut, membimbing, dan berbagi pengetahuan teknis mengenai sistem telekomunikasi.\n"
    "5. Dosen Pembimbing Akademik dan segenap pengelola Program Magang MBKM Fakultas Informatika Universitas Telkom yang telah memfasilitasi dan mengawal proses magang ini.\n"
    "6. Rekan-rekan mahasiswa magang yang telah saling mendukung dan bertukar wawasan selama menjalani masa magang."
)
r_list.font.name = 'Times New Roman'
r_list.font.size = Pt(12)

add_body("Penulis menyadari bahwa dalam penulisan laporan ini masih terdapat ruang untuk penyempurnaan. Oleh karena itu, kritik dan saran yang konstruktif sangat penulis harapkan. Semoga laporan ini dapat memberikan manfaat nyata, baik sebagai bahan evaluasi pelaksanaan magang maupun referensi bagi mahasiswa selanjutnya.", indent=True)

p_ttd = doc.add_paragraph()
format_p(p_ttd, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=12)
r_ttd = p_ttd.add_run("Bandung, 15 September 2026\n\n\nDaniandra Prayudisty Ilham")
r_ttd.font.name = 'Times New Roman'
r_ttd.font.size = Pt(12)
r_ttd.font.bold = True

doc.add_page_break()

# 5. BAB I PENDAHULUAN
add_heading_1("BAB I\nPENDAHULUAN")
add_heading_2("1.1 Latar Belakang")
add_body("Perkembangan industri teknologi informasi dan telekomunikasi saat ini menuntut keandalan sistem yang beroperasi dengan ketersediaan tinggi (high availability) dan tingkat presisi penagihan data yang sempurna. Program Magang Merdeka Belajar Kampus Merdeka (MBKM) memberikan sarana bagi mahasiswa untuk terjun langsung ke dalam dinamika operasional industri skala nasional. Pelaksanaan program magang ini bertempat di PT XLSMART Telecom Sejahtera Tbk, sebuah entitas telekomunikasi terkemuka yang merupakan hasil integrasi strategis antara operator besar nasional (PT XL Axiata Tbk, PT Smartfren Telecom Tbk, dan PT Smart Telecom) yang resmi berlaku sejak 16 April 2025.")
add_body("Proses konsolidasi sistem berskala masif tersebut menciptakan kebutuhan mendesak akan penjaminan mutu pada sistem inti pengisian pulsa, kuota, dan penagihan pelanggan (Core Charging & Billing). Penulis ditempatkan pada unit IT Core Charging dengan fokus penugasan pengujian produk dan konfigurasi sistem. Dalam unit ini, setiap konfigurasi paket data, penawaran promo, aturan diskon, penagihan berulang (recurring), maupun integrasi bundling layanan bernilai tambah (Value-Added Services seperti OTT) harus melalui pengujian verifikasi menyeluruh sebelum dapat dilepas ke sistem produksi. Penempatan ini memberikan kesempatan berharga bagi penulis untuk mengaplikasikan prinsip rekayasa perangkat lunak secara langsung pada infrastruktur telekomunikasi skala nyata.")

add_heading_2("1.2 Ruang Lingkup")
add_body("Ruang lingkup pelaksanaan program Magang MBKM di PT XLSMART Telecom Sejahtera Tbk pada unit IT Core Charging mencakup beberapa area kerja utama:")
p_rl = doc.add_paragraph()
format_p(p_rl, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6)
r_rl = p_rl.add_run(
    "1) Setup Lingkungan Uji dan Keamanan Akses: Pengaturan akses identitas melalui Saviynt, konfigurasi jaringan aman VPN perusahaan, konfigurasi proxy internal, serta penyiapan perangkat pengujian database dan API (Postman, DBeaver, Katalon Studio).\n"
    "2) Analisis Hierarki dan Spesifikasi Produk Telekomunikasi: Pemahaman relasi arsitektural produk katalog, mencakup dekomposisi produk komersial (Commercial Product), produk teknis (Technical Product), relasi ketergantungan (dependency), dan aturan produk operasional harian (Business As Usual / BAU).\n"
    "3) Perancangan dan Penyusunan Skenario Pengujian (Test Design): Penyusunan test scenario dan test case komprehensif berdasarkan tiket penugasan produk baru, mencakup pengujian jalur normal (positive testing), jalur alternatif/kondisi batas (edge case), serta validasi kegagalan sistem (negative testing).\n"
    "4) Eksekusi Pengujian Produk FWA & FTTH (XL SATU): Pelaksanaan pengujian fungsional end-to-end pada produk Fixed Wireless Access (FWA) dan Fiber To The Home (FTTH), verifikasi provisioning Real MDN (Mobile Directory Number), pengujian modul Speedbooster, promo Tebus Murah, hingga penawaran Pilot.\n"
    "5) Verifikasi Integrasi Billing & Penagihan Berulang (Recurring): Pengujian siklus tagihan otomatis (recurring), penerapan whitelist diskon, pergantian paket (changeplan), serta integrasi bundling layanan streaming konten (OTT Bundling Catchplay SVOD/TVOD)."
)
r_rl.font.name = 'Times New Roman'
r_rl.font.size = Pt(12)

add_heading_2("1.3 Tujuan")
add_body("Tujuan utama yang ingin dicapai melalui pelaksanaan program Magang MBKM pada bulan Juli 2026 adalah sebagai berikut:")
p_tj = doc.add_paragraph()
format_p(p_tj, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6)
r_tj = p_tj.add_run(
    "1. Menerapkan keilmuan informatika dan rekayasa perangkat lunak yang diperoleh di Universitas Telkom ke dalam proses pengujian sistem telekomunikasi skala industri.\n"
    "2. Memahami siklus hidup penjaminan mutu produk pada unit IT Core Charging, mulai dari analisis tiket kebutuhan, perancangan skenario uji, hingga eksekusi validasi.\n"
    "3. Menguasai penggunaan perkakas industri seperti Postman, DBeaver, Katalon Studio, Salesforce CPQ/Product Manager, dan infrastruktur VPN korporat.\n"
    "4. Memperoleh kompetensi teknis mengenai arsitektur produk telekomunikasi modern, khususnya ekosistem konvergensi layanan tetap dan nirkabel (FWA dan FTTH XL SATU).\n"
    "5. Mengembangkan profesionalisme, kedisiplinan kerja, etika industri, dan keterampilan komunikasi lintas tim kerja."
)
r_tj.font.name = 'Times New Roman'
r_tj.font.size = Pt(12)

doc.add_page_break()

# 6. BAB II KEGIATAN MAGANG
add_heading_1("BAB II\nKEGIATAN MAGANG DI PT XLSMART TELECOM SEJAHTERA TBK")
add_heading_2("II.1 Rincian Kegiatan Magang di PT XLSMART Telecom Sejahtera Tbk pada Bulan Juli Tahun 2026")
add_body("Pelaksanaan kegiatan magang pada bulan Juli 2026 berlangsung selama 23 hari kerja efektif (1 s.d. 31 Juli 2026) dengan status kehadiran 100% di kantor (Work From Office / WFO). Rekapitulasi mingguan pelaksanaan kegiatan disajikan sebagai berikut:")

# Weekly table
t_week = doc.add_table(rows=6, cols=3)
t_week.alignment = WD_TABLE_ALIGNMENT.CENTER
t_week.style = 'Table Grid'
hdr_cells = t_week.rows[0].cells
hdr_cells[0].text = "No"
hdr_cells[1].text = "Minggu"
hdr_cells[2].text = "Kegiatan Utama"
for cell in hdr_cells:
    shading_elm = parse_xml(r'<w:shd {} w:fill="D9D9D9"/>'.format(nsdecls('w')))
    cell._tc.get_or_add_tcPr().append(shading_elm)
    for p in cell.paragraphs:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.bold = True
            r.font.name = 'Times New Roman'

week_data = [
    ("1", "Pertama (1-3 Juli)", "Onboarding unit IT Core Charging, pengenalan konsep produk (BAU, Dependency, Technical Product, Commercial Product), hierarki produk telekomunikasi, registrasi Saviynt, konfigurasi VPN, instalasi Katalon Studio, Postman, DBeaver, dan peluncuran 'XLSMART FutureReady'."),
    ("2", "Kedua (6-10 Juli)", "Knowledge sharing Salesforce (SF) FWA dan FTTH, verifikasi aktivasi VPN, pengerjaan tiket pengujian perdana FTTH ADDON UPSELL SPEEDBOOSTER V1, serta perancangan skenario FTTH Whitelist Discount & Changeplan."),
    ("3", "Ketiga (13-17 Juli)", "Pengujian recurring Speedbooster, perancangan skenario dan validasi tiket bundling OTT Catchplay SVOD & TVOD (FTTH & FWA), pengenalan konsep BAU, skenario promo Tebus Murah, order entry, dan CPC Manager."),
    ("4", "Keempat (20-24 Juli)", "Testing produk Tebus Murah V01, validasi Change Price DRF, pengujian Speedbooster 150 Mbps Open Eligibility, perancangan skenario dan testing FWA Create Special Offer 1 Month Pilot, serta sesi pemahaman provisioning Real MDN FWA."),
    ("5", "Kelima (27-31 Juli)", "Pengujian tiket Special Offer 1 Month Pilot V3, implementasi produk BAU, perancangan skenario dan eksekusi testing XL SATU FWA 100 Mbps 3 Month 650K, varian Outdoor berskema diskon, konsep recurring, serta Hard Bundling XL Satu PV with OTT.")
]

for idx, (no, w, desc) in enumerate(week_data, start=1):
    row_cells = t_week.rows[idx].cells
    row_cells[0].text = no
    row_cells[1].text = w
    row_cells[2].text = desc
    row_cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    for cell in row_cells:
        for p in cell.paragraphs:
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(10)

doc.add_paragraph()
add_body("Adapun rincian aktivitas harian beserta status kehadiran selama bulan Juli 2026 disajikan secara lengkap pada tabel berikut:")

# Logbook table
daily_logs = [
    ("1", "Rabu, 1 Juli 2026", "WFO", "Meeting sharing item dengan tim Core Charging, pengenalan konsep produk (BAU, Dependency, Technical Product, Commercial Product), hierarki produk telekomunikasi, registrasi akun identitas XLSMART pada Saviynt, dan pengajuan akses VPN korporat."),
    ("2", "Kamis, 2 Juli 2026", "WFO", "Konfigurasi dan setup koneksi VPN, instalasi dan pembelajaran awal Katalon Studio untuk QA Automation Product, serta menghadiri agenda peluncuran inovasi perusahaan 'XLSMART FutureReady'."),
    ("3", "Jumat, 3 Juli 2026", "WFO", "Pendalaman penggunaan Katalon Studio, meeting checkpoint progress automation, konfigurasi lingkungan uji QA Salesforce Product (Wifi internal, pengaturan proxy, Postman collection, DBeaver database client), dan pembelajaran hierarki creation."),
    ("4", "Senin, 6 Juli 2026", "WFO", "Mengikuti sesi Knowledge Sharing mengenai Fixed Wireless Access (FWA) pada lingkungan Salesforce (SF)."),
    ("5", "Selasa, 7 Juli 2026", "WFO", "Mengikuti sesi Knowledge Sharing mengenai arsitektur Fiber To The Home (FTTH) pada lingkungan Salesforce (SF)."),
    ("6", "Rabu, 8 Juli 2026", "WFO", "Meeting sharing item mingguan, verifikasi aktivasi akun VPN, pengujian penggunaan VPN untuk akses server internal."),
    ("7", "Kamis, 9 Juli 2026", "WFO", "Mengerjakan penugasan tiket pengujian produk FTTH ADDON UPSELL SPEEDBOOSTER V1."),
    ("8", "Jumat, 10 Juli 2026", "WFO", "Menyiapkan matriks skenario testing komprehensif pada tiket FTTH Whitelist Discount & Changeplan."),
    ("9", "Senin, 13 Juli 2026", "WFO", "Sesi sharing knowledge lanjutan mengenai FWA, dilanjutkan pelaksanaan testing produk ADDON UPSELL SPEEDBOOSTER V1."),
    ("10", "Selasa, 14 Juli 2026", "WFO", "Melakukan validasi pengujian siklus penagihan berkala (Recurring Test) dan Complete Test pada tiket ADDON UPSELL SPEEDBOOSTER V1."),
    ("11", "Rabu, 15 Juli 2026", "WFO", "Persiapan dan pembuatan skenario testing pada tiket CATCHPLAY SVOD & TVOD, serta analisis Create Product For Change plan V2."),
    ("12", "Kamis, 16 Juli 2026", "WFO", "Eksekusi testing produk Catchplay SVOD & TVOD pada stream layanan FTTH dan FWA, serta sesi sharing knowledge FWA."),
    ("13", "Jumat, 17 Juli 2026", "WFO", "Sharing knowledge proses bisnis produk BAU, pembuatan skenario testing produk TEBUS MURAH, testing konfigurasi Config DRF OTT XLSATU, serta pembelajaran alur Order Entry dan CPC Manager."),
    ("14", "Senin, 20 Juli 2026", "WFO", "Testing produk TEBUS MURAH V01, validasi Change Price DRF (acuan surel subjek 19 Juni 2026), serta pengujian tiket Add On Speedbooster 150 Mbps & Open Eligibility."),
    ("15", "Selasa, 21 Juli 2026", "WFO", "Meeting sharing session ekosistem produk XL SATU dan tata cara verifikasi teknis pada additional offer."),
    ("16", "Rabu, 22 Juli 2026", "WFO", "Menyiapkan matriks skenario testing pada tiket promo FWA CREATE SPECIAL OFFER 1 MONTH Pilot."),
    ("17", "Kamis, 23 Juli 2026", "WFO", "Melaksanakan eksekusi pengujian fungsional dan eligibilitas pada tiket FWA CREATE SPECIAL OFFER 1 MONTH Pilot."),
    ("18", "Jumat, 24 Juli 2026", "WFO", "Sesi sharing session mengenai metodologi provisioning Real MDN pada layanan FWA dan penyiapan test case untuk tiket rilis berikutnya."),
    ("19", "Senin, 27 Juli 2026", "WFO", "Pengerjaan, verifikasi ulang, dan validasi tiket promo CREATE SPECIAL OFFER 1 MONTH Pilot V3."),
    ("20", "Selasa, 28 Juli 2026", "WFO", "Sesi sharing session mengenai lanjutan tata kelola Real MDN, pendalaman operasional produk BAU, serta pengerjaan penyesuaian produk BAU."),
    ("21", "Rabu, 29 Juli 2026", "WFO", "Membuat skenario dan melakukan testing pada tiket XL SATU FWA 100 MBPS 3 MONTH 650K, serta varian XL SATU FWA 75 MBPS - 250 MBPS OUTDOOR."),
    ("22", "Kamis, 30 Juli 2026", "WFO", "Mengikuti sesi sharing session mendalam mengenai konsep perhitungan dan penagihan recurring pada produk FWA dan FTTH."),
    ("23", "Jumat, 31 Juli 2026", "WFO", "Merancang test scenario dan mengeksekusi pengujian pada tiket XL SATU FWA 750 MBPS 250 MBPS OUTDOOR (Discount), Hard Bundling XL Satu PV with OTT, dan XL SATU FWA MONTHLY NON PROMO.")
]

t_daily = doc.add_table(rows=len(daily_logs)+1, cols=4)
t_daily.alignment = WD_TABLE_ALIGNMENT.CENTER
t_daily.style = 'Table Grid'

d_hdr = t_daily.rows[0].cells
d_hdr[0].text = "No"
d_hdr[1].text = "Hari, Tanggal"
d_hdr[2].text = "Status"
d_hdr[3].text = "Uraian Kegiatan"
for cell in d_hdr:
    shading_elm = parse_xml(r'<w:shd {} w:fill="D9D9D9"/>'.format(nsdecls('w')))
    cell._tc.get_or_add_tcPr().append(shading_elm)
    for p in cell.paragraphs:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.bold = True
            r.font.name = 'Times New Roman'

for idx, (no, d, st, act) in enumerate(daily_logs, start=1):
    r_cells = t_daily.rows[idx].cells
    r_cells[0].text = no
    r_cells[1].text = d
    r_cells[2].text = st
    r_cells[3].text = act
    r_cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_cells[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_cells[2].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    for cell in r_cells:
        for p in cell.paragraphs:
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(9.5)

doc.add_paragraph()
add_body("Secara keseluruhan, jumlah hari kerja yang tercatat pada bulan Juli 2026 adalah 23 hari, seluruhnya berstatus Work From Office (WFO).")

doc.add_page_break()

# 7. ANALISA HASIL KEGIATAN, HAMBATAN, REKOMENDASI
add_heading_2("II.2 Analisa Hasil Kegiatan")
add_body("1) Penguasaan Dekomposisi Produk Telekomunikasi: Pemahaman yang mendalam mengenai pemisahan antara Commercial Product dan Technical Product terbukti menjadi faktor krusial. Pada unit IT Core Charging, pengujian tidak hanya memverifikasi tampilan penawaran di sisi pengguna, melainkan harus memvalidasi relasi dependensi teknis di database (melalui DBeaver dan CPC Manager) guna mencegah kesalahan provisioning pada level jaringan.")
add_body("2) Verifikasi Rigoritas Ekosistem XL SATU (FWA & FTTH): Karakteristik teknis antara layanan nirkabel FWA dan kabel serat optik FTTH memiliki parameter aktivasi yang berbeda. Pada FWA, keberadaan validasi Real MDN sangat menentukan keberhasilan registrasi modem router, sedangkan pada FTTH, pemetaan port dan kapasitas bandwidth menjadi tumpuan utama. Pengujian yang dilakukan penulis berhasil memastikan kedua stream tersebut memiliki konsistensi aturan bisnis.")
add_body("3) Ketelitian Pengujian Mekanisme Recurring dan Diskon: Fitur penagihan berkala (recurring billing) dan skema potongan harga (whitelist discount) merupakan area dengan risiko finansial tinggi. Pengujian tiket Speedbooster dan Special Offer Pilot menuntut verifikasi teliti pada tanggal jatuh tempo, perpanjangan otomatis kuota, pemotongan saldo/invoicing, serta pemulihan kecepatan normal apabila masa aktif paket berakhir.")
add_body("4) Validasi Kemitraan Digital (Value-Added OTT Bundling): Pengujian produk bundling Catchplay SVOD & TVOD memperluas wawasan penulis mengenai integrasi API lintas platform pihak ketiga. Penulis berhasil memvalidasi bahwa setiap pembelian paket bundling internet XL SATU secara otomatis menerbitkan token otorisasi langganan video yang dapat diakses langsung oleh pelanggan tanpa hambatan otentikasi.")
add_body("5) Penerapan Siklus Penjaminan Mutu Berkelanjutan: Keterlibatan dalam perancangan skenario hingga eksekusi pengujian melatih kedisiplinan pencatatan hasil uji secara sistematis, pelaporan defect yang dapat direproduksi (reproducible bug), serta penyampaian rekomendasi teknis yang konstruktif sebelum tiket dinyatakan siap rilis (Ready for Deployment).")

add_heading_2("II.3 Hambatan dan Upaya untuk Mengatasinya")
p_h1 = doc.add_paragraph()
format_p(p_h1, space_after=4)
r_h1 = p_h1.add_run("Hambatan 1: Ketergantungan Akses Identitas dan Stabilitas Jaringan VPN Korporat\nPada awal masa magang (pekan pertama), penulis belum dapat mengakses sistem pengujian internal secara penuh karena proses verifikasi akun pada Saviynt Identity Management dan sertifikat VPN membutuhkan tahapan persetujuan keamanan berjenjang.")
r_h1.font.name = 'Times New Roman'
r_h1.font.size = Pt(12)

p_u1 = doc.add_paragraph()
format_p(p_u1, space_after=8)
r_u1 = p_u1.add_run("Upaya Mengatasi:\nPenulis memanfaatkan waktu tunggu tersebut secara proaktif dengan mempelajari dokumentasi arsitektur produk, materi presentasi sistem, dan pedoman produk BAU yang telah diunduh sebelumnya. Penulis juga berkoordinasi aktif dengan IT Helpdesk dan mentor pembimbing sehingga proses aktivasi VPN dapat tuntas sebelum pekan kedua dimulai.")
r_u1.font.name = 'Times New Roman'
r_u1.font.size = Pt(12)

p_h2 = doc.add_paragraph()
format_p(p_h2, space_after=4)
r_h2 = p_h2.add_run("Hambatan 2: Kompleksitas Matriks Skenario Uji pada Tiket Bundling Berdiskon\nPada saat menguji produk berskema kombinasi rumit (seperti bundling XL SATU Outdoor dengan diskon khusus dan langganan OTT), terdapat banyak permutasi kondisi batas (edge case), seperti eligibilitas pelanggan lama versus pelanggan baru, status perangkat, dan kegagalan provisioning nomor MDN.")
r_h2.font.name = 'Times New Roman'
r_h2.font.size = Pt(12)

p_u2 = doc.add_paragraph()
format_p(p_u2, space_after=12)
r_u2 = p_u2.add_run("Upaya Mengatasi:\nPenulis mengatasi kendala ini dengan membangun tabel matriks skenario uji (decision table) yang terstruktur sebelum pengujian dimulai. Penulis juga aktif berkonsultasi dalam sesi sharing harian bersama mentor untuk memverifikasi alur logika sistem sebelum tiket dieksekusi di lingkungan uji.")
r_u2.font.name = 'Times New Roman'
r_u2.font.size = Pt(12)

add_heading_2("II.4 Rekomendasi")
p_rek = doc.add_paragraph()
format_p(p_rek, space_after=12)
r_rek = p_rek.add_run(
    "• Standarisasi Template Matriks Uji FWA/FTTH: Unit IT Core Charging disarankan menyusun repositori template skenario uji standar untuk produk turunan broadband (Addon, Speedbooster, Promo Pilot) agar pengujian tiket baru memiliki acuan konsisten dan memangkas waktu penyusunan skenario dari nol.\n"
    "• Penyiapan Test Data Management (TDM) Mandiri: Penyediaan bank data akun uji dan nomor uji (Test MDN) yang siap pakai di lingkungan staging akan sangat membantu mempercepat proses pengujian tanpa harus menunggu pembuatan nomor dummy secara manual.\n"
    "• Eksplorasi Otomasi Skrip Regression Testing: Skenario pengujian yang bersifat rutin dan berulang (seperti verifikasi harga paket dan skema changeplan standar) direkomendasikan untuk secara bertahap dialihkan ke pengujian otomatis menggunakan Katalon Studio guna meningkatkan efisiensi sprint."
)
r_rek.font.name = 'Times New Roman'
r_rek.font.size = Pt(12)

doc.add_page_break()

# 8. BAB III PENUTUP
add_heading_1("BAB III\nPENUTUP")
add_heading_2("III.1 Kesimpulan")
add_body("Pelaksanaan program Magang MBKM pada bulan Juli 2026 di unit IT Core Charging PT XLSMART Telecom Sejahtera Tbk telah berjalan dengan lancar dan sukses. Seluruh rangkaian penugasan teknis yang tercatat pada 23 hari kerja WFO berhasil diselesaikan dengan baik, mencakup:")
p_kes = doc.add_paragraph()
format_p(p_kes, space_after=12)
r_kes = p_kes.add_run(
    "1. Keberhasilan onboarding dan penyiapan infrastruktur pengujian (Saviynt, VPN, Postman, DBeaver, Katalon).\n"
    "2. Penguasaan konsep hierarki produk telekomunikasi (Commercial vs Technical Product, dependency, BAU).\n"
    "3. Perancangan skenario dan eksekusi pengujian fungsional pada tiket-tiket strategis broadband XL SATU (FTTH Addon Speedbooster, Whitelist Discount, Catchplay SVOD/TVOD bundling, Tebus Murah, FWA Special Offer Pilot 1 Month, dan varian Outdoor).\n"
    "4. Pemahaman mendalam mengenai alur order entry, CPC Manager, alokasi Real MDN, serta validasi penagihan berulang (recurring billing)."
)
r_kes.font.name = 'Times New Roman'
r_kes.font.size = Pt(12)

add_heading_2("III.2 Saran")
p_sar = doc.add_paragraph()
format_p(p_sar, space_after=12)
r_sar = p_sar.add_run(
    "1. Bagi Mahasiswa: Diharapkan terus memperdalam integrasi antara pengujian fungsional manual dan otomasi skrip (Katalon), serta memperkuat kemampuan kueri basis data pada tabel transaksi charging untuk validasi backend yang lebih mendalam.\n"
    "2. Bagi Perusahaan: Kerjasama yang telah terjalin sangat baik antara mentor unit IT Core Charging dan peserta magang diharapkan terus dipertahankan, terutama melalui keterlibatan langsung mahasiswa dalam proyek-proyek rilis sistem baru yang menantang."
)
r_sar.font.name = 'Times New Roman'
r_sar.font.size = Pt(12)

output_path = "/home/daniilham/Laporan_Bulanan_MBKM_Juli_2026_Daniandra_Prayudisty_Ilham.docx"
doc.save(output_path)
print(f"DOCX saved to {output_path}")
