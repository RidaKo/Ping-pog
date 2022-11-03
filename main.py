from racket import Racket
from turtle import Screen

screen  = Screen()
screen.screensize(canvwidth=800, canvheight = 600,bg ="Black")
screen.title("Pong")

player = Racket()

screen.listen()
screen.onkey(fun = player.move_up, key ="Up")
screen.onkey(fun = player.move_down, key = "Down")

screen.exitonclick()