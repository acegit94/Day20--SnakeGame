import random
from turtle import Turtle

COLOR = "blue"

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.create_food()
        self.refresh()

    def create_food(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color(COLOR)
        self.speed("fastest")

    def refresh(self):
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 275)
        self.goto(random_x, random_y)