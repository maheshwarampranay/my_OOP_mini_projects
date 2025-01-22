from turtle import Turtle
move_distance=20
start_pos=[(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
    def create_snake(self):
        for position in start_pos:
            self.add_segment(position)

    def add_segment(self,position):
            snake=Turtle('square')
            snake.color('white')
            snake.penup();snake.speed(10)
            snake.goto(position)
            self.segments.append(snake)
            self.head=self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for i in self.segments:
            i.goto(1000,1000)

        self.segments.clear()
        self.create_snake()

    def move_snake(self):
        for mukka in range(len(self.segments)-1,0,-1):
            x=self.segments[mukka-1].xcor()
            y=self.segments[mukka-1].ycor()
            self.segments[mukka].goto(x,y)
        self.segments[0].forward(move_distance)
    def up(self):
        self.segments[0].setheading(90)
    def down(self):
        self.segments[0].setheading(270)
    def left(self):
        self.segments[0].setheading(180)
    def right(self):
        self.segments[0].setheading(0)

