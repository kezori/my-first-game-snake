from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score_board import ScoreBoard
from player import Player
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("My Snake Game")
screen.tracer(0)

player = Player()
snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(player.speed)
    snake.move()

    if snake.head.distance(food) < 15:
        food.creat_food()
        snake.extend()
        score_board.increase_score()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()


screen.exitonclick()
