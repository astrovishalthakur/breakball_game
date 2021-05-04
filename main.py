from turtle import Screen
import time
from ball import Ball
# from scoreboard import Scoreboard
from paddle import Paddle
from blocks import BlockManager

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Break out")
screen.tracer(0)
block_manager = BlockManager()
block_manager.create()

paddle = Paddle((0, -280))
ball = Ball()
# scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle) < 55 and ball.ycor() < -250:
        ball.bounce_y()

    # Detect paddle misses
    if ball.ycor() < -280:
        ball.reset_position()
        game_is_on = False
        # scoreboard.point()

    # Detect collision with blocks
    for block in block_manager.all_blocks:
        if ball.distance(block) < 30:
            block_manager.destroy(block)
            ball.bounce_y()



screen.exitonclick()
