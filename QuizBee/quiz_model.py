class Quiz:
    def __init__(self):
        self.quizzes = {
            'easy': [],
            'normal': [],
            'hard': []
        }

    def add_question(self, level: str, question: str, answer: bool):
        if self.validate_level(level):
            self.quizzes[level].append({
                'question': question,
                'answer': answer
            })
        else:
            print(
                f"Invalid level: \"{level}\". Please choose from {self.quizzes.keys()}")

    @staticmethod
    def validate_level(level: str) -> bool:
        if level.lower() not in ["easy", "normal", "hard"]:
            return False
        return True

    @staticmethod
    def check_answer(answer: str, correct_answer: bool) -> bool:
        return answer.lower() == str(correct_answer).lower()
