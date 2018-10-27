import turtle
import time
import random


delay = .08
global_increment = 20
# delay = 0.003

# screen setup
window = turtle.Screen()
window.title("slither.io")
window.bgcolor("white")
window.setup(width=600, height=600)
window.tracer(0)  # turns off screen update

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"


#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("black")
food.penup()
food.goto(0, 100)

segments = []

# functions

def move_up():
    head.direction = "up"
    head.setheading(90)

def move_down():
    head.direction = "down"
    head.setheading(270)

def move_left():
    head.direction = "left"
    head.setheading(180)

def move_right():
    head.direction = "right"
    head.setheading(0)

def move_stop():
    head.direction = "stop"

def pen_down():
    head.pendown()

def pen_up():
    head.penup()


def move_head():
    movement_increment = global_increment
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + movement_increment)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - movement_increment)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - movement_increment)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + movement_increment)

# add a new segment
def add_segment():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape('square')
    new_segment.color('grey')
    new_segment.penup()
    segments.append(new_segment)

def move():
    x = head.xcor()
    y = head.ycor()
    move_head()
    if len(segments) > 0:
        for index in range(len(segments) - 1, 0, -1):
            xs = segments[index - 1].xcor()
            ys = segments[index - 1].ycor()
            segments[index].goto(xs, ys)
        segments[0].goto(x, y)

# def move():
#     move_head()
#     move_tail()

#keybindings
window.listen()
window.onkeypress(move_up, "w")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")
window.onkeypress(move_down, "s")

window.onkeypress(move_up, "Up")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.onkeypress(move_down, "Down")

window.onkeypress(move_stop, "space")
window.onkeypress(pen_down, "e")
window.onkeypress(pen_up, "f")

# main game loop
while True:
    window.update()

# check for collision with the food
    if head.distance(food) < 20:
        #move the food to random spot on screen
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        add_segment()

    move()


    time.sleep(delay)

window.mainloop()
