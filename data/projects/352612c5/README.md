# Proposal TA — Daffa — Template Metodologi Penelitian 2026

## Status dan pilihan berkas
- `main.tex` adalah **edisi fidelitas 37 halaman**, dengan teks LaTeX nyata di `pages/page01.tex` sampai `page37.tex`, bukan tangkapan layar halaman. Angka halaman, salah ketik, instruksi, contoh penelitian, halaman kosong, daftar isi cache, dan contoh AI dipertahankan dari sumber. Ini templat contoh, **bukan proposal Daffa yang sudah diisi/disetujui**.
- `identity.tex` memusatkan judul, nama, NIM, tahun. Semua masih persis placeholder sumber karena identitas lengkap/topik belum diberikan. Nama proyek menyebut Daffa; isi tidak mengarang identitas.
- `editable-content.tex` adalah **seluruh konten DOCX dalam LaTeX semantik/reflowing**, termasuk tabel, heading, rumus, dan media asli; lebih nyaman untuk menulis panjang. Ini berkas konten, bukan standalone. Jangan menganggap pagination-nya identik dengan PDF. Direktori `docxmedia/` mempertahankan jalur impor aslinya.
- `writing-style.tex` berisi helper penulisan lanjut (paragraf tanpa indentasi, 1,5 spasi, tabel 11 pt single, caption, citet/citep). Belum dimuat oleh main.tex agar tidak diam-diam merusak fidelitas.
- `CHECKLIST_AUDIT.md/json`: semua 51 kriteria nyata (nomor 11 di sumber berulang), status implementasi/manual/konflik dan alasan. **Bukan klaim semua checklist lulus.**

## Kompilasi yang benar
`latexmk -pdf -no-shell-escape -interaction=nonstopmode -halt-on-error -outdir=build main.tex`

`.latexmkrc` mengarahkan aturan PDF ke XeLaTeX untuk font subset asli. Shell escape tetap nonaktif. Tidak ada perubahan compiler/backend Studio/global project. Instalasi lokal memerlukan texlive-xetex, latexmk, fontspec, graphicx, xcolor. Studio berada pada server yang sama dan dapat memuat konfigurasi proyek ini.

## Cara mengedit
1. Identitas: ubah `identity.tex`, pertahankan escaping LaTeX untuk `%`, `&`, `_`.
2. Teks tetap visual: cari komentar/teks di `pages/pageNN.tex`; setiap kata/fragmen nyata ada sebagai argumen terakhir-sebelum-warna `\Exact`. Parameter meliputi font, ukuran asli dalam bp, posisi x/y dan lebar. **Edisi fidelitas menggunakan posisi tetap: tambahan panjang tidak mengalir otomatis, dan resizebox mempertahankan lebar lama**. Untuk pergantian paragraf panjang gunakan `editable-content.tex` sebagai edisi penulisan ulang, bukan menumpuk teks pada halaman tetap.
3. Edisi semantik mempertahankan contoh dan instruksi, tetapi daftar isi/sitasi hasil DOCX masih membutuhkan migrasi ke field LaTeX otomatis. Jangan menyatakan daftar isi/referensi contoh sebagai terverifikasi. Ganti hanya setelah materi penelitian diberikan.
4. Font di `assets/font*.ttf` adalah subset font asli dari PDF, sehingga glyph baru yang tidak ada dapat hilang. Untuk naskah dengan identitas/teks baru, sediakan font Times New Roman berlisensi lengkap atau gunakan fallback Liberation Serif dengan pengakuan perbedaan metrik; kompilasi dan audit ulang. Font63 (MS-PMincho) dan font84 (Cambria Math) hanya mendapat glyph spasi kosong tambahan; garis besar glyph asli tidak diubah.

## Sumber dan pelestarian
Sumber otoritatif adalah DOCX asli `Template Metodologi Penelitian 2026 v16Oktober2026.docx`; PDF pasangannya menjadi referensi penempatan visual. XML section/style/numbering, relationship image dan semua 7 media asli telah diinventarisasi dalam folder bukti luar. DOCX menyatakan Normal Times New Roman 12 pt, 1,5 line, after 8 pt; Heading1 14 pt bold, centered; portrait 4 cm kiri/3 cm lainnya, landscape 3 cm kiri/4 cm atas. PDF menggunakan MediaBox dibulatkan 596×842 bp (landscape 842×596 pada halaman PDF 26), dipertahankan demi fidelitas.

`assets/original-graphics-only.pdf` **bukan PDF halaman penuh dengan teks**: semua operator teks BT…ET telah dihapus; hanya path/vektor, gambar raster asli, clipping dan warna sumber yang dipakai untuk mempertahankan tabel, logo, screenshot, chart, diagram. Teks utama termasuk isi tabel dan caption dibuat ulang sebagai LaTeX nyata. Tidak ada logo, wajah, tanda tangan atau gambar sintetis. `assets/image*` adalah media DOCX identik-byte. Pada PDF contoh ada tujuh ilustrasi: logo, chart cabai, contoh paragraf, login aplikasi, grafik, flowchart, screenshot wawancara.

## Konflik yang tidak disembunyikan
- PDF front matter memakai angka Arab meskipun DOCX menyebut lowerRoman; edisi visual mengikuti PDF.
- Daftar isi cache menyebut abstrak dan Bab IV–VI yang tidak memiliki halaman di sumber; tidak dibuat isi/hasil palsu.
- Halaman 8/9 memisahkan heading daftar lampiran dari isinya; halaman PDF 30 hanya nomor 21; halaman-halaman contoh jarang isi tetap dipertahankan.
- Nomor Gambar I-1 berulang, rujukan I-2 tidak sinkron; daftar referensi contoh state-of-art tidak lengkap; tidak dikarang untuk menutupinya.
- Checklist meminta 3 kalimat/paragraf sedangkan instruksi template menyebut 2; penulisan final perlu mengikuti yang lebih ketat atas konfirmasi pembimbing.
- Klaim penggunaan ChatGPT/Gemini/Claude pada lampiran adalah **contoh kata sumber**, bukan bukti Daffa benar-benar memakai layanan tersebut. Daffa harus mengisi disclosure dan bukti aktual.

## Verifikasi
Kompilasi nyata XeLaTeX tanpa shell escape, 37 halaman; pemeriksaan semua halaman/MediaBox, font, gambar dan teks; komparasi raster per halaman 72 dpi tersimpan di `visual_comparison.json` folder bukti. Hasil dekat secara terukur tetapi **tidak diklaim pixel-perfect**. Rendering anti-aliasing, shaping dan title/TOC dapat berbeda. Setelah edit apa pun, kompilasi dan review ulang seluruh halaman yang terpengaruh. Tidak ada kriteria substantif riset yang dapat disahkan hanya dari templat.
