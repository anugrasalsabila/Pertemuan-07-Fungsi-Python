def jumlah_n(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total


n = int(input("Masukkan nilai n: "))

hasil = jumlah_n(n)

print("Jumlah 1 sampai", n, "=", hasil)