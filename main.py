import time
import turtle
from turtle import Turtle, Screen, listen

from Snake import Snake

#Setting up a screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
keep_playing = True
position_x = 0

#Set up segment object
snake = Snake()



while keep_playing:
    screen.update()
    time.sleep(0.4)
    snake.move_snake()



listen()
screen.exitonclick()
