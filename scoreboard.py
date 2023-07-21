from turtle import Turtle

ALIGNMENT = "CENTER"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def restart_game(self):
        self.goto(0, -70)
        self.write(f"""
    Your score was {self.score}, press 'space'
    if you want to start again.""", align=ALIGNMENT, font=("Courier", 18, "normal"))
        self.score = 0
