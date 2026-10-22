from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

game_running = True

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

board = Scoreboard()
apple = Food()
rotten = Food()
rotten.color('yellow')
viper = Snake()

screen.listen()
screen.onkey(viper.up, "Up")
screen.onkey(viper.up, "w")
screen.onkey(viper.down, "Down")
screen.onkey(viper.down, "s")
screen.onkey(viper.left, "Left")
screen.onkey(viper.left, "a")
screen.onkey(viper.right, "Right")
screen.onkey(viper.right, "d")


def game_over():
    global game_running
    game_running = False
    board.game_over()
    viper.blink()


def sleep(score):
    if score >= 50:
        time.sleep(0.3)
    else:
        time.sleep(0.07 + score * 0.0046)


while game_running:

    # detect collision with itself + I want to show it's eating itself on screen before screen.update()
    for segment in viper.segments[1:]:
        if viper.head.distance(segment) < 10:
            game_over()

    # detect collision with food 🍎
    if viper.head.distance(apple) < 15:
        board.add()
        viper.eat()
        apple.refresh()

    if viper.head.distance(rotten) < 15:
        if board.current == 0 or len(viper.segments) == 1:
            game_over()
        else:
            board.subtract()
            viper.vomit()
            rotten.refresh()

    # detect collision with wall: begin
    if viper.head.xcor() > 380 or viper.head.xcor() < -380:
        game_over()

    if viper.head.ycor() > 380 or viper.head.ycor() < -380:
        game_over()
    # detect collision with wall: end

    screen.update()
    viper.move()
    sleep(board.current)


screen.exitonclick()
