# CLASS MAHASISWA
class Mahasiswa:
    def __init__(self, nama, nim, ipk):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk

    def info(self):
        return f"{self.nama} (NIM: {self.nim}) - IPK: {self.ipk}"

# LIST OF OBJECT MAHASISWA
daftar_mahasiswa = [
    Mahasiswa("Hani", "IT001", 3.5),
    Mahasiswa("Clara", "IT002", 3.2),
    Mahasiswa("Melda", "IT003", 3.8)
]

print("=== Daftar Mahasiswa ===")
for mhs in daftar_mahasiswa:
    print(mhs.info())

print("\n=== Mahasiswa dengan IPK > 3.5 ===")
for mhs in daftar_mahasiswa:
    if mhs.ipk > 3.5:
        print(mhs.info())


# =========================
# CLASS BUKU
# =========================
class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def info(self):
        return f"Judul: {self.judul}, Penulis: {self.penulis}, Tahun: {self.tahun}"


# =========================
# LIST OF OBJECT BUKU
# =========================
daftar_buku = [
    Buku("Laskar Pelangi", "Andrea Hirata", 2005),
    Buku("Bumi", "Tere Liye", 2014),
    Buku("Negeri 5 Menara", "Ahmad Fuadi", 2009),
    Buku("Hujan", "Tere Liye", 2016),
    Buku("Dilan 1990", "Pidi Baiq", 2014)
]


# =========================
# FUNGSI PENCARIAN BUKU
# =========================
def cari_buku_penulis(daftar, nama_penulis):
    hasil = []
    for buku in daftar:
        if buku.penulis.lower() == nama_penulis.lower():
            hasil.append(buku)
    return hasil


# =========================
# OUTPUT PENCARIAN
# =========================
print("\n=== Pencarian Buku Berdasarkan Penulis ===")
penulis_dicari = input("Masukkan nama penulis: ")

hasil_cari = cari_buku_penulis(daftar_buku, penulis_dicari)

if hasil_cari:
    print("\nBuku ditemukan:")
    for buku in hasil_cari:
        print(buku.info())
else:
    print("Buku dengan penulis tersebut tidak ditemukan.")
