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
    }
}
