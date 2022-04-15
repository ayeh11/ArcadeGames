import turtle
import time
import random
import sys

wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("white")
wn.setup(550, 550)
wn.tracer(0)

score = 0
high_score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("black")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0,240)
score_pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


delay = .1

class Player():
    def __init__(self):
        self.x = 12
        self.y = 12

        self.direction = "stop"

    def go_up(self, grid):
        if self.direction != "down":
            self.direction = "up"

    def go_down(self, grid):
        if self.direction != "up":
            self.direction = "down"

    def go_left(self, grid):
        if self.direction != "right":
            self.direction = "left"

    def go_right(self, grid):
        if self.direction != "left":
            self.direction = "right"

    def move(self, grid):
        if self.direction == "up":
            checker_grid(grid)
            if self.y - 1 > -1:
                self.y -= 1
            else:
                restart_game(grid)
            grid[self.y][self.x] = 2
            self.move_segment(grid, 0, 1)

        if self.direction == "down":
            checker_grid(grid)
            if self.y + 1 < 24:
                self.y += 1
            else:
                restart_game(grid)
            grid[self.y][self.x] = 2
            self.move_segment(grid, 0, -1)

        if self.direction == "left":
            checker_grid(grid)
            if self.x - 1 > -1:
                self.x -= 1
            else:
                restart_game(grid)
            grid[self.y][self.x] = 2
            self.move_segment(grid, 1, 0)

        if self.direction == "right":
            checker_grid(grid)
            if self.x + 1 < 24:
                self.x += 1
            else:
                restart_game(grid)
            grid[self.y][self.x] = 2
            self.move_segment(grid, -1, 0)

    def move_segment(self, grid, to_x, to_y):
        if(len(segments) > 0):
            segments[0].x = self.x + to_x
            segments[0].y = self.y + to_y
            # grid[segments[0].y][segments[0].x] = 4

        if (len(segments) > 1):
            for s in range(len(segments)-1, 0, -1):
                segments[s].move_segments(grid, s)


segments = []
class Segment():
    def __init__(self):
        self.x = 0
        self.y = 0

    def move_segments(self, grid, s):
        self.x = segments[s-1].x
        self.y = segments[s-1].y
        grid[segments[s].y][segments[s].x] = 4


def add_segment(grid):
    new_s = Segment()
    segments.append(new_s)

class Food():
    def __init__(self):
        self.x = random.randint(0, 23)
        self.y = random.randint(0, 23)

    def new_pos(self, grid):
        self.x = random.randint(0, 23)
        self.y = random.randint(0, 23)
        if (self.x, self.y) not in segments:
            grid[self.y][self.x] = 3

grid =[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.setundobuffer(1)

player = Player()
food = Food()

def eat(grid):
    global score
    global high_score

    if player.x == food.x and player.y == food.y:
        food.new_pos(grid)
        add_segment(grid)

        score += 10
        score_pen.clear()
        score_pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        if score > high_score:
            high_score = score
        score_pen.clear()
        score_pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


def checker_grid(grid):
    for y in range(len(grid)-1, -1, -2):
        for x in range(len(grid[0])-1, -1, -2):
            grid[y][x] = 1
    for y in range(len(grid)-2, -1, -2):
        for x in range(len(grid[0])-2, -1, -2):
            grid[y][x] = 1
    for y in range(len(grid)-1, -1, -2):
        for x in range(len(grid[0])-2, -1, -2):
            grid[y][x] = 0
    for y in range(len(grid)-2, -1, -2):
        for x in range(len(grid[0])-1, -1, -2):
            grid[y][x] = 0
    grid[food.y][food.x] = 3

checker_grid(grid)
def draw_grid(pen, grid):
    pen.clear()
    top = 220
    left = -232

    colors = ["green", "darkgreen", "yellow", "red", "grey"]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            screen_x = left + (x*20)
            screen_y = top - (y*20)
            color = grid[y][x]
            pen.color(colors[color])
            pen.goto(screen_x, screen_y)
            pen.stamp()

def restart_game(grid):
    time.sleep(1)
    checker_grid(grid)
    segments.clear()

    player.x = 12
    player.y = 12
    grid[player.y][player.x] = 2
    player.direction = "stop"

    global score
    score = 0
    score_pen.clear()
    score_pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

grid[player.y][player.x] = 2
draw_grid(pen, grid)

wn.listen()
wn.onkeypress(lambda: player.go_up(grid), "Up")
wn.onkeypress(lambda: player.go_down(grid), "Down")
wn.onkeypress(lambda: player.go_left(grid), "Left")
wn.onkeypress(lambda: player.go_right(grid), "Right")

player = Player()
while True:
    wn.update()

    player.move(grid)
    eat(grid)
    for s in segments:
        if s.x == player.x and s.y == player.y:
            restart_game(grid)

    draw_grid(pen, grid)

    time.sleep(delay)

wn.mainloop()