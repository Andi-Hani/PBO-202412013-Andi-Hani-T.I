import tkinter as tk
from tkinter import ttk, messagebox, filedialog


# =========================
# Class Mahasiswa
# =========================
class Mahasiswa:
    def __init__(self, nim, nama, jurusan, ipk):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk

    def info(self):
        return f"{self.nim} - {self.nama} - {self.jurusan} - IPK: {self.ipk}"

    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru


# =========================
# Aplikasi GUI
# =========================
class SistemManajemenMahasiswa:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Manajemen Mahasiswa")
        self.root.geometry("900x500")

        # Dictionary of objects
        self.data_mahasiswa = {}

        # ================= Frame Input =================
        frame_input = tk.LabelFrame(root, text="Input Data Mahasiswa", padx=10, pady=10)
        frame_input.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(frame_input, text="NIM").grid(row=0, column=0)
        tk.Label(frame_input, text="Nama").grid(row=1, column=0)
        tk.Label(frame_input, text="Jurusan").grid(row=2, column=0)
        tk.Label(frame_input, text="IPK").grid(row=3, column=0)

        self.entry_nim = tk.Entry(frame_input)
        self.entry_nama = tk.Entry(frame_input)
        self.entry_jurusan = tk.Entry(frame_input)
        self.entry_ipk = tk.Entry(frame_input)

        self.entry_nim.grid(row=0, column=1, padx=5)
        self.entry_nama.grid(row=1, column=1, padx=5)
        self.entry_jurusan.grid(row=2, column=1, padx=5)
        self.entry_ipk.grid(row=3, column=1, padx=5)

        # ================= Frame Tombol =================
        frame_button = tk.Frame(root)
        frame_button.pack(pady=5)

        tk.Button(frame_button, text="Tambah", command=self.tambah_mahasiswa).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_button, text="Update IPK", command=self.update_ipk).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_button, text="Hapus", command=self.hapus_mahasiswa).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_button, text="Cari", command=self.cari_mahasiswa).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_button, text="Tampilkan Semua", command=self.tampilkan_semua).pack(side=tk.LEFT, padx=5)

        # ================= Frame Filter =================
        frame_filter = tk.Frame(root)
        frame_filter.pack(pady=5)

        tk.Label(frame_filter, text="Filter Jurusan:").pack(side=tk.LEFT)
        self.entry_filter = tk.Entry(frame_filter)
        self.entry_filter.pack(side=tk.LEFT, padx=5)
        tk.Button(frame_filter, text="Filter", command=self.filter_jurusan).pack(side=tk.LEFT)

        # ================= Treeview =================
        frame_table = tk.Frame(root)
        frame_table.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.tree = ttk.Treeview(
            frame_table,
            columns=("NIM", "Nama", "Jurusan", "IPK"),
            show="headings"
        )
        for col in ("NIM", "Nama", "Jurusan", "IPK"):
            self.tree.heading(col, text=col)

        self.tree.pack(fill=tk.BOTH, expand=True)

        # ================= Frame Fitur Tambahan =================
        frame_extra = tk.Frame(root)
        frame_extra.pack(pady=5)

        tk.Button(frame_extra, text="Rata-rata IPK", command=self.rata_rata_ipk).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_extra, text="IPK Tertinggi", command=self.ipk_tertinggi).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_extra, text="Export Data", command=self.export_data).pack(side=tk.LEFT, padx=5)

    # ================= Fungsi =================
    def validasi_input(self):
        if not self.entry_nim.get() or not self.entry_nama.get() or \
           not self.entry_jurusan.get() or not self.entry_ipk.get():
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return False
        try:
            ipk = float(self.entry_ipk.get())
            if ipk < 0 or ipk > 4:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "IPK harus angka antara 0 - 4")
            return False
        return True

    def tambah_mahasiswa(self):
        if not self.validasi_input():
            return

        nim = self.entry_nim.get()
        if nim in self.data_mahasiswa:
            messagebox.showerror("Error", "NIM sudah terdaftar!")
            return

        mhs = Mahasiswa(
            nim,
            self.entry_nama.get(),
            self.entry_jurusan.get(),
            float(self.entry_ipk.get())
        )
        self.data_mahasiswa[nim] = mhs
        self.tampilkan_semua()

    def hapus_mahasiswa(self):
        selected = self.tree.selection()
        if not selected:
            return
        nim = self.tree.item(selected[0])["values"][0]
        del self.data_mahasiswa[nim]
        self.tampilkan_semua()

    def update_ipk(self):
        selected = self.tree.selection()
        if not selected:
            return
        nim = self.tree.item(selected[0])["values"][0]
        ipk_baru = float(self.entry_ipk.get())
        self.data_mahasiswa[nim].update_ipk(ipk_baru)
        self.tampilkan_semua()

    def cari_mahasiswa(self):
        keyword = self.entry_nim.get() or self.entry_nama.get()
        self.tree.delete(*self.tree.get_children())
        for mhs in self.data_mahasiswa.values():
            if keyword.lower() in mhs.nim.lower() or keyword.lower() in mhs.nama.lower():
                self.tree.insert("", tk.END, values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))

    def filter_jurusan(self):
        jurusan = self.entry_filter.get()
        self.tree.delete(*self.tree.get_children())
        for mhs in self.data_mahasiswa.values():
            if jurusan.lower() in mhs.jurusan.lower():
                self.tree.insert("", tk.END, values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))

    def tampilkan_semua(self):
        self.tree.delete(*self.tree.get_children())
        for mhs in self.data_mahasiswa.values():
            self.tree.insert("", tk.END, values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))

    def rata_rata_ipk(self):
        if not self.data_mahasiswa:
            return
        avg = sum(m.ipk for m in self.data_mahasiswa.values()) / len(self.data_mahasiswa)
        messagebox.showinfo("Rata-rata IPK", f"Rata-rata IPK: {avg:.2f}")

    def ipk_tertinggi(self):
        if not self.data_mahasiswa:
            return
        mhs = max(self.data_mahasiswa.values(), key=lambda x: x.ipk)
        messagebox.showinfo("IPK Tertinggi", mhs.info())

    def export_data(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt")
        if not file:
            return
        with open(file, "w") as f:
            for mhs in self.data_mahasiswa.values():
                f.write(mhs.info() + "\n")
        messagebox.showinfo("Sukses", "Data berhasil diexport!")


# ================= Main =================
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemManajemenMahasiswa(root)
    root.mainloop()
