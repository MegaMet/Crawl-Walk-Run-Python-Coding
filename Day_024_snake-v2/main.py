from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Scoreboard

BOUND_LIMIT = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key= "Up", fun= snake.up)
screen.onkey(key= "Down", fun= snake.down)
screen.onkey(key= "Left", fun= snake.left)
screen.onkey(key= "Right", fun= snake.right)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #dectect collision with wall
    if snake.head.xcor() > BOUND_LIMIT or snake.head.xcor() < -BOUND_LIMIT or snake.head.ycor() > BOUND_LIMIT or snake.head.ycor() < -BOUND_LIMIT:
        snake.reset()
        scoreboard.reset()

    #dectect collision with wall
    for s in snake.snake_seg[1:]:
        if snake.head.distance(s) < 10:
            snake.reset()
            scoreboard.reset()








screen.exitonclick()