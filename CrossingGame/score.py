from turtle import Turtle

LEVEL_LIMIT = 2


class Scoreboard(Turtle):
    def __init__(self):
        self.current_level = 1
        self.game_is_over = False

        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.show()

    def show(self):
        self.clear()
        self.goto(-240, 260)
        self.write(f"Level {self.current_level}",
                   align="center", font=("Arial", 14, "bold"))

    def level_passed(self):
        self.current_level += 1

    def game_over(self):
        self.show()
        self.goto(0, 50)
        self.write(f"Try again!", align="center", font=("Arial", 24, "bold"))

    def check_win(self):
        if self.current_level > LEVEL_LIMIT:
            self.clear()
            self.goto(0, 50)
            self.write(f"Congratulations 🎉", align="center",
                       font=("Arial", 24, "bold"))
            return True
        else:
            return False
