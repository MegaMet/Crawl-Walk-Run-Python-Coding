from turtle import Turtle
STARTING_POSITION = [(0,0), (-20, 0), (-40, 0)]
SNAKE_SEG_LENGTH = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_seg = []
        self.create_snake()
        self.head = self.snake_seg[0]

    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_seg(i)

    def add_seg(self, position):
        seg = Turtle("square")
        seg.color("white")
        seg.penup()
        seg.setposition(position)

        self.snake_seg.append(seg)

    def extend(self):
        self.add_seg(self.snake_seg[-1].position())

    def move(self):
        for s in range(len(self.snake_seg) - 1, 0, -1):
            new_x = self.snake_seg[s - 1].xcor()
            new_y = self.snake_seg[s - 1].ycor()
            self.snake_seg[s].goto(new_x, new_y)

        self.head.forward(SNAKE_SEG_LENGTH)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

