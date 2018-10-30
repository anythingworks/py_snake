import turtle
import time
import random


delay = 0.2
global_increment = 20

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
next_heading = 0
next_direction = "stop"

# functions

opposing_direction = {
    'up': 'down',
    'down': 'up',
    'left': 'right',
    'right': 'left',
    'stop': 'stop'
}




def move_up():
    global next_direction, next_heading
    next_direction = "up"
    next_heading = 90


def move_down():
    global next_direction, next_heading
    next_direction = "down"
    next_heading = 270


def move_left():
    global next_direction, next_heading
    next_direction = "left"
    next_heading = 180


def move_right():
    global next_direction, next_heading
    next_direction = "right"
    next_heading = 0

def move_stop():
    head.direction = "stop"

def pen_down():
    head.pendown()

def pen_up():
    head.penup()


# add a new segment
def add_segment():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape('square')
    new_segment.color('grey')
    new_segment.penup()
    segments.append(new_segment)


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


def move():
    global next_direction, next_heading
    if next_direction != opposing_direction[head.direction]:
        head.direction = next_direction
        head.setheading(next_heading)
    if len(segments) > 0:
        for index in range(len(segments) - 1, 0, -1):
            xs = segments[index - 1].xcor()
            ys = segments[index - 1].ycor()
            segments[index].goto(xs, ys)
        segments[0].goto(head.xcor(), head.ycor())
    move_head()

def detect_collision():
    def reset_segments():
        head.goto(0, 0)
        head.direction = "stop"
        # hide segments
        for segment in segments:
            # segment.goto(1000, 1000)
            # Delete the turtle trail (if any)
            segment.clear()
            # Hide the turtle
            segment.ht()
            # Delete the turtle object
            del segment
        segments.clear()

    # check for collision with segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            reset_segments()

    # check for collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        reset_segments()

def detect_food():
    # check for collision with the food
    if head.distance(food) < 20:
        # move the food to random spot on screen
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        add_segment()

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

    detect_food()
    move()
    detect_collision()

    time.sleep(delay)
    print(head.direction)


