# Class Penulis
class Penulis:
    def __init__(self, nama):
        self.nama = nama

    def info_penulis(self):
        return f"Penulis: {self.nama}"


# Class Buku (memiliki objek Penulis → Composition)
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis  # composition

    def info_buku(self):
        return f"Buku '{self.judul}' ditulis oleh {self.penulis.nama}"


# Instansiasi
penulis1 = Penulis("Tere Liye")
buku1 = Buku("Bumi", penulis1)

# Output
print(buku1.info_buku())
