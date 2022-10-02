from turtle import Screen, Turtle
DIFFICULTY = ["0.1", "0.09", "0.08", "0.07", "0.06", "0.05"]


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = 0.0
        self.color("black")
        self.penup()
        self.hideturtle()
        screen = Screen()
        self.difficulty = screen.textinput(title="Difficulty", prompt="Choose a difficulty. Type 1, 2, 3, 4, 5 or 6: ")
        self.set_speed(int(self.difficulty))

    def set_speed(self, speed):
        self.speed = float(DIFFICULTY[speed - 1])
        return self.speed



