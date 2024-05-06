import tkinter as tk
import random

class Bubble:
    def __init__(self, canvas, x, y, radius, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = random.randint(-3, 3)
        self.speed_y = random.randint(-3, 3)
        self.draw()

    def draw(self):
        x0 = self.x - self.radius
        y0 = self.y - self.radius
        x1 = self.x + self.radius
        y1 = self.y + self.radius
        self.oval = self.canvas.create_oval(x0, y0, x1, y1, fill=self.color)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.canvas.move(self.oval, self.speed_x, self.speed_y)
        if self.x - self.radius <= 0 or self.x + self.radius >= canvas_width:
            self.speed_x *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= canvas_height:
            self.speed_y *= -1

def update(canvas, bubbles):
    for bubble in bubbles:
        bubble.move()
    canvas.after(30, update, canvas, bubbles)

def start_animation(canvas):
    global canvas_width, canvas_height
    canvas_width = canvas.winfo_reqwidth()  # Get canvas width
    canvas_height = canvas.winfo_reqheight()  # Get canvas height
    
    # Create bubbles
    bubbles = []
    for _ in range(10):
        x = random.randint(50, canvas_width - 50)
        y = random.randint(50, canvas_height - 50)
        radius = random.randint(10, 30)
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        bubble = Bubble(canvas, x, y, radius, color)
        bubbles.append(bubble)

    # Start animation loop
    update(canvas, bubbles)
