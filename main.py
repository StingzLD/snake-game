from food import Food
from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Instantiate and configure screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("STINGZ SNAKE GAME")
screen.tracer(0)

# Initialize game
snake = Snake()
apple = Food(screen_width=SCREEN_WIDTH,screen_length=SCREEN_HEIGHT)
sb = Scoreboard(screen_width=SCREEN_WIDTH, screen_length=SCREEN_HEIGHT)
sb.display_score()

# Listen for keystrokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Play game
snake_alive = True
score = 0
while snake_alive:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(apple) < 15:
        apple.new_apple()
        snake.extend()
        sb.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > SCREEN_WIDTH / 2 * 0.95 or \
       snake.head.xcor() < -SCREEN_WIDTH / 2 * 0.95 or \
       snake.head.ycor() > SCREEN_HEIGHT / 2 * 0.90 or \
       snake.head.ycor() < -SCREEN_HEIGHT / 2 * 0.95:
        sb.game_over()
        snake_alive = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            sb.game_over()
            snake_alive = False

screen.exitonclick()
