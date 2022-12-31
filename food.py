from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, screen_width, screen_length):
        super().__init__()
        self.screen_width = screen_width
        self.screen_length = screen_length
        self.create_apple()
        self.new_apple()

    def create_apple(self):
        # Create apple object
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")

    def new_apple(self):
        # Place apple in random place on board
        x_limit = int(self.screen_length / 2 * 0.95)
        y_limit = int(self.screen_width / 2 * 0.95)
        random_x = random.randint(-x_limit, x_limit)
        random_y = random.randint(-y_limit, int(y_limit * 0.9))
        self.setposition(random_x, random_y)
