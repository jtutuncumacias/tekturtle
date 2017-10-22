#Agar.io
#More advanced lab idea combining multiple concepts -
# would likely span several days of work

#Concepts:
#-Tkinter
#-random
#-functions
#-lists


from tkinter import *
import random

def update_game():
    for ball1 in ballsList:
        ball1.draw()
    tk.update_idletasks()
    tk.after(10, update_game)

tk = Tk()
tk.title("Agar.io")
tk.resizable(0, 0)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

def randomColor():
    return "#%02x%02x%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

class Ball:
    def __init__(self, canvas, color, size):
        self.canvas = canvas
        self.size = size
        startx = random.randint(0, canvas.winfo_width())
        starty = random.randint(0, canvas.winfo_height())
        self.id = canvas.create_oval(startx, starty, startx + size, starty + size, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.x = random.randint(3, 6)
        self.y = random.randint(3, 6)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        

class OtherBall(Ball):
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        currentPosition = self.canvas.coords(self.id)
        if currentPosition[0] <= 0 or currentPosition[0] + self.size >= self.canvas_width:
            self.x = -self.x
        if currentPosition[1] <= 0 or currentPosition[1] + self.size >= self.canvas_height:
            self.y = -self.y
        playerPosition = canvas.coords(ball.id)
        if (currentPosition[0] >= playerPosition[0] and currentPosition[0] <= playerPosition[2] and
        currentPosition[2] >= playerPosition[0] and currentPosition[2] <= playerPosition[2] and
        currentPosition[1] >= playerPosition[1] and currentPosition[1] <= playerPosition[3] and
        currentPosition[3] >= playerPosition[1] and currentPosition[3] <= playerPosition[3]):
            ballsList.remove(self)
            canvas.delete(self.id)
            ball.size += 2
            playerPosition[2] += 2
            playerPosition[3] += 2
            canvas.coords(ball.id, playerPosition)

def motion(event):
    x = event.x
    y = event.y
    currentPosition = canvas.coords(ball.id)
    canvas.move(ball.id, x - currentPosition[0], y - currentPosition[1])

ball = Ball(canvas, "#E7CFFF", 20)
ballsList = []
for num in range(30):
    ballsList.append(OtherBall(canvas, randomColor(), random.randint(5, 30)))
tk.bind("<Motion>", motion)

tk.after(10, update_game)
tk.mainloop()

