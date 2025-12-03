class Kendaraan:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

    def info(self):
        return f"Kendaraan: {self.merk} ({self.tahun})"


class Mobil(Kendaraan):
    def __init__(self, merk, tahun, jumlah_pintu):
        super().__init__(merk, tahun)
        self.jumlah_pintu = jumlah_pintu

    def info(self):
        return f"Mobil: {self.merk}, {self.jumlah_pintu} pintu ({self.tahun})"


# Class Person
class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        return f"Nama: {self.nama}, Umur: {self.umur} tahun"


# Class Mahasiswa mewarisi Person
class Mahasiswa(Person):
    def __init__(self, nama, umur, nim):
        # Gunakan super() untuk memanggil konstruktor Person
        super().__init__(nama, umur)
        self.nim = nim

    # override method info()
    def info(self):
        return f"Mahasiswa: {self.nama}, Umur: {self.umur}, NIM: {self.nim}"


# Instansiasi objek dan panggil info()
if __name__ == "__main__":
    # dari contoh
    k = Kendaraan("Yamaha", 2020)
    m = Mobil("Toyota", 2022, 4)

    print(k.info())
    print(m.info())

    # tugas Person & Mahasiswa
    p1 = Person("Budi", 30)
    mhs1 = Mahasiswa("Siti", 20, "23001")

    print(p1.info())
    print(mhs1.info())
