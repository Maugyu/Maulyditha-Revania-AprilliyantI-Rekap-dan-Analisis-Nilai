def input_nama():
    """Meminta nama siswa dan menolak nama kosong."""
    while True:
        nama = input("Masukkan nama siswa: ").strip()

        if nama:
            return nama

        print("Nama tidak boleh kosong.")


def input_nilai():
    """Meminta nilai siswa dengan rentang 0 sampai 100."""
    while True:
        masukan = input("Masukkan nilai (0-100): ").strip()

        try:
            nilai = float(masukan)

        except ValueError:
            print(
                "Input tidak valid. "
                "Masukkan nilai berupa angka."
            )
            continue

        if not 0 <= nilai <= 100:
            print("Nilai harus berada antara 0 dan 100.")
            continue

        return nilai