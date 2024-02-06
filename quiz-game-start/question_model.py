from data import *
import random

# my method
class QuestionConstructor():

    def __init__(self):
        self.question = random.choice(question_data)
        self.text = self.question["text"]
        self.answer = self.question["answer"]

# course suggested method
class QuestionBankConstructor:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
