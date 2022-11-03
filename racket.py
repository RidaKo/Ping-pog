from turtle import Turtle

class Racket(Turtle):
    def __init__(self, xcor) -> None:
        super().__init__(shape="square")
        self.color("White")
        self.pu()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(xcor, 0)


    def move_up(self) -> None:
        new_y = self.ycor() +20
        self.goto(self.xcor(), new_y)
    def move_down(self) -> None:
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

        

