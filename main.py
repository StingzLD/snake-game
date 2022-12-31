import time
import turtle as t

# Instantiate and configure screen
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("STINGZ SNAKE GAME")
screen.tracer(0)

# Snake segments
segments = []

# Create starting segments
for n in range(3):
    new_segment = t.Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.setposition(-20 * n, 0)
    segments.append(new_segment)

# Play game
snake_alive = True
while snake_alive:
    screen.update()
    time.sleep(0.1)

    # Move snake by making each segment copy the segment in front of its
    # position, then move the head according to the user's input
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].setposition(new_x, new_y)

    segments[0].forward(20)

screen.exitonclick()
