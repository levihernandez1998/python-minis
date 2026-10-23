from turtle import Turtle, Screen
import time

screen = Screen()

MOVE_DISTANCE = 5


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("darkgreen")
        self.penup()
        self.reset()  # bottom center

        self.left(90)
        self.facing_up = True
        self.facing_down = False
        self.facing_right = False
        self.facing_left = False

    def key_up(self):
        self.facing("up")
        if (self.ycor() < 280):
            self.sety(self.ycor() + MOVE_DISTANCE)

    def key_down(self):
        self.facing("down")
        if (self.ycor() > -280):
            self.sety(self.ycor() - MOVE_DISTANCE)

    def key_left(self):
        self.facing("left")
        if (self.xcor() > -280):
            self.setx(self.xcor() - MOVE_DISTANCE)

    def key_right(self):
        self.facing("right")
        if (self.xcor() < 280):
            self.setx(self.xcor() + MOVE_DISTANCE)

    def reset(self):
        self.showturtle()
        self.goto(0, -280)

    def blink(self):
        count = 0
        ishidden = False
        while count <= 4:
            if ishidden:
                self.showturtle()
            else:
                self.hideturtle()

            screen.update()
            count += 0.5
            time.sleep(0.5)
            ishidden = not ishidden

        self.showturtle()

    def facing(self, direction="up"):
        if (direction == "up"):
            if not self.facing_up:
                self.facing_up = True
                self.facing_down = False
                self.facing_right = False
                self.facing_left = False
                self.setheading(90)
        elif (direction == "down"):
            if not self.facing_down:
                self.facing_up = False
                self.facing_down = True
                self.facing_right = False
                self.facing_left = False
                self.setheading(270)
        elif (direction == "left"):
            if not self.facing_left:
                self.facing_up = False
                self.facing_down = False
                self.facing_right = False
                self.facing_left = True
                self.setheading(180)
        elif (direction == "right"):
            if not self.facing_right:
                self.facing_up = False
                self.facing_down = False
                self.facing_right = True
                self.facing_left = False
                self.setheading(0)
        else:
            pass
