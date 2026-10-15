def luas_persegi_panjang(p, l):
    luas = p * l
    return luas


def luas_segitiga(a, t):
    luas = 0.5 * a * t
    return luas


def jumlah_n(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total


def faktorial(n):
    hasil = 1

    for i in range(2, n + 1):
        hasil = hasil * i

    return hasil


def tampilkan_menu():
    print("\n=== UTILITAS MATEMATIKA ===")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")


tampilkan_menu()

pilihan = input("Masukkan pilihan: ")

if pilihan == "1":
    p = float(input("Masukkan panjang: "))
    l = float(input("Masukkan lebar: "))

    hasil = luas_persegi_panjang(p, l)
    print("Luas persegi panjang =", hasil)

elif pilihan == "2":
    a = float(input("Masukkan alas: "))
    t = float(input("Masukkan tinggi: "))

    hasil = luas_segitiga(a, t)
    print("Luas segitiga =", hasil)

elif pilihan == "3":
    n = int(input("Masukkan nilai n: "))

    if n >= 0:
        hasil = jumlah_n(n)
        print("Jumlah 1 sampai", n, "=", hasil)
    else:
        print("n harus bilangan bulat nonnegatif")

elif pilihan == "4":
    n = int(input("Masukkan nilai n: "))

    if n >= 0:
        hasil = faktorial(n)
        print("Faktorial", n, "=", hasil)
    else:
        print("n harus bilangan bulat nonnegatif")

else:
    print("Pilihan tidak valid")