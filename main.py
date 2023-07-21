from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep
import winsound

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer()

paddle1 = Paddle((280, 0))
paddle2 = Paddle((-290, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")
screen.onkey(paddle2.move_up, "w")
screen.onkey(paddle2.move_down, "s")


def bounce_sound():
    winsound.Beep(1000, 50)


def game_over_sound():
    winsound.Beep(150, 1000)


def game():
    # Sleep for 1 sec for not rushing player
    sleep(1)
    screen.onkey(None, "space")  # Disable the key event during the game
    game_is_on = True
    while game_is_on:
        screen.update()
        ball.move()
        # Bounce from wall if it's within 10 px
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.bounce_wall()
        # Bounce from paddles if it's within 70 px to paddle and 40/30 px to wall
        if ball.distance(paddle1) < 70 and ball.xcor() > 260 or ball.distance(paddle2) < 70 and ball.xcor() < -270:
            ball.bounce_paddle()
            scoreboard.increase_score() # Increase score everytime it hits a paddle
            bounce_sound()

        if ball.xcor() == 300 or ball.xcor() == -300: # Game over if ball hits side walls
            scoreboard.game_over()
            game_over_sound()
            screen.update()  # Update the screen after displaying the game over message
            scoreboard.restart_game()
            screen.onkey(start_game, "space")
            return


def start_game(): #Start and reset the game
    screen.onkey(None, "space")
    ball.goto(0, 0)
    scoreboard.goto(0, 250)
    scoreboard.clear()
    game()


screen.ontimer(start_game, 1500)

screen.exitonclick()
