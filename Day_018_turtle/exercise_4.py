import turtle as t
import random

t.colormode(255)

tim = t.Turtle()


## 360 / number of sides

travel_distatnce = 20
directions = [0,90,180,270]

for i in range(10):
    num = random.randrange(-200, 200, travel_distatnce)
    print(num)

tim.penup()
tim.pensize(5)
tim.speed(10)
tim.sety(random.randrange(-200, 200, travel_distatnce))
tim.setx(random.randrange(-200, 200, travel_distatnce))
tim.pendown()

## Experimenting with using a dictionary and calling a random function
# def turn_left():
#     tim.left(90)
#
# def turn_right():
#     tim.right(90)
#
# direction = [turn_right, turn_left]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

for i in range(100):
    #random.choice(direction)()
    tim.setheading(random.choice(directions))
    tim.color(random_color())
    tim.forward(travel_distatnce)













screen = t.Screen()
screen.exitonclick()