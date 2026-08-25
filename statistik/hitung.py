"""Perhitungan statistik sederhana."""


def rata_rata(angka):
    return sum(angka) / len(angka)


def median(angka):
    urut = sorted(angka)
    tengah = len(urut) // 2
    # Keliru untuk jumlah data genap: seharusnya rata-rata dua nilai tengah.
    return float(urut[tengah])
