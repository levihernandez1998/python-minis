from turtle import Turtle
from random import Random
import random

COLORS = ["red", "blue", "yellow", "green",
          "orange", "purple", "pink", "brown", "black"]
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []

    def create(self, level=1):
        chance = random.randint(1, 10 if level <= 5 else 6)
        if chance == 1:
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            if level % 2 == 0:
                car.goto(-300, random.randint(-250, 250))
            else:
                car.goto(300, random.randint(-250, 250))
            self.cars.append(car)

    def drive(self, level=1):
        for car in self.cars:
            if level % 2 == 0:
                car.forward(random.randint(3, level*MOVE_INCREMENT))
            else:
                car.backward(random.randint(3, level*MOVE_INCREMENT))

    def reset(self):
        for car in self.cars:
            car.hideturtle()
        self.cars = []
