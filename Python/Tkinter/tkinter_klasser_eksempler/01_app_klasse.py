import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("App som klasse")
        self.geometry("350x120")

        tk.Label(self, text="Hei! Dette er en App-klasse.").pack(pady=20)


if __name__ == "__main__":
    App().mainloop()
