class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def __str__(self):
        return f"Nama: {self.nama}, Nilai: {self.nilai}"

    def __gt__(self, other):
        return self.nilai > other.nilai

    def __add__(self, other):
        return self.nilai + other.nilai

    def __mul__(self, faktor):
        return self.nilai * faktor

    def __len__(self):
        return len(self.nama)

    def __eq__(self, other):
        return self.nilai == other.nilai


m1 = Mahasiswa("Hani", 80)
m2 = Mahasiswa("Clara", 90)
m3 = Mahasiswa("Melda", 80)

print(m1)
print(m2)
print(m3)

# Panjang nama
print("Panjang nama m1:", len(m1))

# Perbandingan kesetaraan nilai
print("m1 == m2 :", m1 == m2)
print("m1 == m3 :", m1 == m3)

# Operasi matematika
print("Total nilai m1 + m2:", m1 + m2)
print("Nilai m2 x 2:", m2 * 2)

# Pengurutan tanpa __lt__
list_mahasiswa = [m1, m2, m3]
list_urut = sorted(list_mahasiswa, key=lambda x: x.nilai)

print("\nDaftar mahasiswa setelah diurutkan berdasarkan nilai:")
for m in list_urut:
    print(m)
