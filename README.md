# Pertemuan 03 Seleksi Python

**Nama:** Fridha Septiana
**NIM:** 2225250068
**Kelas:** 3E

## Tujuan

Pertemuan ini bertujuan untuk memahami dan menerapkan struktur seleksi dalam Python, yaitu `if`, `if-else`, kondisi majemuk menggunakan operator `and` dan `or`, serta **nested if**. Program dibuat untuk melatih kemampuan dalam membuat keputusan berdasarkan kondisi tertentu.

## Daftar Program

| No. | Nama Berkas                             | Fungsi                                                                                       |
| --- | --------------------------------------- | -------------------------------------------------------------------------------------------- |
| 1   | `latihan/01_genap_ganjil.py`            | Menentukan apakah suatu bilangan termasuk genap atau ganjil.                                 |
| 2   | `latihan/02_bandingkan_dua_bilangan.py` | Membandingkan dua bilangan dan menentukan bilangan yang lebih besar, lebih kecil, atau sama. |
| 3   | `latihan/03_kelulusan_bersyarat.py`     | Menentukan kelulusan berdasarkan nilai akhir dan persentase kehadiran.                       |
| 4   | `latihan/04_jenis_segitiga.py`          | Menentukan jenis segitiga berdasarkan panjang ketiga sisinya.                                |
| 5   | `tugas/analisis_persamaan_kuadrat.py`   | Menganalisis jenis akar persamaan kuadrat berdasarkan nilai diskriminan.                     |

## Cara Menjalankan

Program dapat dijalankan melalui terminal menggunakan Python.

Untuk menjalankan tugas utama:

```bash
python3 tugas/analisis_persamaan_kuadrat.py
```

Pada Windows, jika `python3` tidak dapat digunakan, dapat menggunakan:

```bash
python tugas/analisis_persamaan_kuadrat.py
```

## Algoritma Tugas

Program menerima tiga koefisien persamaan kuadrat, yaitu `a`, `b`, dan `c`.

Langkah-langkah pengambilan keputusan:

1. Masukkan nilai koefisien `a`, `b`, dan `c`.
2. Periksa apakah nilai `a` sama dengan `0`.
3. Jika `a` sama dengan `0`, tampilkan bahwa input bukan persamaan kuadrat.
4. Jika `a` tidak sama dengan `0`, hitung nilai diskriminan dengan rumus `D = b² - 4ac`.
5. Jika `D` lebih besar dari `0`, hitung dua akar real yang berbeda.
6. Jika `D` tidak lebih besar dari `0`, periksa apakah `D` sama dengan `0`.
7. Jika `D` sama dengan `0`, hitung satu akar real kembar.
8. Jika `D` kurang dari `0`, tampilkan bahwa persamaan tidak memiliki akar real.
9. Tampilkan hasil perhitungan dengan dua angka di belakang koma.

## Hasil Pengujian

| No. | Input (a, b, c) | Keluaran yang Diharapkan               | Keluaran Aktual                                  | Status   |
| --- | --------------- | -------------------------------------- | ------------------------------------------------ | -------- |
| 1   | (1, -5, 6)      | D = 1.00, dua akar real: 3.00 dan 2.00 | D = 1.00, akar pertama = 3.00, akar kedua = 2.00 | Berhasil |
| 2   | (1, 2, 1)       | D = 0.00, akar kembar: -1.00           | D = 0.00, akar = -1.00                           | Berhasil |
| 3   | (1, 0, 1)       | D = -4.00, tidak ada akar real         | D = -4.00, tidak ada akar real                   | Berhasil |
| 4   | (0, 2, 3)       | Bukan persamaan kuadrat                | Bukan persamaan kuadrat                          | Berhasil |

## Refleksi

Saat membuat program, salah satu hal yang perlu diperhatikan adalah urutan pengecekan kondisi. Kesalahan logika yang dapat terjadi adalah langsung menghitung akar sebelum memeriksa apakah `a` sama dengan `0`. Jika `a` bernilai `0`, persamaan tersebut bukan persamaan kuadrat dan perhitungan akar dengan penyebut `2 * a` tidak dapat dilakukan.

Kesalahan tersebut diperbaiki dengan memeriksa `a == 0` terlebih dahulu. Jika `a` sama dengan `0`, program langsung menampilkan pesan bahwa input bukan persamaan kuadrat. Jika `a` tidak sama dengan `0`, barulah program menghitung diskriminan dan menentukan jenis akar menggunakan nested if.
