import time
import turtle
from paddle import Paddle
from ball import Ball
from scorebaord import Scoreboard

screen = turtle
scoreboard = Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

right_paddle = Paddle(360, 0)
left_paddle = Paddle(-360, 0)


screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

ball = Ball()


is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    scoreboard.update_scoreboard()
    # bounce back when it hits upper and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # bounce back ball when a paddle is hit
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() > -340:
        ball.bounce_x()

    # detect when right paddle misses
    if ball.xcor() > 360:
        ball.reset_positions()
        scoreboard.l_point()

    # detect when left paddle is missed
    if ball.xcor() < -360:
        ball.reset_positions()
        scoreboard.r_point()

screen.exitonclick()

