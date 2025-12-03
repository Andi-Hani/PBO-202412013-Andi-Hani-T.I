import math

# Class Bentuk
class Bentuk:
    def luas(self):
        return 0

# Class Persegi (override method luas)
class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

# Class Lingkaran (override method luas)
class Lingkaran(Bentuk):
    def __init__(self, radius):
        self.radius = radius

    def luas(self):
        return math.pi * self.radius * self.radius


# Demonstrasi pemanggilan method luas()
if __name__ == "__main__":
    bentuk = Bentuk()
    persegi = Persegi(5)
    lingkaran = Lingkaran(7)

    print("Luas Bentuk:", bentuk.luas())        # 0
    print("Luas Persegi:", persegi.luas())      # 25
    print("Luas Lingkaran:", lingkaran.luas())  # 153.938...
