from turtle import Turtle
POINTS = 1
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += POINTS
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game over", align=ALIGNMENT, font=FONT)



