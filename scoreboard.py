from turtle import Turtle


def get_high_score():
    with open("high_score.txt", "r") as file:
        return int(file.read())


class Scoreboard(Turtle):
    def __init__(self, screen_width, screen_length):
        super().__init__()
        self.screen_width = screen_width
        self.screen_length = screen_length
        self.STARTING_POSITION = (0, int(self.screen_width / 2 * 0.90))
        self.penup()
        self.hideturtle()
        self.setposition(self.STARTING_POSITION)
        self.color("white")
        self.score = 0
        self.high_score = get_high_score()

    def display_score(self):
        self.clear()
        self.write(f"SCORE: {self.score}  HIGH SCORE: {self.high_score}",
                   align="center",
                   font=('Courier', 16, 'bold'))

    def increase_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.setposition(x=0, y=100)
        self.write("GAME OVER",
                   align="center",
                   font=('Courier', 20, 'bold'))
        self.check_high_score()

    def update_high_score(self):
        self.high_score = self.score
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def check_high_score(self):
        if self.score > self.high_score:
            self.update_high_score()
            self.setposition(x=0, y=60)
            self.write("NEW HIGH SCORE!",
                       align="center",
                       font=('Courier', 20, 'bold'))

    def new_game(self):
        self.setposition(self.STARTING_POSITION)
        self.score = 0
        self.display_score()
