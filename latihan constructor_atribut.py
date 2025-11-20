class ManajerInventori:
    def __init__(self):
        self.inventori = {}

    def tambah_barang(self, nama, jumlah):
        if jumlah > 0:
            if nama in self.inventori:
                self.inventori[nama] += jumlah
            else:
                self.inventori[nama] = jumlah
            return f"Berhasil menambah {jumlah} unit {nama}. Total: {self.inventori[nama]}"
        return "Jumlah harus positif"

    def hapus_barang(self, nama, jumlah):
        if nama not in self.inventori:
            return f"{nama} tidak ditemukan dalam inventori."
        
        if 0 < jumlah <= self.inventori[nama]:
            self.inventori[nama] -= jumlah
            if self.inventori[nama] == 0:
                del self.inventori[nama]
                return f"{nama} habis dan dihapus dari inventori."
            return f"Berhasil mengurangi {jumlah} unit {nama}. Sisa: {self.inventori[nama]}"
        
        return "Jumlah tidak valid atau melebihi stok."

    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori kosong."
        return f"Inventori saat ini: {self.inventori}"


inv = ManajerInventori()

print(inv.tambah_barang("Laptop", 5))
print(inv.tambah_barang("Mouse", 10))
print(inv.tambah_barang("Laptop", 3))

print(inv.lihat_inventori())

print(inv.hapus_barang("Mouse", 4))
print(inv.hapus_barang("Laptop", 8))
print(inv.hapus_barang("Laptop", 0))

print(inv.lihat_inventori())
