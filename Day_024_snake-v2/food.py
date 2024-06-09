from turtle import Turtle
import random

BOUND_LIMIT = 260

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randrange(-BOUND_LIMIT, BOUND_LIMIT, 20)
        random_y = random.randrange(-BOUND_LIMIT, BOUND_LIMIT, 20)
        self.setposition(random_x, random_y)