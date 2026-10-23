from turtle import Turtle
from random import Random

random = Random()


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)

        # directions
        self.x_direction = 5
        self.y_direction = 5

        self.reset()
        self.speed(0)

    def move(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)

    def bounce(self, axis="y"):
        if axis == "y":
            self.y_direction *= -1
        else:
            self.x_direction *= -1

    def reset(self):
        random_y = random.randrange(1, 10)
        random_x = random.randrange(1, 10)
        if random_y % 2:
            self.y_direction *= -1
        if random_x % 2:
            self.x_direction *= -1

        self.goto(0, 0)
