import tkinter as tk


class ThermoWaterGlassApp(tk.Tk):
    """
    Enkel termofysikk-simulering: vann i et glass som nærmer seg romtemperatur.
    Modell: dT/dt = -k (T - T_rom)  (Newtons avkjølingslov)

    Viser:
      - Glass med "vann" som skifter farge etter temperatur
      - Termometer (kolonne)
      - Live graf T(t)
    """

    def __init__(self):
        super().__init__()
        self.title("Termofysikk: Vann i glass som utjevner temperatur (Tkinter)")

        # --- Layout ---
        self.sim_W, self.sim_H = 560, 380
        self.graph_W, self.graph_H = 560, 220

        self.sim = tk.Canvas(self, width=self.sim_W, height=self.sim_H, bg="white")
        self.sim.grid(row=0, column=0, padx=8, pady=8)

        self.graph = tk.Canvas(self, width=self.graph_W, height=self.graph_H, bg="white")
        self.graph.grid(row=1, column=0, padx=8, pady=(0, 8))

        panel = tk.Frame(self)
        panel.grid(row=0, column=1, rowspan=2, sticky="n", padx=10, pady=10)

        # --- Kontroller ---
        self.T_room_var = tk.DoubleVar(value=22.0)   # °C
        self.T_init_var = tk.DoubleVar(value=60.0)   # °C
        self.k_var = tk.DoubleVar(value=0.08)        # 1/min (omtrent)
        self.dt_real_var = tk.DoubleVar(value=0.10)  # sek per frame (UI)
        self.speed_var = tk.DoubleVar(value=10.0)    # "minutter per sekund" i simulering

        tk.Label(panel, text="Romtemperatur (°C)").pack(anchor="w")
        tk.Scale(panel, from_=-10, to=35, resolution=0.5, orient="horizontal",
                 variable=self.T_room_var, length=260).pack()

        tk.Label(panel, text="Starttemperatur vann (°C)").pack(anchor="w", pady=(8, 0))
        tk.Scale(panel, from_=-5, to=90, resolution=0.5, orient="horizontal",
                 variable=self.T_init_var, length=260).pack()

        tk.Label(panel, text="Varmeutveksling k (1/min)").pack(anchor="w", pady=(8, 0))
        tk.Scale(panel, from_=0.00, to=0.40, resolution=0.01, orient="horizontal",
                 variable=self.k_var, length=260).pack()

        tk.Label(panel, text="Sim hastighet (min per sekund)").pack(anchor="w", pady=(8, 0))
        tk.Scale(panel, from_=1, to=60, resolution=1, orient="horizontal",
                 variable=self.speed_var, length=260).pack()

        btns = tk.Frame(panel)
        btns.pack(anchor="w", pady=(10, 0))
        tk.Button(btns, text="Start", width=10, command=self.start).grid(row=0, column=0, padx=(0, 6))
        tk.Button(btns, text="Pause", width=10, command=self.pause).grid(row=0, column=1, padx=(0, 6))
        tk.Button(btns, text="Reset", width=10, command=self.reset).grid(row=0, column=2)

        self.info = tk.Label(panel, text="", justify="left")
        self.info.pack(anchor="w", pady=(12, 0))

        tk.Label(panel, text="Modell: dT/dt = -k (T - T_rom)", fg="gray30").pack(anchor="w", pady=(10, 0))

        # --- Sim state ---
        self.running = False
        self.t_min = 0.0         # simulert tid (min)
        self.T = self.T_init_var.get()

        # --- Graph state ---
        self.max_points = 500
        self.T_hist = []   # temperaturhistorikk
        self.t_hist = []   # tid (min)
        self.g_pad = 30

        self.after_id = None
        self.reset()
        self.loop()

    # -------------------------
    # Control actions
    # -------------------------
    def start(self):
        self.running = True

    def pause(self):
        self.running = False

    def reset(self):
        self.running = False
        self.t_min = 0.0
        self.T = float(self.T_init_var.get())

        self.T_hist = [self.T]
        self.t_hist = [self.t_min]

        self.draw_sim()
        self.draw_graph()
        self.update_info()

    # -------------------------
    # Simulation loop
    # -------------------------
    def loop(self):
        # UI timestep
        dt_real = float(self.dt_real_var.get())  # seconds, not shown in UI currently
        if self.running:
            # Konverter "hastighet" til simulert tidssteg:
            # speed = (min simulert) / (sek ekte)
            speed = float(self.speed_var.get())
            dt_min = speed * 0.016  # ca 60 fps -> 0.016 s per frame

            self.step_physics(dt_min)
            self.append_history()
            self.draw_sim()
            self.draw_graph()
            self.update_info()

        # kjør ~60fps
        self.after(16, self.loop)

    def step_physics(self, dt_min: float):
        # Newtons avkjølingslov: dT/dt = -k (T - T_room)
        T_room = float(self.T_room_var.get())
        k = float(self.k_var.get())

        dTdt = -k * (self.T - T_room)
        self.T += dTdt * dt_min
        self.t_min += dt_min

    def append_history(self):
        self.T_hist.append(self.T)
        self.t_hist.append(self.t_min)
        if len(self.T_hist) > self.max_points:
            self.T_hist.pop(0)
            self.t_hist.pop(0)

    # -------------------------
    # Drawing helpers
    # -------------------------
    def temp_to_color(self, T: float, Tmin=-5.0, Tmax=90.0) -> str:
        """
        Enkel fargeinterpolasjon:
        kald -> blå, varm -> rød, middels -> lilla/rosa.
        Returnerer en hex-farge.
        """
        # clamp
        if T < Tmin:
            T = Tmin
        if T > Tmax:
            T = Tmax
        u = (T - Tmin) / (Tmax - Tmin)  # 0..1

        # RGB: blå(0,0,255) -> rød(255,0,0)
        r = int(255 * u)
        g = int(40 * (1 - abs(u - 0.5) * 2))  # litt grønn midt, for "varmefølelse"
        b = int(255 * (1 - u))
        return f"#{r:02x}{g:02x}{b:02x}"

    def draw_sim(self):
        c = self.sim
        c.delete("all")

        # "Rom"
        c.create_rectangle(10, 10, self.sim_W - 10, self.sim_H - 10, outline="gray70")
        c.create_text(18, 18, anchor="nw", text="Rom", fill="gray40")

        # Bord
        table_y = 285
        c.create_rectangle(40, table_y, self.sim_W - 40, table_y + 50, fill="gray90", outline="gray70")

        # Glass (enkelt)
        gx0, gy0 = 170, 90
        gx1, gy1 = 320, table_y
        c.create_rectangle(gx0, gy0, gx1, gy1, outline="gray30", width=2)

        # Vannnivå (fast nivå for enkelhet)
        water_level = 0.72  # 72% fylt
        wx0 = gx0 + 6
        wx1 = gx1 - 6
        wy1 = gy1 - 6
        wy0 = wy1 - (gy1 - gy0 - 12) * water_level

        water_color = self.temp_to_color(self.T)
        c.create_rectangle(wx0, wy0, wx1, wy1, fill=water_color, outline="")

        # "Damp" eller "kulde" hint (kun visuelt)
        T_room = float(self.T_room_var.get())
        if self.T > T_room + 2:
            c.create_text((gx0 + gx1) / 2, gy0 - 10, text="(varmt vann)", fill="gray30")
        elif self.T < T_room - 2:
            c.create_text((gx0 + gx1) / 2, gy0 - 10, text="(kaldt vann)", fill="gray30")
        else:
            c.create_text((gx0 + gx1) / 2, gy0 - 10, text="(nær romtemp)", fill="gray30")

        # Termometer på siden
        tx0, ty0 = 420, 90
        tx1, ty1 = 455, table_y
        c.create_rectangle(tx0, ty0, tx1, ty1, outline="gray30", width=2)
        c.create_oval(tx0 - 10, ty1 - 20, tx1 + 10, ty1 + 10, fill="gray85", outline="gray40")

        # Termometerkolonne: map T til høyde
        Tmin, Tmax = -10.0, 90.0
        u = (self.T - Tmin) / (Tmax - Tmin)
        if u < 0:
            u = 0
        if u > 1:
            u = 1
        col_h = (ty1 - ty0 - 10) * u
        c.create_rectangle(tx0 + 10, ty1 - 5 - col_h, tx1 - 10, ty1 - 5, fill=water_color, outline="")

        # Tekst
        c.create_text(50, 60, anchor="w",
                      text=f"Romtemperatur: {T_room:.1f} °C", fill="gray20")
        c.create_text(50, 85, anchor="w",
                      text=f"Vanntemperatur: {self.T:.1f} °C", fill="gray20")
        c.create_text(50, 110, anchor="w",
                      text=f"Tid: {self.t_min:.1f} min", fill="gray20")

    def draw_graph(self):
        g = self.graph
        g.delete("all")

        W, H = self.graph_W, self.graph_H
        pad = self.g_pad
        left, right = pad, W - pad
        top, bottom = pad, H - pad

        g.create_rectangle(left, top, right, bottom, outline="gray40")
        g.create_text(left, top - 18, anchor="w", text="Graf: Vanntemperatur over tid", fill="gray25")

        if len(self.T_hist) < 2:
            return

        # Bestem grafskala dynamisk, men stabilt:
        # bruk romtemp +/- litt margin, og historikk min/max
        T_room = float(self.T_room_var.get())
        T_min = min(min(self.T_hist), T_room) - 2.0
        T_max = max(max(self.T_hist), T_room) + 2.0
        if T_max - T_min < 5:
            T_max = T_min + 5

        t_min = self.t_hist[0]
        t_max = self.t_hist[-1]
        if t_max - t_min < 1e-6:
            t_max = t_min + 1.0

        # Funksjoner for mapping
        def xpix(t):
            return left + (t - t_min) / (t_max - t_min) * (right - left)

        def ypix(T):
            return bottom - (T - T_min) / (T_max - T_min) * (bottom - top)

        # Tegn romtemp-linje
        y_room = ypix(T_room)
        g.create_line(left, y_room, right, y_room, dash=(4, 3), fill="gray60")
        g.create_text(right, y_room - 10, anchor="e", text=f"T_rom={T_room:.1f}°C", fill="gray50")

        # Polyline for T(t)
        pts = []
        for t, T in zip(self.t_hist, self.T_hist):
            pts.extend([xpix(t), ypix(T)])
        g.create_line(pts, width=2, fill="black")

        # Aksenotater (enkle)
        g.create_text(left, bottom + 6, anchor="nw", text=f"{t_min:.0f} min", fill="gray40")
        g.create_text(right, bottom + 6, anchor="ne", text=f"{t_max:.0f} min", fill="gray40")
        g.create_text(left - 6, top, anchor="ne", text=f"{T_max:.0f}°C", fill="gray40")
        g.create_text(left - 6, bottom, anchor="se", text=f"{T_min:.0f}°C", fill="gray40")

    def update_info(self):
        T_room = float(self.T_room_var.get())
        k = float(self.k_var.get())
        dT = self.T - T_room

        # Litt teori:
        # Løsning: T(t) = T_room + (T0 - T_room)*exp(-k t)
        # Tidskonstant tau = 1/k (i minutter)
        tau = (1 / k) if k > 1e-9 else float("inf")

        self.info.config(
            text=(
                f"Status:\n"
                f"  T_vann = {self.T:6.2f} °C\n"
                f"  T_rom  = {T_room:6.2f} °C\n"
                f"  ΔT = T_vann - T_rom = {dT:+6.2f} °C\n\n"
                f"Modell:\n"
                f"  dT/dt = -k (T - T_rom)\n"
                f"  k = {k:.3f} 1/min\n"
                f"  tidskonstant τ = 1/k ≈ {tau:.1f} min\n"
            )
        )


if __name__ == "__main__":
    ThermoWaterGlassApp().mainloop()
