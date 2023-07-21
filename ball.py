from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.x_velocity = 3
        self.y_velocity = 3

    def move(self):
        # Move by adding velocity to current position
        self.goto(self.xcor() + self.x_velocity, self.ycor() + self.y_velocity)

    def bounce_wall(self):
        self.y_velocity *= -1  # Reverse the y-velocity when hitting a wall

    def bounce_paddle(self):
        self.x_velocity *= -1  # Reverse the x-velocity when hitting a paddle
