# Dua class berbeda dengan method nyalakan()

class Laptop:
    def nyalakan(self):
        return "Laptop menyala... Sistem sedang booting."


class Smartphone:
    def nyalakan(self):
        return "Smartphone menyala... Memuat sistem Android."


# Fungsi duck typing
def tes_nyala(obj):
    print(obj.nyalakan())


# Demonstrasi duck typing
if __name__ == "__main__":
    laptop = Laptop()
    hp = Smartphone()

    tes_nyala(laptop)
    tes_nyala(hp)
