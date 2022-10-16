from turtle import Screen, Turtle
from player import Player
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # mở file high_score.txt lấy dữ liệu cho high_score
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        file.close()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # ghi dữ liệu high_score vào file high_score.txt
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
            file.close()
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()