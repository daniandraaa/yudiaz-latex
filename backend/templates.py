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
