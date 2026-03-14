import tkinter as tk
from tkinter import filedialog
import pandas as pd

class PS5Data:
    def __init__(self):
        self.df = None

    def load_csv(self, path):
        self.df = pd.read_csv(path)

        # Gjør tallkolonner om til numeric (NaN hvis noe er rart)
        self.df["hours_played"] = pd.to_numeric(self.df["hours_played"], errors="coerce")
        self.df["players"] = pd.to_numeric(self.df["players"], errors="coerce")
        self.df["sessions"] = pd.to_numeric(self.df["sessions"], errors="coerce")

    def top10_by_hours(self):
        return (
            self.df[["rank", "game", "hours_played", "players", "sessions", "avg_session"]]
            .sort_values("hours_played", ascending=False)
            .head(10)
        )

    def summary(self):
        return {
            "antall_spill": len(self.df),
            "sum_hours": self.df["hours_played"].sum(),
            "sum_players": self.df["players"].sum(),
            "sum_sessions": self.df["sessions"].sum(),
        }


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("PS5 Game Explorer (enkel)")

        self.data = PS5Data()

        tk.Button(root, text="Last inn CSV", command=self.load_file).pack(pady=5)
        tk.Button(root, text="Vis topp 10", command=self.show_top10).pack(pady=5)

        self.output = tk.Text(root, width=100, height=25)
        self.output.pack(padx=10, pady=10)

    def load_file(self):
        path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if path:
            self.data.load_csv(path)
            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, f"Lastet fil:\n{path}\n\n")
            self.output.insert(tk.END, "Trykk 'Vis topp 10' for analyse.\n")

    def show_top10(self):
        # Minimal sjekk
        if self.data.df is None:
            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, "Du må laste inn en CSV først.\n")
            return

        s = self.data.summary()
        top10 = self.data.top10_by_hours()

        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, "Nøkkeltall\n")
        self.output.insert(tk.END, f"- Antall spill: {s['antall_spill']}\n")
        self.output.insert(tk.END, f"- Sum hours_played: {s['sum_hours']:.0f}\n")
        self.output.insert(tk.END, f"- Sum players: {s['sum_players']:.0f}\n")
        self.output.insert(tk.END, f"- Sum sessions: {s['sum_sessions']:.0f}\n\n")

        self.output.insert(tk.END, "Top 10 spill (sortert på hours_played)\n\n")
        self.output.insert(tk.END, top10.to_string(index=False))


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
