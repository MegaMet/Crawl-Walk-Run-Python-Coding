ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
SCORE_FILE_LOCATION = "Snake_score\score.txt"

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open(SCORE_FILE_LOCATION) as file:
            contents = file.read()
            self.high_score = int(contents)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align= ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(SCORE_FILE_LOCATION, mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()
        # self.setposition(0, 0)
        # self.write(f"GAME OVER", align= ALIGNMENT, font= FONT)