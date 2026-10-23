from turtle import Turtle

WINNING_SCORE = 2


class Scoreboard(Turtle):
    def __init__(self):
        self.score_left = 0
        self.score_right = 0
        self.game_is_over = False
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.show()

    def show(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"{self.score_left}   vs   {self.score_right}",
                   align="center", font=("Arial", 28, "bold"))

    def add_score(self, player="left"):
        if player == "left":
            self.score_left += 1
        else:
            self.score_right += 1

        if self.score_left == WINNING_SCORE:
            self.game_over("Left")
            self.game_is_over = True

        if self.score_right == WINNING_SCORE:
            self.game_over("Right")
            self.game_is_over = True

    def game_over(self, player="Left"):
        self.show()
        self.goto(0, 50)
        self.write(f"{player} wins 🎉", align="center",
                   font=("Arial", 24, "bold"))
