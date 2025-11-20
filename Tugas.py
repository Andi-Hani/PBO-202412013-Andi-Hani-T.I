class Mahasiswa:
    # Class Attribute
    universitas = "STITEK Bontang"

    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def perkenalan_diri(self):
        print(f"Halo, nama saya {self.nama}. Saya dari jurusan {self.jurusan} "
              f"dengan NIM {self.nim}. Saya kuliah di {Mahasiswa.universitas}.")

    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru
        print(f"IPK {self.nama} telah diperbarui menjadi {self.ipk}")

    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Tidak Lulus"


mhs1 = Mahasiswa("Hani", "20241213", "Teknik Informatika", 3.6)
mhs2 = Mahasiswa("Melda", "202412007", "Sistem Informasi", 3.1)
mhs3 = Mahasiswa("Clara", "20241201", "Teknik Elektro")

print("=== PERKENALAN DIRI ===")
mhs1.perkenalan_diri()
mhs2.perkenalan_diri()
mhs3.perkenalan_diri()

print("\n=== UPDATE IPK ===")
mhs3.update_ipk(2.8)

print("\n=== PREDIKAT KELULUSAN ===")
print(f"{mhs1.nama} : {mhs1.predikat_kelulusan()}")
print(f"{mhs2.nama} : {mhs2.predikat_kelulusan()}")
print(f"{mhs3.nama} : {mhs3.predikat_kelulusan()}")
