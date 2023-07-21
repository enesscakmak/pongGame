from turtle import Screen, Turtle

MOVE_DISTANCE = 40
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.create_paddle()
        self.goto(starting_position)

    def up(self):
        self.setheading(UP)

    def down(self):
        self.setheading(DOWN)

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=7, stretch_len=1)
        self.penup()

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y < 241:
            self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y > -241:
            self.sety(new_y)
