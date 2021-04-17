import random

import requests


class QuizBrain:
    questions = list()
    score = 0

    def __init__(self, amount, question_factory):
        self.amount = amount
        self.question_factory = question_factory

    def play(self):
        self._init_questions()
        print("Get ready to play!")
        print()
        self._loop()
        print("========= FINAL =========")
        print(f"Your final score: {self.score}")
        self._reset()

    def _init_questions(self):
        response = requests.get(f"https://opentdb.com/api.php?amount={self.amount}")
        response.raise_for_status()
        response_json = response.json()
        questions = response_json["results"]
        for question in questions:
            self.questions.append(self.question_factory.create_from_json(question))

    def _loop(self):
        remained_questions = self.questions
        while len(remained_questions) > 0:
            next_question_index = random.randint(0, len(remained_questions) - 1)
            next_question = remained_questions[next_question_index]
            remained_questions.pop(next_question_index)
            print("========= NEXT QUESTION =========")
            print(next_question.description)
            answer = input("Answer: ").lower()
            if next_question.check_answer(answer):
                print("Correct!")
                self.score += 1
            else:
                print("Wrong :(")
            print(f"Your new score: {self.score}")
            print(f"Remained questions: {len(remained_questions)}")
            print()

    def _reset(self):
        self.questions = list()
        self.score = 0
