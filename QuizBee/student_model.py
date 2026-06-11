from prettytable import PrettyTable


class Student:
    def __init__(self, name: str):
        self.name = name.title()
        self.level = None
        self.total_score = 0
        self.total_errors = 0
        self.questions = []

    def report(self):
        table = PrettyTable()
        table.add_row(["Name", self.name])
        table.add_row(["Level", self.level.capitalize()])
        table.add_row(
            ["Score", f"{self.total_score}/{len(self.questions)}"])
        table.add_row(["Errors", f"-{self.total_errors}"])
        table.add_row(
            ["Total Score", f"{self.total_score - self.total_errors}/{len(self.questions)}"])
        grade = self.compute_grade()
        table.add_row(["Grade", grade])
        print(table, "\n")
        self.closing_message(grade)

    def compute_grade(self):
        percentage = ((self.total_score - self.total_errors) /
                      len(self.questions)) * 100
        if percentage >= 90:
            return "A"
        elif percentage >= 80:
            return "B"
        elif percentage >= 70:
            return "C"
        elif percentage >= 60:
            return "D"
        else:
            return "F"

    def closing_message(self, grade: str):
        if grade == "A":
            print("Congratulations! You did great! 🏆")
        elif grade == "B":
            print("Good job! You did well! 👏")
        elif grade == "C":
            print("You did okay. Try harder next time! 👍")
        elif grade == "D":
            print("Oops! You need to study harder! 🤔")
        else:
            print("Don't worry, practice makes you perfect. Study harder next time! 📚")
