from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__(shape = "circle")
        self.color("White")
        self.pu()
        self.new_y = 15
        
        

    def move(self) -> None:
        self.racket_collision()
        self.goto(self.xcor()+10, self.ycor() + self.new_y)
    
    def racket_collision(self) -> None:
        if self.ycor()>280:
            self.new_y = -15
        elif self.ycor()<-280:
            self.new_y = 15
        
        


