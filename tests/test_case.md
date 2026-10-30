# Dokumentasi Test Case

## Nama Proyek
Aplikasi Analisis Nilai Siswa

## Tujuan Pengujian
Memastikan fungsi pengolahan nilai bekerja sesuai
dengan spesifikasi program.

## Tabel Test Case

| ID | Fitur | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC01 | Rata-rata | [70,80,90] | 80 | 80 | PASS |
| TC02 | Data kosong | [] | 0 | 0 | PASS |
| TC03 | Kelulusan | 60 | Lulus | Lulus | PASS |
| TC04 | Tidak lulus | 59 | Tidak lulus | Tidak lulus | PASS |
| TC05 | Nilai minimum | [70,50,90] | 50 | 50 | PASS |
| TC06 | Nilai maksimum | [70,50,90] | 90 | 90 | PASS |
| TC07 | Minimum kosong | [] | None | None | PASS |
| TC08 | Maksimum kosong | [] | None | None | PASS |
| TC09 | Ringkasan | [70,80,50] | Rata-rata 66.67 | 66.67 | PASS |
| TC10 | Ringkasan kosong | [] | Jumlah 0 | 0 | PASS |

## Kesimpulan

Test case dirancang untuk memeriksa kondisi normal,
batas kelulusan, dan data kosong.

Status aktual harus disesuaikan dengan hasil pengujian
yang benar-benar dilakukan.

Pengujian input tidak valid dan penyimpanan file CSV
dilakukan secara terpisah melalui program utama.