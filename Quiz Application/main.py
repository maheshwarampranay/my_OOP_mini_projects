from data import question_data as que
from question_model import Question
from quiz_brain import QuizBrain
Question_bank=[]
for i in que:
    new_question=Question(i['question'],i['correct_answer'])
    Question_bank.append(new_question)
master = QuizBrain(Question_bank)
while master.questions_left():
    master.next_question()
    master.evaluator()
else:
    master.concluder()