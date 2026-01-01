# 1. ABSTRACTION
class Pengguna:
    def __init__(self, nama):
        self.nama = nama

    def akses(self):
        pass


class Member(Pengguna):
    def __init__(self, nama, poin):
        super().__init__(nama)
        self.poin = poin

    # implementasi abstract method
    def akses(self):
        return "Hak akses: Member (diskon, reward, event khusus)"

    # 2. SPECIAL METHODS
    def __str__(self):
        return f"Member: {self.nama} – Poin: {self.poin}"

    def __add__(self, other):
        return self.poin + other.poin

    def __len__(self):
        return len(self.nama)


# 4. CUSTOM EXCEPTION
class PoinTidakValidError(Exception):
    """Exception untuk poin tidak valid"""
    pass


# 3. & 5. PROGRAM UTAMA
def input_poin(nama_member):
    poin_input = input(f"Masukkan poin untuk {nama_member}: ").strip()

    if poin_input == "":
        raise ValueError("Input poin tidak boleh kosong!")

    poin = int(poin_input)

    if poin < 0:
        raise PoinTidakValidError("Poin tidak boleh negatif!")

    return poin


if __name__ == "__main__":
    try:
        poin1 = input_poin("Member 1")
        poin2 = input_poin("Member 2")

        m1 = Member("Hani", poin1)
        m2 = Member("Arin", poin2)

        print("\n=== INFO MEMBER ===")
        print(m1)
        print(m2)

        print("\nHak akses:")
        print(m1.akses())

        print("\nJumlah poin m1 + m2:", m1 + m2)
        print("Panjang nama m1:", len(m1))

    except ValueError as ve:
        print("Error input:", ve)

    except PoinTidakValidError as pe:
        print("Error poin:", pe)

    except Exception as e:
        print("Terjadi kesalahan:", e)
