def luas_persegi_panjang(p, l):
    luas = p * l
    return luas

p = float(input("Masukkan panjang: "))
l = float(input("Masukkan lebar: "))

hasil = luas_persegi_panjang(p, l)

print("Luas persegi panjang =", hasil)