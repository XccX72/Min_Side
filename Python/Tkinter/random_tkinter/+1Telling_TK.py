import tkinter as tk

def lag_teller_app():
    app = tk.Tk()
    teller = 0

    app.title("BLA BLA BLA")

    teller_label = tk.Label(app, text = str(teller))
    teller_label.pack()

    def oek_teller():
        nonlocal teller
        teller += 1
        teller_label.configure(text = f"{teller}")

    tk.Button(
        app, 
        text = "Pluss 1", 
        command = oek_teller
    ).pack()
    
    app.mainloop()
    return app

lag_teller_app()

