# projectile_motion.py
# Simple projectile motion simulator with optional air resistance (linear drag).
# Controls: sliders for speed/angle/drag, reset + launch.

import math
import tkinter as tk


class ProjectileApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Projectile Motion (Tkinter)")

        # Canvas
        self.W, self.H = 900, 520
        self.canvas = tk.Canvas(self, width=self.W, height=self.H, bg="white")
        self.canvas.grid(row=0, column=0, rowspan=20)

        # Ground line
        self.ground_y = self.H - 40
        self.canvas.create_line(0, self.ground_y, self.W, self.ground_y)

        # Control panel
        panel = tk.Frame(self)
        panel.grid(row=0, column=1, sticky="n", padx=10, pady=10)

        self.speed_var = tk.DoubleVar(value=25.0)   # m/s
        self.angle_var = tk.DoubleVar(value=45.0)   # degrees
        self.drag_var = tk.DoubleVar(value=0.00)    # 1/s approx
        self.use_drag = tk.BooleanVar(value=False)

        tk.Label(panel, text="Initial speed (m/s)").grid(row=0, column=0, sticky="w")
        tk.Scale(panel, from_=5, to=60, resolution=0.5, orient="horizontal",
                 variable=self.speed_var, length=240).grid(row=1, column=0)

        tk.Label(panel, text="Angle (deg)").grid(row=2, column=0, sticky="w")
        tk.Scale(panel, from_=5, to=85, resolution=1, orient="horizontal",
                 variable=self.angle_var, length=240).grid(row=3, column=0)

        tk.Checkbutton(panel, text="Enable air resistance (linear)",
                       variable=self.use_drag, command=self._sync_drag_enabled).grid(row=4, column=0, sticky="w")

        self.drag_scale = tk.Scale(panel, from_=0.0, to=1.2, resolution=0.02, orient="horizontal",
                                   variable=self.drag_var, length=240, state="disabled")
        tk.Label(panel, text="Drag coefficient k (1/s)").grid(row=5, column=0, sticky="w")
        self.drag_scale.grid(row=6, column=0)

        btns = tk.Frame(panel)
        btns.grid(row=7, column=0, pady=(10, 0), sticky="w")
        tk.Button(btns, text="Launch", width=10, command=self.launch).grid(row=0, column=0, padx=(0, 6))
        tk.Button(btns, text="Reset", width=10, command=self.reset).grid(row=0, column=1)

        # Info labels
        self.info = tk.Label(panel, text="", justify="left")
        self.info.grid(row=8, column=0, sticky="w", pady=(10, 0))

        # Physics + drawing state
        self.scale = 12.0  # pixels per meter
        self.dt = 0.02     # seconds per step (simulation timestep)

        self.origin_x = 60
        self.origin_y = self.ground_y

        self.ball_r = 7
        self.ball_id = self.canvas.create_oval(0, 0, 0, 0, fill="black")
        self.trail_ids = []

        self.running = False
        self.reset()

        self.after(16, self.update_loop)

    def _sync_drag_enabled(self):
        self.drag_scale.config(state=("normal" if self.use_drag.get() else "disabled"))

    def reset(self):
        # Reset physics variables
        self.running = False
        self.t = 0.0
        self.x = 0.0
        self.y = 0.0
        self.vx = 0.0
        self.vy = 0.0

        # Clear trail
        for tid in self.trail_ids:
            self.canvas.delete(tid)
        self.trail_ids.clear()

        self._draw_ball()
        self._update_info()

    def launch(self):
        # Set initial velocity based on sliders
        v0 = self.speed_var.get()
        angle = math.radians(self.angle_var.get())
        self.vx = v0 * math.cos(angle)
        self.vy = v0 * math.sin(angle)

        self.t = 0.0
        self.x = 0.0
        self.y = 0.0
        self.running = True

        # Clear trail before new launch
        for tid in self.trail_ids:
            self.canvas.delete(tid)
        self.trail_ids.clear()

    def update_loop(self):
        # Main animation loop (called ~60 times per second)
        if self.running:
            self.step_physics()
            self._draw_ball()
            self._update_info()

            # Stop if it hits the ground
            if self.y <= 0 and self.t > 0:
                self.y = 0
                self.running = False

        self.after(16, self.update_loop)

    def step_physics(self):
        # Euler integration (simple and very readable)
        g = 9.81
        k = self.drag_var.get() if self.use_drag.get() else 0.0

        # Acceleration with linear drag: a = -k*v (separately for x/y) + gravity in y
        ax = -k * self.vx
        ay = -g - k * self.vy

        # Update velocities
        self.vx += ax * self.dt
        self.vy += ay * self.dt

        # Update positions
        self.x += self.vx * self.dt
        self.y += self.vy * self.dt
        self.t += self.dt

        # Add small trail dot every few steps (cheap and helpful)
        if int(self.t / self.dt) % 3 == 0:
            cx, cy = self._world_to_canvas(self.x, self.y)
            tid = self.canvas.create_oval(cx - 1, cy - 1, cx + 1, cy + 1, outline="", fill="gray40")
            self.trail_ids.append(tid)
            # keep trail from growing forever
            if len(self.trail_ids) > 1200:
                self.canvas.delete(self.trail_ids.pop(0))

    def _world_to_canvas(self, x_m, y_m):
        # World coordinates: x to right, y up. Canvas y is down.
        cx = self.origin_x + x_m * self.scale
        cy = self.origin_y - y_m * self.scale
        return cx, cy

    def _draw_ball(self):
        cx, cy = self._world_to_canvas(self.x, self.y)
        r = self.ball_r
        self.canvas.coords(self.ball_id, cx - r, cy - r, cx + r, cy + r)

    def _update_info(self):
        self.info.config(
            text=(
                f"t = {self.t:5.2f} s\n"
                f"x = {self.x:5.2f} m\n"
                f"y = {self.y:5.2f} m\n"
                f"vx = {self.vx:5.2f} m/s\n"
                f"vy = {self.vy:5.2f} m/s\n"
            )
        )


if __name__ == "__main__":
    ProjectileApp().mainloop()
