# Pertemuan 07 Fungsi Python

Nama: Intan Anugra Salsabila
NIM: 2225250154
Kelas: 3F

## Tujuan

Menggunakan fungsi, parameter, return value, dan scope untuk membuat program modular.

## Cara Menjalankan

python3 praktik/utilitas_matematika.py

Pada Windows, gunakan perintah berikut jika python3 tidak dikenali:

python praktik/utilitas_matematika.py

## Struktur Fungsi

1. salam(nama, kelas): menerima nama dan kelas sebagai parameter, kemudian menampilkan salam.
2. luas_persegi_panjang(p, l): menghitung luas persegi panjang dan mengembalikan hasil menggunakan return.
3. jumlah_n(n): menghitung jumlah bilangan dari 1 sampai n menggunakan perulangan for.
4. statistik(data): menghitung nilai minimum, maksimum, dan rata-rata data.
5. demo(x): menunjukkan perbedaan variabel lokal dan variabel global.
6. luas_segitiga(a, t): menghitung luas segitiga dan mengembalikan hasil menggunakan return.
7. faktorial(n): menghitung faktorial menggunakan perulangan dan mengembalikan hasil.
8. tampilkan_menu(): menampilkan pilihan operasi matematika.

## Hasil Pengujian

### Latihan 1 - Fungsi Salam

Input:
Nama = Intan Anugra Salsabila
Kelas = 3F

Hasil yang diharapkan:
Program menampilkan salam beserta nama dan kelas.

Hasil aktual:
Halo, Intan Anugra Salsabila dari kelas 3F. Selamat belajar Python!

### Latihan 2 - Luas Persegi Panjang

Pengujian pertama:
Input: p = 8, l = 5
Hasil yang diharapkan: 40
Hasil aktual: 40.0

Pengujian kedua:
Input: p = 2.5, l = 4
Hasil yang diharapkan: 10
Hasil aktual: 10.0

Pengujian ketiga:
Input: p = 0, l = 7
Hasil yang diharapkan: 0
Hasil aktual: 0.0

### Latihan 3 - Jumlah 1 sampai n

Pengujian pertama:
Input: n = 1
Hasil yang diharapkan: 1
Hasil aktual: 1

Pengujian kedua:
Input: n = 5
Hasil yang diharapkan: 15
Hasil aktual: 15

Pengujian ketiga:
Input: n = 10
Hasil yang diharapkan: 55
Hasil aktual: 55

Pengujian keempat:
Input: n = 100
Hasil yang diharapkan: 5050
Hasil aktual: 5050

### Latihan 4 - Statistik Sederhana

Input:
Data = [70, 80, 65, 90, 75]

Hasil yang diharapkan:
Nilai minimum = 65
Nilai maksimum = 90
Rata-rata = 76.0

Hasil aktual:
Nilai minimum = 65.0
Nilai maksimum = 90.0
Rata-rata = 76.0

### Latihan 5 - Eksperimen Scope

Input:
x = 10
demo(20)

Hasil yang diharapkan:
Variabel x di luar fungsi tetap 10 dan hasil fungsi adalah 25.

Hasil aktual:
di dalam fungsi: 20 25
di luar fungsi: 10 25


### Praktik 2 - Utilitas Matematika Modular

#### Pengujian 1 - Luas Persegi Panjang

| Input | Hasil yang Diharapkan | Hasil Aktual |
|---|---|---|
| p = 8, l = 5 | 40 | 40.0 |

#### Pengujian 2 - Luas Segitiga

| Input | Hasil yang Diharapkan | Hasil Aktual |
|---|---|---|
| a = 10, t = 6 | 30.0 | 30.0 |

#### Pengujian 3 - Jumlah 1 sampai n

| Input | Hasil yang Diharapkan | Hasil Aktual |
|---|---|---|
| n = 10 | 55 | 55 |

#### Pengujian 4 - Faktorial

| Input | Hasil yang Diharapkan | Hasil Aktual |
|---|---|---|
| n = 5 | 120 | 120 | 
| n = 0 | 1 | 1 | 


## Refleksi

Setelah program dibagi menjadi beberapa fungsi, kode menjadi lebih terstruktur dan mudah dibaca. Setiap fungsi memiliki tugas tertentu sehingga rumus dapat digunakan kembali tanpa menulis ulang kode. Parameter digunakan untuk menerima data, sedangkan return digunakan untuk mengembalikan hasil perhitungan agar dapat digunakan pada bagian program lain. Pemahaman scope membantu membedakan variabel lokal dan variabel global.