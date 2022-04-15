import turtle
import random
import time
import sys

dis = 50
# window
wn = turtle.Screen()
wn.title("Asteroids")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("blue")
border_pen.penup()
border_pen.setposition(-200,-200)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(400)
    border_pen.lt(90)
border_pen.right(-90)
for x in range(9):
    x *= dis
    border_pen.penup()
    border_pen.setposition(-200 + x,-200)
    border_pen.pendown()
    border_pen.fd(400)
border_pen.right(90)
for y in range(9):
    y *= dis
    border_pen.penup()
    border_pen.setposition(-200,-200 + y)
    border_pen.pendown()
    border_pen.fd(400)

border_pen.hideturtle()

# player
player = turtle.Turtle()
player.color("white")
player.shape("triangle")
player.speed(0)
player.penup()
player.setposition(0,0)
player.setheading(90)

moved = 0

# enemy
number_of_enemies = 15
enemies = []
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("green")
    enemy.shape("circle")
    enemy.speed(0)
    enemy.penup()

    x = random.randint(-4, 4)
    y = random.randint(-4, 4)
    if x == 0 and y == 0:
        x += 1
        y += 1
    x *= dis
    y *= dis
    pos = (x, y)
    enemy.setposition(pos)

moves = 0
# pen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-190,210)
scorestring = "Moves: {}".format(moves)
score_pen.write(scorestring, False, align="center", font=("Arial", 14, "normal"))
score_pen.hideturtle()

def move_left():
    d = player.heading()
    d += 90
    player.setheading(d)

def move_right():
    d = player.heading()
    d -= 90
    player.setheading(d)

def move_fd():
    global moved
    global moves
    h = player.heading()/90
    num = h % 4
    if player.xcor() < 195:
        if num == 0:
            x = player.xcor()
            x += dis
            player.setx(x)
            moved += 1
            moves += 1

    if player.xcor() > -195:
        if num == 2:
            x = player.xcor()
            x -= dis
            player.setx(x)
            moved += 1
            moves += 1

    if player.ycor() < 195:
        if num == 1:
            y = player.ycor()
            y += dis
            player.sety(y)
            moved += 1
            moves += 1

    if player.ycor() > -195:
        if num == 3:
            y = player.ycor()
            y -= dis
            player.sety(y)
            moved += 1
            moves += 1

def enemy_move(r):
    #right
    if r == 0:
        x = enemy.xcor()
        x += dis
        enemy.setx(x)
    #up
    if r == 1:
        y = enemy.ycor()
        y += dis
        enemy.sety(y)
    #left
    if r == 2:
        x = enemy.xcor()
        x -= dis
        enemy.setx(x)
    #down
    if r == 3:
        y = enemy.ycor()
        y -= dis
        enemy.sety(y)

def game_over():
    score_pen.clear()
    scorestring = "Game Over"
    score_pen.goto(0, 210)
    score_pen.write(scorestring, False, align="center", font=("Arial", 30, "normal"))
    time.sleep(3)
    sys.exit(0)

wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(move_fd, "Up")

while True:
    wn.update()

    if moved % 2 != 0:
        for enemy in enemies:
            r = random.randint(0, 3)
            enemy_move(r)
            if enemy.xcor() > 200:
                enemy.setx(200)
            if enemy.xcor() < -200:
                enemy.setx(-200)
            if enemy.ycor() > 200:
                enemy.sety(200)
            if enemy.ycor() < -200:
                enemy.sety(-200)

            moved += 1

            scorestring = "Moves: {}".format(moves)
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

            if player.distance(enemy) == 0:
                game_over()





wn.mainloop()
