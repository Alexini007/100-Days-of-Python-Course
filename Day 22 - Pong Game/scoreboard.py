from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 230)
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 230)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))

    def left_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def end_of_game(self):
        self.goto(0, 0)
        if self.l_score > self.r_score:
            self.write("GAME OVER - LEFT WINS", align="center", font=("Courier", 20, "normal"))
        elif self.l_score < self.r_score:
            self.write("GAME OVER - RIGHT WINS", align="center", font=("Courier", 20, "normal"))