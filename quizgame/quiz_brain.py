from os import system

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        
    def next_question(self):
        valid = 1
        while valid:
            user_answer = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False)?: ").title()
            system('clear')       
            valid = self.check_answer(user_answer, self.question_list[self.question_number].answer) 
        self.question_number += 1
        
    def still_has_question(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_answer, correct_answer):
        if(user_answer == correct_answer):
            print("You got it right!")
            self.score += 1
        elif(user_answer != correct_answer and (user_answer == "True" or user_answer == "False")):
            print("You got it wrong.")
            print(f"The correct answer was {correct_answer}.")
        else:
            print("Invalid Input")
            return 1
            
        print(f"Your current score is: {self.score}/{self.question_number+1}.")
        return 0
        
            