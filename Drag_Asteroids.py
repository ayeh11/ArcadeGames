import turtle
import random
import sys
import time
import math

# window
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Dodge the Planets")
wn.setup(500, 500)
wn.tracer(0)

pen_bg = turtle.Turtle()
pen_bg.speed(0)
pen_bg.color("white")
pen_bg.penup()
pen_bg.setposition(-200, 200)
pen_bg.pendown()
for i in range(4):
    pen_bg.fd(400)
    pen_bg.right(90)
pen_bg.hideturtle()

# pen for score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(0, 200)
score_pen.hideturtle()

# pen for line
class Pens(turtle.Turtle):
    def __init__(self):
         turtle.Turtle.__init__(self)
         self.speed(0)
         self.shape("circle")
         self.color("blue")
         self.penup()
         self.hideturtle()

    def draw(self, x, y, move_to_x, move_to_y):
        self.setposition(x, y)
        self.pendown()
        self.goto(move_to_x, move_to_y)
        self.penup()

pen = Pens()

# planets
planets = []
number_of_planets = 8

class Planets(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("green")
        self.shape("circle")
        self.speed(0)
        self.penup()

        x = random.randint(*random.choice([(-200, -100), (100, 200)]))
        y = random.randint(*random.choice([(-200, -100), (100, 200)]))
        self.setposition(x, y)

        self.move_to_x = random.randint(-200, 200)
        self.move_to_y = random.randint(-200, 200)

        self.run = 0

    def move(self):
        x = self.xcor()
        y = self.ycor()

        dx = self.move_to_x - x
        dy = self.move_to_y - y

        pen.draw(x, y, self.move_to_x, self.move_to_y)

        if self.run == 0:
            self.angle = self.towards(self.move_to_x, self.move_to_y)
            self.run += 1

        if abs(dx) < 5 and abs(dy) < 5:
            self.move_to_x = random.randint(-200, 200)
            self.move_to_y = random.randint(-200, 200)
            pen.clear()
            self.run = 0
        else:
            self.setheading(self.angle)
            self.fd(speed)

    def crash(self, other):
        if self.distance(other) < 5 and self.distance(other) != 0:
            return True

ship = turtle.Turtle()
ship.color("white")
ship.shape("triangle")
ship.speed(0)
ship.penup()
ship.setpos(0,0)

def crash(s):
    for p in planets:
        if s.distance(p) < 15:
            return True

def setup():
    for i in range(number_of_planets):
        planets.append(Planets())

def dragged(x, y):
    if x < 200 and x > -200 and y < 200 and y > -200:
        ship.ondrag(None)  # disable drag inside func
        ship.setheading(ship.towards(x, y))  # turn toward cursor
        ship.goto(x, y)  # move toward cursor
        ship.ondrag(dragged)

run_once = 100
def game_starts():
    number_start = int(run_once / 20)
    scorestring = "{}".format(number_start)
    score_pen.goto(0, 0)
    score_pen.write(scorestring, False, align="center", font=("Arial", 50, "normal"))

score = 0
def score_sys():
    global score
    score_pen.clear()
    score_pen.goto(0, 210)
    score += 1
    scorestring = "Score: {}".format(score)
    score_pen.write(scorestring, False, align="center", font=("Arial", 14, "normal"))

def game_over():
    scorestring = "Game Over"
    score_pen.goto(0, 0)
    score_pen.write(scorestring, False, align="center", font=("Arial", 30, "normal"))
    time.sleep(3)
    sys.exit(0)

setup()
timer = 0
timer2 = 0

wn.tracer(0)

while True:
    wn.update()

    for p in planets:
        turtle.ontimer(p.move, t=1)

    turtle.listen()
    ship.ondrag(dragged)

    if run_once > 0:
        speed = 0
        run_once -= 1
        game_starts()
        if run_once % 20 == 0:
            score_pen.clear()
    else:
        speed = 4
        if timer == 0:
            score_sys()
            timer = 50
        else:
            timer -= 1

        if timer2 == 0:
            pen.clear()
            timer2 = 3
        else:
            timer2 -= 1

    if crash(ship):
        game_over()

wn.mainloop()


