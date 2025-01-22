from turtle import Turtle
from time import sleep
ALIGNMENT='center' ; FONT=('Courier',24,'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.score=0
        self.penup()
        self.highest_score=0
        self.goto(0,265)
        self.color('white')
        self.update_score()


    def update_score(self):
        with open('highest_score.txt','r') as f:
            self.highest_score = f.read()
        self.write(arg=f'score:{self.score}  Highest Score:{self.highest_score}',align=ALIGNMENT,font=FONT)

    def reset(self):
        self.clear()
        strin=str(self.score)
        if strin > self.highest_score :
            with open('highest_score.txt','w') as f:
                self.highest_score = f.write(str(self.score))
        self.score=0
        self.update_score()

    def upscore(self):
        self.score+=1
        self.clear()
        self.update_score()
