import tkinter as tk


class Model:
    """Her kan vi legge logikk/data. Foreløpig bare en enkel beregning."""
    def double(self, x: int) -> int:
        return 2 * x


class MVCApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Enkel MVC")
        self.geometry("420x200")

        self.model = Model()

        tk.Label(self, text="Skriv et tall:").pack(pady=(15, 5))
        self.entry = tk.Entry(self, width=20)
        self.entry.pack()

        tk.Button(self, text="Dobbel", command=self.on_double).pack(pady=10)

        self.label = tk.Label(self, text="Resultat:")
        self.label.pack(pady=10)

    def on_double(self):
        # Minimal feilsjekk (hvis ikke tall, blir det 0)
        try:
            x = int(self.entry.get())
        except ValueError:
            x = 0
        y = self.model.double(x)
        self.label.config(text=f"Resultat: {y}")


if __name__ == "__main__":
    MVCApp().mainloop()
