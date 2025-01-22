from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('The snake game.')
snacky=Snake()

food= Food()

board=Scoreboard()

screen.listen()
screen.onkey(fun=snacky.up,key='Up')
screen.onkey(fun=snacky.down,key='Down')
screen.onkey(fun=snacky.left,key='Left')
screen.onkey(fun=snacky.right,key='Right')

game_is_on=True

while game_is_on:
    time.sleep(0.17)
    screen.update()
    snacky.move_snake()

    # eating food
    if snacky.head.distance(food) < 15:
        food.refresh()
        board.upscore()
        snacky.extend()

    # detect collision with walls
    if snacky.head.xcor()>280 or snacky.head.ycor()>280 or snacky.head.xcor()<-280 or snacky.head.ycor()<-280:
        board.reset()
        snacky.reset()

    #detection of collision with itself
    for mukka in snacky.segments[1::]:
        if snacky.head.distance(mukka) < 10:
            board.reset()
            snacky.reset()

screen.exitonclick()