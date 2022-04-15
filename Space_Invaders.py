import turtle
import os
import math
import time
import random

# Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

score = 0

# pen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

player_speed = 15

enemy_speed = 2
number_of_enemies = 5
enemies = []
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    # enemy
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)


# weapon
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(.5, .5)
bullet.hideturtle()

bullet_speed = 20

#bullet states
    #ready to fire and bullet is firing
bullet_state = "ready"


def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #any changes in this function are public to everything else
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"

    # move the bullet to above player
    x = player.xcor()
    y = player.ycor() + 10
    bullet.setposition(x,y)
    bullet.showturtle()

# keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# main game loop
while True:

    for enemy in enemies:
        # move enemy
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # enemy reverse and moves all enemies down
        if enemy.xcor() > 280 or enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemy_speed *= -1

        # check collision
        if bullet.distance(enemy) < 15:
            # Reset bullet
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.setposition(0, -400)
            # reset enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # update score
            score += 10
            scorestring = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))


        if enemy.distance(player) < 20:
            player.hideturtle()
            enemy.hideturtle()
            break

    # move the bullet
    if(bullet_state == "fire"):
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)


    # check border for bullet
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"





wn.mainloop()