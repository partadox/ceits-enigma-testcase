# Contoh kiriman Enigma — mode REPO

Repositori ini adalah **contoh pekerjaan mahasiswa**, bukan bagian dari sistem
Enigma. Gunanya satu: bahan uji untuk mode `REPO`, tempat mahasiswa
mengumpulkan tautan repositori lalu memilih commit mana yang dinilai.

> Repositori kiriman harus **publik**. Enigma tidak pernah memegang kredensial
> siapa pun untuk membacanya — klon dilakukan tanpa kredensial sama sekali,
> justru supaya tidak ada rahasia yang bisa bocor lewat jalur ini.

## Soalnya

Baca sederet bilangan bulat dari satu baris masukan, lalu cetak dua baris:

```
rata-rata: <dua angka di belakang koma>
median: <dua angka di belakang koma>
```

Contoh:

```
masukan : 3 1 4 1 5
keluaran: rata-rata: 2.80
          median: 3.00
```

## Isinya

```
main.py             berkas utama — yang dijalankan
statistik/
  __init__.py
  hitung.py         rata-rata dan median
```

Struktur berbilang berkas ini disengaja: ia menguji bahwa runner benar-benar
menyerahkan seluruh isi repositori ke dalam kotak, bukan hanya satu berkas.

## Yang disetel dosen di Enigma

Kriteria **Uji keluaran**, dengan berkas utama `main.py` dan beberapa kasus:

| Masukan | Keluaran yang diharapkan |
| --- | --- |
| `3 1 4 1 5` | `rata-rata: 2.80` / `median: 3.00` |
| `10` | `rata-rata: 10.00` / `median: 10.00` |
| `2 4 6 8` | `rata-rata: 5.00` / `median: 5.00` |

Kriteria **Periksa aturan penulisan** boleh melarang `os` dan `subprocess` —
soal ini tidak membutuhkan keduanya.
