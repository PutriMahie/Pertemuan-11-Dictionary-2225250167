
def cari(data, nim):
    return data.get(nim, "Data tidak ditemukan")


mahasiswa = {
    "A001": {"nama": "Juhoon", "nilai": 85},
    "A002": {"nama": "Keonho", "nilai": 78}
}

print(cari(mahasiswa, "A002"))
print(cari(mahasiswa, "A003"))
