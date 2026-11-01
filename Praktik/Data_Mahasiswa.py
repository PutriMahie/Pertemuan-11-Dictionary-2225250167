
def cari_mahasiswa(data, nim):
    if nim in data:
        return data[nim]
    return "Data mahasiswa tidak ditemukan."


def rata_rata_nilai(data):
    total = 0

    for mahasiswa in data.values():
        total += mahasiswa["nilai"]

    return total / len(data)


data_mahasiswa = {
    "A001": {"nama": "Martin", "kelas": "A", "nilai": 85},
    "A002": {"nama": "James", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Juhoon", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Seonghyeon", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Keonho", "kelas": "A", "nilai": 88}
}

# Operasi pencarian
print("=== PENCARIAN MAHASISWA ===")
print(cari_mahasiswa(data_mahasiswa, "A003"))

# Operasi penambahan
print("\n=== PENAMBAHAN MAHASISWA ===")
data_mahasiswa["A006"] = {
    "nama": "Soobin",
    "kelas": "B",
    "nilai": 80
}
print("Data mahasiswa berhasil ditambahkan.")

# Operasi pembaruan
print("\n=== PEMBARUAN NILAI ===")
data_mahasiswa["A002"]["nilai"] = 82
print("Nilai James berhasil diperbarui.")

# Menampilkan seluruh data
print("\n=== DATA SELURUH MAHASISWA ===")
for nim, mahasiswa in data_mahasiswa.items():
    print(
        nim,
        mahasiswa["nama"],
        mahasiswa["kelas"],
        mahasiswa["nilai"]
    )

# Rekap rata-rata nilai
print("\n=== REKAP NILAI ===")
print("Rata-rata nilai:", rata_rata_nilai(data_mahasiswa))
