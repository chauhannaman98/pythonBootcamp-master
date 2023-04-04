from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_obj = Question(question["text"], question["answer"])
    question_bank.append(question_obj)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"You final score is: {quiz.score}/{quiz.question_number}")
