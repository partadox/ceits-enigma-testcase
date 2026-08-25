from statistik.hitung import rata_rata


def main():
    angka = [int(x) for x in input().split()]
    print("rata-rata: %.2f" % rata_rata(angka))


if __name__ == "__main__":
    main()
