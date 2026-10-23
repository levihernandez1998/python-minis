from turtle import Turtle, Screen
import time

screen = Screen()


class Paddle(Turtle):
    def __init__(self, side="right"):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.side = side
        if side == "left":
            self.goto(-360, 0)
        else:
            self.goto(360, 0)

    def up(self):
        if (self.ycor() < 280):
            self.sety(self.ycor() + 20)

    def down(self):
        if (self.ycor() > -280):
            self.sety(self.ycor() - 20)

    def back(self):
        if self.side == "right":
            if (self.xcor() < 360):
                self.setx(self.xcor() + 20)
        else:
            if (self.xcor() > -360):
                self.setx(self.xcor() - 20)

    def forward(self):
        if self.side == "right":
            if (self.xcor() > 40):
                self.setx(self.xcor() - 20)
        else:
            if (self.xcor() < -40):
                self.setx(self.xcor() + 20)

    def blink(self):
        self.color("green")
        count = 0
        ishidden = False
        while count <= 20:
            if ishidden:
                self.showturtle()
            else:
                self.hideturtle()

            screen.update()
            count += 0.5
            time.sleep(0.5)
            ishidden = not ishidden
