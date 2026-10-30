from pathlib import Path

from src.input_data import input_nama, input_nilai
from src.proses import (
    hitung_rata_rata,
    ringkasan,
    status_lulus,
)
from src.output import tampilkan_data, tampilkan_ringkasan


# Lokasi file data
BASE_DIR = Path(__file__).resolve().parent
FILE_DATA = BASE_DIR / "data" / "nilai_siswa.csv"


def muat_data():
    """Memuat data siswa dari file CSV."""
    import csv

    data_siswa = []

    if not FILE_DATA.exists():
        return data_siswa

    try:
        with FILE_DATA.open(
            mode="r",
            newline="",
            encoding="utf-8",
        ) as file:
            pembaca = csv.DictReader(file)

            for baris in pembaca:
                try:
                    nama = baris["nama"].strip()
                    nilai = float(baris["nilai"])

                    if nama and 0 <= nilai <= 100:
                        data_siswa.append({
                            "nama": nama,
                            "nilai": nilai,
                        })

                except (ValueError, KeyError, TypeError):
                    # Lewati baris yang tidak valid.
                    continue

    except OSError as error:
        print(f"Gagal membaca data: {error}")

    return data_siswa


def simpan_data(data_siswa):
    """Menyimpan data siswa ke file CSV."""
    import csv

    try:
        FILE_DATA.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with FILE_DATA.open(
            mode="w",
            newline="",
            encoding="utf-8",
        ) as file:
            kolom = ["nama", "nilai"]

            penulis = csv.DictWriter(
                file,
                fieldnames=kolom,
            )

            penulis.writeheader()
            penulis.writerows(data_siswa)

        return True

    except OSError as error:
        print(f"Gagal menyimpan data: {error}")
        return False


def tambah_siswa(data_siswa):
    """Memasukkan data siswa baru."""
    print("\n--- Tambah Data Siswa ---")

    nama = input_nama()
    nilai = input_nilai()

    siswa = {
        "nama": nama,
        "nilai": nilai,
    }

    data_siswa.append(siswa)

    if simpan_data(data_siswa):
        print("Data siswa berhasil disimpan.")
    else:
        data_siswa.pop()
        print("Data tidak ditambahkan karena gagal disimpan.")


def tampilkan_semua(data_siswa):
    """Menampilkan seluruh data siswa."""
    print("\n--- Daftar Nilai Siswa ---")

    if not data_siswa:
        print("Belum ada data siswa.")
        return

    tampilkan_data(data_siswa)


def analisis_nilai(data_siswa):
    """Menampilkan ringkasan statistik nilai."""
    print("\n--- Analisis Nilai Siswa ---")

    if not data_siswa:
        print("Belum ada data untuk dianalisis.")
        return

    nilai = [
        siswa["nilai"]
        for siswa in data_siswa
    ]

    hasil = ringkasan(nilai)

    tampilkan_ringkasan(hasil)

    print("\n--- Status Kelulusan ---")

    for siswa in data_siswa:
        status = (
            "Lulus"
            if status_lulus(siswa["nilai"])
            else "Tidak Lulus"
        )

        print(
            f"{siswa['nama']}: "
            f"{siswa['nilai']:.2f} - {status}"
        )


def main():
    """Menjalankan menu utama aplikasi."""
    data_siswa = muat_data()

    while True:
        print("\n================================")
        print(" APLIKASI ANALISIS NILAI SISWA")
        print("================================")
        print("1. Tambah data siswa")
        print("2. Tampilkan data siswa")
        print("3. Analisis nilai")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            tambah_siswa(data_siswa)

        elif pilihan == "2":
            tampilkan_semua(data_siswa)

        elif pilihan == "3":
            analisis_nilai(data_siswa)

        elif pilihan == "4":
            print("Terima kasih telah menggunakan program.")
            break

        else:
            print(
                "Pilihan tidak valid. "
                "Silakan masukkan angka 1 sampai 4."
            )


if __name__ == "__main__":
    main()