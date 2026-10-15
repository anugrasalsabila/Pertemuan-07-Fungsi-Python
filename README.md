# Pertemuan 07 Fungsi Python

Nama: Intan Anugra Salsabila
NIM: 2225250154
Kelas: 3F

## Tujuan

Menggunakan fungsi, parameter, return value, dan scope untuk membuat program modular.

## Cara Menjalankan

Jalankan program utama melalui terminal VS Code:

    python3 praktik/utilitas_matematika.py

Pada Windows, gunakan perintah berikut jika python3 tidak dikenali:

    python praktik/utilitas_matematika.py

## Struktur Fungsi

1. salam(nama, kelas): menerima nama dan kelas, kemudian menampilkan salam.
2. luas_persegi_panjang(p, l): menghitung luas persegi panjang dan mengembalikan hasil menggunakan return.
3. jumlah_n(n): menghitung jumlah bilangan dari 1 sampai n menggunakan perulangan for.
4. statistik(data): menghitung nilai minimum, maksimum, dan rata-rata data.
5. demo(x): menunjukkan perbedaan variabel lokal dan variabel global.
6. luas_segitiga(a, t): menghitung luas segitiga dan mengembalikan hasil menggunakan return.
7. faktorial(n): menghitung faktorial menggunakan perulangan dan mengembalikan hasil.
8. tampilkan_menu(): menampilkan pilihan operasi matematika.

## Hasil Pengujian

| Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|
| p=8, l=5 | 40 | 40.0 | Sesuai |
| p=2.5, l=4 | 10 | 10.0 | Sesuai |
| p=0, l=7 | 0 | 0.0 | Sesuai |
| a=10, t=6 | 30.0 | 30.0 | Sesuai |
| Jumlah n=1 | 1 | 1 | Sesuai |
| Jumlah n=5 | 15 | 15 | Sesuai |
| Jumlah n=10 | 55 | 55 | Sesuai |
| Jumlah n=100 | 5050 | 5050 | Sesuai |
| Statistik [70, 80, 65, 90, 75] | Min=65, maks=90, rata-rata=76.0 | Min=65, maks=90, rata-rata=76.0 | Sesuai |
| Scope: x=10, demo(20) | x luar=10, hasil=25 | x luar=10, hasil=25 | Sesuai |
| Praktik luas persegi panjang: p=8, l=5 | 40 | 40.0 | Sesuai |
| Praktik luas segitiga: a=10, t=6 | 30.0 | 30.0 | Sesuai |
| Praktik jumlah n=10 | 55 | 55 | Sesuai |
| Praktik faktorial n=5 | 120 | 120 | Sesuai |
| Praktik faktorial n=0 | 1 | 1 | Sesuai |

Catatan: Jalankan setiap test case untuk memastikan hasil aktual sesuai dengan keluaran program.

## Refleksi

Setelah program dibagi menjadi beberapa fungsi, kode menjadi lebih terstruktur dan mudah dibaca. Setiap fungsi memiliki tugas tertentu sehingga rumus dapat digunakan kembali tanpa menulis ulang kode. Parameter digunakan untuk menerima data, sedangkan return digunakan untuk mengembalikan hasil perhitungan. Pemahaman scope juga membantu membedakan variabel lokal dan variabel global.