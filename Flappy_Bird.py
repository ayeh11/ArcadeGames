import turtle
import time
import random
import sys

wn = turtle.Screen()
wn.title("Flappy Bird")
wn.bgcolor("blue")
wn.setup(width=500, height=700)
wn.tracer(0)

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(0, 300)
score_pen.hideturtle()

player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape("turtle")
player.color("yellow")
player.shapesize(stretch_wid=3, stretch_len=3, outline=None)
player.goto(-80, 0)
player.dy = 1

pipes = []
def spawn():
    for i in range(2):
        pipes.append(Pipe())

y = 0
def pipe_pos():
    global y
    if len(pipes) % 2 == 0:
        y = random.randint(150, 450)
        pos = (250, y)
    else:
        pos = (250, y - 600)
    return pos

class Pipe(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.penup()
        self.shape("square")
        self.color("green")
        self.shapesize(stretch_wid=20, stretch_len=3, outline=None)
        self.dx = -2
        self.setposition(pipe_pos())

    def move(self):
        self.setx(self.xcor() + self.dx)

def go_up():
    player.dy += 4

def game_over():
    if player.ycor() > 350 or player.ycor() < -350:
        return True
    close_ps = []
    for p in pipes:
        if abs(player.xcor() - p.xcor()) < 20:
            close_ps.append(p)
    for ps in close_ps:
        if abs(player.ycor() - ps.ycor()) < 220:
            return True

score = 0
def score_sys():
    global score
    score_pen.clear()
    score += 1
    scorestring = "Score: {}".format(score - 1)
    score_pen.write(scorestring, False, align="center", font=("Arial", 14, "normal"))

gravity = -.1

wn.listen()
wn.onkeypress(go_up, "space")

timer = 0
while True:
    wn.update()

    # add gravity
    player.dy += gravity
    player.sety(player.ycor() + player.dy)

    for p in pipes:
        Pipe.move(p)

    if timer == 0:
        spawn()
        score_sys()
        timer = 150
    else:
        timer -= 1

    if game_over():
        scorestring = "Game Over"
        score_pen.goto(0, 100)
        score_pen.write(scorestring, False, align="center", font=("Arial", 30, "normal"))
        time.sleep(3)
        sys.exit()


wn.mainloop()