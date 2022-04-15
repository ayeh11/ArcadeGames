import turtle
import random
import sys
import time

wn = turtle.Screen()
wn.title("Car Lights")
wn.bgcolor("black")
wn.setup(500, 700)
wn.tracer(0)

bg_road = turtle.Turtle()
bg_road.color("grey")
bg_road.shape("square")
bg_road.shapesize(stretch_len=10, stretch_wid=35, outline=None)

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("black")
score_pen.penup()
score_pen.setposition(0, 300)
score_pen.hideturtle()

num_color = 0
num_colors = []

score = 0

class Car(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_len=2, stretch_wid=2, outline=None)
        self.run_once = 0
        self.color("red")

    def main(self):
        for i in lines:
            if abs(self.ycor() - i.ycor()) < 5:
                car_color(self)

    def go_left(self):
        move_to_x = car.xcor() - 55
        if move_to_x > -70:
            self.goto(move_to_x, 0)

    def go_right(self):
        move_to_x = car.xcor() + 55
        if move_to_x < 70:
            self.goto(move_to_x, 0)

def car_color(obj):
    color_c = ["red", "yellow", "lightgreen"]
    c = len(num_colors) - 2
    c2 = num_colors[c]
    obj.color(color_c[c2])

lights = []
color = ["red", "yellow", "lightgreen"]
def light_color():
    if len(lights) % 3 == 0:
        return (color[0])
    if len(lights) % 3 == 1:
        return (color[1])
    if len(lights) % 3 == 2:
        return (color[2])

class Light(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_len=2, stretch_wid=2, outline=None)
        self.color(light_color())
        self.setpos(Light.set_pos(self))

    def main(self):
        global score
        if abs(self.xcor() - car.xcor()) == 0 and abs(self.ycor() - car.ycor()) < 2:
            hit_color = self.color()
            if str(hit_color) == str(Car.color(car)):
                score_pen.clear()
                score += 1
                self.hideturtle()
            else:
                game_over()

    def set_pos(self):
        if len(lights) % 3 == 0:
            return (-55, 450)
        if len(lights) % 3 == 1:
            return (0, 450)
        if len(lights) % 3 == 2:
            return (55, 450)

    def move(self):
        self.sety(self.ycor() - 5)


lines = []
class Line(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.penup()
        self.speed(0)
        self.setpos(0, 350)
        self.shapesize(stretch_len=10, stretch_wid=.5, outline=None)
        color_c = ["red", "yellow", "lightgreen"]
        self.color(color_c[num_color])

    def move(self):
        self.sety(self.ycor() - 5)


def spawner():
    for i in range(3):
        lights.append(Light())

def score_sys():
    scorestring = "Score: {}".format(score)
    score_pen.write(scorestring, False, align="center", font=("Arial", 30, "normal"))

def game_over():
    score_pen.clear()
    scorestring = "Game Over"
    score_pen.write(scorestring, False, align="center", font=("Arial", 30, "normal"))
    time.sleep(3)
    sys.exit(0)

car = Car()
light = Light()
light.hideturtle()
line = Line()
line.hideturtle()

turtle.listen()
turtle.onkey(car.go_left, "Left")
turtle.onkey(car.go_right, "Right")
turtle.tracer(0)

timer = 0
timer2 = 0

dec_timer = 50
dec_timer2 = 300
timer3 = 0
while True:
    wn.update()

    Car.main(car)
    score_sys()
    for l in lights:
        Light.move(l)
        Light.main(l)
    for i in lines:
        Line.move(i)

    if timer == 0:
        spawner()
        random.shuffle(color)
        timer = dec_timer
    else:
        timer -= 1

    if timer2 == 0:
        for i in range(1):
            lines.append(Line())
        lines[0].setpos(1000,-1000)
        num_color = random.randint(0, 2)
        num_colors.append(num_color)
        timer2 = dec_timer2
    else:
        timer2 -= 1

    if timer3 == 0:
        if dec_timer > 25:
            dec_timer -= 1
            dec_timer2 -= 6
            timer3 = 100
        else:
            dec_timer = 25
            dec_timer2 = 150
    else:
        timer3 -= 1




wn.mainloop()