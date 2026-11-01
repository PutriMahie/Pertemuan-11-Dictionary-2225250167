# Pertemuan 11 - Dictionary/Map

Nama: Putri Ayu Anisa Mahie  
NIM: 2225250167  
Kelas: 3F

## Tujuan
Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value pada Python.

## Struktur Data
Program menggunakan dictionary untuk menyimpan data mahasiswa dengan NIM sebagai key utama.

- **Key:** NIM mahasiswa, seperti `A001` dan `A002`.
- **Value:** Dictionary yang berisi nama dan nilai mahasiswa.
- **Akses data:** Menggunakan key untuk mengambil informasi mahasiswa.
- **Metode:** Menggunakan `get()` untuk mencari data dengan aman dan `items()` untuk menampilkan pasangan key-value.

## Cara Menjalankan
1. Buka folder proyek di VS Code.
2. Buka terminal.
3. Jalankan perintah berikut:

```bash
python3 praktik/data_mahasiswa.py
```

## Test Case

| Input/Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|
| Mengakses NIM `A001` | Menampilkan data Juhoon | Data Juhoon ditampilkan | Berhasil |
| Mengakses NIM `A002` | Menampilkan data Seonghyeon | Data Seonghyeon ditampilkan | Berhasil |
| Mencari NIM `A003` | Menampilkan pesan data tidak ditemukan | Data tidak ditemukan | Berhasil |
| Mengakses key yang tidak tersedia menggunakan `get()` | Menghasilkan nilai default | Nilai default ditampilkan | Berhasil |

## Refleksi
Kesalahan yang ditemukan adalah mengakses key yang tidak tersedia menggunakan tanda kurung siku, misalnya `data["kelas"]`, sehingga Python menghasilkan `KeyError`. Kesalahan tersebut dapat diperbaiki dengan menggunakan `data.get("kelas", "Belum ada")` agar program menampilkan nilai default ketika key tidak ditemukan.
