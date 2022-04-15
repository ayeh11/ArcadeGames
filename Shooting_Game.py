import turtle
import random
import time

wn = turtle.Screen()
wn.title("Shooting")
wn.bgcolor("black")
wn.setup(800, 800)
wn.tracer(0)

sensitivity = 10
speed = 2

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(0, 350)
score_pen.hideturtle()

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("white")
        self.shape("turtle")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid=1.5, stretch_len=1.5, outline=None)
        self.setheading(90)
        self.setpos(0, 0)
        self.angle = 90
        self.direction = "stop"

    def rotate_left(self):
        self.direction = "left"

    def rotate_right(self):
        self.direction = "right"

    def go_fd(self):
        if self.xcor() < 350 and self.xcor() > -350 and self.ycor() < 350 and self.ycor() > -350:
            self.direction = "fd"

    def go_back(self):
        if self.xcor() < 350 and self.xcor() > -350 and self.ycor() < 350 and self.ycor() > -350:
            self.direction = "back"

    def move(self):
        if self.direction == "left":
            self.angle += 1
            self.setheading(self.angle)
        elif self.direction == "right":
            self.angle -= 1
            self.setheading(self.angle)
        elif self.direction == "fd":
            self.fd(1)
        elif self.direction == "back":
            self.back(1)
        elif self.direction == "fire":
            self.color("white")

    def fire(self):
        self.direction = "fire"
        bullet = Bullet()
        bullets.append(bullet)
        bullet.move(self.xcor(), self.ycor(), self.angle)


class Bullet(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid=.2, stretch_len=.2, outline=None)

    def move(self, x, y, angle):
        self.setposition(x, y)
        self.setheading(angle)

colors = ["blue", "cyan", "pink", "purple", "lightgreen"]
class Enemy(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        color = random.choice(colors)
        self.color(color)
        self.shape("circle")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid=1, stretch_len=1, outline=None)

    def move(self):
        angle = self.towards(0, 0)
        self.setheading(angle)
        self.fd(speed)

    def hit(self):
        for b in bullets:
            if self.distance(b) < 20:
                self.hideturtle()
                self.goto(1000,1000)

        if self.distance(player) < 5:
            score_pen.clear()
            score_pen.write("game over", False, align="center", font=("Arial", 30, "normal"))

def spawner():
    enemy = Enemy()
    x = random.randint(*random.choice([(-350, -250), (250, 350)]))
    y = random.randint(*random.choice([(-350, -250), (250, 350)]))
    enemy.setpos(x, y)
    enemies.append(enemy)


bullets = []
enemies = []
player = Player()

wn.listen()
wn.onkey(player.rotate_left, "Left")
wn.onkey(player.rotate_right, "Right")
wn.onkey(player.go_fd, "Up")
wn.onkey(player.go_back, "Down")
wn.onkey(player.fire, "space")

timer = 0
while True:
    wn.update()

    player.move()

    for b in bullets:
        b.fd(5)

    for e in enemies:
        e.move()
        e.hit()

    if timer == 0:
        spawner()
        timer += 50
    else:
        timer -= 1

wn.mainloop()
