# spring_mass.py
# Mass-spring oscillator (simple harmonic motion) with optional damping.
# Uses Euler-Cromer integration (stable for oscillators).
# Shows displacement, velocity, and energies.

import tkinter as tk
import math


class SpringApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mass-Spring Oscillator (Tkinter)")

        self.W, self.H = 900, 420
        self.canvas = tk.Canvas(self, width=self.W, height=self.H, bg="white")
        self.canvas.grid(row=0, column=0, rowspan=20)

        panel = tk.Frame(self)
        panel.grid(row=0, column=1, sticky="n", padx=10, pady=10)

        self.k_var = tk.DoubleVar(value=20.0)     # N/m
        self.m_var = tk.DoubleVar(value=1.5)      # kg
        self.b_var = tk.DoubleVar(value=0.15)     # damping (kg/s)
        self.x0_var = tk.DoubleVar(value=0.35)    # initial displacement (m)
        self.v0_var = tk.DoubleVar(value=0.0)     # initial velocity (m/s)

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

        self.info = tk.Label(panel, text="", justify="left")
        self.info.grid(row=11, column=0, sticky="w", pady=(10, 0))

        # Drawing constants
        self.anchor_x = 80
        self.center_y = self.H // 2
        self.base_len_px = 260  # rest spring length in pixels
        self.px_per_m = 260     # scaling for displacement

        self.mass_w = 60
        self.mass_h = 40

        self.spring_id = None
        self.mass_id = None

        # Simulation
        self.dt = 0.01
        self.running = False

        self.reset()
        self.after(16, self.update_loop)

    def _scale(self, parent, label, var, frm, to, res, row):
        tk.Label(parent, text=label).grid(row=row, column=0, sticky="w")
        tk.Scale(parent, from_=frm, to=to, resolution=res, orient="horizontal",
                 variable=var, length=260).grid(row=row + 1, column=0)

    def reset(self):
        self.running = False
        self.t = 0.0

        # Set initial state from sliders
        self.x = self.x0_var.get()  # meters
        self.v = self.v0_var.get()

        self._draw()
        self._update_info()

    def start(self):
        self.running = True

    def pause(self):
        self.running = False

    def update_loop(self):
        if self.running:
            self.step()
            self._draw()
            self._update_info()
        self.after(16, self.update_loop)

    def step(self):
        # Euler-Cromer: v updated first, then x (good for oscillators)
        k = self.k_var.get()
        m = self.m_var.get()
        b = self.b_var.get()

        # Force: F = -k x - b v
        a = (-k * self.x - b * self.v) / m

        self.v += a * self.dt
        self.x += self.v * self.dt
        self.t += self.dt

    def _draw(self):
        # Map x (meters) to pixels: positive x extends spring to the right
        dx_px = self.x * self.px_per_m
        mass_x = self.anchor_x + self.base_len_px + dx_px
        mass_y = self.center_y

        # Draw spring as a simple zigzag polyline
        x0 = self.anchor_x
        y0 = self.center_y
        x1 = mass_x - self.mass_w / 2  # connect spring to left side of mass

        points = self._spring_points(x0, y0, x1, y0, coils=10, amp=18)

        if self.spring_id is not None:
            self.canvas.delete(self.spring_id)
        self.spring_id = self.canvas.create_line(points, width=3)

        # Draw anchor
        self.canvas.delete("anchor")
        self.canvas.create_rectangle(self.anchor_x - 15, self.center_y - 40,
                                     self.anchor_x + 15, self.center_y + 40,
                                     fill="gray85", outline="gray40", tags="anchor")

        # Draw mass
        xL = mass_x - self.mass_w / 2
        yT = mass_y - self.mass_h / 2
        xR = mass_x + self.mass_w / 2
        yB = mass_y + self.mass_h / 2

        if self.mass_id is not None:
            self.canvas.coords(self.mass_id, xL, yT, xR, yB)
        else:
            self.mass_id = self.canvas.create_rectangle(xL, yT, xR, yB, fill="black")

        # A faint center line
        self.canvas.delete("centerline")
        self.canvas.create_line(self.anchor_x + self.base_len_px, 0,
                                self.anchor_x + self.base_len_px, self.H,
                                dash=(4, 4), fill="gray70", tags="centerline")

    def _spring_points(self, x0, y0, x1, y1, coils=8, amp=14):
        # Build a zigzag between (x0,y0) and (x1,y1)
        # For simplicity we assume horizontal spring (y0==y1).
        length = x1 - x0
        if length < 30:
            length = 30

        pts = []
        pts.extend([x0, y0])

        step = length / (coils * 2)
        x = x0
        sign = 1
        for _ in range(coils * 2 - 1):
            x += step
            pts.extend([x, y0 + sign * amp])
            sign *= -1

        pts.extend([x1, y1])
        return pts

    def _update_info(self):
        k = self.k_var.get()
        m = self.m_var.get()
        # Energies
        pe = 0.5 * k * self.x**2
        ke = 0.5 * m * self.v**2
        self.info.config(
            text=(
                f"t = {self.t:5.2f} s\n"
                f"x = {self.x:+.3f} m\n"
                f"v = {self.v:+.3f} m/s\n"
                f"PE = {pe:6.3f} J\n"
                f"KE = {ke:6.3f} J\n"
                f"Total = {(pe + ke):6.3f} J"
            )
        )


if __name__ == "__main__":
    SpringApp().mainloop()
