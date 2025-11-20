class Kendaraan:
    # Class attribute
    bahan_bakar = "Pertalite"

    # Constructor (instance attributes)
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    # Method untuk menampilkan info
    def info(self):
        return f"Kendaraan {self.merk}, warna {self.warna}, tahun {self.tahun}"
    

# Instansiasi dua objek
mobil = Kendaraan("Toyota Avanza", "Hitam", 2020)
motor = Kendaraan("Honda Beat", "Merah", 2022)

# Menampilkan instance attributes
print(mobil.info())
print(motor.info())

# Mengakses class attribute
print(f"Bahan bakar (akses via class): {Kendaraan.bahan_bakar}")
print(f"Bahan bakar (akses via object mobil): {mobil.bahan_bakar}")
print(f"Bahan bakar (akses via object motor): {motor.bahan_bakar}")
