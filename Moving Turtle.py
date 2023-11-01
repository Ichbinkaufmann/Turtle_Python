import turtle as t
import random as ra

root = t
root.title("Moving Turtle")

def inside_window():
    left_limit = (-t.window_width() / 2) + 100
    right_limit = (t.window_width() / 2) - 100
    top_limit = (t.window_height() / 2) - 300
    bottom_limit = (-t.window_height() / 2) + 100
    (x,y) = t.pos()
    inside = left_limit < x < right_limit and bottom_limit < y < top_limit
    return inside


def turtle_activity():
    if inside_window():
            t.write("Hey, I'm here :D", align="center", font=("White", 25, "italic"))
    else:
            t.write("Oops Turtle was lost for a moment XD", align="center", font=("White", 25, "italic"))

def move_turtle():
    if inside_window():
            angle = ra.randint(0,180)
            t.right(angle)
            t.forward(200)
            t.clear()

    else:
            t.backward(200)
            t.clear()

t.shape('turtle')
t.shapesize(8)
t.fillcolor('red')
t.bgcolor('white')
t.speed('slow')
t.pensize(2)


while True:
    move_turtle(),
    turtle_activity()
