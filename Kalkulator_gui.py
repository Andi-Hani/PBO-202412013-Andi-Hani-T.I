import tkinter as tk
from tkinter import messagebox


class KonversiSuhu:
    def __init__(self, root):
        self.root = root
        self.root.title("Konversi Suhu")
        self.root.geometry("300x220")

        # Label Judul
        self.label_judul = tk.Label(
            root,
            text="Konversi Celsius ke Fahrenheit",
            font=("Arial", 12)
        )
        self.label_judul.pack(pady=10)

        # Entry Celsius
        self.label_celsius = tk.Label(root, text="Masukkan Suhu (°C):")
        self.label_celsius.pack()

        self.entry_celsius = tk.Entry(root, width=25)
        self.entry_celsius.pack(pady=5)

        # Button Konversi
        self.button_konversi = tk.Button(
            root,
            text="Konversi",
            command=self.konversi_suhu
        )
        self.button_konversi.pack(pady=5)

        # Button Reset
        self.button_reset = tk.Button(
            root,
            text="Reset",
            command=self.reset
        )
        self.button_reset.pack(pady=5)

        # Label Hasil
        self.label_hasil = tk.Label(
            root,
            text="Hasil: -",
            font=("Arial", 11)
        )
        self.label_hasil.pack(pady=10)

    def konversi_suhu(self):
        nilai = self.entry_celsius.get()

        # Validasi input kosong
        if nilai.strip() == "":
            messagebox.showwarning("Peringatan", "Input tidak boleh kosong!")
            return

        try:
            celsius = float(nilai)
            fahrenheit = (celsius * 9 / 5) + 32
            self.label_hasil.config(
                text=f"Hasil: {fahrenheit:.2f} °F"
            )
        except ValueError:
            messagebox.showerror(
                "Error",
                "Input harus berupa angka!"
            )

    def reset(self):
        self.entry_celsius.delete(0, tk.END)
        self.label_hasil.config(text="Hasil: -")


if __name__ == "__main__":
    root = tk.Tk()
    app = KonversiSuhu(root)
    root.mainloop()
