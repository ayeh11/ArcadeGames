import turtle
import time
import random

wn = turtle.Screen()
wn.title("Gravity Run")
wn.bgcolor("black")
wn.setup(800, 800)
wn.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.shapesize(stretch_wid=2, stretch_len=2, outline=None)
pen.setundobuffer(1)


class Player(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid=1.5, stretch_len=1.5, outline=None)
        self.gravity = 1
        self.x = x
        self.y = y

    def switch_gravity(self):
        self.gravity *= -1

    def collide(self):
        if grid[self.y][self.x + 1] != 0:
            grid[self.y][self.x] = 0
            self.x -= 1

    def move(self):
        if self.gravity < 0:
            if grid[self.y - 1][self.x] == 0:
                grid[self.y][self.x] = 0
                self.y -= 1
        if self.gravity > 0:
            if grid[self.y + 1][self.x] == 0:
                grid[self.y][self.x] = 0
                self.y += 1


class Obstacle(turtle.Turtle):
    def __init__(self, y):
        turtle.Turtle.__init__(self)
        self.x = 23
        self.y = y

        pattern1 = [[2, 2],
                    [2, 2],
                    [2, 2]]
        pattern2 = [[0, 2, 0, 2],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [2, 0, 2, 0]]
        pattern3 = [[0, 2, 2, 2],
                    [0, 0, 0, 0],
                    [0, 0, 2, 0],
                    [2, 0, 2, 0]]
        pattern4 = [[0, 2, 2, 2, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 2, 0, 0],
                    [2, 0, 2, 0, 2]]
        pattern5 = [[2, 0, 2, 2, 0],
                    [0, 0, 0, 2, 0],
                    [0, 2, 0, 0, 0],
                    [2, 2, 2, 0, 2]]
        pattern6 = [[2, 2, 2, 2, 0],
                    [2, 0, 0, 2, 0],
                    [2, 0, 0, 0, 0],
                    [0, 0, 2, 0, 2]]

        patterns = [pattern1, pattern2, pattern3, pattern4, pattern5, pattern6]

        self.shape = random.choice(patterns)
        self.height = len(self.shape)
        self.width = len(self.shape[0])

    def draw_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if self.shape[y][x] == 2:
                    grid[self.y + y][self.x + x] = 2

    def erase_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if self.shape[y][x] == 2:
                    grid[self.y + y][self.x + x] = 0


grid = [
    # first 5 and last 5 columns are throwaway ones
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

]

player1 = Player(10, 6)
player2 = Player(10, 16)

obstacle_top = Obstacle(3)
obstacle_bot = Obstacle(13)

colors = ["black", "white", "grey", "red", "cyan"]


def draw_grid(grid):
    pen.clear()
    top = 385
    left = -585

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            screen_x = left + (x * 40)
            screen_y = top - (y * 40)
            color_num = grid[y][x]
            pen.color(colors[color_num])
            pen.goto(screen_x, screen_y)
            pen.stamp()


# draw players
grid[player1.y][player1.x] = 3
grid[player2.y][player2.x] = 4

draw_grid(grid)

wn.listen()
wn.onkey(player1.switch_gravity, "w")
wn.onkey(player2.switch_gravity, "Up")

timer = 0
timer2 = 0
while True:
    wn.update()

    player1.move()
    player2.move()

    # obstacle off screen
    if obstacle_top.x < 5 - obstacle_top.width:
        obstacle_top = Obstacle(3)
        grid[player1.y][player1.x] = 0
        player1.x += 1
    else:
        # move obstacle
        if timer == 0:
            player1.collide()
            obstacle_top.erase_shape(grid)
            obstacle_top.x -= 1
            obstacle_top.draw_shape(grid)
            timer += 2
        else:
            timer -= 1

    if obstacle_bot.x < 5 - obstacle_bot.width:
        obstacle_bot = Obstacle(13)
        grid[player2.y][player2.x] = 0
        player2.x += 1
    else:
        # move obstacle
        if timer2 == 0:
            player2.collide()
            obstacle_bot.erase_shape(grid)
            obstacle_bot.x -= 1
            obstacle_bot.draw_shape(grid)
            timer2 += 2
        else:
            timer2 -= 1

    grid[player1.y][player1.x] = 3
    grid[player2.y][player2.x] = 4

    draw_grid(grid)


wn.mainloop()
