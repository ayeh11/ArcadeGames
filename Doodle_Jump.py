import turtle
import random
import time
import sys

wn = turtle.Screen()
wn.title("Doodle Jump")
wn.bgcolor("white")
wn.setup(500, 700)
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.setposition(0, 200)
pen.hideturtle()

gravity = -.18

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("blue")
        self.speed(2)
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=2, outline=None)
        self.dy = 0

    def move_left(self):
        self.setx(self.xcor() - 50)

    def move_right(self):
        self.setx(self.xcor() + 50)


def rand_y(multiple):
    num = len(platforms) % multiple
    rand_50 = random.randint(30, 50)
    rand_75 = random.randint(50, 75)
    rand_100 = random.randint(70, 100)
    rand_120 = random.randint(100, 120)
    py = player.ycor()

    if multiple == 5:
        y = 360 + py + (rand_50 * (num + 1))
        return y
    if multiple == 4:
        y = 360 + py + (rand_75 * (num + 1))
        return y
    if multiple == 3:
        y = 360 + py + (rand_100 * (num + 1))
        return y
    if multiple == 2:
        y = 360 + py + (rand_120 * (num + 1))
        return y


def spawn_location():
    x = random.randint(-200, 200)
    if len(platforms) < 6:
        if len(platforms) % 5 == 0:
            y = random.randint(0, 50)
        if len(platforms) % 5 == 1:
            y = random.randint(50, 75)
        if len(platforms) % 5 == 2:
            y = random.randint(100, 150)
        if len(platforms) % 5 == 3:
            y = random.randint(175, 225)
        if len(platforms) % 5 == 4:
            y = random.randint(250, 350)
    elif 5 < len(platforms) < 32:
        y = rand_y(5)
    elif 31 < len(platforms) < 64:
        y = rand_y(4)
    elif 63 < len(platforms) < 94:
        y = rand_y(3)
    elif len(platforms) > 93:
        y = rand_y(2)

    return(x, y)

class Platform(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.speed(0)
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=5, outline=None)
        self.goto(spawn_location())

    def move_down(self):
        self.sety(self.ycor() - 6)

    def contact(self, player):
        if player.ycor() - self.ycor() < 20 and player.ycor() - self.ycor() > 0:
            if abs(self.xcor() - player.xcor()) < 60:
                if player.dy < -1:
                    player.dy = 7
                    spawn()

platforms = []
platform = Platform()
platform.goto(0, -200)
platforms.append(platform)

player = Player()


def spawn():
    #there is the first one
    if len(platforms) < 32:
        for i in range(5):
            platforms.append(Platform())
    elif 31 < len(platforms) < 64:
        for i in range(4):
            platforms.append(Platform())
    elif 63 < len(platforms) < 94:
        for i in range(3):
            platforms.append(Platform())
    elif len(platforms) > 93:
        for i in range(2):
            platforms.append(Platform())

def player_check():
    player.dy += gravity
    player.sety(player.ycor() + player.dy)

    if player.xcor() < -250:
        player.setx(250)
    if player.xcor() > 250:
        player.setx(-250)
    if player.ycor() < -350:
        pen.write("Game Over", False, align="center", font=("Arial", 30, "normal"))
        time.sleep(1)
        sys.exit()

wn.listen()
wn.onkeypress(player.move_left, "Left")
wn.onkeypress(player.move_right, "Right")

while True:
    wn.update()

    player_check()
    for p in platforms:
        p.contact(player)

        if player.dy > -1:
            p.move_down()



wn.mainloop()