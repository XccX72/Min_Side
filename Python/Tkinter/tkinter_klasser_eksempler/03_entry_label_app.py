import tkinter as tk


class HelloApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HelloApp")
        self.geometry("300x180")

        self.label = tk.Label(self, text = "Skriv navnet ditt", font=("Segoe UI", 12))
        self.label.pack(pady = 10)

        self.entry = tk.Entry(self, width=30)
        self.entry.pack(pady=10)

        self.label = tk.Label(self, text="Trykk på knappen", font=("Segoe UI", 12))
        self.label.pack(pady=10)

        tk.Button(self, text="Oppdater hilsen", command=self.on_hello).pack(pady=5)

    def on_hello(self):
        navn = self.entry.get().strip()
        self.label.config(text=f"Hei, {navn}!")


if __name__ == "__main__":
    HelloApp().mainloop()
