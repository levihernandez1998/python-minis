from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        self.current = 0
        self.highest = 2
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 350)
        self.show()

    def add(self):
        self.current += 1

        if self.current > self.highest:
            self.highest = self.current

        self.show()

    def subtract(self):
        self.current -= 1
        self.show()

    def show(self):
        self.clear()
        self.write(f"🍎 {self.current}  🏆 {self.highest}",
                   align="center", font=("Arial", 20, "normal"))

    def reset(self):
        self.current = 0
        self.show()

    def game_over(self):
        self.clear()

        self.goto(0, 50)
        self.write(f"{self.current}", align="center",
                   font=("Arial", 32, "bold"))

        self.goto(0, 0)
        self.write("🍎 GAME OVER 🐍", align="center", font=("Arial", 24, "bold"))
        if (self.current >= self.highest):
            self.goto(0, -50)
            self.write("NEW HIGHEST SCORE 🎉", align="center",
                       font=("Arial", 20, "normal"))
        else:
            self.goto(0, -50)
            self.write("Try again", align="center",
                       font=("Arial", 20, "normal"))
