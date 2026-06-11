import data
import art
from quiz_model import Quiz
from student_model import Student
import random

student = None
quiz = Quiz()
for level in data.quiz:
    for question in data.quiz[level]:
        quiz.add_question(level, question["question"], question["answer"])


def start():
    global student

    print(art.logo, "\n")
    name = input("What is your name? ")
    student = Student(name)

    print(art.professor, "\n")
    print("Welcome to the quiz bee, " + student.name +
          "☕!\nPlease answer either True or False. 🐝✨\n")

    generate_questions(student)
    take_quiz(student)
    student.report()


def generate_questions(student: Student):
    quiz_level = input(
        "Select difficulty (Easy/Normal/Hard/Random) 🎚️: ").lower()
    while quiz_level not in data.levels:
        print(
            f"Invalid difficulty {quiz_level} does not exist. Please choose (Easy/Normal/Hard).")
        quiz_level = input(
            "Select difficulty (Easy/Normal/Hard/Random) 🎚️: ").lower()

    student.level = quiz_level
    total_items = data.levels[quiz_level]

    if quiz_level == "random":
        for level in quiz.quizzes:
            student.questions.extend(random.sample(
                quiz.quizzes[level], int(total_items/3)))
    else:
        student.questions = random.sample(
            quiz.quizzes[quiz_level], total_items)


def take_quiz(user: Student):
    counter = 0
    print("\n")
    for question in user.questions:
        counter += 1
        answer = input(
            f"Q.{counter}: {question['question']} True or False? ").lower()
        if answer not in ["true", "false"]:
            print("\n⚠️ Please choose either True or False. -1 point! ⚠️\n")
            user.total_errors += 1
            continue

        if Quiz.check_answer(answer, question['answer']):
            user.total_score += 1
        else:
            user.total_errors += 1

        print("\n")


start()
