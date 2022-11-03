from racket import Racket
from turtle import Screen
from ball import Ball
import time
from score import Score

screen  = Screen()
screen.bgcolor("Black")
screen.setup(width=800,height = 600)
screen.title("Pong")
screen.tracer(0)



ball = Ball()
player1 = Racket(350)
score1 = Score(100)

player2 = Racket(-350)
score2 = Score(-100)

screen.listen()
screen.onkey(fun = player1.move_up, key ="Up")
screen.onkey(fun = player1.move_down, key = "Down")
screen.onkey(fun = player2.move_up, key ="w")
screen.onkey(fun = player2.move_down, key = "s")


game_is_on =True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    ball.racket_collision(player = player1)
    ball.racket_collision(player = player2)
    if ball.xcor()>400:
        ball.out_of_bounds(score1)
    elif ball.xcor()<-400:
        ball.out_of_bounds(score2)
    
    


screen.exitonclick()