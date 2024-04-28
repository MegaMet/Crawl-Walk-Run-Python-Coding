#Turtle Race
from turtle import Turtle, Screen
import random

turtle_list = []
screen = Screen()
screen.setup(500, 400)
colors =["red", "orange", "yellow", "blue", "purple", "green"]

#ask user to make a bet
user_bet = screen.textinput(title="Place your bet", prompt="Place your bet. Red, Yellow, Blue, Purple, Green, Orange:").lower()

y_position = -125

for i in range(len(colors)):
    turtle = Turtle("turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.setposition(-230, y_position)
    turtle_list.append(turtle)

    y_position += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for t in turtle_list:
        t.forward(random.randint(0, 10))
        if t.xcor() > 230:
            winning_color = t.pencolor()
            if (winning_color == user_bet):
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")
            is_race_on = False




screen.exitonclick()