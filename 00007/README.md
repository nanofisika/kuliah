# 00007

> **"Tutorial OOMMF: Cara Mengonversi File ODT Menjadi CSV"**
> 
> Seri 10 Menit Mikromagnetika
> 
> Samarthya Lykamanuella - nanofisika
> 
> Selasa, 2 Desember 2025
> 
> https://youtu.be/XTzUU0WE3Sg

## Deskripsi Singkat

File ODT (OOMMF Data Table) merupakan file luaran yang dihasilkan dari simulasi OOMMF. File ini berisi data nilai-nilai yang dihasilkan dari simulasi OOMMF, seperti energi, magnetisasi, dan amplitudo medan luar. File ODT ini tidak dapat dibaca secara tepat pada program-program manipulasi data konvensional seperti Microsoft Excel, sehingga harus dikonversi ke dalam format yang universal. Simak video berikut untuk mempelajari cara mengonversi file OOMMF Data Table menjadi CSV (comma-separated values).

## Panduan Command Prompt

### 1. Instalasi

Setelah menginstal Python di dalam komputer, Anda dapat menginstal program `odt2csv` dengan membuka Command Prompt dan mengetikkan perintah berikut:

```
pip install odt2csv
```

atau, gunakan perintah berikut jika perintah di atas tidak berfungsi:

```
python -m pip install odt2csv
```

Setelah itu, ketikkan perintah berikut untuk memastikan `odt2csv` sudah terintal ke dalam komputer Anda:

```
python -m odt2csv --help
```

Pastikan luaran dari perintah tersebut menghasilkan teks seperti pada gambar berikut:

![](https://github.com/nanofisika/kuliah/blob/main/00007/odt2csv-help.png?raw=true)

### 2. Konversi ODT Menjadi CSV

Buka Command Prompt, lalu `cd` (_change directory_) ke dalam folder di mana file ODT hasil simulasi OOMMF terletak.

```
cd C:\lokasi\simulasi\oommf
```

Kemudian, ketikkan perintah berikut (ganti `namafile.odt` menjadi nama file yang sesungguhnya ada di komputer Anda):

```
python -m odt2csv namafile.odt
```

Jika muncul galat `odt2csv.exceptions.MultipleTableStartsError`, tambahkan parameter _parser mode_ dan atur nilainya menjadi "new" sebagai berikut:

```
python -m odt2csv namafile.odt -p new
```

Untuk dapat memasukkan satuan/unit fisis dari masing-masing kolom di ODT ke dalam CSV, tambahkan parameter _keep unit_ dan atur nilainya menjadi "1" sebagai berikut:

```
python -m odt2csv namafile.odt -k 1
```
