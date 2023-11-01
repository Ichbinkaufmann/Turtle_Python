import turtle as t
import random as ra


def inside_window():
    left_limit = (-t.window_width() / 2) + 100
    right_limit = (t.window_width() / 2) - 100
    top_limit = (t.window_height() / 2) - 100
    bottom_limit = (-t.window_height() / 2) + 100
    (x,y) = t.pos()
    inside = left_limit < x < right_limit and bottom_limit < y < top_limit
    return inside
    
def move_turtle():
    if inside_window():
            angle = ra.randint(0,180)
            t.right(angle)
            t.forward(200)
            print("Turtle is Exploring")

    else:
            t.backward(200)
            print("Oops! Turtle was lost for a moment XD")

t.shape('turtle')
t.fillcolor('red')
t.bgcolor('black')
t.speed('slow')
t.pensize(2)


while True:
    move_turtle()
