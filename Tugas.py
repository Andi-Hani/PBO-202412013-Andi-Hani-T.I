from datetime import date, timedelta

class Buku:
    def __init__(self, judul, penulis, kode_buku, stok, lokasi_rak):
        self.judul = judul              # public
        self.penulis = penulis          # public
        self.kode_buku = kode_buku      # public
        self._stok = stok               # protected
        self.__lokasi_rak = lokasi_rak  # private

    # getter lokasi rak
    def get_lokasi_rak(self):
        return self.__lokasi_rak

    # setter lokasi rak
    def set_lokasi_rak(self, lokasi_baru):
        if lokasi_baru == "":
            raise ValueError("Lokasi rak tidak boleh kosong!")
        self.__lokasi_rak = lokasi_baru

    # tambah stok
    def tambah_stok(self, jumlah):
        self._stok += jumlah

    # kurangi stok
    def kurangi_stok(self, jumlah):
        if jumlah > self._stok:
            raise ValueError("Stok tidak mencukupi!")
        self._stok -= jumlah


class Peminjaman:
    def __init__(self, kode_buku, tanggal_pinjam, tanggal_kembali, status):
        self.kode_buku = kode_buku
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
        self.status = status

    def info_peminjaman(self):
        return (f"{self.kode_buku} | Pinjam: {self.tanggal_pinjam} | "
                f"Kembali: {self.tanggal_kembali} | Status: {self.status}")


class Anggota:
    def __init__(self, id_anggota, nama, maks_pinjam=3):
        self.id_anggota = id_anggota        # public
        self.nama = nama                    # public
        self._maks_pinjam = maks_pinjam     # protected
        self.__status_aktif = True          # private
        self.daftar_peminjaman = []         # AGGREGATION

    # getter status
    def get_status(self):
        return self.__status_aktif

    # setter status
    def set_status(self, status):
        self.__status_aktif = status

    # pinjam buku
    def pinjam_buku(self, buku: Buku, hari_pinjam=7):
        if not self.__status_aktif:
            print(f"❌ Anggota {self.nama} tidak aktif!")
            return

        if len(self.daftar_peminjaman) >= self._maks_pinjam:
            print(f"❌ {self.nama} telah mencapai batas maksimum peminjaman!")
            return

        try:
            buku.kurangi_stok(1)
        except ValueError:
            print(f"❌ Stok buku '{buku.judul}' habis!")
            return

        peminjaman = Peminjaman(
            buku.kode_buku,
            tanggal_pinjam=date.today(),
            tanggal_kembali=date.today() + timedelta(days=hari_pinjam),
            status="Dipinjam"
        )
        self.daftar_peminjaman.append(peminjaman)
        print(f"✔ {self.nama} berhasil meminjam '{buku.judul}'")

    # kembalikan buku
    def kembalikan_buku(self, buku: Buku):
        for p in self.daftar_peminjaman:
            if p.kode_buku == buku.kode_buku and p.status == "Dipinjam":
                p.status = "Dikembalikan"
                buku.tambah_stok(1)
                print(f"✔ {self.nama} mengembalikan '{buku.judul}'")
                return
        print(f"❌ Buku tidak ditemukan dalam daftar pinjaman {self.nama}")


class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.buku_list = []   # COMPOSITION

    def tambah_buku(self, buku: Buku):
        self.buku_list.append(buku)

    def daftar_buku(self):
        print("\n=== DAFTAR BUKU ===")
        for b in self.buku_list:
            print(f"{b.kode_buku} | {b.judul} | Stok: {b._stok} | Rak: {b.get_lokasi_rak()}")


if __name__ == "__main__":
    # Perpustakaan
    p = Perpustakaan("Perpustakaan STITEK")

    # 3 buku
    b1 = Buku("Algoritma", "Arif", "B001", 3, "Rak A1")
    b2 = Buku("Basis Data", "Dina", "B002", 2, "Rak B1")
    b3 = Buku("Python Dasar", "Budi", "B003", 5, "Rak C3")

    p.tambah_buku(b1)
    p.tambah_buku(b2)
    p.tambah_buku(b3)

    # 2 anggota
    a1 = Anggota("A01", "Andi")
    a2 = Anggota("A02", "Siti")

    # Anggota 1 pinjam 2 buku
    a1.pinjam_buku(b1)
    a1.pinjam_buku(b2)

    # Anggota 2 pinjam 1 buku
    a2.pinjam_buku(b3)

    # Pengembalian buku
    a1.kembalikan_buku(b1)

    # Tampilkan daftar buku
    p.daftar_buku()

    # Informasi anggota
    print("\n=== INFORMASI ANGGOTA ===")
    for a in [a1, a2]:
        print(f"{a.id_anggota} - {a.nama} | Status: {a.get_status()}")

    # Daftar peminjaman
    print("\n=== DAFTAR PEMINJAMAN ANGGOTA ===")
    for a in [a1, a2]:
        print(f"\nPeminjaman {a.nama}:")
        if not a.daftar_peminjaman:
            print("  Tidak ada peminjaman.")
        else:
            for pjm in a.daftar_peminjaman:
                print(" ", pjm.info_peminjaman())
