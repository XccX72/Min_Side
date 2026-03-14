import tkinter as tk

root = tk.Tk()
root.title("Spill-database med Grid og Frames")
root.geometry("600x400")

# Konfigurer kolonne-vekting slik at høyre side utvider seg mer enn venstre
root.columnconfigure(1, weight=3)
root.rowconfigure(1, weight=1)

# --- 1. TOPP-RAMME (Overskrift) ---
topp_ramme = tk.Frame(root, bg="#2c3e50", height=50)
topp_ramme.grid(row=0, column=0, columnspan=2, sticky="ew")

overskrift = tk.Label(topp_ramme, text="MIN SPILL-DATABASE", fg="white", bg="#2c3e50", font=("Arial", 16, "bold"))
overskrift.pack(pady=10)


# --- 2. VENSTRE RAMME (Inntasting) ---
venstre_ramme = tk.Frame(root, bg="#f20e0e", padx=10, pady=10, bd=1, relief="solid")
venstre_ramme.grid(row=1, column=0, sticky="nsew")

lbl_rank = tk.Label(venstre_ramme, text="Søk på Rank:", bg="#ecf0f1")
lbl_rank.pack(anchor="w")

ent_rank = tk.Entry(venstre_ramme)
ent_rank.pack(fill="x", pady=5)

btn_søk = tk.Button(venstre_ramme, text="Vis Toppliste", bg="#0099ff", fg="white")
btn_søk.pack(fill="x", pady=10)


# --- 3. HØYRE RAMME (Resultater) ---
høyre_ramme = tk.Frame(root, bg="white", padx=10, pady=10)
høyre_ramme.grid(row=1, column=1, sticky="nsew")

lbl_resultat_tittel = tk.Label(høyre_ramme, text="Resultater:", font=("Arial", 12, "underline"), bg="white")
lbl_resultat_tittel.pack(anchor="w")

# Her ville din spilliste-label ligget
resultat_label = tk.Label(høyre_ramme, text="Ingen søk utført ennå...", bg="white", justify="left")
resultat_label.pack(pady=20)

root.mainloop()