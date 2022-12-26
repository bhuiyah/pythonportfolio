from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from os import system

question_bank = []

for data in question_data:
    question_bank.append(Question(data["question"], data["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

system('clear')
print("You've Complete the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")