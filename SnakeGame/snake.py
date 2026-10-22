from turtle import Turtle, Screen
import time

screen = Screen()

STARTING_POSITIONS = [(0, 0), (-20, 0)]
FORWARD_POSITION = 20
UP = 90
DOWN = UP * 3
LEFT = UP * 2
RIGHT = 0


class Snake():
    def __init__(self):
        self.segments = []
        self.init_snake()
        self.head = self.segments[0]
        self.head.color('darkgreen')

    def init_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('green')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def remove_segment(self):
        self.segments[-1].hideturtle()
        self.segments.pop(-1)

    def move(self):
        self.change_pos()
        self.head.forward(FORWARD_POSITION)

    def up(self):
        if (self.head.heading() != DOWN):
            self.head.setheading(UP)

    def down(self):
        if (self.head.heading() != UP):
            self.head.setheading(DOWN)

    def right(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)

    def left(self):
        if (self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def change_pos(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

    def eat(self):
        last_segment_x = self.segments[-1].xcor()
        last_segment_y = self.segments[-1].ycor()
        self.add_segment((last_segment_x, last_segment_y))

    def vomit(self):
        self.remove_segment()

    def blink(self):
        count = 0
        ishidden = False
        while count <= 20:
            for segment in self.segments:
                if ishidden:
                    segment.showturtle()
                else:
                    segment.hideturtle()

            screen.update()
            count += 0.5
            time.sleep(0.5)
            ishidden = not ishidden
