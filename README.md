# Yudiaz LaTeX Studio
**Enterprise Cloud LaTeX Workspace & Realtime Compiler**  
*Internal Platform — Yudiaz Creative Studio*

---

## 1. Arsitektur & Spesifikasi Sistem
- **Backend**: FastAPI (Python 3.12 via `uv`), Uvicorn ASGI server
- **Engine LaTeX**: TeX Live 2023 (`pdfTeX 3.141592653`, `latexmk 4.83`)
- **Paket Terinstal**: `texlive-latex-base`, `texlive-latex-recommended`, `texlive-latex-extra`, `texlive-publishers` (IEEEtran), `texlive-science`, `texlive-fonts-recommended`
- **Frontend**: SPA Modern Executive Yudiaz Studio (Ace Editor LaTeX mode, PDF live preview, folderization tree)
- **Port Internal**: `127.0.0.1:9559`
- **Reverse Proxy**: Caddy Web Server dengan auto HTTPS/SSL

---

## 2. Domain & Akses
1. **Domain Utama**: `https://latex.daniandraaa.my.id`
   *(Arahkan DNS Record A `latex` ke IP VPS `20.200.220.190` di Cloudflare/Registrar)*
2. **Domain Live Direct (SSL Aktif Sekarang)**:  
   `https://latex.20.200.220.190.sslip.io`

---

## 3. Fitur Utama
1. **Folderisasi Hierarkis Workspace**:
   - Struktur folder bertingkat (e.g. `Bisnis & Klien > Soetahills Real Estate`, `Akademik > Skripsi & Riset`).
   - Dokumen dapat dipindahkan, difilter, dan dikelompokkan sesuai kebutuhan.
2. **Editor LaTeX & Live Compilation**:
   - Syntax highlighting, auto-complete, line number indicator.
   - Shortcut `Ctrl+S` / `Cmd+S` untuk simpan dan auto-kompilasi.
   - Shortcut `Ctrl+Enter` untuk kompilasi instan.
   - Log kompilasi interaktif dengan deteksi baris error.
3. **Online Shareable Preview**:
   - Setiap dokumen memiliki tautan publik unik: `/preview/{share_id}`.
   - Pratinjau PDF di browser tanpa perlu login, lengkap dengan tombol Download PDF.
   - Akses publik dapat diaktifkan/dinonaktifkan kapan saja.
4. **Export & Download**:
   - Download PDF hasil kompilasi langsung.
   - Export Source Code dalam format `.zip` (termasuk aset gambar dan bibliografi).

---

## 4. Integrasi Agent API (Otomasi Dokumen)
Agent AI (Daffa, Raziel, Cucurella) dapat membuat dan mengedit dokumen secara terprogram:

- `POST /api/projects`: Buat dokumen baru dengan template (`blank`, `proposal`, `paper`, `skripsi`)
- `PUT /api/projects/{id}/files/main.tex`: Update isi kode LaTeX
- `POST /api/projects/{id}/compile`: Jalankan kompilasi PDF
- `GET /api/projects/{id}/pdf`: Ambil file PDF
- `GET /preview/{share_id}`: Link pratinjau online untuk klien/rekan kerja

---

## 5. Layanan Systemd VPS
- **Unit**: `/etc/systemd/system/yudiaz-latex.service`
- **Perintah Manajemen**:
  ```bash
  sudo systemctl status yudiaz-latex
  sudo systemctl restart yudiaz-latex
  sudo journalctl -u yudiaz-latex -f
  ```
