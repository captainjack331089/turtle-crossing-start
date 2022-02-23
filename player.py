from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.setposition(0,-300)


    def move(self):
        self.forward(MOVE_DISTANCE)

    def origin(self):
        self.goto(0,-300)