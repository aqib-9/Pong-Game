from turtle import Turtle
class Blocks(Turtle):
    def __init__(self,goto):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5,1)
        self.penup()
        self.goto(goto)
        self.onclick('up',)
    def up(self):
        y = self.ycor()
        y += 20
        self.sety(y)
    def down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)
