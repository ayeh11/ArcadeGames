import turtle
import random
import sys
import time

wn = turtle.Screen()
wn.bgcolor("gray")
wn.title("Maze Game")
wn.setup(700,700)
wn.tracer(0)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)

text_pen = turtle.Turtle()
text_pen.speed(0)
text_pen.color("black")
text_pen.penup()
text_pen.setposition(0, 310)
text_pen.hideturtle()

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)

    def out(self):
        y = self.ycor()
        if y < -330:
            return True


class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0

        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"

        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if(move_to_x, move_to_y) not in walls:
            if move_to_x < 288 and move_to_x > -288 and move_to_y < 288 and move_to_y > -288:
                self.goto(move_to_x, move_to_y)
            else:
                self.direction = random.choice(["up", "down", "left", "right"])
        else:
            self.direction = random.choice(["up", "down", "left", "right"])

        # set timer to move next time
        turtle.ontimer(self.move, t=random.randint(100, 300))

    def is_close(self, other):
        if self.distance(other) < 75:
            return True

class Key(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

    def close(self):
        if self.distance(player) < 5:
            self.goto(2000, 2000)
            self.hideturtle()
            return True

class Lock(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

    def close(self):
        if self.distance(player) < 5:
            self.goto(2000, 2000)
            self.hideturtle()
            return True

class Door(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.goto(x, y)
        self.speed(0)


levels = [""]

level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "X P XXXXXXXXXX  K    XXXX",
    "X   XXXXXXXXXX     E   XX",
    "X       XXXXXX  XXXXX  XX",
    "X  XXX  XXXXXX  XXXXX  XX",
    "X               XXXXX  XX",
    "XX  XXXXXXX  XXXXXXXX  XX",
    "XX  XXXXXXX  XXXXXXXX  XX",
    "XX  XXXXXXX            XX",
    "XX  XXXXXXX  XXXXX    XXX",
    "XX           XXXXX    XXX",
    "XXXXX   XXXXXXXXXX  E XXX",
    "XXXXX   XXXXXXXXXX    XXX",
    "XXXXX   XXXXXXXXXXXX XXXX",
    "XXXXX         XXXX    XXX",
    "XXXXXXXXXXXX  XXX     XXX",
    "XXXXXXXXXXXX       XXXXXX",
    "XXXXXXXXXXXXXXXX   XXXXXX",
    "XXX L   XXXXXXXX   XXXXXX",
    "XXX                XXXXXX",
    "XXX      XXXXXX    XXXXXX",
    "XXX  E   XXXXXXX  XXXXXXX",
    "XXX      XXXXXXX  XXXXXXX",
    "XXXXXXXXXXXXXXXX  XXXXXXX",
    "XXXXXXXXXXXXXXXXDDXXXXXXX",
]

levels.append(level_1)

enemies = []
walls = []
doors = []

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            # get character in x, y coor
            character = level[y][x]
            screen_x = -288 + (x*24)
            screen_y = 288 - (y*24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()

                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))

            if character == "K":
                key.goto(screen_x, screen_y)

            if character == "L":
                lock.goto(screen_x, screen_y)

            if character == "D":
                doors.append(Door(screen_x, screen_y))

pen = Pen()
player = Player()
key = Key()
lock = Lock()

setup_maze(levels[1])

turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

wn.tracer(0)

for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)

def game_over(textstring):
    text_pen.write(textstring, False, align="center", font=("Arial", 30, "normal"))
    time.sleep(3)
    sys.exit(0)


while True:
    wn.update()

    if key.close():
        player.color("yellow")

    if lock.close():
        player.color("white")
        for d in doors:
            d.goto(2000, 2000)
            d.hideturtle()

    if player.out():
        game_over("Pass!")

    for enemy in enemies:
        if player.distance(enemy) < 10:
            game_over("Game Over!")

wn.mainloop()