# =========================
# CLASS PRODUK
# =========================
class Produk:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga

    def info(self):
        return f"{self.nama} - Rp {self.harga:,}"


# =========================
# DICTIONARY OF OBJECT PRODUK
# =========================
katalog_produk = {
    "P001": Produk("P001", "Laptop", 8000000),
    "P002": Produk("P002", "Mouse", 150000),
    "P003": Produk("P003", "Keyboard", 300000)
}

print("=== Katalog Produk ===")
for kode, produk in katalog_produk.items():
    print(f"{kode}: {produk.info()}")

# Mencari produk
cari_kode = "P002"
if cari_kode in katalog_produk:
    print(f"\nProduk ditemukan: {katalog_produk[cari_kode].info()}")


# =================================================
# CLASS PELANGGAN
# =================================================
class Pelanggan:
    def __init__(self, id_pelanggan, nama, email):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.email = email

    def info(self):
        return f"ID: {self.id_pelanggan}, Nama: {self.nama}, Email: {self.email}"


# =================================================
# DICTIONARY OF OBJECT PELANGGAN
# =================================================
data_pelanggan = {
    "C001": Pelanggan("C001", "Hani", "hani@email.com"),
    "C002": Pelanggan("C002", "clara", "clara@email.com"),
    "C003": Pelanggan("C003", "melda", "melda@email.com")
}


# =================================================
# FUNGSI TAMBAH, HAPUS, CARI PELANGGAN
# =================================================
def tambah_pelanggan(data, pelanggan):
    data[pelanggan.id_pelanggan] = pelanggan
    print("Pelanggan berhasil ditambahkan.")


def hapus_pelanggan(data, id_pelanggan):
    if id_pelanggan in data:
        del data[id_pelanggan]
        print("Pelanggan berhasil dihapus.")
    else:
        print("Pelanggan tidak ditemukan.")


def cari_pelanggan(data, id_pelanggan):
    if id_pelanggan in data:
        return data[id_pelanggan]
    else:
        return None


# =================================================
# MENAMPILKAN DAFTAR PELANGGAN
# =================================================
print("\n=== Daftar Pelanggan ===")
for pelanggan in data_pelanggan.values():
    print(pelanggan.info())


# =================================================
# UJI FUNGSI
# =================================================
print("\n=== Uji Tambah Pelanggan ===")
p_baru = Pelanggan("C004", "Al", "al@email.com")
tambah_pelanggan(data_pelanggan, p_baru)

print("\n=== Daftar Pelanggan Setelah Ditambah ===")
for pelanggan in data_pelanggan.values():
    print(pelanggan.info())

print("\n=== Uji Cari Pelanggan ===")
hasil = cari_pelanggan(data_pelanggan, "C002")
if hasil:
    print("Pelanggan ditemukan:", hasil.info())
else:
    print("Pelanggan tidak ditemukan.")

print("\n=== Uji Hapus Pelanggan ===")
hapus_pelanggan(data_pelanggan, "C001")

print("\n=== Daftar Pelanggan Setelah Dihapus ===")
for pelanggan in data_pelanggan.values():
    print(pelanggan.info())
