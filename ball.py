from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__(shape = "circle")
        self.color("White")
        self.pu()
        self.new_y = 15
        self.new_x = 10
        self.move_speed = 0.1

        
        

    def move(self) -> None:
        self.wall_collision()
        self.goto(self.xcor()+ self.new_x, self.ycor() + self.new_y)
    
    def wall_collision(self) -> None:
        if self.ycor()>280:
            self.new_y = -15
        elif self.ycor()<-280:
            self.new_y = 15
    def racket_collision(self, player: object) -> None:
        if self.distance(player.position()) < 50 and (self.xcor()>320 or self.xcor()< -320):
            self.new_x = self.new_x * -1
            self.move_speed = self.move_speed * 0.9
    
    def out_of_bounds(self, score: object):
            self.goto(0, 0)
            self.new_x = self.new_x * -1
            score.update()
            self.move_speed = 0.1

    
        
        


