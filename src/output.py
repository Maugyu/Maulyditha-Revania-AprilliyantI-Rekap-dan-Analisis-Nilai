def tampilkan_data(data_siswa):
    """Menampilkan daftar nama dan nilai siswa."""
    print("-" * 40)
    print(f"{'No.':<5}{'Nama':<22}{'Nilai':>10}")
    print("-" * 40)

    for nomor, siswa in enumerate(data_siswa, start=1):
        print(
            f"{nomor:<5}"
            f"{siswa['nama']:<22}"
            f"{siswa['nilai']:>10.2f}"
        )

    print("-" * 40)


def tampilkan_ringkasan(hasil):
    """Menampilkan hasil analisis statistik."""
    print(f"Jumlah siswa  : {hasil['jumlah']}")
    print(f"Rata-rata     : {hasil['rata_rata']:.2f}")

    if hasil["minimum"] is None:
        print("Nilai minimum: Tidak tersedia")
    else:
        print(f"Nilai minimum : {hasil['minimum']:.2f}")

    if hasil["maksimum"] is None:
        print("Nilai maksimum: Tidak tersedia")
    else:
        print(f"Nilai maksimum: {hasil['maksimum']:.2f}")

    print(f"Jumlah lulus  : {hasil['jumlah_lulus']}")
    print(
        f"Jumlah tidak lulus: "
        f"{hasil['jumlah'] - hasil['jumlah_lulus']}"
    )