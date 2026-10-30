# Aplikasi Analisis Nilai Siswa

## 1. Deskripsi
Aplikasi Analisis Nilai Siswa merupakan program Python
untuk membantu pengguna mengelola dan menganalisis nilai siswa.

Program dapat menghitung rata-rata nilai, menentukan
kelulusan, serta menampilkan nilai minimum dan maksimum.

## 2. Tujuan
1. Mempermudah pengolahan nilai siswa.
2. Menghitung statistik nilai secara otomatis.
3. Menentukan status kelulusan siswa.
4. Menyimpan data nilai agar dapat digunakan kembali.

## 3. Fitur
- Menambahkan data siswa.
- Memvalidasi nilai siswa.
- Menampilkan seluruh data siswa.
- Menghitung rata-rata nilai.
- Menampilkan nilai tertinggi dan terendah.
- Menentukan status kelulusan.
- Menyimpan data ke file CSV.
- Memuat data dari file CSV.

## 4. Persyaratan
- Python 3.10 atau versi yang lebih baru.
- Visual Studio Code (opsional).
- Tidak memerlukan library eksternal.

## 5. Cara Menjalankan

Buka terminal pada folder proyek, kemudian jalankan:

python main.py

## 6. Struktur Folder

- main.py: program utama.
- src/input_data.py: validasi input pengguna.
- src/proses.py: pengolahan dan analisis nilai.
- src/output.py: tampilan hasil analisis.
- data/nilai_siswa.csv: penyimpanan data siswa.
- tests/test_proses.py: pengujian otomatis.
- docs/test_case.md: dokumentasi pengujian.
- docs/bug_log.md: catatan bug dan perbaikannya.

## 7. Aturan Kelulusan

Siswa dinyatakan lulus apabila memperoleh nilai
minimal 60.

Rentang nilai yang diterima adalah 0 sampai 100.

## 8. Pengujian

Jalankan pengujian otomatis menggunakan perintah:

python -m unittest discover -s tests -v

Pengujian mencakup:
- Perhitungan rata-rata.
- Data kosong.
- Nilai minimum dan maksimum.
- Penentuan kelulusan.
- Input nilai di luar rentang.

## 9. Penyimpanan Data

Data siswa disimpan dalam format CSV di folder data.
Data dapat dibaca kembali ketika program dijalankan.

## 10. Known Issues

- Program berjalan melalui terminal.
- Tampilan program masih berbasis teks.
- Program belum memiliki sistem login pengguna.

## 11. Anggota dan Kontribusi

Nama anggota 1: [Isi nama]
Kontribusi: [Isi kontribusi]

Nama anggota 2: [Isi nama]
Kontribusi: [Isi kontribusi]

## 12. Referensi

- Bahan Ajar Algoritma dan Pemrograman Pertemuan 15.
- Dokumentasi resmi Python.
- Dokumentasi modul unittest Python.

Bantuan AI digunakan dalam penyusunan awal kode dan dokumentasi.
Kode perlu dipahami, diperiksa, dan diuji kembali oleh anggota tim.