import turtle
import time


delay = 0.003

# screen setup
window = turtle.Screen()
window.title("slither.io")
window.bgcolor("#d6629c")
# window.bgcolor("#b70303")
window.setup(width=600, height=600)
window.tracer(0)  # turns off screen update

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("triangle")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"


# function
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


def move():
    movement_increment = 1

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

    move()

    time.sleep(delay)

window.mainloop()
