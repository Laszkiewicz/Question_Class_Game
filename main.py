from questionclass import Question
from data import question_data
from brainclass import QuizBrain

question_list = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_list.append(new_question)


quiz = QuizBrain(question_list)

while quiz.still_has_questions():
    quiz.next_question()

print("you have finished")
print(f"your score is, {quiz.score}, out of {quiz.question_number} quiz questions")