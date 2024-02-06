class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print(f"Game ended! \nYour score was: {self.score}/{len(self.question_list)}")
            return False
    def nxtquestion(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"{self.question_number}:{current_question.text}(True/False):")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score = self.score + 1
        else:
            print("That's wrong")








