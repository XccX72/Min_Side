# collisions_1d.py
# 1D collision simulator: elastic or perfectly inelastic.
# Shows momentum and kinetic energy before/after.

import tkinter as tk


class CollisionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("1D Collisions (Tkinter)")
        self.state("zoomed")


        self.W, self.H = 900, 280
        self.canvas = tk.Canvas(self, width=self.W, height=self.H, bg="white")
        self.canvas.grid(row=0, column=0, rowspan=20)

        self.track_y = self.H // 2
        self.left_wall = 40
        self.right_wall = self.W - 40
        self.canvas.create_line(self.left_wall, self.track_y, self.right_wall, self.track_y, width=3)

        panel = tk.Frame(self)
        panel.grid(row=0, column=1, sticky="n", padx=10, pady=10)

        self.m1 = tk.DoubleVar(value=2.0)
        self.m2 = tk.DoubleVar(value=1.0)
        self.v1 = tk.DoubleVar(value=3.0)
        self.v2 = tk.DoubleVar(value=-1.0)

        self.mode = tk.StringVar(value="elastic")  # "elastic" or "inelastic"
        tk.Radiobutton(panel, text="Elastic", variable=self.mode, value="elastic").grid(row=0, column=0, sticky="w")
        tk.Radiobutton(panel, text="Perfectly inelastic (stick)", variable=self.mode, value="inelastic").grid(row=1, column=0, sticky="w")

        self._scale(panel, "m1", self.m1, 0.5, 10.0, 0.5, row=2)
        self._scale(panel, "m2", self.m2, 0.5, 10.0, 0.5, row=4)
        self._scale(panel, "v1", self.v1, -8.0, 8.0, 0.2, row=6)
        self._scale(panel, "v2", self.v2, -8.0, 8.0, 0.2, row=8)

        btns = tk.Frame(panel)
        btns.grid(row=10, column=0, pady=(10, 0), sticky="w")
        tk.Button(btns, text="Start", width=10, command=self.start).grid(row=0, column=0, padx=(0, 6))
        tk.Button(btns, text="Reset", width=10, command=self.reset).grid(row=0, column=1)

        self.info = tk.Label(panel, text="", justify="left")
        self.info.grid(row=11, column=0, sticky="w", pady=(10, 0))

        # Simulation state
        self.dt = 0.02
        self.running = False

        # Positions in "meters" mapped to pixels (simple: 1 m = 80 px)
        self.px_per_m = 80.0
        self.x1 = 2.0
        self.x2 = 6.5
        self.vx1 = 0.0
        self.vx2 = 0.0

        self.r1 = 18
        self.r2 = 18
        self.ball1 = self.canvas.create_oval(0, 0, 0, 0, fill="black")
        self.ball2 = self.canvas.create_oval(0, 0, 0, 0, fill="gray20")

        self.reset()
        self.after(16, self.update_loop)

    def _scale(self, parent, label, var, frm, to, res, row):
        tk.Label(parent, text=f"{label}").grid(row=row, column=0, sticky="w")
        tk.Scale(parent, from_=frm, to=to, resolution=res, orient="horizontal",
                 variable=var, length=240).grid(row=row + 1, column=0)

    def reset(self):
        self.running = False
        self.x1 = 2.0
        self.x2 = 6.5
        self.vx1 = self.v1.get()
        self.vx2 = self.v2.get()
        self._draw()
        self._update_info(prefix="Ready.")

    def start(self):
        self.vx1 = self.v1.get()
        self.vx2 = self.v2.get()
        self.running = True
        self._update_info(prefix="Running...")

    def update_loop(self):
        if self.running:
            self.step()
            self._draw()
        self.after(16, self.update_loop)

    def step(self):
        m1 = self.m1.get()
        m2 = self.m2.get()

        # Move
        self.x1 += self.vx1 * self.dt
        self.x2 += self.vx2 * self.dt

        # Wall bounces (keeps things contained)
        if self._to_px(self.x1) - self.r1 < self.left_wall:
            self.x1 = self._to_m(self.left_wall + self.r1)
            self.vx1 *= -1
        if self._to_px(self.x2) + self.r2 > self.right_wall:
            self.x2 = self._to_m(self.right_wall - self.r2)
            self.vx2 *= -1

        # Collision check (1D spheres on a line)
        dist_px = abs(self._to_px(self.x2) - self._to_px(self.x1))
        if dist_px <= (self.r1 + self.r2):
            # Record before values
            p_before = m1 * self.vx1 + m2 * self.vx2
            ke_before = 0.5 * m1 * self.vx1**2 + 0.5 * m2 * self.vx2**2

            if self.mode.get() == "elastic":
                # Standard 1D elastic collision formulas
                u1, u2 = self.vx1, self.vx2
                self.vx1 = ((m1 - m2) / (m1 + m2)) * u1 + (2 * m2 / (m1 + m2)) * u2
                self.vx2 = (2 * m1 / (m1 + m2)) * u1 + ((m2 - m1) / (m1 + m2)) * u2
            else:
                # Perfectly inelastic: they stick together
                v = (m1 * self.vx1 + m2 * self.vx2) / (m1 + m2)
                self.vx1 = v
                self.vx2 = v

            p_after = m1 * self.vx1 + m2 * self.vx2
            ke_after = 0.5 * m1 * self.vx1**2 + 0.5 * m2 * self.vx2**2

            self._update_info(prefix="Collision!",
                              extra=f"Δp={p_after - p_before:+.3f},  ΔKE={ke_after - ke_before:+.3f}")

            # Separate them slightly to prevent repeated collision detection each frame
            mid = (self.x1 + self.x2) / 2
            sep_m = (self.r1 + self.r2) / self.px_per_m
            self.x1 = mid - sep_m / 2
            self.x2 = mid + sep_m / 2

    def _to_px(self, x_m):
        return self.left_wall + x_m * self.px_per_m

    def _to_m(self, x_px):
        return (x_px - self.left_wall) / self.px_per_m

    def _draw(self):
        x1p = self._to_px(self.x1)
        x2p = self._to_px(self.x2)
        self.canvas.coords(self.ball1, x1p - self.r1, self.track_y - self.r1, x1p + self.r1, self.track_y + self.r1)
        self.canvas.coords(self.ball2, x2p - self.r2, self.track_y - self.r2, x2p + self.r2, self.track_y + self.r2)

    def _update_info(self, prefix="", extra=""):
        m1 = self.m1.get()
        m2 = self.m2.get()
        p = m1 * self.vx1 + m2 * self.vx2
        ke = 0.5 * m1 * self.vx1**2 + 0.5 * m2 * self.vx2**2
        self.info.config(
            text=(
                f"{prefix}\n"
                f"v1={self.vx1:+.2f} m/s,  v2={self.vx2:+.2f} m/s\n"
                f"Total momentum p = {p:+.3f}\n"
                f"Total kinetic energy KE = {ke:.3f}\n"
                f"{extra}"
            )
        )


if __name__ == "__main__":
    CollisionApp().mainloop()
