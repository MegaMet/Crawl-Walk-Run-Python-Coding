from turtle import Screen
from paddle import Paddle
from ball import  Ball
from score_board import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(key= "Up", fun= r_paddle.move_paddle_up)
screen.onkey(key= "Down", fun= r_paddle.move_paddle_down)

screen.onkey(key= "w", fun= l_paddle.move_paddle_up)
screen.onkey(key= "s", fun= l_paddle.move_paddle_down)


game_is_on = True

while game_is_on:
    time.sleep(0.001)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    #detect collision with paddles
    if (ball.distance(r_paddle) < 45 and ball.xcor() > 340) or (ball.distance(l_paddle) < 45 and ball.xcor() < -340):
        ball.bounce_x()

    #detect if right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    #detect if right paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()

screen.exitonclick()