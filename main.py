from turtle import Turtle, Screen
from block import Blocks
from Ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 500)
screen.title('GAME')
screen.tracer(0)

block1 = Blocks((380, 0))
block2 = Blocks((-390, 0))

ball = Ball()
score = Score()

screen.listen()
screen.onkey(block1.up, "Up")
screen.onkey(block1.down, "Down")
screen.onkey(block2.up, "w")
screen.onkey(block2.down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Ball bounces on the top and bottom walls
    if ball.ycor() > 235 or ball.ycor() < -235:
        ball.bounce_y()

    # Ball bounces when hitting block1 (right block)
    if ball.distance(block1) < 50 and ball.xcor() > 350:
        ball.bounce_x()
        ball.move_speed *= 0.9

    # Ball bounces when hitting block2 (left block)
    if ball.distance(block2) < 50 and ball.xcor() < -355:
        ball.bounce_x()
        ball.move_speed *= 0.9

    if ball.xcor() > 390:
        ball.reset_pos()
        score.l_point()


    if ball.xcor() < -390:
        ball.reset_pos()
        score.r_point()
    
    

screen.exitonclick()
