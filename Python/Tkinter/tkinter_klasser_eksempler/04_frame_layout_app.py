import tkinter as tk


class TopBar(tk.Frame):
    def __init__(self, master, on_ok):
        super().__init__(master)
        self.entry = tk.Entry(self, width=25)
        self.entry.pack(side="left", padx=5)
        tk.Button(self, text="OK", command=on_ok).pack(side="left", padx=5)


class MainView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = tk.Label(self, text="Resultat vises her", font=("Segoe UI", 12))
        self.label.pack(pady=20)


class FrameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("App med Frames")
        self.geometry("450x220")

        self.top = TopBar(self, on_ok=self.on_ok)
        self.top.pack(pady=10)

        self.view = MainView(self)
        self.view.pack(fill="both", expand=True)

    def on_ok(self):
        tekst = self.top.entry.get().strip()
        self.view.label.config(text=f"Du skrev: {tekst}")


if __name__ == "__main__":
    FrameApp().mainloop()
