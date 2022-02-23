from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.color('black')
        self.update()

    def update(self):
        self.clear()
        self.goto(-270,250)
        self.write(f"Level: {self.score}", align='left', font=FONT)

    def level_up(self):
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=FONT)