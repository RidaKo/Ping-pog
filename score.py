from turtle import Turtle
class Score(Turtle):
    def __init__(self, place) -> None:
        super().__init__(visible=False)
        self.color("White")
        self.pu()
        self.score =0
        self.goto(place, 200)
        self.write(self.score, align = "Center", font = ("Courier", 80, "normal"))
    
    def update(self):
        self.score = self.score +1
        self.clear()
        self.write(self.score, align = "Center", font = ("Courier", 80, "normal"))