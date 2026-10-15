# Template Elsevier elsarticle — Daniandra

Proyek baru terpisah dari IEEE dan naskah jurnal yang sudah ada. Dokumen ini hanya kerangka; bukan artikel ilmiah selesai. Penulis yang dicantumkan: Daniandra Prayudisty Ilham. Afiliasi, kontak, jurnal tujuan, rekan penulis, isi ilmiah, hasil, dan referensi harus dikonfirmasi sendiri; tidak diasumsikan.

## Mulai menggunakan
1. Buka `main.tex` sebagai dokumen utama di editor dan klik Compile.
2. Ganti judul, abstrak, kata kunci, serta setiap paragraf pending dengan isi yang Anda setujui. Tambahkan afiliasi memakai sintaks `\affiliation{organization={...},...}` pada contoh resmi setelah datanya pasti.
3. Isi `references.bib` dengan sumber terverifikasi. Hapus judul References manual dan paragraf placeholder; aktifkan `\bibliographystyle{elsarticle-num}` dan `\bibliography{references}`. Tambahkan `\cite{key}` yang cocok. Jangan menambahkan referensi palsu untuk sekadar menghilangkan placeholder.
4. Compile ulang; latexmk menjalankan pass yang diperlukan.

## Pilihan format resmi
Baris aktif saat ini: `\documentclass[preprint,12pt]{elsarticle}` (satu kolom, numerik).
Pilihan lain, hanya jika diminta jurnal:
- `\documentclass[preprint,review,12pt]{elsarticle}`: review dengan spasi diperlebar.
- `\documentclass[final,1p,times]{elsarticle}`: format 1p.
- `\documentclass[final,3p,times]{elsarticle}` atau tambahkan `twocolumn` sesuai petunjuk: format 3p.
- `\documentclass[final,5p,times,twocolumn]{elsarticle}`: format 5p.
Jangan mengaktifkan beberapa documentclass sekaligus. Persyaratan jurnal tujuan SELALU mengalahkan pilihan default template ini. Template generik Elsevier tidak menjamin cocok untuk semua jurnal Elsevier atau status submission-ready.

## Sitasi numerik dan author–year
- Numerik: `elsarticle-template-num.tex`, `elsarticle-num.bst`, dan `\biboptions{numbers,sort&compress}` seperti main.tex saat ini.
- Numerik dengan nama: lihat `elsarticle-template-num-names.tex` dan `elsarticle-num-names.bst`.
- Harvard / author–year: ikuti `elsarticle-template-harv.tex`, tambahkan opsi kelas `authoryear`, ganti biboptions numerik menjadi `\biboptions{authoryear}`, dan gunakan `\bibliographystyle{elsarticle-harv}`. Gunakan `\citet{key}` / `\citep{key}` sesuai kebutuhan; jangan pertahankan opsi numbers.

## Berkas resmi dan asal
- `elsarticle.cls` di root dihasilkan TANPA modifikasi dari .dtx/.ins unggahan pengguna dengan `latex -no-shell-escape -interaction=nonstopmode -halt-on-error elsarticle.ins`.
- Tiga `.bst` dan tiga contoh `.tex` asli tersedia di root. Contoh asli bukan isi naskah Anda dan bukan main document.
- `official-template/elsarticle/` menyimpan sumber teks, manifest, README, changelog, dan sumber dokumentasi asli, tanpa diubah.
- `assets/elsarticle-original.zip` mempertahankan arsip unggahan byte-identik, termasuk seluruh struktur dokumentasi PDF asli.
- PDF dokumentasi/contoh juga tersedia di `assets/`, termasuk `elsdoc.pdf`. Endpoint upload studio menaruh berkas biner dalam folder assets; struktur aslinya tetap lengkap di ZIP.
- `PROVENANCE.json`: hash arsip dan daftar hash sumber asli.

## Kompilasi aman di terminal Linux
```
latexmk -pdf -interaction=nonstopmode -halt-on-error -no-shell-escape -outdir=build main.tex
```
Backend Studio memakai perintah ini. Jangan aktifkan shell escape untuk template ini. Folder build berisi keluaran otomatis; edit sumber, bukan PDF.
