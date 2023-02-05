from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.write(f"Level: {self.level}",font = FONT)

    def next_level(self):
        self.level += 1
        self.write(f"Level: {self.level}",font = FONT)

    def end(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", align = "center",  font = FONT)




