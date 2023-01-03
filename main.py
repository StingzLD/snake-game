from food import Food
from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def play_again():
    choice = screen.textinput(title="PLAY AGAIN",
                              prompt="Press 'Okay to play again")
    if choice is None:
        return False
    else:
        return True


def new_game():
    sb.new_game()
    snake.reset()
    apple.new_apple()


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

# Keystrokes to listen for
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Play game
continue_game = True

while continue_game:
    screen.listen()
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
        if play_again():
            new_game()
        else:
            continue_game = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            sb.game_over()
            if play_again():
                new_game()
            else:
                continue_game = False

screen.exitonclick()
