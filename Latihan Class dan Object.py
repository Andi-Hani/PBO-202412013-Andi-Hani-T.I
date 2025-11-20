class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Nama Dosen: {self.nama} (NIDN: {self.nidn}) mengajar mata kuliah {mata_kuliah}"


dosen1 = Dosen("Prof.Firman", "123456")
dosen2 = Dosen("Rachma.S.Kom", "789012")

print(dosen1.ajar_mata_kuliah("Pemrograman Python"))
print(dosen2.ajar_mata_kuliah("Basis Data"))
