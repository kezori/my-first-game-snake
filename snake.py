from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = None
        self.creat_snake()
        self.head = self.segments[0]

    def creat_snake(self):
        self.segments = []
        for i in range(0, 3):
            new_segment = Turtle(shape="square")
            new_segment.color("black")
            new_segment.penup()
            new_segment.goto(x=-i * 20, y=0)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

        if self.head.xcor() > 280:
            self.head.goto(-280, self.head.ycor())
        elif self.head.xcor() < -280:
            self.head.goto(280, self.head.ycor())
        elif self.head.ycor() > 250:
            self.head.goto(self.head.xcor(), -280)
        elif self.head.ycor() < -280:
            self.head.goto(self.head.xcor(), 240)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("black")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.creat_snake()
        self.head = self.segments[0]