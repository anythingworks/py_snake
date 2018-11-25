import turtle
import time
import random
import os

score_file = open('resources/score', 'r')
all_time_high_score = int(score_file.read())
current_all_time_high_score = all_time_high_score
score_file.close()
# score_file = open('resources/score', 'w')

delay = .07
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


# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("black")
food.penup()
food.goto(0, 100)

# pen
pen = turtle.Turtle()
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0 All Time High Score: 0", align="center", font=("courier", 11, "normal"))

# score
score = 0
high_score = 0
segments = []
next_heading = 0
next_direction = "stop"
paused = False
waiting_to_move = False


# functions

opposing_direction = {
    'up': 'down',
    'down': 'up',
    'left': 'right',
    'right': 'left',
    'stop': 'stop'
}




def move_up():
    global waiting_to_move
    if not waiting_to_move and head.direction != "down":
        head.direction = "up"
        head.setheading(90)
        waiting_to_move = True

def move_down():
    global waiting_to_move
    if not waiting_to_move and head.direction != "up":
        head.direction = "down"
        head.setheading(270)
        waiting_to_move = True

def move_left():
    global waiting_to_move
    if not waiting_to_move and head.direction != "right":
        head.direction = "left"
        head.setheading(180)
        waiting_to_move = True

def move_right():
    global waiting_to_move
    if not waiting_to_move and head.direction != "left":
        head.direction = "right"
        head.setheading(0)
        waiting_to_move = True

def move_stop():
    head.direction = "stop"

# functions

def pause():
    global paused
    if not paused:
        paused = True
    else:
        paused = False

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
    global waiting_to_move
    if not paused:
        if len(segments) > 0:
            for index in range(len(segments) - 1, 0, -1):
                xs = segments[index - 1].xcor()
                ys = segments[index - 1].ycor()
                segments[index].goto(xs, ys)
            segments[0].goto(head.xcor(), head.ycor())
        move_head()
        waiting_to_move = False

def detect_collision():
    global score

    def new_ahs():
        global all_time_high_score, current_all_time_high_score
        if current_all_time_high_score > all_time_high_score:
            score_file = open('resources/score', 'w')
            score_file.write(str(current_all_time_high_score))

    def reset_segments():
        global next_direction
        head.goto(0, 0)
        head.direction = "stop"
        next_direction = "stop"

        # hide segments
        for segment in segments:
            # segment.goto(1000, 1000)
            # Delete the turtle trail (if any)
            segment.clear()
            # Hide the turtle
            segment.ht()
            # Delete the turtle object
            del segment
        segments.clear( )

    # check for collision with segments
    for segment in segments:
        if segment.distance(head) < 20:
            new_ahs()
            time.sleep(1)
            reset_segments()
            score = 0


    # check for collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        new_ahs()
        time.sleep(1)
        reset_segments()
        score = 0
    pen.clear()
    pen.write("Score: {}  High_Score: {}  All Time High Score {} ".format(score, high_score, current_all_time_high_score), align = "center", font=("courier", 11, "normal"))


def detect_food():
    global score, high_score, current_all_time_high_score
    # check for collision with the food
    # global points
    if head.distance(food) < 20:
        # move the food to random spot on screen
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        add_segment()
        # increase score

        score += 1
        if score > high_score:
            high_score = score
        if high_score > current_all_time_high_score:
            current_all_time_high_score = high_score

        pen.clear()
        pen.write("Score: {}  High_Score: {}  All Time High Score {} ".format(score, high_score, current_all_time_high_score), align = "center", font=("courier", 11, "normal"))

# keybindings
window.listen()
window.onkeypress(move_up, "w")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")
window.onkeypress(move_down, "s")

window.onkeypress(move_up, "Up")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.onkeypress(move_down, "Down")

window.onkeypress(pause, "space")

# main game loop

while True:
    window.update()
    detect_food()
    move()
    detect_collision()


    time.sleep(delay)


