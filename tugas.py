class Karyawan:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok

    def info_gaji(self):
        return f"{self.nama} memiliki gaji pokok: {self.gaji_pokok}"


class Manager(Karyawan):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama, gaji_pokok)
        self.tunjangan = tunjangan

    # Override
    def info_gaji(self):
        total = self.gaji_pokok + self.tunjangan
        return f"Manager {self.nama} memiliki total gaji: {total}"


class Programmer(Karyawan):
    def __init__(self, nama, gaji_pokok, bonus):
        super().__init__(nama, gaji_pokok)
        self.bonus = bonus

    # Override
    def info_gaji(self):
        total = self.gaji_pokok + self.bonus
        return f"Programmer {self.nama} memiliki total gaji: {total}"


class Departemen:
    def __init__(self, nama_dept):
        self.nama_dept = nama_dept
        self.daftar_karyawan = []  # list of objects

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_karyawan(self):
        print(f"\nDaftar Karyawan di Departemen {self.nama_dept}:")
        for k in self.daftar_karyawan:
            print(k.info_gaji())


# Membuat 2 objek Manager
m1 = Manager("Budi", 5000000, 2000000)
m2 = Manager("Ani", 5500000, 2500000)

# Membuat 2 objek Programmer
p1 = Programmer("Rudi", 4000000, 1500000)
p2 = Programmer("Dina", 4500000, 1800000)

# Membuat Departemen
dept_it = Departemen("IT")

# Menambahkan ke departemen
dept_it.tambah_karyawan(m1)
dept_it.tambah_karyawan(m2)
dept_it.tambah_karyawan(p1)
dept_it.tambah_karyawan(p2)

# Tampilkan info gaji semua karyawan
dept_it.tampilkan_karyawan()
