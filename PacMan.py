import turtle
import time
import random

wn = turtle.Screen()
wn.title("Pac-Man")
wn.bgcolor("black")
wn.setup(700, 850)
wn.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.setundobuffer(1)

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0,380)
score_pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

score = 0
lives = 3
eaten = 0

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.direction = "stop"

    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24

        if (move_to_x, move_to_y) not in walls:
            self.direction = "up"

    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            self.direction = "down"

    def go_left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.direction = "left"

    def go_right(self):
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.direction = "right"

    def move(self):
        if self.direction == "up":
            move_to_x = self.xcor()
            move_to_y = self.ycor() + 24

            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)
        elif self.direction == "down":
            move_to_x = self.xcor()
            move_to_y = self.ycor() - 24

            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)
        elif self.direction == "left":
            move_to_x = self.xcor() - 24
            move_to_y = self.ycor()

            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)
            if move_to_x < -350:
                self.setposition(move_to_x + 24*27, move_to_y)
        elif self.direction == "right":
            move_to_x = self.xcor() + 24
            move_to_y = self.ycor()

            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)
            if move_to_x > 350:
                self.setposition(move_to_x - 24*27, move_to_y)


class Food(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.color("white")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=.2, stretch_len=.2, outline=None)
        self.speed(0)
        self.goto(x, y)

    def eaten(self):
        global score
        if self.xcor() == player.xcor() and self.ycor() == player.ycor():
            self.hideturtle()
            self.goto(1000,1000)

            score += 10
            score_pen.clear()
            score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

class Super_Food(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.color("white")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=.8, stretch_len=.8, outline=None)
        self.speed(0)
        self.goto(x, y)

    def eaten(self):
        global score
        global eaten
        if self.xcor() == player.xcor() and self.ycor() == player.ycor():
            self.hideturtle()
            self.goto(1000,1000)

            score += 20
            score_pen.clear()
            score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
            eaten += 1

direction = ["up", "down", "left", "right"]
colors = ["red", "cyan", "pink", "orange"]
class Enemy(turtle.Turtle): # moves randomly
    def __init__(self, num):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.shapesize(stretch_wid=.8, stretch_len=.8, outline=None)
        self.setheading(90)
        self.color(colors[num])
        self.penup()
        self.speed(0)
        self.direction = random.choice(direction)

    def move(self, num, screen_x, screen_y):
        if self.direction == "up":
            move_to_x = self.xcor()
            move_to_y = self.ycor() + 24

            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)
            else:
                if num == 1:
                    if self.is_close(player, 72):
                        self.follow()
                    else:
                        self.direction = random.choice(direction)
                elif num == 2:
                    if self.is_close(player, 240):
                        self.follow()
                    else:
                        self.direction = random.choice(direction)
                elif num == 3:
                    self.follow()
                elif num == 0:
                    self.direction = random.choice(direction)

        elif self.direction == "down":
            move_to_x = self.xcor()
            move_to_y = self.ycor() - 24

            if (move_to_x, move_to_y) not in walls:
                if (move_to_x, move_to_y) not in doors:
                    self.goto(move_to_x, move_to_y)
            else:
                self.direction = random.choice(direction)
        elif self.direction == "left":
            move_to_x = self.xcor() - 24
            move_to_y = self.ycor()

            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)
            else:
                self.direction = random.choice(direction)
            if move_to_x < -350:
                self.setposition(move_to_x + 24 * 27, move_to_y)
        elif self.direction == "right":
            move_to_x = self.xcor() + 24
            move_to_y = self.ycor()

            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)
            else:
                self.direction = random.choice(direction)
            if move_to_x > 350:
                self.setposition(move_to_x - 24 * 27, move_to_y)

        global lives
        if eaten == 1:
            self.color("blue")
            if self.is_close(player, 20):
                self.goto(screen_x, screen_y)
        elif eaten == 0:
            self.color(colors[num])
            if self.is_close(player, 20):
                lives -= 1
                lose_life()
                reset()

    def is_close(self, other, dis):
        if self.distance(other) < dis:
            return True

    def follow(self):
        if player.xcor() < self.xcor():
            self.direction = "left"
        elif player.xcor() > self.xcor():
            self.direction = "right"
        elif player.ycor() < self.ycor():
            self.direction = "down"
        elif player.ycor() > self.ycor():
            self.direction = "up"


class Door(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("blue", "black")
        self.shape("square")
        self.shapesize(stretch_wid=1.2, stretch_len=1.2, outline=None)
        self.goto(x, y)

grid = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XFFFFFFFFFFFFXFFFFFFFFFFFFX",
    "XFXXXXFXXXXXFXFXXXXXFXXXXFX",
    "XSXXXXFXXXXXFXFXXXXXFXXXXSX",
    "XFXXXXFXXXXXFXFXXXXXFXXXXFX",
    "XFFFFFFFFFFFFFFFFFFFFFFFFFX",
    "XFXXXXFXXFXXXXXXXFXXFXXXXFX",
    "XFXXXXFXXFXXXXXXXFXXFXXXXFX",
    "XFFFFFFXXFFFFXFFFFXXFFFFFFX",
    "XXXXXXFXXXXX X XXXXXFXXXXXX",
    "     XFXXXXX X XXXXXFX     ",
    "     XFXX    R    XXFX     ",
    "     XFXX XDDDDDX XXFX     ",
    "XXXXXXFXX X     X XXFXXXXXX",
    "      FXX X CKO X XXF      ",
    "XXXXXXFXX X     X XXFXXXXXX",
    "     XFXX XXDDDXX XXFX     ",
    "     XFXX         XXFX     ",
    "     XFXX XXXXXXX XXFX     ",
    "XXXXXXFXX XXXXXXX XXFXXXXXX",
    "XFFFFFFFFFFFFXFFFFFFFFFFFFX",
    "XFXXXXFXXXXXFXFXXXXXFXXXXFX",
    "XFXXXXFXXXXXFXFXXXXXFXXXXFX",
    "XSFFXXFFFFFFFPFFFFFFFXXFFSX",
    "XXXFXXFXXFXXXXXXXFXXFXXFXXX",
    "XXXFXXFXXFXXXXXXXFXXFXXFXXX",
    "XFFFFFFXXFFFFXFFFFXXFFFFFFX",
    "XFXXXXXXXXXXFXFXXXXXXXXXXFX",
    "XFXXXXXXXXXXFXFXXXXXXXXXXFX",
    "XFFFFFFFFFFFFFFFFFFFFFFFFFX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

def draw_grid(grid):
    pen.clear()
    top = 350
    left = -329

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            screen_x = left + (x*24)
            screen_y = top - (y*24)
            character = grid[y][x]

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.color("blue", "black")
                pen.shape("square")
                pen.shapesize(stretch_wid=1.2, stretch_len=1.2, outline=None)
                pen.stamp()

                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x,screen_y)

            if character == "R":
                red.goto(screen_x, screen_y)

            if character == "C":
                cyan.goto(screen_x, screen_y)

            if character == "K":
                pink.goto(screen_x, screen_y)

            if character == "O":
                orange.goto(screen_x, screen_y)

            if character == "D":
                doors.append(Door(screen_x, screen_y))

            if lives > 2 or score == 2460:
                if character == "F":
                    foods.append(Food(screen_x, screen_y))

                if character == "S":
                    super_foods.append(Super_Food(screen_x, screen_y))

class Life(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("yellow")
        self.shape("circle")
        self.shapesize(stretch_wid=1.2, stretch_len=1.2, outline=None)
        self.setposition(x, y)

life1 = Life(220, 390)
life2 = Life(260, 390)
life3 = Life(300, 390)
def lose_life():
    if lives == 2:
        life3.hideturtle()
    elif lives == 1:
        life2.hideturtle()
    elif lives == 0:
        life1.hideturtle()
    elif lives == -1:
        game_over()

def reset():
    draw_grid(grid)
    time.sleep(1)
    score_pen.clear()
    score_pen.write("Score: {}".format(score), False, align="center", font=("Courier", 24, "normal"))

def game_over():
    score_pen.clear()
    score_pen.write("Game Over", False, align="center", font=("Courier", 24, "normal"))

def level_completed():
    if score == 2460:
        score_pen.clear()
        score_pen.write("Level Complete", False, align="center", font=("Courier", 24, "normal"))

player = Player()
red = Enemy(0)
cyan = Enemy(1)
pink = Enemy(2)
orange = Enemy(3)

walls = []
foods = []
super_foods = []
doors = []
enemies = [red, cyan, pink, orange]

draw_grid(grid)

wn.listen()
wn.onkey(player.go_left, "Left")
wn.onkey(player.go_right, "Right")
wn.onkey(player.go_up, "Up")
wn.onkey(player.go_down, "Down")

wn.tracer()

player_timer = 0
enemy_timer = 0
start_moving = 0
enemy_start_timer = 300
timer = 300
while True:
    wn.update()

    for f in foods:
        f.eaten()
    for s in super_foods:
        s.eaten()

    if player_timer == 0:
        player.move()
        player_timer += 4
    else:
        player_timer -= 1

    if enemy_timer == 0:
        red.move(0, -17, 86)
        if start_moving > 0:
            cyan.move(1, -41, 14)
            for d in doors:
                d.goto(1000, 1000)
        if start_moving > 1:
            pink.move(2, -17, 14)
        if start_moving > 2:
            orange.move(3, 7, -14)
        enemy_timer += 3
    else:
        enemy_timer -= 1


    if enemy_start_timer > -1:
        enemy_start_timer -= 1
    if enemy_start_timer == 200:
        start_moving += 1
    elif enemy_start_timer == 100:
        start_moving += 1
    elif enemy_start_timer == 0:
        start_moving += 1

    if eaten == 1:
        timer -= 1
        if timer < 0:
            eaten = 0
            timer = 300

    level_completed()



wn.mainloop()