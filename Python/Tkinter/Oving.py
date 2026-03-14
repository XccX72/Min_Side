marg = 10

    x1_sp = marg
    y1_sp = (RADER - 1) * RUTE_STØRRELSE + marg
    x2_sp = RUTE_STØRRELSE - marg
    y2_sp = RADER * RUTE_STØRRELSE - marg
    spiller1 = Brett_Canvas.create_rectangle(x1_sp, y1_sp, x2_sp, y2_sp, fill = "black", outline= "white")
    return spiller1