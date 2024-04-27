import turtle as t
import random

t.colormode(255)

tim = t.Turtle()


## 360 / number of sides

angle_distatnce = 20
directions = [0,90,180,270]
tim.speed("fastest")
tim.pensize(3)

def draw_spirogragh(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

draw_spirogragh(angle_distatnce)














screen = t.Screen()
screen.exitonclick()