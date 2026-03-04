<img width="1915" height="940" alt="Screenshot 2026-03-04 163807" src="https://github.com/user-attachments/assets/39505842-b9fa-4e3e-b0a7-fc5678c3d368" />
<img width="1899" height="939" alt="Screenshot 2026-03-04 163816" src="https://github.com/user-attachments/assets/85a5729d-e735-49ac-9bda-e9417107e97b" />

# Django CRUD & API Integration - Data Produk

Sebuah proyek *fullstack web development* yang dibangun menggunakan kerangka kerja (framework) Django. Aplikasi ini berfungsi untuk mengelola data produk dengan fitur lengkap *Create, Read, Update, Delete* (CRUD), serta dilengkapi dengan kemampuan mengimpor data secara langsung dari antarmuka pemrograman aplikasi (API) eksternal ke dalam *database* lokal, Project ini saya setting ditampilan Website hanya untuk menampilkan barang yang bisa dijual.

# Installasi Modul
* pip install django & pip install requests

# Migrasi Database (Sebelum migrasi silahkan isi nama database kalian di folder CRUD/settings.py dan cari kalimat DATABASES)
* python manage.py makemigrations
* python manage.py migrate

# Fitur Utama

* **Sistem CRUD Lengkap:** Tambah, lihat, ubah, dan hapus data produk dengan mudah.
* **Integrasi API Eksternal:** Mengambil data produk dari sumber luar dan menyimpannya secara otomatis ke dalam *database* bawaan Django (SQLite).
* **Antarmuka Pengguna Modern:** Tampilan *front-end* yang responsif dan rapi menggunakan **Bootstrap 5** dan **Bootstrap Icons**.
* **Format Mata Uang Lokal:** Implementasi filter `intcomma` dari modul `django.contrib.humanize` untuk menampilkan harga dalam format Rupiah (contoh: Rp 12.500).
* **Validasi Aksi:** Konfirmasi pop-up (JavaScript sederhana) sebelum menghapus data untuk mencegah kesalahan pengguna.

# Teknologi yang Digunakan

* **Bahasa Pemrograman:** Python 3.x
* **Back-end Framework:** Django
* **Front-end:** HTML5, CSS3, Bootstrap 5
* **Database:** SQLite (Bawaan Django)

# Panduan Instalasi dan Penggunaan
Ikuti langkah-langkah berikut untuk menjalankan proyek ini di komputer lokal Anda.

### 1. Persiapan Awal
Pastikan Anda sudah menginstal Python di komputer Anda. Disarankan untuk menggunakan *Virtual Environment* agar proyek terisolasi dengan rapi.

### 2. Kloning Repositori
Buka terminal atau *command prompt*, lalu jalankan perintah berikut:
- git clone https://github.com/Rahmadani05/Django_CRUD.git
- cd nama-repositori-anda

# Run Server
* python manage.py runserver
