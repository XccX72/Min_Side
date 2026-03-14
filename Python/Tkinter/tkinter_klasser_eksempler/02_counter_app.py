import tkinter as tk


class CounterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CounterApp")
        self.geometry("300x160")

        self.count = 0  # instansvariabel

        self.label = tk.Label(self, text="Teller: 0", font=("Segoe UI", 14))
        self.label.pack(pady=10)

        tk.Button(self, text="Klikk", command=self.on_click).pack(pady=5)
        tk.Button(self, text="Nullstill", command=self.on_reset).pack(pady=5)

    def on_click(self):
        self.count += 1
        self.label.config(text=f"Teller: {self.count}")

    def on_reset(self):
        self.count = 0
        self.label.config(text="Teller: 0")


if __name__ == "__main__":
    CounterApp().mainloop()
