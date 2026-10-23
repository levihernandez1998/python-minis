from turtle import Screen
from player import Player
from score import Scoreboard, LEVEL_LIMIT
from car_manage import CarManager
import time


screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

score = Scoreboard()
car_manager = CarManager()
player = Player()

screen.listen()
screen.onkeypress(player.key_up, "Up")
screen.onkeypress(player.key_down, "Down")
screen.onkeypress(player.key_up, "w")
screen.onkeypress(player.key_down, "s")
screen.onkeypress(player.key_up, "W")
screen.onkeypress(player.key_down, "S")
screen.onkeypress(player.key_left, "Left")
screen.onkeypress(player.key_right, "Right")
screen.onkeypress(player.key_left, "a")
screen.onkeypress(player.key_right, "d")
screen.onkeypress(player.key_left, "A")
screen.onkeypress(player.key_right, "D")

game_running = True
level_running = True

while game_running:
    while level_running:
        car_manager.create(score.current_level)
        car_manager.drive(score.current_level)
        time.sleep(0.05)
        screen.update()

        for car in car_manager.cars:
            if car.distance(player) < 20:
                score.game_over()
                level_running = False
                game_running = False

        # check if player reached the y wall
        if player.ycor() >= 280:
            car_manager.reset()
            player.reset()
            score.level_passed()

            if (score.check_win()):
                level_running = False
                game_running = False
            else:
                score.show()
                level_running = False
                player.reset()
                player.blink()

    player.reset()
    screen.update()
    time.sleep(1)
    level_running = True


screen.exitonclick()
