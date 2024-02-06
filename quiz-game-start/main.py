from question_model import *
from data import *
from quiz_brain import QuizBrain
list_of_questions = []

for q in question_data:
    q_text = q["question"]
    q_answer = q["correct_answer"]
    new_question = QuestionBankConstructor(q_text=q_text, q_answer=q_answer)
    list_of_questions.append(new_question)

a = QuizBrain(list_of_questions)
print(list_of_questions)

quiz = QuizBrain(list_of_questions)
while quiz.still_has_questions():
    quiz.nxtquestion()
