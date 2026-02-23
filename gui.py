import tkinter as tk
import math

class JarvisGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("JARVIS")
        self.root.geometry("500x500")
        self.root.configure(bg="black")

        self.canvas = tk.Canvas(self.root, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.status = self.canvas.create_text(
            250, 460, text="SLEEP",
            fill="cyan", font=("Arial", 18)
        )

        self.angle = 0
        self.animate()

    def animate(self):
        self.canvas.delete("radar")
        for r in range(80, 200, 30):
            self.canvas.create_oval(
                250-r, 250-r, 250+r, 250+r,
                outline="cyan", tags="radar"
            )

        x = 250 + 200 * math.cos(math.radians(self.angle))
        y = 250 + 200 * math.sin(math.radians(self.angle))
        self.canvas.create_line(
            250, 250, x, y,
            fill="cyan", width=2, tags="radar"
        )

        self.angle = (self.angle + 3) % 360
        self.root.after(50, self.animate)

    def set_status(self, text):
        self.canvas.itemconfig(self.status, text=text)

    def run(self):
        self.root.mainloop()
