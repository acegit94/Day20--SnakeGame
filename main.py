import time
import turtle
from turtle import Turtle, Screen, listen

from Snake import Snake

#Setting up a SCREEN
SCREEN = Screen()
SCREEN.setup(width=600, height=600)
SCREEN.bgcolor("black")
SCREEN.title("Snake Game")
SCREEN.tracer(0)
KEEP_PLAYING = True

#Set up segment object
snake = Snake()
listen()
SCREEN.onkey(snake.up, "Up")
SCREEN.onkey(snake.down, "Down")
SCREEN.onkey(snake.left, "Left")
SCREEN.onkey(snake.right, "Right")


while KEEP_PLAYING:
    SCREEN.update()
    time.sleep(0.1)
    snake.move_snake()




SCREEN.exitonclick()
