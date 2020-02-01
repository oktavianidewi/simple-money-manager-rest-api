# Simple Money Manager REST API

Module ini dibuat sebagai latihan dari program mentoring di KCMI (Kelompok Coding Mom Indonesia) selama 3 minggu di bulan Februari 2020.

# Daftar Isi

- [Tujuan Belajar](#tujuan-belajar)
- [Setting Up Environment](#setting-up-environment)
  - [Prerequisites](#prerequisites)
  - [Menginstall Alat yang Dibutuhkan](#menginstall-alat-yang-dibutuhkan)
    - [Menginstall `python`](#menginstal-python)
    - [Menginstall `pip`](#menginstal-pip)
    - [Menginstall `git`](#menginstal-git)
    - [Menginstall `flask`](#menginstal-flask)
- [Implementasi](#imlementasi)
  - [Problem Overview](#problem-overview)
  - [Membuat Aplikasi Dasar di Flask](#membuat-aplikasi-dasar-di-flask)
    - [Cloning Project dari Repositori](#cloning-project-dari-repositori)
    - [Membuat API](#membuat-api)
    - [Membuat Koneksi API ke Database](#membuat-koneksi-api-ke-database)
      - [`/POST` Method](#post-method)
      - [`/GET` Method](#get-method)
      - [`/PUT` Method](#put-method)
      - [`/DELETE` Method]((#delete-method))
- [Menggunakan Insomnia untuk Testing](#menggunakan-insomnia-untuk-testing)

# Tujuan Belajar

# Setting Up Environment

## Prerequisites

Untuk mengikuti tutorial ini, diharapkan tools yang dibutuhkan seperti: python, pip sudah terinstall. Jika belum, ikuti proses instalasi berikut ini:

## Menginstal Alat yang Dibutuhkan

### Menginstall `python`

https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation

### Menginstall `pip`

`pip` adalah sebuah alat yang bisa digunakan untuk menginstal dan me-manage `library` atau `package` tambahan yang dibutuhkan di Python. Dalam bahasa sederhana, `pip` adalah package manager-nya `python`, sama seperti `npm` untuk `Javascript` dan `gem` untuk `Ruby`.

Jika kita menginstall python versi 3.4, pip sudah terinstall juga. Sehingga kita tidak perlu menginstall pip lagi secara terpisah. Pada python versi 3 dan 2.7, instalasi python dan pip perlu dilakukan secara terpisah.

Untuk menge-cek apakah pip sudah terinstall, bisa dengan command: 

```shell

pip --version
pip 19.3.1 from /Users/dewioktaviani/.pyenv/versions/3.6.2/lib/python3.6/site-packages/pip (python 3.6)

```

Sumber:
- https://realpython.com/what-is-pip/

## Menginstall `git` 
Git adalah salah satu tool yang sering digunakan dalam proyek pengembangan software. Git adalah salah satu sistem pengontrol versi (Version Control System) yang bertugas mencatat setiap perubahan pada file proyek yang dikerjakan oleh banyak orang maupun sendiri.

Untuk lebih lengkap tentang Git, silakan membacaa artikel disini https://www.petanikode.com/tutorial/git/.

## Menginstall `flask`

Flask adalah sebuah lightweight WSGI (Web Server Gateway Interface). Flask didesain untuk dapat digunakan dengan cepat dan mudah bagi pemula. Cara instalasi Flask adalah dengan menjalankan command berikut ini di terminal:

```shell
pip install -U Flask

```
![Proses instalasi Flask di terminal](/sandbox/instalasi-flask.png)

Sumber:
- https://pypi.org/project/Flask/


# Implementasi

## Problem Overview


### Cloning Project dari Repositori

`git clone`


### Membuat dan Menjalankan Aplikasi di Flask

Jalankan command di bawah ini:

```shell
➜  simple-money-manager-rest-api git:(master) ✗ python api/1_lesson_api.py
```

akan muncul hasil seperti ini di terminal:

```shell
 * Serving Flask app "1_lesson_api" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 319-406-145
```

Anda akan melihat beberapa baris code yang menandakan bahwa Flask sedang running d localhost (di komputer anda) di alamat: http://127.0.0.1:5000/. Klik link tersebut, akan muncul `Hello world` pada browser.

Penjelasan: 

Ketika kita melakukan koneksi dengan flask server di http://127.0.0.1:5000/, Flask melakukan pengecekan dan memetakan antara HTTP Request (URL path `/` ) dengan fungsi Python. Karena `/` termapping dengan fungsi yang bernama `home`, maka Flask mengembalikan result berupa `Hello world` ke browser.

Proses pemetaan/mapping URL dan fungsi ini disebut dengan `routing`.



### Membuat API

Untuk menyelesaikan problem di atas, silakan download/clone project yang sudah disediakan di repository ini. Kami menyediakan contoh code untuk implementasi `/POST` di project ini. Untuk implementasi `/GET`, `/PUT` dan `/DELETE` silakan dikerjakan masing-masing sebagai self-study.


### Membuat Koneksi API ke Database

#### POST Metchod (Example)

buka file

#### GET Method
#### PUT Method
#### DELETE Method

# Menggunakan Insomnia untuk Testing
