# 00006

> **"Tutorial OOMMF: Cara Mengonversi File OMF Menjadi BMP dan PNG"**
> 
> Seri 10 Menit Mikromagnetika
> 
> Samarthya Lykamanuella - nanofisika
> 
> Senin, 24 November 2025
> 
> https://youtu.be/UzuyR7Vjwxg

## Deskripsi Singkat

Video ini menjelaskan bagaimana cara mengubah file OMF hasil generasi simulasi OOMMF ke dalam format BMP atau PNG. Video ini juga menjelaskan cara memuat file konfigurasi mmDisp ke dalam avf2ppm, sehingga tampilan BMP/PNG yang dikonversi akan terlihat sama persis dengan yang ditampilkan di mmDisp.

## Panduan Command Prompt

Untuk dapat mengonversi file OMF di dalam suatu folder `C:\data-simulasi` menjadi file PNG atau BMP, buka Command Prompt lalu jalankan perintah berikut. Jangan lupa untuk mengubah `C:\data-simulasi` menjadi folder di mana file OMF hasil simulasi Anda disimpan, serta `C:\oommf\oommf.tcl` menjadi lokasi tempat Anda menyimpan instalasi program OOMMF.

Untuk mengonversi ke dalam format BMP, ubah `-format PNG` menjadi `-format B24`.

```
cd "C:\data-simulasi"
tclsh "C:\oommf\oommf.tcl" avf2ppm -ipat *.omf -format PNG
```

Untuk memuat file konfigurasi agar sama persis sesuai tampilan pada mmDisp, ekspor konfigurasi dari mmDisp lalu tambahkan parameter `-config` seperti berikut ini. Jangan lupa untuk mengubah `C:\oommf\config.config` menjadi lokasi file konfigurasi yang Anda simpan.

```
tclsh "C:\oommf\oommf.tcl" avf2ppm -ipat *.omf -format PNG -config "C:\oommf\config.config"
```

Contoh file konfigurasi avf2ppm tersedia dalam folder repositori GitHub ini. ([Tautan](https://github.com/nanofisika/kuliah/blob/main/00006/sample.config).)
