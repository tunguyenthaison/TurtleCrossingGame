from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(UP)
        self.reset_pos()

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def reach_finish(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False

    def reset_pos(self):
        self.goto(STARTING_POSITION)





