"""Perhitungan statistik sederhana."""


def rata_rata(angka):
    return sum(angka) / len(angka)


def median(angka):
    urut = sorted(angka)
    tengah = len(urut) // 2
    if len(urut) % 2 == 1:
        return float(urut[tengah])
    return (urut[tengah - 1] + urut[tengah]) / 2
