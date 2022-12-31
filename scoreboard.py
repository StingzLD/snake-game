from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, screen_width, screen_length):
        super().__init__()
        self.screen_width = screen_width
        self.screen_length = screen_length
        self.penup()
        self.hideturtle()
        self.setposition(0, int(self.screen_width / 2 * 0.90))
        self.color("white")
        self.score = 0

    def display_score(self):
        self.clear()
        self.write(f"SCORE: {self.score}",
                   align="center",
                   font=('Courier', 16, 'bold'))

    def increase_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.home()
        self.write("GAME OVER",
                   align="center",
                   font=('Courier', 20, 'bold'))
