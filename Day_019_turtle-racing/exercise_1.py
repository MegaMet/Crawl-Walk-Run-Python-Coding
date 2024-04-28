#Etch-A-Sketch

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
travel_amount = 10
rotation_amount = 10

def move_forward():
    tim.forward(travel_amount)

def move_backwards():
    tim.backward(travel_amount)

def rot_clockwise():
    tim.setheading(tim.heading() + rotation_amount)

def rot_counterclockwise():
    tim.setheading(tim.heading() - rotation_amount)

def clear():
    tim.reset()

print(tim.position())

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=rot_clockwise)
screen.onkey(key="a", fun=rot_counterclockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()