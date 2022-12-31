from snake import Snake
from turtle import Screen
import time

# Instantiate and configure screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("STINGZ SNAKE GAME")
screen.tracer(0)

# Create snake
snake = Snake()

# Play game
snake_alive = True
while snake_alive:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
