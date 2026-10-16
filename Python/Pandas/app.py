import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

class DataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Datafiltrering med Pandas")

        # Label og knapp for å åpne fil
        self.label = tk.Label(root, text="Velg en CSV-fil:")
        self.label.pack(pady=5)

        self.load_button = tk.Button(root, text="Åpne fil", command=self.load_file)
        self.load_button.pack(pady=5)

        # Input for å filtrere på år
        self.filter_label = tk.Label(root, text="Skriv inn år (f.eks. 2020):")
        self.filter_label.pack(pady=5)

        self.year_entry = tk.Entry(root)
        self.year_entry.pack(pady=5)

        self.filter_button = tk.Button(root, text="Filtrer data", command=self.filter_data)
        self.filter_button.pack(pady=5)

        # Tekstfelt for å vise resultater
        self.text_box = tk.Text(root, height=15, width=60)
        self.text_box.pack(pady=10)

        self.df = None

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV-filer", "*.csv")])
        if file_path:
            try:
                self.df = pd.read_csv(file_path, encoding="utf-8", sep="\t")
                messagebox.showinfo("Suksess", "Fil lastet inn!")
            except Exception as e:
                messagebox.showerror("Feil", f"Kunne ikke lese filen: {e}")
            print(self.df.info)

    def filter_data(self):
        if self.df is None:
            messagebox.showwarning("Ingen data", "Last inn en fil først.")
            return

        year = self.year_entry.get()
        if year not in self.df["År"].astype(str).values:
            messagebox.showwarning("Feil", "Året finnes ikke i datasettet.")
            return

        result = self.df[self.df["År"] == int(year)]
        self.text_box.delete("1.0", tk.END)
        self.text_box.insert(tk.END, result.to_string(index=False))

# Kjøre appen
root = tk.Tk()
app = DataApp(root)
root.mainloop()
