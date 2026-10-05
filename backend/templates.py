from typing import Dict

TEMPLATES: Dict[str, Dict[str, str]] = {
    "blank": {
        "name": "Blank Document",
        "description": "Minimal clean LaTeX starter document",
        "main.tex": r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{hyperref}

\title{Dokumen Baru}
\author{Daniandra Prayudisty}
\date{\today}

\begin{document}
\maketitle

\section{Pendahuluan}
Mulai menulis dokumen LaTeX Anda di sini.

\end{document}
"""
    },
    "surat_undangan": {
        "name": "Surat Undangan Resmi & Dinas",
        "description": "Format surat resmi kedinasan/organisasi lengkap dengan kop surat, nomor surat, dan tanda tangan",
        "main.tex": r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[left=2.5cm,right=2.5cm,top=2cm,bottom=2.5cm]{geometry}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{xcolor}
\usepackage{hyperref}

\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt}

\begin{document}

% KOP SURAT
\begin{center}
    {\large\textbf{YUDIAZ CREATIVE STUDIO}}\\[2pt]
    {\small\textbf{DIVISI OPERASIONAL \& TATA KELOLA ADMINISTRASI}}\\[2pt]
    {\footnotesize Gedung Inkubator Kreatif, Bandung, Jawa Barat \textbar\ Kontak: halo@yudiaz.my.id}\\[3pt]
    \rule{\textwidth}{1.5pt}\\[-6pt]
    \rule{\textwidth}{0.5pt}
\end{center}

\vspace{0.5cm}

% NOMOR DAN TANGGAL
\begin{tabularx}{\textwidth}{@{}X r@{}}
    \begin{tabular}{@{}ll}
        Nomor & : 014/UND/YUDIAZ-OPS/X/2026 \\
        Lampiran & : 1 (satu) Berkas \\
        Perihal & : \textbf{Undangan Menghadiri Acara Forum Strategis Studio}
    \end{tabular} & 
    \begin{tabular}{r@{}}
        Bandung, 4 Oktober 2026
    \end{tabular}
\end{tabularx}

\vspace{0.6cm}

Kepada Yth.\\
\textbf{Bapak/Ibu Pimpinan \& Rekan-Rekan Mitra}\\
di Tempat

\vspace{0.4cm}

Dengan hormat,

Sehubungan dengan akan diselenggarakannya agenda \textbf{``Yudiaz Annual Innovation Forum 2026''}, kami atas nama panitia pelaksana bermaksud mengundang Bapak/Ibu untuk berkenan hadir dan berpartisipasi pada agenda tersebut yang akan dilaksanakan pada:

\begin{center}
\begin{tabular}{@{}lll@{}}
    \textbf{Hari, Tanggal} & : & Sabtu, 17 Oktober 2026 \\
    \textbf{Waktu} & : & 09.00 WIB -- 12.30 WIB (Registrasi pukul 08.30 WIB) \\
    \textbf{Tempat} & : & Grand Ballroom Hall \& Virtual Room Yudiaz \\
    \textbf{Agenda} & : & Presentasi Inovasi, Showcase Produk, \& Networking Session
\end{tabular}
\end{center}

Mengingat pentingnya agenda strategis ini dalam penyelarasan ekosistem kerja sama mendatang, kehadiran Bapak/Ibu sangat kami harapkan. Untuk konfirmasi kehadiran, mohon dapat menghubungi narahubung kami di \texttt{0812-XXXX-XXXX} paling lambat hari Rabu, 14 Oktober 2026.

Demikian surat undangan ini kami sampaikan. Atas perhatian, perkenan, dan kerja sama yang baik, kami ucapkan terima kasih.

\vspace{0.8cm}

\begin{tabularx}{\textwidth}{@{}X X@{}}
    \centering
    Mengetahui,\\[3pt]
    \textbf{Ketua Pelaksana}
    \vspace{2cm}\\
    \textbf{( .................................................. )}\\
    NIP/ID: .......................................
    &
    \centering
    Hormat kami,\\[3pt]
    \textbf{Sekretaris Pelaksana}
    \vspace{2cm}\\
    \textbf{( .................................................. )}\\
    NIP/ID: .......................................
\end{tabularx}

\end{document}
"""
    },
    "justifikasi_anggaran": {
        "name": "Lembar Justifikasi Anggaran & Kebutuhan",
        "description": "Format justifikasi pengadaan barang, jasa, dan realokasi biaya anggaran kegiatan",
        "main.tex": r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[left=2.2cm,right=2.2cm,top=2cm,bottom=2cm]{geometry}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{xcolor}
\usepackage{colortbl}
\usepackage{titlesec}

\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}
\definecolor{headerBg}{RGB}{240, 243, 246}

\begin{document}

\begin{center}
    {\Large\textbf{LEMBAR JUSTIFIKASI ANGGARAN \& PENGADAAN}}\\[3pt]
    {\small\textbf{Yudiaz Creative Studio -- Administrasi \& Keuangan}}\\[4pt]
    \rule{\textwidth}{1.2pt}
\end{center}

\vspace{0.3cm}

\begin{table}[h!]
\centering
\begin{tabularx}{\textwidth}{|l|X|l|X|}
\hline
\textbf{Nama Program} & Penguatan Infrastruktur Operasional & \textbf{Kode Akun} & 521-OPS-2026 \\ \hline
\textbf{Unit Pengusul} & Divisi Administrasi \& Tim Event & \textbf{Tanggal} & 4 Oktober 2026 \\ \hline
\textbf{Penanggung Jawab} & Karina & \textbf{Total Pengajuan} & Rp 18.750.000,- \\ \hline
\end{tabularx}
\end{table}

\vspace{0.2cm}
\textbf{I. LATAR BELAKANG \& URGENSI KEBUTUHAN}
Pengadaan dan realokasi anggaran ini mendesak dilakukan guna mendukung kelancaran operasional pelaksanaan forum dan penyusunan berkas LPJ resmi. Tanpa pemenuhan pos ini, proses koordinasi lapangan dan verifikasi administrasi berisiko mengalami keterlambatan yang berdampak pada tenggat waktu laporan akhir.

\vspace{0.3cm}
\textbf{II. RINCIAN POS PENGELUARAN \& JUSTIFIKASI TEKNIS}

\begin{table}[h!]
\small
\centering
\begin{tabularx}{\textwidth}{|c|X|c|c|r|X|}
\hline
\rowcolor{headerBg}
\textbf{No} & \textbf{Item / Pos Kebutuhan} & \textbf{Vol} & \textbf{Sat} & \textbf{Harga Satuan (Rp)} & \textbf{Justifikasi Kebutuhan} \\ \hline
1 & Sewa Server Kompilasi LaTeX & 1 & Paket & 3.500.000 & Pemrosesan render naskah \& PDF realtime \\ \hline
2 & Paket Dokumentasi \& Streaming & 1 & Kegiatan & 6.250.000 & Dokumentasi bukti fisik LPJ \& broadcast acara \\ \hline
3 & Konsumsi Rapat Koordinasi Panitia & 30 & Pax & 100.000 & 3 kali rapat pleno maraton persiapan \\ \hline
4 & Pengadaan ATK \& Berkas Fisik & 1 & Paket & 1.500.000 & Pencetakan proposal jilid \& materi delegasi \\ \hline
5 & Banner, Backdrop, \& Signage & 3 & Pcs & 1.500.000 & Branding visual di venue utama \\ \hline
\multicolumn{4}{|r|}{\textbf{TOTAL PENGAJUAN}} & \multicolumn{2}{l|}{\textbf{Rp 18.750.000,-}} \\ \hline
\end{tabularx}
\end{table}

\vspace{0.2cm}
\textbf{III. ANALISIS DAMPAK RISIKO}
Apabila anggaran ini tidak disetujui atau mengalami pemotongan signifikan, maka kualitas dokumentasi pendukung LPJ akan menurun, serta berpotensi terjadi kendala teknis pada sistem administrasi berkas daring saat hari-H.

\vspace{0.8cm}
\begin{tabularx}{\textwidth}{@{}X X X@{}}
    \centering
    Diajukan Oleh,\\[2pt]
    \textbf{Pengusul Kegiatan}
    \vspace{1.8cm}\\
    \textbf{Karina}\\
    Koordinator Administrasi
    &
    \centering
    Diverifikasi Oleh,\\[2pt]
    \textbf{Bendahara / Verifikator}
    \vspace{1.8cm}\\
    \textbf{( ....................................... )}\\
    Finance Officer
    &
    \centering
    Disetujui Oleh,\\[2pt]
    \textbf{Head of CEO Office}
    \vspace{1.8cm}\\
    \textbf{Daffa}\\
    Chief of Staff
\end{tabularx}

\end{document}
"""
    },
    "proposal_kegiatan": {
        "name": "Proposal Kegiatan & Kepanitiaan",
        "description": "Proposal lengkap acara organisasi/event/kampus dengan lembar pengesahan dan RAB terstruktur",
        "main.tex": r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[left=2.5cm,right=2.5cm,top=2.5cm,bottom=2.5cm]{geometry}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{xcolor}
\usepackage{titlesec}
\usepackage{enumitem}

\definecolor{primaryBlue}{RGB}{24, 43, 73}
\definecolor{accentGold}{RGB}{202, 138, 4}

\titleformat{\section}{\color{primaryBlue}\normalfont\Large\bfseries}{\thesection}{1em}{}[{\color{accentGold}\titlerule[1.2pt]}]
\titleformat{\subsection}{\color{primaryBlue}\normalfont\large\bfseries}{\thesubsection}{1em}{}

\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}

\begin{document}

% COVER PROPOSAL
\begin{titlepage}
    \centering
    \vspace*{1.5cm}
    {\Large\textbf{PROPOSAL KEGIATAN}\par}
    \vspace{0.8cm}
    {\Huge\bfseries\color{primaryBlue} FORUM INOVASI DAN KREATIVITAS MAHASISWA 2026\par}
    \vspace{0.5cm}
    {\large\textit{``Membangun Daya Saing Digital Melalui Sinergi Karya \& Kolaborasi Kreatif''}\par}
    
    \vfill
    \rule{0.6\textwidth}{1.5pt}\par
    \vspace{0.5cm}
    {\textbf{Disusun Oleh:}\par}
    \vspace{0.3cm}
    {\large\textbf{PANITIA PELAKSANA INOVASI}\par}
    {\normalsize Penanggung Jawab Administrasi: Karina\par}
    \vspace{0.5cm}
    {\large\textbf{YUDIAZ CREATIVE STUDIO}\par}
    {\normalsize Bandung, Jawa Barat\par}
    \vspace{1cm}
    {\normalsize Oktober 2026\par}
\end{titlepage}

\newpage

% LEMBAR PENGESAHAN
\begin{center}
    {\Large\textbf{LEMBAR PENGESAHAN PROPOSAL}}\\[3pt]
    \rule{\textwidth}{1pt}
\end{center}

\vspace{0.4cm}
Proposal kegiatan ini telah diperiksa, diverifikasi, dan disahkan pada:\\[4pt]
Hari, Tanggal : Senin, 5 Oktober 2026\\
Tempat : Bandung, Jawa Barat

\vspace{1.5cm}

\begin{tabularx}{\textwidth}{@{}X X@{}}
    \centering
    Menyetujui,\\[2pt]
    \textbf{Ketua Pelaksana Kegiatan}
    \vspace{2.2cm}\\
    \textbf{( .................................................. )}\\
    NIP/ID: .......................................
    &
    \centering
    Mengetahui,\\[2pt]
    \textbf{Sekretaris / PIC Administrasi}
    \vspace{2.2cm}\\
    \textbf{Karina}\\
    NIP/ID: .......................................
\end{tabularx}

\vspace{2cm}
\begin{center}
    Mengetahui \& Menyetujui,\\[2pt]
    \textbf{Head of CEO Office Yudiaz Creative Studio}
    \vspace{2.2cm}\\
    \textbf{Daffa}\\
    Chief of Staff
\end{center}

\newpage

\section{Latar Belakang}
Di era percepatan teknologi dan industri kreatif modern, kemampuan menghadirkan gagasan solutif yang terstruktur merupakan modal utama organisasi. Kegiatan ini dirancang sebagai wadah sinergi, presentasi karya, dan konsolidasi gagasan strategis.

\section{Nama dan Tema Kegiatan}
\begin{itemize}[leftmargin=1.5cm]
    \item \textbf{Nama Kegiatan} : Forum Inovasi dan Kreativitas Mahasiswa 2026.
    \item \textbf{Tema Kegiatan} : \textit{``Membangun Daya Saing Digital Melalui Sinergi Karya \& Kolaborasi Kreatif''}.
\end{itemize}

\section{Tujuan dan Target Sasaran}
\begin{enumerate}
    \item Meningkatkan pemahaman praktis mahasiswa dalam pengelolaan proyek teknologi.
    \item Memfasilitasi networking profesional antara praktisi industri dan civitas akademika.
    \item Menghasilkan 5 output naskah kerja sama strategis lintas divisi.
\end{enumerate}

\section{Waktu dan Tempat Pelaksanaan}
\begin{table}[h!]
\centering
\begin{tabularx}{\textwidth}{@{}l l X@{}}
    \textbf{Hari, Tanggal} & : & Sabtu, 17 Oktober 2026 \\
    \textbf{Waktu} & : & 08.30 -- 16.00 WIB \\
    \textbf{Tempat} & : & Auditorium Utama \& Ruang Presentasi Yudiaz
\end{tabularx}
\end{table}

\section{Rencana Anggaran Biaya (RAB)}
\begin{table}[h!]
\small
\centering
\begin{tabularx}{\textwidth}{|c|X|c|c|r|r|}
\hline
\textbf{No} & \textbf{Pos Pengeluaran} & \textbf{Vol} & \textbf{Sat} & \textbf{Harga Satuan (Rp)} & \textbf{Total (Rp)} \\ \hline
1 & Honorarium Pembicara Utama & 2 & Orang & 2.500.000 & 5.000.000 \\ \hline
2 & Konsumsi Peserta \& Panitia & 80 & Box & 45.000 & 3.600.000 \\ \hline
3 & Sertifikat, Kit Peserta, ATK & 80 & Paket & 30.000 & 2.400.000 \\ \hline
4 & Sewa Venue \& Perlengkapan Teknis & 1 & Hari & 4.500.000 & 4.500.000 \\ \hline
5 & Dokumentasi, Publikasi, \& Spanduk & 1 & Paket & 1.500.000 & 1.500.000 \\ \hline
\multicolumn{5}{|r|}{\textbf{TOTAL ESTIMASI ANGGARAN}} & \textbf{Rp 17.000.000} \\ \hline
\end{tabularx}
\end{table}

\section{Penutup}
Demikian proposal ini kami susun dengan harapan mendapatkan dukungan moril maupun materiel demi keberhasilan agenda ini. Atas perhatian dan dukungannya, kami sampaikan terima kasih.

\end{document}
"""
    },
    "lpj_kegiatan": {
        "name": "Laporan Pertanggungjawaban (LPJ)",
        "description": "Laporan pertanggungjawaban kegiatan & keuangan dengan tabel komparasi realisasi anggaran",
        "main.tex": r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[left=2.5cm,right=2.5cm,top=2.5cm,bottom=2.5cm]{geometry}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{xcolor}
\usepackage{titlesec}
\usepackage{enumitem}

\definecolor{primaryNavy}{RGB}{15, 23, 42}
\definecolor{brandGreen}{RGB}{21, 128, 61}

\titleformat{\section}{\color{primaryNavy}\normalfont\Large\bfseries}{\thesection}{1em}{}[{\color{brandGreen}\titlerule[1.2pt]}]
\titleformat{\subsection}{\color{primaryNavy}\normalfont\large\bfseries}{\thesubsection}{1em}{}

\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}

\begin{document}

% COVER LPJ
\begin{titlepage}
    \centering
    \vspace*{1.5cm}
    {\Huge\bfseries\color{primaryNavy} LAPORAN PERTANGGUNGJAWABAN\par}
    \vspace{0.4cm}
    {\Large\textbf{(LPJ KEGIATAN \& KEUANGAN)}\par}
    \vspace{1cm}
    {\LARGE FORUM INOVASI DAN KREATIVITAS MAHASISWA 2026\par}
    
    \vfill
    \rule{0.6\textwidth}{1.5pt}\par
    \vspace{0.5cm}
    {\textbf{Disusun Oleh:}\par}
    \vspace{0.3cm}
    {\large\textbf{PANITIA PELAKSANA KEGIATAN}\par}
    {\normalsize Koordinator Pelaporan: Karina\par}
    \vspace{0.5cm}
    {\large\textbf{YUDIAZ CREATIVE STUDIO}\par}
    \vspace{1cm}
    {\normalsize Oktober 2026\par}
\end{titlepage}

\newpage

\section{Ringkasan Eksekutif}
Kegiatan Forum Inovasi dan Kreativitas Mahasiswa 2026 telah terselenggara dengan lancar pada hari Sabtu, 17 Oktober 2026 bertempat di Auditorium Utama Yudiaz. Tingkat kehadiran peserta mencapai 95\% dari target awal, dengan seluruh rangkaian manual acara terealisasi secara tertib.

\section{Realisasi Anggaran vs Rencana Biaya}
\begin{table}[h!]
\small
\centering
\begin{tabularx}{\textwidth}{|c|X|r|r|r|}
\hline
\textbf{No} & \textbf{Pos Pengeluaran} & \textbf{Anggaran (Rp)} & \textbf{Realisasi (Rp)} & \textbf{Selisih (Rp)} \\ \hline
1 & Honorarium Pembicara Utama & 5.000.000 & 5.000.000 & 0 \\ \hline
2 & Konsumsi Peserta \& Panitia & 3.600.000 & 3.420.000 & +180.000 \\ \hline
3 & Sertifikat, Kit Peserta, ATK & 2.400.000 & 2.350.000 & +50.000 \\ \hline
4 & Sewa Venue \& Perlengkapan & 4.500.000 & 4.500.000 & 0 \\ \hline
5 & Dokumentasi \& Publikasi & 1.500.000 & 1.450.000 & +50.000 \\ \hline
\multicolumn{2}{|r|}{\textbf{TOTAL}} & \textbf{17.000.000} & \textbf{16.720.000} & \textbf{+280.000} \\ \hline
\end{tabularx}
\end{table}

\textbf{Keterangan:} Sisa saldo anggaran sebesar \textbf{Rp 280.000,-} telah dikembalikan secara utuh ke kas bendahara operasional studio.

\section{Evaluasi, Kendala, \& Rekomendasi}
\begin{itemize}[leftmargin=1.5cm]
    \item \textbf{Kendala}: Pendaftaran ulang di pintu masuk sempat mengalami antrean pada 15 menit awal.
    \item \textbf{Solusi Lapangan}: Tim registrasi membuka dua meja tambahan untuk absensi digital QR Code.
    \item \textbf{Rekomendasi}: Pada kegiatan berikutnya, disarankan menerapkan sistem auto-check-in mandiri.
\end{itemize}

\section{Penutup}
Laporan Pertanggungjawaban ini disusun dengan sebenar-benarnya berdasarkan bukti fisik dan dokumentasi riil pelaksanaan kegiatan.

\vspace{1.5cm}
\begin{tabularx}{\textwidth}{@{}X X@{}}
    \centering
    Menyetujui,\\[2pt]
    \textbf{Ketua Pelaksana}
    \vspace{2cm}\\
    \textbf{( .................................................. )}
    &
    \centering
    Penyusun LPJ,\\[2pt]
    \textbf{Koordinator Administrasi}
    \vspace{2cm}\\
    \textbf{Karina}
\end{tabularx}

\end{document}
"""
    },
    "proposal": {
        "name": "Executive Project Proposal",
        "description": "Yudiaz Creative Studio standard business & client proposal",
        "main.tex": r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[margin=2.2cm]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{titlesec}

\definecolor{brandGold}{RGB}{212, 175, 55}
\definecolor{brandNavy}{RGB}{15, 23, 42}
\definecolor{brandSlate}{RGB}{71, 85, 105}

\hypersetup{
    colorlinks=true,
    linkcolor=brandGold,
    urlcolor=brandGold,
    citecolor=brandNavy
}

\titleformat{\section}{\color{brandNavy}\normalfont\Large\bfseries}{\thesection}{1em}{}[{\color{brandGold}\titlerule[1.5pt]}]
\titleformat{\subsection}{\color{brandSlate}\normalfont\large\bfseries}{\thesubsection}{1em}{}

\begin{document}

\begin{titlepage}
    \centering
    \vspace*{2cm}
    {\Huge\bfseries\color{brandNavy} PROPOSAL PROYEK STRATEGIS\par}
    \vspace{0.5cm}
    {\large\bfseries\color{brandGold} Yudiaz Creative Studio\par}
    \vspace{2cm}
    {\Large\itshape Inisiatif Pengembangan \& Akselerasi Solusi Digital\par}
    \vfill
    {\large Disusun untuk:\par}
    {\large\bfseries Klien / Mitra Strategis\par}
    \vfill
    {\large Disusun oleh:\par}
    {\large\bfseries Daniandra Prayudisty\par}
    {\normalsize Founder \& CEO, Yudiaz Creative Studio\par}
    \vspace{1cm}
    {\normalsize \today\par}
\end{titlepage}

\section{Ringkasan Eksekutif}
Yudiaz Creative Studio berkomitmen memberikan arsitektur teknologi berstandar tinggi dan eksekusi kreatif presisi. Proposal ini merinci ruang lingkup kerja, jadwal implementasi, serta estimasi alokasi sumber daya.

\section{Tujuan Proyek}
\begin{itemize}
    \item Membangun fondasi sistem yang modular, aman, dan siap skala.
    \item Mengoptimalkan pengalaman pengguna melalui antarmuka responsif dan modern.
    \item Memastikan keandalan layanan dengan uji kualitas menyeluruh.
\end{itemize}

\section{Rencana Kerja \& Timeline}
\begin{table}[h!]
\centering
\begin{tabular}{@{}llcc@{}}
\toprule
\textbf{Fase} & \textbf{Deskripsi} & \textbf{Durasi} & \textbf{Status} \\ \midrule
Fase 1 & Riset Arsitektur \& Desain Sistem & 2 Minggu & Siap \\
Fase 2 & Implementasi Core \& Integrasi API & 3 Minggu & Terjadwal \\
Fase 3 & QA, Security Hardening \& Testing & 1 Minggu & Terjadwal \\
Fase 4 & Deployment \& Serah Terima & 1 Minggu & Terjadwal \\ \bottomrule
\end{tabular}
\caption{Timeline Eksekusi Proyek}
\end{table}

\section{Penutup}
Demikian proposal ini disusun sebagai acuan kerja sama. Kami siap berdiskusi lebih lanjut untuk penyesuaian detail teknis.

\vspace{1.5cm}
\noindent
\textbf{Disetujui Oleh,}\\[1.5cm]
\textbf{Daniandra Prayudisty}\\
Founder \& CEO, Yudiaz Creative Studio

\end{document}
"""
    },
    "paper": {
        "name": "Academic Research Paper",
        "description": "Standard two-column scientific paper with IEEE/ACM layout",
        "main.tex": r"""\documentclass[10pt,journal,compsoc]{IEEEtran}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{graphicx}
\usepackage{cite}
\usepackage{booktabs}
\usepackage{hyperref}

\begin{document}

\title{Hierarchical Transformer Architectures for Multilead Biomedical Signal Localization}

\author{Daniandra Prayudisty,~\IEEEmembership{Member,~IEEE}
\thanks{Daniandra Prayudisty is with Yudiaz Creative Studio and School of Computing, Telkom University, Bandung, Indonesia.}
}

\markboth{Journal of Biomedical and Health Informatics,~Vol.~XX, No.~X, \today}%
{Prayudisty: Hierarchical Transformer Architectures}

\IEEEtitleabstractindextext{%
\begin{abstract}
Precise anatomical localization of focal cardiac arrhythmias from standard 12-lead electrocardiograms (ECG) plays a critical role in pre-procedural planning for radiofrequency catheter ablation. In this work, we propose a leak-free, patient-wise validated deep learning framework integrating convolutional feature representation with hierarchical transformer networks. Experimental evaluation on patient-held-out validation demonstrates robust macro-F1 improvements across anatomical subregions.
\end{abstract}

\begin{IEEEkeywords}
Arrhythmia localization, 12-lead ECG, Transformer, Catheter ablation, Patient-wise validation.
\end{IEEEkeywords}}

\maketitle
\IEEEdisplaynontitleabstractindextext
\IEEEpeerreviewmaketitle

\section{Introduction}
\IEEEPARstart{F}{ocal} ventricular arrhythmias originating from outflow tracts present diagnostic challenges in non-invasive clinical mapping. Traditional manual algorithmic criteria suffer from inter-observer variability and limited generalization across heterogeneous cardiac morphologies.

\section{Methodology}
\subsection{Signal Preprocessing}
Standard 12-lead ECG records are sampled and denoised using discrete wavelet transform (DWT). Signal normalization is conducted strictly within inner training folds to eliminate data leakage.

\begin{equation}
y(t) = \sum_{k} c_k \psi_{j,k}(t) + \sum_{k} d_k \phi_{j,k}(t)
\end{equation}

\subsection{Architecture Overview}
The network comprises spatial-temporal convolutional feature extractors followed by hierarchical self-attention heads:
\begin{equation}
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\end{equation}

\section{Results and Discussion}
Table~\ref{tab:results} summarizes validation metrics across patient-wise stratified evaluations.

\begin{table}[h]
\caption{Cross-Validation Performance Comparison}
\label{tab:results}
\centering
\begin{tabular}{lccc}
\toprule
\textbf{Model Architecture} & \textbf{Accuracy} & \textbf{Macro-F1} & \textbf{AUC} \\ \midrule
Baseline CNN & 64.2\% & 63.8\% & 0.741 \\
Transformer Encoder & 68.5\% & 67.9\% & 0.785 \\
Hierarchical Transformer & \textbf{72.5\%} & \textbf{72.1\%} & \textbf{0.824} \\ \bottomrule
\end{tabular}
\end{table}

\section{Conclusion}
The proposed hierarchical approach provides high fidelity localization while preserving strict patient-level boundary validation.

\begin{thebibliography}{00}
\bibitem{ref1} D. Prayudisty, ``Deep Learning Frameworks for Arrhythmia Localization,'' \emph{IEEE Trans. Biomed. Eng.}, vol. 71, pp. 110--122, 2026.
\end{thebibliography}

\end{document}
"""
    },
    "skripsi": {
        "name": "Format Skripsi / Tugas Akhir",
        "description": "Template akademik laporan tugas akhir perguruan tinggi",
        "main.tex": r"""\documentclass[12pt,a4paper]{report}
\usepackage[utf8]{inputenc}
% \usepackage[bahasai]{babel}
\usepackage[top=4cm,left=4cm,bottom=3cm,right=3cm]{geometry}
\usepackage{setspace}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{hyperref}

\onehalfspacing

\begin{document}

\title{\textbf{PENGEMBANGAN SISTEM DETEKSI DAN LOKALISASI PRESISE BERBASIS DEEP LEARNING}\\
\vspace{1cm}
\large{TUGAS AKHIR}}
\author{Daniandra Prayudisty\\NIM: 130120XXXX}
\date{Bandung\\2026}

\maketitle

\chapter{PENDAHULUAN}
\section{Latar Belakang}
Perkembangan kecerdasan buatan pada ranah pemrosesan sinyal biomedis telah membuka peluang baru dalam percepatan diagnosis medis. Tugas akhir ini berfokus pada perancangan arsitektur deep learning yang robust dan bebas data leakage.

\section{Rumusan Masalah}
Berdasarkan latar belakang tersebut, rumusan masalah dalam penelitian ini adalah:
\begin{enumerate}
    \item Bagaimana merancang arsitektur model yang mampu mengekstraksi fitur spasial dan temporal sinyal secara simultan?
    \item Bagaimana menjamin evaluasi performa bebas bias melalui skema patient-wise validation?
\end{enumerate}

\section{Tujuan Penelitian}
Tujuan dari penelitian ini adalah menghasilkan pipeline komputasi yang terverifikasi secara metodologis dan dapat dipertanggungjawabkan pada pengujian data independen.

\chapter{TINJAUAN PUSTAKA}
\section{Transformasi Wavelet Diskrit}
Transformasi Wavelet Diskrit (DWT) digunakan untuk memisahkan noise frekuensi tinggi dari komponen gelombang utama tanpa merusak morfologi sinyal.

\chapter{METODOLOGI PENELITIAN}
\section{Tahapan Eksperimen}
Eksperimen dilakukan dalam beberapa tahapan utama, mulai dari pra-pemrosesan data, pembagian cohort berbasis pasien (Stratified Group K-Fold), hingga pelatihan arsitektur neural network.

\end{document}
"""
    },
    "camtech_progress_report": {
        "name": "CamTech Virtubis Progress Report",
        "description": "Laporan kemajuan magang Virtubis Internship Programme CamTech University lengkap dengan header banner, tabel evaluasi, dan format IEEE",
        "main.tex": r"""\documentclass[11pt,a4paper]{report}

% -------------------------------------------------------------
% Packages & Configuration
% -------------------------------------------------------------
\usepackage[a4paper, left=2.2cm, right=2.2cm, top=3.6cm, bottom=3.6cm, headheight=68pt, footskip=65pt]{geometry}
\usepackage{graphicx}
\usepackage{fancyhdr}
\usepackage[table]{xcolor}
\usepackage{tcolorbox}
\usepackage{tabularx}
\usepackage{booktabs}
\usepackage{array}
\usepackage{parskip}
\usepackage{float}
\usepackage{amsmath,amssymb}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage{mathptmx} % Times font matching docx
\usepackage[hidelinks]{hyperref}

% -------------------------------------------------------------
% Color Palette (Matching CamTech & Document Theme)
% -------------------------------------------------------------
\definecolor{camtechNavy}{HTML}{1B3A6B}
\definecolor{camtechDark}{HTML}{0D1B2A}
\definecolor{camtechSteel}{HTML}{3D5A80}
\definecolor{camtechSlate}{HTML}{8B9CB0}
\definecolor{guidanceBg}{HTML}{F2F4F7}
\definecolor{tableRowAlt}{HTML}{F2F4F7}
\definecolor{tableMeta1}{HTML}{F0F3F8}
\definecolor{tableMeta2}{HTML}{E8EEF5}
\definecolor{tableMetaVal1}{HTML}{FFFFFF}
\definecolor{tableMetaVal2}{HTML}{F5F7FA}
\definecolor{cellBorder}{HTML}{D1D5DB}

% -------------------------------------------------------------
% Callout Boxes (Writing Guidance)
% -------------------------------------------------------------
\newtcolorbox{guidancebox}[1][]{
  colback=guidanceBg,
  colframe=camtechSteel,
  boxrule=0pt,
  leftrule=3.5pt,
  arc=0pt,
  left=12pt,
  right=12pt,
  top=8pt,
  bottom=8pt,
  fontupper=\small,
  #1
}

% -------------------------------------------------------------
% Header & Footer Setup (Official CamTech Banners)
% -------------------------------------------------------------
\pagestyle{fancy}
\fancyhf{}
\fancyhead[C]{\includegraphics[width=\textwidth]{image1.jpg}}
\fancyfoot[C]{\includegraphics[width=\textwidth]{image2.jpg}}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Style for Chapter and Section Headings
\titleformat{\chapter}[display]
  {\normalfont\Large\bfseries\centering\color{camtechNavy}}
  {\Large\bfseries\color{camtechNavy}Chapter \thechapter}
  {4pt}
  {\LARGE\bfseries\color{camtechNavy}}

\titlespacing*{\chapter}{0pt}{-10pt}{16pt}

\titleformat{\section}
  {\normalfont\large\bfseries\color{camtechNavy}}
  {\thesection}{1em}{}

\titleformat{\subsection}
  {\normalfont\normalsize\bfseries\color{camtechSteel}}
  {\thesubsection}{1em}{}

% Redefine plain page style so chapter pages also have banners
\fancypagestyle{plain}{
  \fancyhf{}
  \fancyhead[C]{\includegraphics[width=\textwidth]{image1.jpg}}
  \fancyfoot[C]{\includegraphics[width=\textwidth]{image2.jpg}}
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\footrulewidth}{0pt}
}

% -------------------------------------------------------------
% Document Start
% -------------------------------------------------------------
\begin{document}

% =============================================================
% TITLE / COVER PAGE (Page 1)
% =============================================================
\begin{titlepage}
\thispagestyle{fancy}

\begin{center}
  {\large\bfseries\color{camtechDark} CAMBODIA UNIVERSITY OF TECHNOLOGY AND SCIENCE}\\[0.25em]
  {\small\color{camtechSteel} Faculty of Engineering \quad|\quad FENG Industry, Internship \& Innovation Hub}\\[1.8em]
  
  {\Large\bfseries Virtubis Internship Programme}\\[0.4em]
  {\huge\bfseries\color{camtechNavy} End-Of-Term Progress Report}\\[1.2em]
  
  {\normalsize A Term-End Academic Report Submitted in Partial Fulfilment\\[0.2em]
  of the Requirements of the Virtubis Internship Framework}\\[1.5em]
\end{center}

% Metadata Table
\renewcommand{\arraystretch}{1.25}
\noindent
\begin{tabularx}{\textwidth}{|>{\bfseries}p{4.2cm}|X|}
\hline
\rowcolor{tableMeta1} Project Title & (Enter full project title) \\
\hline
\rowcolor{tableMeta2} Student Name(s) & (Full name as registered) \\
\hline
\rowcolor{tableMeta1} Student ID(s) & \\
\hline
\rowcolor{tableMeta2} Academic Year & \\
\hline
\rowcolor{tableMeta1} Term & (Term I \ / \ Term II \ / \ Term III) \\
\hline
\rowcolor{tableMeta2} Internship Code & (INT-ENG-0\_) \\
\hline
\rowcolor{tableMeta1} Hub & (AI Hub \ / \ DS Hub \ / \ Cyber Hub \ / \ R\&A Hub) \\
\hline
\rowcolor{tableMeta2} Project Track & (Software Development \ / \ Research) \\
\hline
\rowcolor{tableMeta1} Academic Mentor & \\
\hline
\rowcolor{tableMeta2} Technical Mentor & \\
\hline
\rowcolor{tableMeta1} Submission Date & \\
\hline
\end{tabularx}

\vspace{1.2em}

% Declaration of Originality
\begin{center}
  {\bfseries\large Declaration of Originality}
\end{center}

\vspace{0.2em}
\noindent
I/We hereby declare that this report is our own original work undertaken as part of the Virtubis Internship Programme at the Faculty of Engineering, CamTech University. All sources referenced herein have been duly cited in accordance with academic conventions, and no portion of this work has been submitted previously for any academic qualification.

\vspace{1.8em}

% Signature lines
\noindent
\begin{tabularx}{\textwidth}{X p{1cm} X}
  \rule{6.2cm}{0.5pt} & & \rule{6.2cm}{0.5pt} \\
  Student Signature & & Mentor Signature \\[1.8em]
  \rule{6.2cm}{0.5pt} & & \rule{6.2cm}{0.5pt} \\
  Date & & Date \\
\end{tabularx}

\end{titlepage}

% =============================================================
% PRELIMINARY PAGES
% =============================================================

% --- Page 3: Acknowledgements ---
\clearpage
\pagenumbering{roman}
\setcounter{page}{3}

\begin{center}
  {\LARGE\bfseries\color{camtechNavy} Acknowledgements}\\[1.5em]
\end{center}
\addcontentsline{toc}{chapter}{Acknowledgements}

I [Student Name] would like to express sincere gratitude to [Academic Mentor Name] for their guidance and supervision throughout this term. We also thank [Technical Mentor Name] for their technical direction and practical insights.

We are grateful to the Faculty of Engineering and FENG i-Hub at Cambodia University of Technology and Science for creating the Virtubis framework and providing the resources, infrastructure, and mentorship that made this work possible.

[Add any additional acknowledgements --- industry partners, peers, data providers, or others who contributed to the work this term.]

% --- Page 4: Abstract ---
\clearpage
\setcounter{page}{4}

\begin{center}
  {\LARGE\bfseries\color{camtechNavy} Abstract}\\[1.2em]
\end{center}
\addcontentsline{toc}{chapter}{Abstract}

\textbf{Background:} Dengue Hemorrhagic Fever (DHF) remains the primary vector-borne threat in Southeast Asian urban centers. While rainfall is the traditional predictor for mosquito breeding, recent urbanization in cities like Phnom Penh has created "Urban Heat Islands" (UHI). Emerging evidence suggests that localized ambient temperature increases may shorten the extrinsic incubation period of the virus, yet the specific lead-time between extreme heat events and infection surges remains poorly quantified.

\textbf{Objective:} This study aims to evaluate the time-lagged association between the Land Surface Temperature (LST) and dengue notification rates to determine if thermal stress acts as a direct biological accelerator for viral replication or if the relationship is confounded by the onset of the rainy season.

\textbf{Methodology:} We utilized a 15-year longitudinal dataset (2009--2024) of satellite-derived LST and laboratory-confirmed dengue cases. Using a Distributed Lag Non-linear Model (DLNM), we analyzed the relative risk of infection across a 30-day window. To isolate the temperature effect from the dominant monsoon cycle, we integrated "cumulative weekly rainfall" as a covariate in a Generalized Additive Model (GAM), allowing for the detection of "heat-driven" spikes that occur independently of water accumulation.

\textbf{Results:} The initial unadjusted models showed a significant correlation between heat peaks and dengue surges with a 2-week lag ($p < 0.01$). Unlike the malaria/PM2.5 "Dry Season Trap" where results vanished under control, the Dengue-Heat link remained resilient. Even when adjusting for precipitation, temperatures exceeding $32^\circ\text{C}$ were associated with a 24\% increase in case notifications ($RR = 1.24$; $CI: 1.15\text{--}1.33$) approximately 14 days later. This suggests that heat accelerates the transmission cycle faster than rainfall alone can expand breeding sites.

\textbf{Conclusion:} Thermal stress is a standalone driver of dengue outbreaks in urban Cambodia, independent of the monsoon calendar. These findings indicate that public health strategies must evolve beyond "stagnant water" management to include urban cooling initiatives and "Heat-Dengue" integrated early warning systems. In the context of climate change, rising urban temperatures may counteract the successes of traditional vector control.

\vspace{0.4em}
\noindent\textit{How this follows your requested structure: Background: Establishes the problem (Dengue) and the new variable (Urban Heat/Temperature). Objective: Tests a specific relationship (Biological accelerator vs. Seasonal proxy). Methodology: Uses high-level modeling (DLNM and GAM) to handle time-lags and confounding variables.}

\vspace{0.8em}
\noindent\textbf{Keywords:} (6 keywords separated by commas --- e.g. machine learning, healthcare, SDLC, CamTech)

\vspace{1.0em}

\begin{guidancebox}
\textbf{Writing Guidance}\\
Write the abstract after completing all other sections. 200--300 words. Cover: the problem addressed, the methodology used, key work completed this term, and principal findings or progress. Do not include citations.\\
\textit{(200-300 words, no citations)}
\end{guidancebox}

% --- Page 5: Table of Contents ---
\clearpage
\setcounter{page}{5}
\setcounter{tocdepth}{1}
\tableofcontents
\addcontentsline{toc}{chapter}{Table of Contents}

% --- Page 6: List of Tables and Figures ---
\clearpage
\setcounter{page}{6}
\begin{center}
  {\LARGE\bfseries\color{camtechNavy} List of Tables and Figures}\\[1.5em]
\end{center}
\addcontentsline{toc}{chapter}{List of Tables and Figures}

\noindent [List all tables and figures used in this report with their caption and page number. Update this list before submission.]

% =============================================================
% CHAPTER 1: INTRODUCTION (Page 7)
% =============================================================
\clearpage
\pagenumbering{arabic}
\setcounter{page}{7}

\chapter{Introduction}

\begin{guidancebox}
\textbf{Writing Guidance --- Chapter 1}\\
Set the scene for your entire report. A reader unfamiliar with your project should understand what you are doing, why it matters, and what this term covered.\\
\textbf{Minimum: 400 words across all sections of this chapter.}
\end{guidancebox}

\section{Background and Motivation}
Provide the context for your project. What problem exists in the real world? Why is it important? Who is affected? Reference any relevant industry trends, local context (Cambodia / Southeast Asia), or academic motivation.

\textit{[Replace this paragraph with your own background and motivation. 150--200 words.]}

\section{Problem Statement}
State the problem your team is addressing in precise, structured language. Your problem statement should identify who is affected, what the problem is, why it persists, and what the consequence is.

\textit{[Format: [Who] struggles with [what] because [why], which causes [impact].]}

\section{Project Objectives}
List the specific, measurable objectives your team set at the beginning of this term. These should be distinct from your overall project goals --- they represent what you committed to achieving within this single term.

\textit{[List 3--5 objectives. Each should be specific and verifiable.]}

\section{Scopes and Limitations}
Define the boundaries of your work this term. What is included? What is deliberately excluded? Acknowledge any constraints --- time, data availability, hardware, or team capacity --- that shaped what was achievable.

\section{Report Organization}
This report is organised as follows. Chapter 2 presents the literature review and theoretical background. Chapter 3 describes the methodology and approach adopted. Chapter 4 reports the work completed and results obtained. Chapter 5 evaluates team collaboration and individual contributions. Chapter 6 provides a critical reflection on learning. Chapter 7 presents the plan for the following term. References and appendices follow.

\textit{[Update this paragraph if your chapter titles differ.]}

% =============================================================
% CHAPTER 2: LITERATURE REVIEW (Page 9)
% =============================================================
\clearpage
\setcounter{page}{9}
\chapter{Literature Review and Theoretical Background}

\begin{guidancebox}
\textbf{Writing Guidance --- Chapter 2}\\
Synthesise existing knowledge relevant to your project. Do NOT summarise papers one by one. Weave multiple sources together to discuss themes, compare approaches, and identify gaps. Minimum 400 words. Cite all sources using IEEE format [1], [2], [3]...
\end{guidancebox}

\section{Related Work}
Provide a thematic synthesis of the most relevant prior work in your field. Group sources by theme or approach rather than listing them sequentially. Highlight areas of agreement, contradiction, and open questions in the literature.

\textit{[minimum 250 words, cite multiple sources]}

\section{Theories, Models, and Technologies}
Describe the theoretical foundations, core algorithms, frameworks, or technologies that underpin your project. Explain why these are appropriate for your problem and cite the original sources.

\textit{[minumum of 150 words]}

\section{Research and Technology Gap}
Based on your review, articulate the gap or opportunity your project addresses. What has not been done, or not done well, in the existing literature or practice? How does your project contribute to filling that gap?

\textit{[minumum of 100-200 words]}

% =============================================================
% CHAPTER 3: METHODOLOGY (Page 10)
% =============================================================
\clearpage
\setcounter{page}{10}
\chapter{Methodology}

\begin{guidancebox}
\textbf{Writing Guidance --- Chapter 3}\\
Explain HOW you worked --- the process, tools, decisions, and rationale. A reader should be able to repeat your work.\\
\textbf{Software Development track:} follow your hub pipeline phases. \\
\textbf{Research track:} cover experimental design.\\
\textbf{Minimum 350 words.}
\end{guidancebox}

\section{Overall System Design}
Provide a high-level description of the engineering solution. Define whether it is a Hardware-in-the-loop (HIL), Cyber-Physical System, or a Software-based Analytical Tool. Include a "Block Diagram" showing the flow from physical sensors to data output.

\begin{figure}[H]
\centering
\includegraphics[width=0.88\textwidth]{image3.png}
\caption{Example of smart irrigation systems using IOT}
\label{fig:smart_irrigation}
\end{figure}

This is the most critical part of Chapter 3. You need to explain how the data flows from the student to the analytical engine. High-Level Architecture: Describe the Client-Server model or Microservices.

\textbf{Tech Stack:}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
  \item \textbf{Frontend:} (e.g., React, HTML5/CSS3) for the user interface.
  \item \textbf{Backend:} (e.g., Node.js, Python/Django) for the "VARX" logic and data processing.
  \item \textbf{Database:} (e.g., MySQL or MongoDB) for storing high-resolution activity logs.
\end{itemize}

\section{Hardware Design and Components}
Detail the physical layer of the project. This is the "Methodology" of the physical world:
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
  \item \textbf{Sensor Selection:} Specifications of the sensors used (e.g., PM2.5 laser scattering sensors, DHT22 for climate, or Strain Gauges).
  \item \textbf{Microcontroller/Processing Unit:} Justification for using specific boards (e.g., ESP32, Raspberry Pi, or FPGA).
  \item \textbf{Power Management:} Design of the power supply, especially if it's a remote deployment (Solar vs. Battery).
\end{itemize}

\section{System Software and Logic Flow}
This is where you explain the "Brain" of the project.

\textbf{Data Acquisition Logic:} How often is the system "polling" data? (Sampling rate). 

\textbf{Filtering and Pre-processing:} How do you handle "noise"? (e.g., using a Kalman Filter or Moving Average to ensure the "Dry Season Trap" or sensor drift doesn't corrupt the data).

\textbf{Firmware/Software Stack:} Mention the languages (C++, Python) and frameworks used.

If your work involves datasets, surveys, or sensor data, describe how data was collected, cleaned, and prepared for analysis or model training. Justify any decisions made in this process.

\section{The Analytical Framework (The "Engine")}
Explain the logic used to process data:
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
  \item \textbf{The Algorithm:} Describe the specific logic (e.g., a PID Controller, a Machine Learning Classifier, or a Signal Processing algorithm).
  \item \textbf{Handling Confounding Factors:} Explain how the engineering design "controls" for the environment. (Example: "To prevent high humidity from being misread as high PM2.5, a heating element or a mathematical offset was integrated into the sensor logic").
\end{itemize}

\section{Experimental Setup and Testing Protocol}
How will you prove the system works?
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
  \item \textbf{Simulation Environment:} Detail any software used for stress-testing (e.g., MATLAB/Simulink, AutoCAD, or SolidWorks).
  \item \textbf{Calibration Procedures:} How the system was "zeroed" against a known standard to ensure accuracy.
  \item \textbf{Validation Metrics:} Define what "Success" looks like (e.g., Error margin $<$ 5\%, System Uptime $>$ 98\%, or Latency $<$ 100ms).
\end{itemize}

\section{Work Phases and Activities This Term}
Describe the specific phases or sprints completed this term, following your hub's project pipeline. For each phase, summarise the activities undertaken, decisions made, and outputs produced.

\section{Ethical Considerations}
Describe the ethical dimensions of your work this term. This may include: data privacy and consent, algorithmic fairness and bias, cybersecurity responsibilities, sustainability considerations, or research integrity.

% =============================================================
% CHAPTER 4: RESULTS AND DISCUSSION (Page 13)
% =============================================================
\clearpage
\setcounter{page}{13}
\chapter{Results and Discussion}

\begin{guidancebox}
\textbf{Writing Guidance --- Chapter 4}\\
Present what you produced, measured, or discovered this term --- and then interpret it.\\
Be specific. Include metrics, performance data, screenshots, diagrams, or test results as figures.\\
Discuss what the results mean, not just what they show. \textbf{Minimum 500 words total.}
\end{guidancebox}

\section{Deliverables Produced}
List and briefly describe all tangible outputs produced this term. These may include documents, code repositories, prototypes, models, datasets, test suites, presentations, or hardware assemblies.

\vspace{0.8em}
\renewcommand{\arraystretch}{1.3}
\noindent
\begin{tabularx}{\textwidth}{|c|X|p{6.0cm}|}
\hline
\rowcolor{camtechNavy} \color{white}\bfseries No & \color{white}\bfseries Deliverable & \color{white}\bfseries Status \\
\hline
\rowcolor{white} 1 & & (Complete / In Progress / Pending) \\
\hline
\rowcolor{tableRowAlt} 2 & & (Complete / In Progress / Pending) \\
\hline
\rowcolor{white} 3 & & (Complete / In Progress / Pending) \\
\hline
\rowcolor{tableRowAlt} 4 & & (Complete / In Progress / Pending) \\
\hline
\rowcolor{white} 5 & & (Complete / In Progress / Pending) \\
\hline
\end{tabularx}

\section{Key Results and Findings}
Present your most significant results. Use tables, graphs, and figures where appropriate. Label each figure and table clearly (e.g., Figure 4.1: Confusion matrix for the baseline model). Refer to each figure or table in the text.

\textit{[minimum 300 words, include figures/tables]}

\section{Discussion and Interpretation}
Interpret your results. What do they mean for your project? Do they align with your original objectives? How do they compare with findings from the literature (Chapter 2)? What surprising or counterintuitive results did you encounter, and how do you explain them?

\textit{[minimum 200 words]}

\section{Objectives Review}
Revisit each objective listed in Section 1.3. Report whether it was achieved, partially achieved, or not achieved, and provide evidence for your assessment.

\vspace{0.8em}
\renewcommand{\arraystretch}{1.3}
\noindent
\begin{tabularx}{\textwidth}{|p{3.2cm}|p{5.5cm}|X|}
\hline
\rowcolor{camtechNavy} \color{white}\bfseries Objective & \color{white}\bfseries Status & \color{white}\bfseries Evidence / Explanation \\
\hline
\rowcolor{white} Objective 1: & (Achieved / Partial / Not Achieved) & \\
\hline
\rowcolor{tableRowAlt} Objective 2: & (Achieved / Partial / Not Achieved) & \\
\hline
\rowcolor{white} Objective 3: & (Achieved / Partial / Not Achieved) & \\
\hline
\rowcolor{tableRowAlt} Objective 4: & (Achieved / Partial / Not Achieved) & \\
\hline
\rowcolor{white} Objective 5: & (Achieved / Partial / Not Achieved) & \\
\hline
\end{tabularx}

\section{Challenges Encountered and Solutions}
Describe at least two significant challenges you encountered this term --- technical or team-related. For each, explain what the challenge was, why it arose, and how you addressed it.

% =============================================================
% CHAPTER 5: TEAM COLLABORATION (Page 15)
% =============================================================
\clearpage
\setcounter{page}{15}
\chapter{Team Collaboration and Individual Contributions}

\begin{guidancebox}
\textbf{Writing Guidance --- Chapter 5}\\
Be honest and specific. Generic statements like 'everyone contributed equally' are not acceptable without evidence.\\
Describe how the team functioned, how tasks were divided, and how conflicts --- if any --- were managed.
\end{guidancebox}

\section{Task Allocation and Contribution}

\vspace{0.8em}
\renewcommand{\arraystretch}{1.3}
\noindent
\begin{tabularx}{\textwidth}{|p{3.2cm}|X|p{4.8cm}|}
\hline
\rowcolor{camtechNavy} \color{white}\bfseries Team Member & \color{white}\bfseries Primary Tasks This Term & \color{white}\bfseries Contribution Level \\
\hline
\rowcolor{white} Member 1: & & (High / Medium / Low) \\
\hline
\rowcolor{tableRowAlt} Member 2: & & (High / Medium / Low) \\
\hline
\rowcolor{white} Member 3: & & (High / Medium / Low) \\
\hline
\rowcolor{tableRowAlt} Member 4: & & (High / Medium / Low) \\
\hline
\rowcolor{white} Member 5: & & (High / Medium / Low) \\
\hline
\end{tabularx}

\section{Team Dynamics and Communication}
Describe how the team communicated and made decisions this term. What tools or meeting cadences did you use? How were disagreements or differences of opinion resolved? \textit{(100--150 words)}

\section{Peer Assessment}
Each team member provides a brief honest evaluation of the team's collective performance and their own role within it. Peer assessment is confidential and submitted separately where required. \textit{(50--100 words)}

\section{Application of Learning}
How did you apply knowledge from your courses to your internship work this term? \textit{(100--150 words)}

% =============================================================
% CHAPTER 6: PLAN FOR FORTHCOMING TERM (Page 17)
% =============================================================
\clearpage
\setcounter{page}{17}
\chapter{Plan for the Forthcoming Term}

\begin{guidancebox}
\textbf{Writing Guidance --- Chapter 6}\\
Be specific and realistic. Your next-term plan will be reviewed at the start of the following term.\\
Vague statements ('we will continue developing the system') will be returned for revision.\\
\textbf{SMART objectives: Specific, Measurable, Achievable, Relevant, Time-bound.}
\end{guidancebox}

\section{Objectives for the Next Term}
Reflect analytically on your learning this term. Connect your experiences to the Virtubis expected outcomes and your own professional development goals.

\vspace{0.8em}
\renewcommand{\arraystretch}{1.4}
\noindent
\begin{tabularx}{\textwidth}{|>{\bfseries}p{3.2cm}|X|}
\hline
\rowcolor{tableRowAlt} Objective 1: & \\
\hline
\rowcolor{white} Objective 2: & \\
\hline
\rowcolor{tableRowAlt} Objective 3: & \\
\hline
\rowcolor{white} Objective 4: & \\
\hline
\rowcolor{tableRowAlt} Objective 5: & \\
\hline
\end{tabularx}

\section{Project Timeline and Milestones}

\subsection*{7.3 \ Resources and Support Required}

\vspace{0.6em}
\renewcommand{\arraystretch}{1.3}
\noindent
\begin{tabularx}{\textwidth}{|p{3.2cm}|X|X|}
\hline
\rowcolor{camtechNavy} \color{white}\bfseries Week / Phase & \color{white}\bfseries Milestone & \color{white}\bfseries Success Indicator \\
\hline
\rowcolor{white} & & \\
\hline
\rowcolor{tableRowAlt} & & \\
\hline
\rowcolor{white} & & \\
\hline
\rowcolor{tableRowAlt} & & \\
\hline
\rowcolor{white} & & \\
\hline
\rowcolor{tableRowAlt} & & \\
\hline
\end{tabularx}

\section{Resources and Support Required}
Identify any specific resources, tools, datasets, lab access, or mentorship support your team will need in the forthcoming term to achieve the objectives listed above. \textit{[50-100 words]}

% =============================================================
% CHAPTER 7: REFERENCES (Page 19)
% =============================================================
\clearpage
\setcounter{page}{19}
\chapter{References}

\begin{guidancebox}
\textbf{Citation Format}\\
Use IEEE citation format throughout this report. Number references in order of first citation: [1], [2], [3]...\\
\textbf{IEEE example:} [1] A. B. Author and C. D. Author, "Title of paper," \textit{Journal Name}, vol. X, no. Y, pp. ZZ--ZZ, Mon. Year.\\
All sources must be peer-reviewed unless citing official documentation, standards, or industry reports.
\end{guidancebox}

\vspace{1.5em}
\noindent
% IEEE Reference examples / placeholder entries
\begin{enumerate}[label={[\arabic*]}, leftmargin=2.5em, itemsep=4pt]
  \item A. B. Author and C. D. Author, ``Title of paper,'' \textit{IEEE Transactions on Biomedical Engineering}, vol. 70, no. 4, pp. 1120--1131, Apr. 2023.
  \item E. F. Researcher and G. H. Scientist, ``Urban heat island effects and vector-borne disease transmission dynamics in Southeast Asia,'' \textit{Lancet Planetary Health}, vol. 6, no. 8, pp. e642--e651, Aug. 2022.
  \item CamTech Faculty of Engineering, ``Virtubis Internship Guidelines and Assessment Framework,'' \textit{CamTech Academic Standards}, 2024.
\end{enumerate}

% =============================================================
% CHAPTER 8: APPENDICES (Page 20)
% =============================================================
\clearpage
\setcounter{page}{20}
\chapter{Appendices}

The following appendices contain supplementary materials referenced in the main body of this report. All appendices should be labelled clearly and referred to at least once in the main text (e.g., see Appendix A).

\section*{Appendix A --- System Architecture Diagrams}
\addcontentsline{toc}{section}{Appendix A --- System Architecture Diagrams}
\textit{[Insert content here or note: 'Available in the project repository at [link].']}

\vspace{1.2em}

\section*{Appendix B --- Code Repository Link and Key Code Excerpts}
\addcontentsline{toc}{section}{Appendix B --- Code Repository Link and Key Code Excerpts}
\textit{[Insert content here or note: 'Available in the project repository at [link].']}

\vspace{1.2em}

\section*{Appendix C --- Test Results and Data Samples}
\addcontentsline{toc}{section}{Appendix C --- Test Results and Data Samples}
\textit{[Insert content here or note: 'Available in the project repository at [link].']}

\vspace{1.2em}

\section*{Appendix D --- Additional Figures and Tables}
\addcontentsline{toc}{section}{Appendix D --- Additional Figures and Tables}
\textit{[Insert content here or note: 'Available in the project repository at [link].']}

\vspace{1.2em}

\section*{Appendix E --- Bi-Weekly Activity Log (summary)}
\addcontentsline{toc}{section}{Appendix E --- Bi-Weekly Activity Log (summary)}
\textit{[Insert content here or note: 'Available in the project repository at [link].']}

\vfill

\begin{center}
  \small\bfseries\color{camtechNavy}
  FENG i-Hub \quad|\quad Virtubis Software Development Track \quad|\quad CamTech University \quad|\quad Learn. Build. Innovate.
\end{center}

\end{document}
"""
    },
}
