from turtle import Turtle

BALL_SPEED = 4
BALL_SPEED_INCREASE = 1
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

        self.xspeed = BALL_SPEED
        self.yspeed = BALL_SPEED

    def move(self):
        new_x = self.xcor() + self.xspeed
        new_y = self.ycor() + self.yspeed
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.yspeed *= -1

    def bounce_x(self):
        self.xspeed *= -1
        self.xspeed *= 1.1
        self.yspeed *= 1.1



    def reset_ball(self):
        self.setposition(0,0)
        self.xspeed = BALL_SPEED * 0.9
        self.yspeed = BALL_SPEED * 0.9
        self.bounce_x()