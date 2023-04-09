# UCS dan A* Algorithm to Find Shortest Path
Disusun untuk memenuhi Tugas Kecil 3 IF2211 Strategi Algoritma "Implementasi Algoritma UCS dan A* untuk Menentukan Lintasan 
Terpendek".

## Daftar Isi
* [Deskripsi Singkat Program](#deskripsi-singkat-program)
* [Sistematika File](#sistematika-file)
* [Requirements](#requirements)
* [Cara Kompilasi Program](#cara-kompilasi-program)
* [Cara Menjalankan Program](#cara-menjalankan-program)
* [Dibuat Oleh](#dibuat-oleh)
## Deskripsi Singkat Program
  Algoritma UCS (Uniform cost search) dan A* (atau A star) dapat digunakan untuk menentukan lintasan terpendek dari suatu titik ke titik lain. Lintasan terpendek ini dibentuk dari sebuah peta ruas - ruas jalan yang dibentuk menjadi sebuah graf dengan membentuk simpul - simpul sebagai simpangan atau ujung jalan. Graf yang merepresentasikan peta tersebut kemudian diukur lintasan terpendek dari simpul awal hingga simpul akhir atau tujuan. Hasil lintasan terpendek ini kemudian divisualisaskan dan dalam program ini menggunakan folium pada bahasa Python.
lintasan terpendek dari suatu titik ke titik lain
## Sistematika File
```bash
├─── doc
|   ├─── Tucil3_13521120_13521145.pdf
├─── src
│   ├─── aStar.py
│   ├─── graph.py
│   ├─── main.py
│   ├─── node.py
│   ├─── prioqueue.py
│   ├─── UCS.py
├─── test
│   ├─── test.txt
│   ├─── test2.txt
│   ├─── test3.txt
│   ├─── test4.txt
├─── README.md
```
## Requirements
Python versi 3.9.64 atau lebih baru serta extension matplotlib, networkx, plotly, dan folium.
## Cara Kompilasi Program
1. Pastikan sudah ada Python pada mesin eksekusi sesuai requirement yang ada.
2. Ekstensi matplotlib dapat diunduh dengan cara mengeksekusi perintah berikut pada terminal: <br /> 
`pip install matplotlib` <br />
`pip install networkx` <br />
`pip install plotly` <br />
`pip install folium` <br />
## Cara Menjalankan Program
1. Pada directory file main, jalankan `python -u <directory folder main>/src/main.py`
2. Selain cara tersebut, python dapat dijalankan langsung dengan melalui arsip `main.py` secara langsung.
## Dibuat oleh
<br /> Nama: Febryan Arota Hia
<br /> NIM: 13521120
<br /> Prodi/Jurusan: STEI/Teknik Informatika
<br /> Profile Github: febryanarota
<br />
<br /> Nama: Kenneth Dave Bahana
<br /> NIM: 13521145
<br /> Prodi/Jurusan: STEI/Teknik Informatika
<br /> Profile Github: kenndave
