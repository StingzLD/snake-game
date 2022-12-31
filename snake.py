import turtle as t


class Snake():
    def __init__(self):
        self.segments = []

        # Create starting segments
        for n in range(3):
            new_segment = t.Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.setposition(-20 * n, 0)
            self.segments.append(new_segment)

    def move(self):
        # Move snake by making each segment copy the segment in front of its
        # position, then move the head according to the user's input
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].setposition(new_x, new_y)

        self.segments[0].forward(20)
