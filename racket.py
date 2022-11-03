from turtle import Turtle

class Racket(Turtle):
    def __init__(self) -> None:
        super().__init__(shape="square")
        self.color("White")
        self.pu()
        self.goto(350, 0)
        self.seth(90)

        # self.racket = self.make_racket()



    def move_up(self) -> None:
        self.forward(20)
    def move_down(self) -> None:
        self.backward(s)


    # def make_racket(self) -> list:
    #     racket = []
    #     place =0
    #     for racket_part in range(0, 3):
    #         racket_part = Turtle(shape="square")
    #         racket_part.color("White")
    #         racket_part.pu()
    #         racket_part.seth(90)
    #         racket_part.goto(-450,place)
    #         place +=20
    #         racket.append(racket_part)
    #     return racket

    # def move_up(self) -> None:
    #     for racket_part in self.racket:
    #         racket_part.forward(20)
        
    # def move_down(self) -> None:
    #     for racket_part in self.racket:
    #         racket_part.backward(20)

        

