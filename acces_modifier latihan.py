class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        # Public
        self.nim = nim
        self.nama = nama

        # Protected
        self._semester = semester

        # Private
        self.__ipk = ipk

    # Getter & Setter Semester (protected)
    def get_semester(self):
        return self._semester

    def set_semester(self, smt):
        if smt <= 0:
            raise ValueError("Semester tidak boleh 0 atau negatif.")
        self._semester = smt

    # Getter & Setter IPK (private)
    def get_ipk(self):
        return self.__ipk

    def set_ipk(self, nilai):
        if not (0.0 <= nilai <= 4.0):
            raise ValueError("IPK harus antara 0.0 dan 4.0.")
        self.__ipk = round(nilai, 2)


# Membuat 2 objek Mahasiswa

m1 = Mahasiswa("23001", "Budi", 2, 3.1)
m2 = Mahasiswa("23002", "Siti", 4, 3.8)

print("DATA AWAL:")
print(m1.nim, m1.nama, m1.get_semester(), m1.get_ipk())
print(m2.nim, m2.nama, m2.get_semester(), m2.get_ipk())


# Mengganti semester & IPK
m1.set_semester(3)
m1.set_ipk(3.5)

m2.set_semester(5)
m2.set_ipk(3.9)

print("\nSETELAH DIUBAH:")
print(m1.nim, m1.nama, m1.get_semester(), m1.get_ipk())
print(m2.nim, m2.nama, m2.get_semester(), m2.get_ipk())
