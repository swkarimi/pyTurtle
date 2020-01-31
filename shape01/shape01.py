import turtle
turtle.TurtleScreen._RUNNING = True

win = turtle.Screen()
W , H = 500, 500
win.setup(W, H)
win.title("Shape1")
win.clear()
win.bgcolor("white")

# ppu -> pixel per unit
ppu = 15
# number of line in each corner
nline = 12

n1 = nline * ppu
n2 = (nline - 1) * ppu

t = turtle.Turtle()
t.hideturtle()
t.speed(7)
t.pencolor("blue")

t.penup()
t.goto(-n1, n1)
t.pendown()
for _ in range(4):
    t.forward(2*n1)
    t.right(90)
    
def drawline(turtlex, x1, y1, x2, y2):
    turtlex.penup()
    turtlex.goto(x1, y1)
    turtlex.pendown()
    turtlex.goto(x2, y2)
    
for i in range(0, n1, ppu):
    drawline(t, -n1, i, i - n2, n1)
    drawline(t, i, n1, n1, n2 - i)
    drawline(t, n1, -i, n2 - i, -n1)
    drawline(t, -i, -n1, -n1, i - n2)    

from sys import platform
if platform == "win32":
    win.exitonclick()
