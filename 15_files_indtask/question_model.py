import html
import random
from abc import ABC, abstractmethod


class Question(ABC):
    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def check_answer(self, answer):
        pass


class BinaryQuestion(Question):
    question = ""
    answer = False

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    @property
    def description(self):
        return f"{self.question} True or False?"

    def check_answer(self, user_answer):
        answer = user_answer in ["y", "t", "yes", "true"]
        return answer == self.answer

class MultipleChoiceQuestion(Question):
    question = ""
    answers = list()
    correct_answer_index = 0

    def __init__(self, question, correct_answer, other_answers):
        self.question = question
        other_answers.append(correct_answer)
        self.answers = other_answers
        random.shuffle(self.answers)
        for i, answer in enumerate(self.answers):
            if answer == correct_answer:
                self.correct_answer_index = i
                break

    @property
    def description(self):
        answers = "\n".join(f"{i + 1}. {answer}" for i, answer in enumerate(self.answers))
        return f"{self.question}\nAnswers:\n{answers}"

    def check_answer(self, user_answer):
        answer_index = int(user_answer)
        return answer_index - 1 == self.correct_answer_index


class QuestionFactory:
    def create_from_json(self, json):
        if json["type"] == "boolean":
            return self._create_binary_question(json)
        elif json["type"] == "multiple":
            return self._create_multiple_answers_question(json)
        else:
            raise ValueError("Unknown question type!")

    def _create_binary_question(self, json):
        question = html.unescape(json["question"])
        answer = True if json["correct_answer"] == "True" else False
        return BinaryQuestion(question, answer)

    def _create_multiple_answers_question(self, json):
        question = html.unescape(json["question"])
        correct_answer = html.unescape(json["correct_answer"])
        other_answers = [html.unescape(answer) for answer in json["incorrect_answers"]]
        return MultipleChoiceQuestion(html.unescape(question), correct_answer, other_answers)
