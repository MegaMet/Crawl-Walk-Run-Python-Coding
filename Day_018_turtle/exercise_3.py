from turtle import Turtle, Screen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tim = Turtle()


## 360 / number of sides

travel_distatnce = 50

tim.penup()
tim.sety(200)
tim.setx(travel_distatnce/2)
tim.pendown()

for i in range(3, 20):
    angle = 360 / i
    tim.color(random.choice(colours))

    for s in range(i):
        tim.right(angle)
        tim.forward(travel_distatnce)












screen = Screen()
screen.exitonclick()