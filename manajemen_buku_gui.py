import tkinter as tk
from tkinter import messagebox, ttk, simpledialog


class Tugas:
    def __init__(self, judul, status="Belum Selesai"):
        self.judul = judul
        self.status = status


class AplikasiManajemenTugas:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Tugas (To-Do List)")
        self.root.geometry("600x400")

        # List of objects
        self.daftar_tugas = []

        # ===== Frame Input =====
        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack()

        tk.Label(frame_input, text="Nama Tugas:").grid(row=0, column=0, sticky=tk.W)
        self.entry_tugas = tk.Entry(frame_input, width=30)
        self.entry_tugas.grid(row=0, column=1, padx=5, pady=5)

        # ===== Frame Tombol =====
        frame_tombol = tk.Frame(root, padx=10, pady=10)
        frame_tombol.pack()

        tk.Button(frame_tombol, text="Tambah", command=self.tambah_tugas)\
            .pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Edit", command=self.edit_tugas)\
            .pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Hapus", command=self.hapus_tugas)\
            .pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Tandai Selesai", command=self.tandai_selesai)\
            .pack(side=tk.LEFT, padx=5)

        # ===== Frame Treeview =====
        frame_tabel = tk.Frame(root, padx=10, pady=10)
        frame_tabel.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(
            frame_tabel,
            columns=("Tugas", "Status"),
            show="headings"
        )
        self.tree.heading("Tugas", text="Tugas")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(
            frame_tabel,
            orient=tk.VERTICAL,
            command=self.tree.yview
        )
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # ===== Fungsi =====
    def tambah_tugas(self):
        judul = self.entry_tugas.get()

        if judul.strip() == "":
            messagebox.showwarning("Peringatan", "Nama tugas tidak boleh kosong!")
            return

        tugas = Tugas(judul)
        self.daftar_tugas.append(tugas)
        self.tree.insert("", tk.END, values=(tugas.judul, tugas.status))
        self.entry_tugas.delete(0, tk.END)

    def hapus_tugas(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan dihapus!")
            return

        item = self.tree.item(selected[0])
        judul = item["values"][0]

        self.daftar_tugas = [t for t in self.daftar_tugas if t.judul != judul]
        self.tree.delete(selected[0])

    def edit_tugas(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan diedit!")
            return

        item = self.tree.item(selected[0])
        judul_lama = item["values"][0]

        judul_baru = simpledialog.askstring(
            "Edit Tugas", "Masukkan nama tugas baru:"
        )

        if judul_baru:
            for tugas in self.daftar_tugas:
                if tugas.judul == judul_lama:
                    tugas.judul = judul_baru
                    break
            self.tree.item(selected[0], values=(judul_baru, item["values"][1]))

    def tandai_selesai(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih tugas terlebih dahulu!")
            return

        item = self.tree.item(selected[0])
        judul = item["values"][0]

        for tugas in self.daftar_tugas:
            if tugas.judul == judul:
                tugas.status = "Selesai"
                break

        self.tree.item(selected[0], values=(judul, "Selesai"))


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiManajemenTugas(root)
    root.mainloop()
