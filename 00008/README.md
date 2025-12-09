# 00008

> **"Tutorial OOMMF: Cara Ekstraksi Otomatis File OMF pada Waktu Spesifik"**
> 
> Seri 10 Menit Mikromagnetika
> 
> Samarthya Lykamanuella - nanofisika
> 
> Selasa, 9 Desember 2025
> 
> https://youtu.be/7gwMiPbEzj8

## Deskripsi Singkat

Setiap simulasi OOMMF akan menghasilkan file-file OMF, yang merupakan representasi mikrograf magnetisasi dari material yang disimulasikan pada setiap waktunya. Akan tetapi, mencocokkan nilai numerik DataTable dengan file OMF satu per satu merupakan proses manual yang sangat melelahkan. Dalam video ini, akan dijelaskan langkah-langkah dalam mengekstraksi mikrograf OMF pada waktu spesifik secara otomatis, tanpa perlu mencocokkan DataTabel secara manual.

## Panduan Command Prompt

### 1. Instalasi

Persiapan Python yang perlu dijalankan sebelum mengeksekusi skrip Python dalam folder repositori ini adalah sebagai berikut (jalankan di terminal atau Command Prompt):

```
pip install odt2csv pandas
```

Lalu, di dalam skrip `autoextract_omf_micrograph.py` baris 130-133, spesifikasikan sebagai berikut:
- **`omf_dir`:** lokasi tempat semua file OMF hasil simulasi berada;
- **`odt_file`:** lokasi file ODT (OOMMF DataTable) hasil simulasi, yang biasanya terletak di dalam `omf_dir`;
- **`oommf_path`:** lokasi file `oommf.tcl` yang terinstal di dalam komputer Anda; dan
- **`out_dir`:** lokasi tempat Anda ingin menyimpan file OMF (dan konversi PNG) hasil ekstraksi.

### 2. Ekstraksi File OMF pada Waktu Tertentu

Untuk dapat mengekstraksi mikrograf magnetisasi OMF pada waktu tertentu (misalnya, pada 0.5 ns, 1.0 ns, dan 1.5 ns), spesifikasikan sebagai berikut di dalam skrip `autoextract_omf_micrograph.py`:

```python
if __name__ == '__main__':
    get_all_omf(
        coordinates=[
            (0.5e-9, 0.5e-9),
            (1.0e-9, 1.0e-9),
            (1.5e-9, 1.5e-9),
        ],
        x_col = 'Oxs_TimeDriver::Simulation time',
        y_col = 'Oxs_TimeDriver::Simulation time',
        ...
    )
...
```

### 3. Ekstraksi File OMF Spesifik pada Kasus Simulasi Histeresis

Untuk dapat mengekstraksi mikrograf magnetisasi OMF pada waktu koordinat Bx-mx (medan luar sejajar sumbu-X dan magnetisasi sejajar sumbu-X) tertentu, terutama pada simulasi histeresis, spesifikasikan sebagai berikut di dalam skrip `autoextract_omf_micrograph.py`.

![](https://github.com/nanofisika/kuliah/blob/main/00008/hyst.png?raw=true)

Dimisalkan, kita hendak mengekstraksi mikrograf magnetisasi OMF pada titik A, C, D, dan F seperti diilustrasikan pada gambar di atas (dengan asumsi medan saturasi sebesar ±1000 mT dan medan koersi sebesar ±80 mT).

```python
if __name__ == '__main__':
    get_all_omf(
        coordinates=[
            (1000 ,  1.0),
            (-80  ,  0.0),
            (-1000, -1.0),
            (80   ,  0.0),
        ],
        x_col = 'Oxs_UZeeman::Bx',
        y_col = 'Oxs_TimeDriver::mx',
        ...
    )
...
```
