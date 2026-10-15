def statistik(data):
    total = 0
    minimum = data[0]
    maksimum = data[0]

    for x in data:
        total = total + x

        if x < minimum:
            minimum = x

        if x > maksimum:
            maksimum = x

    rata_rata = total / len(data)

    return minimum, maksimum, rata_rata


jumlah_data = int(input("Masukkan banyak data: "))

data = []

if jumlah_data > 0:
    for i in range(jumlah_data):
        nilai = float(input("Masukkan nilai ke-" + str(i + 1) + ": "))
        data.append(nilai)

    minimum, maksimum, rata_rata = statistik(data)

    print("Nilai minimum =", minimum)
    print("Nilai maksimum =", maksimum)
    print("Rata-rata =", rata_rata)
else:
    print("Banyak data harus lebih dari 0")