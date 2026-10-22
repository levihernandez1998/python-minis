from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.food = super()
        self.food.shape('circle')
        self.food.color('red')
        self.food.penup()
        self.food.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.food.goto(random.randint(-380, 380), random.randint(-380, 380))
