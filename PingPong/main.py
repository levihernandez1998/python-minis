from turtle import Screen
from paddle import Paddle
from score import Scoreboard
from ball import Ball
import time

game_running = True
game_over = False

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard()
paddle_left = Paddle("left")
paddle_right = Paddle()

screen.listen()
screen.onkeypress(paddle_right.up, "Up")
screen.onkeypress(paddle_right.down, "Down")
screen.onkeypress(paddle_left.up, "w")
screen.onkeypress(paddle_left.down, "s")

screen.onkeypress(paddle_right.forward, "Left")
screen.onkeypress(paddle_right.back, "Right")
screen.onkeypress(paddle_left.forward, "d")
screen.onkeypress(paddle_left.back, "a")


right_won = False
left_won = False

while not game_over:
    while game_running:
        screen.update()
        time.sleep(0.05)
        ball.move()

        # detect collision with the Y axis wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce("y")

        # detect collision with paddles
        if (ball.distance(paddle_right) < 30) or (ball.distance(paddle_left) < 30):
            ball.bounce("x")

        if ball.xcor() > 380:  # score to left player
            scoreboard.add_score("left")
            if not scoreboard.game_is_over:
                scoreboard.show()
            else:
                left_won = True
            game_over = scoreboard.game_is_over
            game_running = False

        if ball.xcor() < -380:  # score to right player
            scoreboard.add_score("right")
            if not scoreboard.game_is_over:
                scoreboard.show()
            else:
                right_won = True
            game_over = scoreboard.game_is_over
            game_running = False

    screen.update()
    time.sleep(1)
    ball.reset()
    game_running = True

if right_won:
    paddle_right.blink()

if left_won:
    paddle_left.blink()

screen.exitonclick()
