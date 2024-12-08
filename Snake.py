import turtle
from turtle import Turtle
MOVE_DISTANCE = 20
TURN_ANGLE = 90

class Snake:

    def __init__(self):
        self.position_x = 0
        self.snake_segments = []
        self.create_snake()

    def create_snake(self):
        for segment_index in range(0, 3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(self.position_x, 0)
            self.snake_segments.append(segment)
            self.position_x = segment.xcor() - 20

    def move_snake(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(x=new_x, y=new_y)

        self.snake_segments[0].left(TURN_ANGLE)
        self.snake_segments[0].forward(MOVE_DISTANCE)

