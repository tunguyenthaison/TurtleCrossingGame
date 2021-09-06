from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level = 0
        self.goto(-260, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.level += 1
        self.write("Level {}".format(self.level), False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER, YOU LOST!", False, align=ALIGNMENT, font=FONT)
