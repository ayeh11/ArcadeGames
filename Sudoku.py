import turtle
import time
import random

wn = turtle.Screen()
wn.title("Sudoku")
wn.bgcolor("white")
wn.setup(500, 700)
wn.tracer(0)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape("square")
        self.color("black", "white")
        self.shapesize(stretch_wid=2, stretch_len=2, outline=None)
        self.setundobuffer(1)

# grid
pen = Pen()
pen.hideturtle()

# board
pen2 = Pen()
pen2.hideturtle()

# numbers
pen3 = Pen()
pen3.hideturtle()


top = 190
left = -160

grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

board = [[0, 0, 2, 9, 0, 0, 0, 0, 3],
         [7, 0, 4, 0, 2, 0, 0, 5, 0],
         [0, 0, 0, 0, 7, 5, 0, 0, 2],
         [0, 0, 0, 0, 0, 7, 2, 4, 0],
         [0, 0, 0, 2, 0, 4, 0, 0, 0],
         [0, 2, 9, 6, 0, 0, 0, 0, 0],
         [6, 0, 0, 1, 3, 0, 0, 0, 0],
         [0, 9, 0, 0, 5, 0, 7, 0, 4],
         [5, 0, 0, 0, 0, 2, 9, 0, 0]]

numbers = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]

def highlight(x, y):
    if y > -150:
        for b in range(len(grid)):
            for a in range(len(grid[b])):
                if grid[b][a] == 1:
                    grid[b][a] = 0
                else:
                    grid_x = round((x - left) / 40)
                    grid_y = round((y - top) / -40)
                    grid[grid_y][grid_x] = 1
    else:
        grid_x = round((x - left) / 40)
        grid_y = round((y + 250) / -40)
        num = numbers[grid_y][grid_x]
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    board[y][x] = num
                    if not check(num, x, y) and num != 0:
                        grid[y][x] = 3

    draw_grid()
    draw_board()

colors = ["white", "lightblue", "lightgreen", "pink"]
def draw_grid():
    pen.clear()

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            screen_x = left + (x*40)
            screen_y = top - (y*40)
            color = grid[y][x]
            pen.color("black", colors[color])
            pen.goto(screen_x, screen_y)
            pen.stamp()

    draw((-60, 210), 90)
    draw((60, 210), 0)
    draw((-180, -30), 270)
    draw((-180, 90), 0)

# thick lines on grid
def draw(pos, angle):
    pen.pensize(4)
    pen.setpos(pos)
    pen.pendown()
    pen.right(angle)
    pen.fd(360)
    pen.penup()

def draw_board():
    for y in range(len(board)):
        for x in range(len(board[y])):
            screen_x = left + (x*40)
            screen_y = top - (y*40)
            pen2.goto(screen_x, screen_y - 10)

            grid_x = round((screen_x - left) / 40)
            grid_y = round((screen_y - top) / -40)
            num = board[grid_y][grid_x]
            if num != 0:
                pen2.write("{}".format(num), align="center", font=("Courier", 24, "normal"))

def draw_numbers():
    for x in range(len(numbers[0])):
        screen_x = left + (x*40)
        screen_y = -250
        pen3.goto(screen_x, screen_y)

        grid_x = round((screen_x - left) / 40)
        num = numbers[0][grid_x]
        if num != 0:
            pen3.write("{}".format(num), align="center", font=("Courier", 24, "normal"))

def check(num, row, col):
    # check columns
    for y in range(len(board)):
        if board[y][row] == num and y != col:
            return False

    # check rows
    for x in range(len(board[0])):
        if board[col][x] == num and x != row:
            return False

    # check box
    box_x = row // 3
    box_y = col // 3

    for y in range(box_y*3, box_y*3 + 3):
        for x in range(box_x*3, box_x*3 + 3):
            if board[y][x] == num and x != row and y != col:
                return False

    return True

def solve():
    pos = find_zeros()
    if pos:
        row, col = pos
    else:
        return True

    for i in range(1, 10):
        if check(i, row, col):
            board[col][row] = i

            if solve():
                return True

            board[col][row] = 0

    return False

def find_zeros():
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 0:
                return(x, y)

    return None

def finish():
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] != 0 and grid[y][x] != 3:
                print("finish")

draw_grid()
draw_board()
draw_numbers()

wn.tracer(0)

wn.listen()
wn.onclick(highlight)
wn.onkeypress(solve, "space")

while True:
    wn.update()



wn.mainloop()