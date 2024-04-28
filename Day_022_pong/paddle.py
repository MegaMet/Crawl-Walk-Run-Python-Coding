from turtle import Turtle

MOVEMENT_AMOUNT = 40

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        self.color("white")
        self.penup()
        self.setposition(position)
        # self.is_moving = False

    def move_paddle_up(self):
        new_y = self.ycor() + MOVEMENT_AMOUNT
        self.goto(self.xcor(), new_y)
    def move_paddle_down(self):
        new_y = self.ycor() - MOVEMENT_AMOUNT
        self.goto(self.xcor(), new_y)


