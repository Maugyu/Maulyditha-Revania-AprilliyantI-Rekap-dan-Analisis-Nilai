BATAS_LULUS = 60


def hitung_rata_rata(nilai):
    """Menghitung rata-rata nilai.

    Mengembalikan 0 jika daftar nilai kosong.
    """
    if not nilai:
        return 0

    return sum(nilai) / len(nilai)


def status_lulus(nilai, batas=BATAS_LULUS):
    """Menentukan apakah nilai memenuhi batas kelulusan."""
    return nilai >= batas


def nilai_minimum(nilai):
    """Mengembalikan nilai terendah atau None jika kosong."""
    if not nilai:
        return None

    return min(nilai)


def nilai_maksimum(nilai):
    """Mengembalikan nilai tertinggi atau None jika kosong."""
    if not nilai:
        return None

    return max(nilai)


def ringkasan(nilai):
    """Menghasilkan ringkasan statistik nilai."""
    return {
        "jumlah": len(nilai),
        "rata_rata": hitung_rata_rata(nilai),
        "minimum": nilai_minimum(nilai),
        "maksimum": nilai_maksimum(nilai),
        "jumlah_lulus": sum(
            1 for angka in nilai
            if status_lulus(angka)
        ),
    }