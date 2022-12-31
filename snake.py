import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        # Create the first three segments of the snake
        for position in STARTING_POSITIONS:
            new_segment = t.Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.setposition(position)
            self.segments.append(new_segment)

    def move(self):
        # Make each segment copy the segment in front of its position
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].setposition(new_x, new_y)
        # Move head of snake
        self.segments[0].forward(MOVE_DISTANCE)
