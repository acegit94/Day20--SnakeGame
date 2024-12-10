import time
from turtle import Screen, listen

from Scoreboard import Scoreboard
from Snake import Snake
from Food import Food

#Setting up a SCREEN
SCREEN = Screen()
SCREEN.setup(width=600, height=600)
SCREEN.bgcolor("black")
SCREEN.title("Snake Game")
SCREEN.tracer(0)
KEEP_PLAYING = True

#Set up segment object
snake = Snake()
food = Food()
scoreboard = Scoreboard()

listen()
SCREEN.onkey(snake.up, "Up")
SCREEN.onkey(snake.down, "Down")
SCREEN.onkey(snake.left, "Left")
SCREEN.onkey(snake.right, "Right")


while KEEP_PLAYING:
    SCREEN.update()
    time.sleep(0.1)
    snake.move_snake()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        KEEP_PLAYING = False
        scoreboard.game_over()


    #Detect collision with tail:
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            KEEP_PLAYING = False
            scoreboard.game_over()




SCREEN.exitonclick()
