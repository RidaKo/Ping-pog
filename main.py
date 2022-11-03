from racket import Racket
from turtle import Screen
from ball import Ball
import time

screen  = Screen()
screen.bgcolor("Black")
screen.setup(width=800,height = 600)
screen.title("Pong")
screen.tracer(0)



ball = Ball()
player = Racket(350)
ai_player = Racket(-350)

screen.listen()
screen.onkey(fun = player.move_up, key ="Up")
screen.onkey(fun = player.move_down, key = "Down")
screen.onkey(fun = ai_player.move_up, key ="w")
screen.onkey(fun = ai_player.move_down, key = "s")


game_is_on =True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


screen.exitonclick()