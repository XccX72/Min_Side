# spring_mass_graph.py
# Mass-spring oscillator with damping + LIVE scrolling graph in Tkinter (no extra libs).
#
# Graph shows:
#   - displacement x(t)
#   - velocity v(t)
#   - total energy E(t) = KE + PE
#
# Uses Euler-Cromer integration (stable for oscillators).
# Designed to be readable and easy to extend.

import tkinter as tk


class SpringGraphApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mass-Spring Oscillator + Live Graph (Tkinter)")

        # --- Layout ---
        # Left: simulation canvas
        # Right: controls + info
        self.sim_W, self.sim_H = 900, 320
        self.graph_W, self.graph_H = 900, 240

        self.sim_canvas = tk.Canvas(self, width=self.sim_W, height=self.sim_H, bg="white")
        self.sim_canvas.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.graph_canvas = tk.Canvas(self, width=self.graph_W, height=self.graph_H, bg="white")
        self.graph_canvas.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=(6, 0))

        panel = tk.Frame(self)
        panel.grid(row=0, column=2, rowspan=2, sticky="n", padx=10, pady=10)

        # --- Controls ---
        self.k_var = tk.DoubleVar(value=20.0)     # N/m
        self.m_var = tk.DoubleVar(value=1.5)      # kg
        self.b_var = tk.DoubleVar(value=0.15)     # kg/s damping
        self.x0_var = tk.DoubleVar(value=0.35)    # m initial displacement
        self.v0_var = tk.DoubleVar(value=0.0)     # m/s initial velocity

        self._scale(panel, "Spring constant k (N/m)", self.k_var, 1, 80, 1, row=0)
        self._scale(panel, "Mass m (kg)", self.m_var, 0.2, 10, 0.1, row=2)
        self._scale(panel, "Damping b (kg/s)", self.b_var, 0.0, 3.0, 0.02, row=4)
        self._scale(panel, "Initial x0 (m)", self.x0_var, -0.8, 0.8, 0.01, row=6)
        self._scale(panel, "Initial v0 (m/s)", self.v0_var, -4.0, 4.0, 0.05, row=8)

        btns = tk.Frame(panel)
        btns.grid(row=10, column=0, pady=(10, 0), sticky="w")
        tk.Button(btns, text="Start", width=10, command=self.start).grid(row=0, column=0, padx=(0, 6))
        tk.Button(btns, text="Pause", width=10, command=self.pause).grid(row=0, column=1, padx=(0, 6))
        tk.Button(btns, text="Reset", width=10, command=self.reset).grid(row=0, column=2)

        tk.Label(panel, text="Graph legend:", anchor="w").grid(row=11, column=0, sticky="w", pady=(12, 0))
        self.legend = tk.Label(
            panel,
            text="x(t) = black   v(t) = gray25   E(t) = gray60",
            justify="left",
            anchor="w",
        )
        self.legend.grid(row=12, column=0, sticky="w")

        self.info = tk.Label(panel, text="", justify="left", anchor="w")
        self.info.grid(row=13, column=0, sticky="w", pady=(12, 0))

        # --- Simulation drawing constants ---
        self.anchor_x = 80
        self.center_y = self.sim_H // 2
        self.base_len_px = 260    # rest spring length in pixels
        self.px_per_m = 260       # conversion from meters to pixels (for displacement)

        self.mass_w = 60
        self.mass_h = 40

        self.spring_id = None
        self.mass_id = None

        # --- Physics state ---
        self.dt = 0.01            # physics time step
        self.running = False
        self.t = 0.0
        self.x = 0.0
        self.v = 0.0

        # --- Graph settings ---
        # We'll store a rolling window of samples
        self.max_points = 700
        self.samples_x = []
        self.samples_v = []
        self.samples_E = []

        # Graph axis ranges (auto-ish, but stable):
        # x_range and v_range can expand if needed
        self.x_range = 0.8    # meters
        self.v_range = 4.0    # m/s
        self.E_range = 5.0    # joules (auto updates upward if needed)

        # Graph padding
        self.g_pad = 35
        self.reset()

        # Main UI loop
        self.after(16, self.update_loop)

    def _scale(self, parent, label, var, frm, to, res, row):
        tk.Label(parent, text=label, anchor="w").grid(row=row, column=0, sticky="w")
        tk.Scale(
            parent,
            from_=frm,
            to=to,
            resolution=res,
            orient="horizontal",
            variable=var,
            length=260,
        ).grid(row=row + 1, column=0)

    # ----------------------------
    # Buttons
    # ----------------------------
    def start(self):
        self.running = True

    def pause(self):
        self.running = False

    def reset(self):
        self.running = False
        self.t = 0.0
        self.x = self.x0_var.get()
        self.v = self.v0_var.get()

        # Clear graph history
        self.samples_x.clear()
        self.samples_v.clear()
        self.samples_E.clear()

        # Reset energy range to a reasonable baseline
        self.E_range = 5.0

        # Add first sample so the graph isn't empty
        self._append_sample()

        self._draw_sim()
        self._draw_graph()
        self._update_info()

    # ----------------------------
    # Main loop
    # ----------------------------
    def update_loop(self):
        if self.running:
            # You can do multiple physics steps per UI frame to keep it smooth
            # without requiring a tiny dt for rendering.
            steps_per_frame = 2
            for _ in range(steps_per_frame):
                self._step_physics()
                self._append_sample()

            self._draw_sim()
            self._draw_graph()
            self._update_info()

        self.after(16, self.update_loop)

    # ----------------------------
    # Physics
    # ----------------------------
    def _step_physics(self):
        k = self.k_var.get()
        m = self.m_var.get()
        b = self.b_var.get()

        # Force: F = -k x - b v
        a = (-k * self.x - b * self.v) / m

        # Euler-Cromer: update v first, then x
        self.v += a * self.dt
        self.x += self.v * self.dt
        self.t += self.dt

        # Expand graph ranges if needed (keeps lines visible without constant rescale jitter)
        self.x_range = max(self.x_range, abs(self.x) * 1.1, 0.2)
        self.v_range = max(self.v_range, abs(self.v) * 1.1, 0.5)

    def _energies(self):
        k = self.k_var.get()
        m = self.m_var.get()
        pe = 0.5 * k * self.x * self.x
        ke = 0.5 * m * self.v * self.v
        return pe, ke, pe + ke

    # ----------------------------
    # Simulation drawing
    # ----------------------------
    def _draw_sim(self):
        self.sim_canvas.delete("all")

        # Convert displacement x [m] to pixels
        dx_px = self.x * self.px_per_m

        # Mass center position
        mass_cx = self.anchor_x + self.base_len_px + dx_px
        mass_cy = self.center_y

        # Spring connection point to mass (left edge)
        spring_end_x = mass_cx - self.mass_w / 2

        # Anchor block
        self.sim_canvas.create_rectangle(
            self.anchor_x - 15, self.center_y - 40,
            self.anchor_x + 15, self.center_y + 40,
            fill="gray85", outline="gray40"
        )

        # Center reference line (rest position)
        self.sim_canvas.create_line(
            self.anchor_x + self.base_len_px, 0,
            self.anchor_x + self.base_len_px, self.sim_H,
            dash=(4, 4), fill="gray70"
        )

        # Draw spring as zigzag
        points = self._spring_points(self.anchor_x, self.center_y, spring_end_x, self.center_y, coils=10, amp=18)
        self.sim_canvas.create_line(points, width=3)

        # Draw mass
        xL = mass_cx - self.mass_w / 2
        yT = mass_cy - self.mass_h / 2
        xR = mass_cx + self.mass_w / 2
        yB = mass_cy + self.mass_h / 2
        self.sim_canvas.create_rectangle(xL, yT, xR, yB, fill="black")

        # Text overlay
        pe, ke, e = self._energies()
        self.sim_canvas.create_text(
            10, 10, anchor="nw",
            text=f"t={self.t:.2f}s   x={self.x:+.3f}m   v={self.v:+.3f}m/s   E={e:.3f}J"
        )

    def _spring_points(self, x0, y0, x1, y1, coils=8, amp=14):
        # Zigzag between (x0,y0) and (x1,y1). Assume horizontal.
        length = max(x1 - x0, 30)
        pts = [x0, y0]

        step = length / (coils * 2)
        x = x0
        sign = 1
        for _ in range(coils * 2 - 1):
            x += step
            pts.extend([x, y0 + sign * amp])
            sign *= -1

        pts.extend([x1, y1])
        return pts

    # ----------------------------
    # Graph data handling
    # ----------------------------
    def _append_sample(self):
        pe, ke, e = self._energies()

        self.samples_x.append(self.x)
        self.samples_v.append(self.v)
        self.samples_E.append(e)

        # Keep a rolling buffer
        if len(self.samples_x) > self.max_points:
            self.samples_x.pop(0)
            self.samples_v.pop(0)
            self.samples_E.pop(0)

        # Expand energy range upward if needed (avoid shrinking to reduce flicker)
        if e > self.E_range * 0.95:
            self.E_range = max(self.E_range * 1.2, e * 1.1, 1.0)

    # ----------------------------
    # Graph drawing
    # ----------------------------
    def _draw_graph(self):
        c = self.graph_canvas
        c.delete("all")

        W = self.graph_W
        H = self.graph_H
        pad = self.g_pad

        # Plot area
        left = pad
        right = W - pad
        top = pad
        bottom = H - pad

        # Axes box
        c.create_rectangle(left, top, right, bottom, outline="gray40")

        # Axis labels
        c.create_text(left, top - 18, anchor="w", text="Live Graph (scrolling):")
        c.create_text(left, bottom + 8, anchor="nw", text="time → (latest on the right)")

        # Horizontal midline for x and v (0 line)
        mid_y = (top + bottom) / 2
        c.create_line(left, mid_y, right, mid_y, dash=(3, 3), fill="gray70")

        # If we don't have enough samples, nothing to draw
        n = len(self.samples_x)
        if n < 2:
            return

        # X coordinate spacing: equally spaced over the plot width
        dx = (right - left) / (self.max_points - 1)

        # Mapping functions (value -> y pixel)
        # For x and v we use centered scaling around mid_y:
        def y_from_centered(val, val_range):
            # val_range maps to half-height
            half_h = (bottom - top) / 2
            return mid_y - (val / val_range) * half_h

        # For energy we map 0..E_range to bottom..top
        def y_from_energy(val):
            val = max(0.0, val)
            return bottom - (val / self.E_range) * (bottom - top)

        # Build polyline points
        pts_x = []
        pts_v = []
        pts_E = []

        start_x = right - dx * (n - 1)
        for i in range(n):
            xpix = start_x + i * dx
            pts_x.extend([xpix, y_from_centered(self.samples_x[i], self.x_range)])
            pts_v.extend([xpix, y_from_centered(self.samples_v[i], self.v_range)])
            pts_E.extend([xpix, y_from_energy(self.samples_E[i])])

        # Draw the lines:
        # x(t) black, v(t) dark gray, E(t) lighter gray
        c.create_line(pts_x, width=2, fill="black")
        c.create_line(pts_v, width=2, fill="gray25")
        c.create_line(pts_E, width=2, fill="gray60")

        # Small scale labels on the left
        c.create_text(left + 6, top + 6, anchor="nw",
                      text=f"x range: ±{self.x_range:.2f} m\nv range: ±{self.v_range:.2f} m/s\nE max: {self.E_range:.2f} J")

    # ----------------------------
    # Info panel
    # ----------------------------
    def _update_info(self):
        pe, ke, e = self._energies()
        self.info.config(
            text=(
                f"t = {self.t:6.2f} s\n"
                f"x = {self.x:+.4f} m\n"
                f"v = {self.v:+.4f} m/s\n"
                f"PE = {pe:7.4f} J\n"
                f"KE = {ke:7.4f} J\n"
                f"E  = {e:7.4f} J"
            )
        )


if __name__ == "__main__":
    SpringGraphApp().mainloop()
