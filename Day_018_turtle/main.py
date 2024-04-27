import turtle as t
import colorgram as cg
import random

t.colormode(255)

## get a list of colors using colorgram
rgb_color = []
image_file = "Kirby-and-the-Forgotten-Land-art-3830431384.jpg"
colors = cg.extract(image_file, 10)
for c in colors:
    r = c.rgb.r
    g = c.rgb.g
    b = c.rgb.b

    new_color = (r,g,b)

    rgb_color.append(new_color)


tim = t.Turtle()
travel_distance = 50
repeat = 11
tim.penup()
tim.speed("fastest")
tim.hideturtle()

offsetx = (travel_distance * repeat) / 2
offsety = (travel_distance * repeat) / 2

for x in range(repeat):
    tim.setx((x * travel_distance) - offsetx)
    for y in range(repeat):

        tim.sety((y * travel_distance) - offsety)
        tim.dot(20, random.choice(rgb_color))









screen = t.Screen()
screen.exitonclick()