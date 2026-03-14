import tkinter as tk


def lag_teller_fabrikk(start_verdi):
    teller = start_verdi

    def oek_og_hent():
        nonlocal teller
        teller += 1
        return teller
    return oek_og_hent

