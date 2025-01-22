class QuizBrain:
    def __init__(self,q_list):
        self.question_list = q_list
        self.score = 0
        self.number = 0
    def next_question(self):
        self.question=self.question_list[self.number]
        self.number+=1
        self.user_ans=input(f'Q{self.number}. {self.question.text}. True or False? ').title()
    def questions_left(self):
        '''returns True if questions left otherwise False'''
        if self.number<=10:
            return True
        else:
            return False
    def evaluator(self):
        if self.user_ans == self.question.answer:
            self.score+=1
            print(f'Correct Answer! score is {self.score}')
        else:
            print(f'Incorrect Answer.score is {self.score}')
    def concluder(self):
        print(f'your Score is {self.score}')
        if self.score==11 or self.score==12:
            print('TADA!! You won.')
        elif self.score>6:
            print('You Qualified!')
        else:
            print('You lost!')