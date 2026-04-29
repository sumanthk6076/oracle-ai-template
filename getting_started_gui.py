import tkinter as tk
from tkinter import ttk, font
import random
import math

# ── Theme ──────────────────────────────────────────────────────────────────────
BG          = "#0d0d1a"
CARD_BG     = "#1a1a2e"
ACCENT      = "#00f5d4"
PURPLE      = "#7b2fff"
YELLOW      = "#f5c518"
GREEN       = "#39d353"
WHITE       = "#e8eaf6"
DIM         = "#555577"

STEPS = [
    ("🛠  Set up your environment",  GREEN),
    ("📝  Write your first script",  ACCENT),
    ("▶   Run & test your code",     YELLOW),
    ("📚  Level up your skills",     PURPLE),
    ("🚀  Build something amazing!", "#ff6b6b"),
]

# ── Particle ───────────────────────────────────────────────────────────────────
class Particle:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.w = width
        self.h = height
        self.reset()

    def reset(self):
        self.x  = random.randint(0, self.w)
        self.y  = random.randint(0, self.h)
        self.r  = random.uniform(1.5, 3.5)
        self.vx = random.uniform(-0.4, 0.4)
        self.vy = random.uniform(-0.6, -0.1)
        colors  = [ACCENT, PURPLE, YELLOW, GREEN, "#ff6b6b", WHITE]
        self.color = random.choice(colors)
        self.alpha = random.randint(60, 200)
        self.id = self.canvas.create_oval(
            self.x - self.r, self.y - self.r,
            self.x + self.r, self.y + self.r,
            fill=self.color, outline=""
        )

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.canvas.move(self.id, self.vx, self.vy)
        if self.y < -10 or self.x < -10 or self.x > self.w + 10:
            self.canvas.delete(self.id)
            self.reset()

# ── App ────────────────────────────────────────────────────────────────────────
class GettingStartedApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Just Getting Started 🚀")
        self.geometry("680x560")
        self.resizable(False, False)
        self.configure(bg=BG)

        self._step_index   = 0
        self._bar_value    = 0
        self._title_chars  = 0
        self._title_text   = "JUST GETTING STARTED"
        self._particles    = []
        self._pulse_angle  = 0
        self._check_labels = []

        self._build_ui()
        self.after(300, self._animate_title)
        self.after(200, self._spawn_particles)
        self.after(200, self._move_particles)
        self.after(200, self._pulse_glow)

    # ── UI build ───────────────────────────────────────────────────────────────
    def _build_ui(self):
        # Particle canvas (background layer)
        self.canvas = tk.Canvas(self, width=680, height=560, bg=BG,
                                highlightthickness=0)
        self.canvas.place(x=0, y=0)

        # Card frame
        card = tk.Frame(self, bg=CARD_BG, bd=0)
        card.place(relx=0.5, rely=0.5, anchor="center", width=600, height=490)

        # Glowing title label (drawn on canvas so we can pulse it)
        self.title_label = tk.Label(
            card, text="", font=("Consolas", 22, "bold"),
            fg=ACCENT, bg=CARD_BG
        )
        self.title_label.pack(pady=(30, 4))

        # Sub-tagline
        self.tag_label = tk.Label(
            card, text="", font=("Consolas", 11),
            fg=DIM, bg=CARD_BG
        )
        self.tag_label.pack()

        # Separator
        sep = tk.Frame(card, height=2, bg=PURPLE)
        sep.pack(fill="x", padx=40, pady=14)

        # Progress section
        prog_frame = tk.Frame(card, bg=CARD_BG)
        prog_frame.pack(fill="x", padx=50)

        self.prog_label = tk.Label(prog_frame, text="Initializing...",
                                   font=("Consolas", 10), fg=DIM, bg=CARD_BG,
                                   anchor="w")
        self.prog_label.pack(fill="x")

        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Cool.Horizontal.TProgressbar",
                        troughcolor=BG, background=ACCENT,
                        thickness=12, borderwidth=0)

        self.progress = ttk.Progressbar(prog_frame, style="Cool.Horizontal.TProgressbar",
                                        length=500, mode="determinate", maximum=100)
        self.progress.pack(pady=(4, 16))

        # Checklist
        check_frame = tk.Frame(card, bg=CARD_BG)
        check_frame.pack(fill="x", padx=50)

        for text, color in STEPS:
            lbl = tk.Label(check_frame, text=f"  ○  {text}",
                           font=("Consolas", 11), fg=DIM, bg=CARD_BG, anchor="w")
            lbl.pack(fill="x", pady=3)
            self._check_labels.append((lbl, color))

        # Bottom message
        self.bottom_msg = tk.Label(card, text="",
                                   font=("Consolas", 12, "bold"),
                                   fg=YELLOW, bg=CARD_BG)
        self.bottom_msg.pack(pady=(18, 0))

        # Start button
        self.start_btn = tk.Button(
            card, text="▶  Start Journey", font=("Consolas", 12, "bold"),
            fg=BG, bg=ACCENT, activebackground=PURPLE, activeforeground=WHITE,
            relief="flat", padx=20, pady=8, cursor="hand2",
            command=self._start_sequence
        )
        self.start_btn.pack(pady=(12, 0))

    # ── Particles ──────────────────────────────────────────────────────────────
    def _spawn_particles(self):
        if len(self._particles) < 55:
            p = Particle(self.canvas, 680, 560)
            self._particles.append(p)
        self.after(120, self._spawn_particles)

    def _move_particles(self):
        for p in self._particles:
            p.move()
        self.after(30, self._move_particles)

    # ── Title typewriter ───────────────────────────────────────────────────────
    def _animate_title(self):
        if self._title_chars <= len(self._title_text):
            self.title_label.config(
                text=self._title_text[:self._title_chars] + (
                    "█" if self._title_chars < len(self._title_text) else ""
                )
            )
            self._title_chars += 1
            self.after(60, self._animate_title)
        else:
            self.title_label.config(text=self._title_text)
            self.tag_label.config(text="Your launchpad to building great things.")

    # ── Glow pulse ─────────────────────────────────────────────────────────────
    def _pulse_glow(self):
        self._pulse_angle += 0.07
        val = int(200 + 55 * math.sin(self._pulse_angle))
        hex_color = f"#{val:02x}f5d4" if val <= 0xff else "#00f5d4"
        try:
            self.title_label.config(fg=hex_color)
        except Exception:
            pass
        self.after(50, self._pulse_glow)

    # ── Sequence ───────────────────────────────────────────────────────────────
    def _start_sequence(self):
        self.start_btn.config(state="disabled", bg=DIM)
        self._bar_value = 0
        self._step_index = 0
        self.bottom_msg.config(text="")
        for lbl, _ in self._check_labels:
            lbl.config(fg=DIM, text=f"  ○  {STEPS[self._check_labels.index((lbl, _))][0]}")
        self._run_step()

    def _run_step(self):
        if self._step_index >= len(STEPS):
            self._finish()
            return

        text, color = STEPS[self._step_index]
        self.prog_label.config(text=f"Loading: {text.strip()} …", fg=color)
        self._bar_value = (self._step_index / len(STEPS)) * 100
        self._animate_bar(target=(self._step_index + 1) / len(STEPS) * 100,
                          on_done=self._tick_step)

    def _animate_bar(self, target, on_done):
        if self._bar_value < target:
            self._bar_value = min(self._bar_value + 1.8, target)
            self.progress["value"] = self._bar_value
            self.after(18, lambda: self._animate_bar(target, on_done))
        else:
            self.progress["value"] = target
            self.after(120, on_done)

    def _tick_step(self):
        lbl, color = self._check_labels[self._step_index]
        lbl.config(text=f"  ✔  {STEPS[self._step_index][0]}",
                   fg=color, font=("Consolas", 11, "bold"))
        self._step_index += 1
        self.after(250, self._run_step)

    def _finish(self):
        self.progress["value"] = 100
        self.prog_label.config(text="All systems go! 🎉", fg=GREEN)
        self._typewrite_bottom("You're all set — the only way is forward! 💡", 0)
        self.start_btn.config(state="normal", bg=ACCENT, text="▶  Run Again")

    def _typewrite_bottom(self, text, idx):
        if idx <= len(text):
            self.bottom_msg.config(text=text[:idx])
            self.after(45, lambda: self._typewrite_bottom(text, idx + 1))


if __name__ == "__main__":
    app = GettingStartedApp()
    app.mainloop()
