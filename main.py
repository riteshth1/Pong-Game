from turtle import Screen
from paddle import Paddle
from Ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()
score = Scoreboard()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

r_paddle.create_paddle()
l_paddle.create_paddle()

screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")

screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detecting collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # check if r_paddle miss the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # check if l_paddle miss the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
