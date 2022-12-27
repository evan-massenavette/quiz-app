from __future__ import annotations
import json
from typing import NamedTuple


class JSONable(dict):
    def to_json(self):
        return json.dumps(self)

    def __getattr__(self, name: str):
        return self[name]

    def __setattr__(self, name: str, value):
        self[name] = value


class Answer(JSONable):
    def __init__(self, text: str, isCorrect: bool):
        self.text = text
        self.isCorrect = isCorrect

    @classmethod
    def from_json(cls, json_obj: dict):
        return cls(json_obj['text'], json_obj['isCorrect'])


class Question(JSONable):
    def __init__(self, title: str, text: str, image: str, position: int, possibleAnswers: list[Answer]):
        self.title = title
        self.text = text
        self.image = image
        self.position = position
        self.possibleAnswers = possibleAnswers

    @classmethod
    def from_json(cls, json_obj: dict):
        possibleAnswers = [Answer.from_json(
            answer_json) for answer_json in json_obj['possibleAnswers']]
        return cls(json_obj['title'], json_obj['text'], json_obj['image'], json_obj['position'], possibleAnswers)

    class DbTuple(NamedTuple):
        title: str
        text: str
        image: str
        position: int
        possible_answer_0_text: str
        possible_answer_1_text: str
        possible_answer_2_text: str
        possible_answer_3_text: str
        correct_answer_idx: int

    @classmethod
    def from_tuple(cls, question_tuple: DbTuple | tuple) -> Question:
        # Check input tuple
        if question_tuple is None:
            raise TypeError('Given question tuple cannot be None')
        if not isinstance(question_tuple, cls.DbTuple):
            question_tuple = cls.DbTuple(*question_tuple)

        # Convert possible answers
        possible_answers = []
        for idx_question in range(4):
            possible_answers.append(Answer.from_json(
                {"text": question_tuple[5+idx_question], "isCorrect": idx_question == question_tuple[9]}))

        # Get other data from tuple
        title = question_tuple[1]
        text = question_tuple[2]
        position = question_tuple[3]
        image = question_tuple[4]

        # Return the question
        return cls(title, text, image, position, possible_answers)

    def to_tuple(self) -> DbTuple:
        # Find correct answer for this question
        try:
            correct_answer_idx = [
                answer.isCorrect for answer in self.possibleAnswers].index(True)
        except ValueError:
            raise ValueError(
                'Question must have at least 1 correct answer, but none was found')

        return self.DbTuple(
            title=self.title,
            text=self.text,
            image=self.image,
            position=self.position,
            possible_answer_0_text=self.possibleAnswers[0].text,
            possible_answer_1_text=self.possibleAnswers[1].text,
            possible_answer_2_text=self.possibleAnswers[2].text,
            possible_answer_3_text=self.possibleAnswers[3].text,
            correct_answer_idx=correct_answer_idx
        )
