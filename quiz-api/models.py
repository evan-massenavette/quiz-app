from __future__ import annotations
import json
from typing import NamedTuple


class JSONable(dict):
    def to_json(self):
        json_obj = json.loads(json.dumps(self))
        json_obj["position"] = int(json_obj["position"])
        return json_obj

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
    def __init__(self, id: int | None, title: str, text: str, position: int, image: str, possibleAnswers: list[Answer]):
        self.id = id
        self.title = title
        self.text = text
        self.position = position
        self.image = image
        self.possibleAnswers = possibleAnswers

    @classmethod
    def from_json(cls, id: int | None, json_obj: dict):
        possibleAnswers = [Answer.from_json(
            answer_json) for answer_json in json_obj['possibleAnswers']]
        return cls(id, json_obj['title'], json_obj['text'], int(json_obj['position']), json_obj['image'], possibleAnswers)

    @classmethod
    def from_tuple(cls, question_tuple: tuple) -> Question:
        # Check input tuple
        if question_tuple is None:
            raise TypeError('Given question tuple cannot be None')

        # Get data from tuple
        id = question_tuple[0]
        title = question_tuple[1]
        text = question_tuple[2]
        position = question_tuple[3]
        image = question_tuple[4]
        possible_answers = question_tuple[5:9]
        correct_answer_idx = question_tuple[9]

        # Convert possible answers
        possible_answers_converted = []
        for idx, answer_text in enumerate(possible_answers):
            # Stop converting when we reach first null answer
            if answer_text is None:
                break
            possible_answers_converted.append(
                Answer(answer_text, idx == correct_answer_idx))

        # Return the question
        return cls(id, title, text, position, image, possible_answers_converted)

    def to_tuple(self) -> tuple:
        # Find correct answer for this question
        try:
            correct_answer_idx = [
                answer.isCorrect for answer in self.possibleAnswers].index(True)
        except ValueError:
            raise ValueError(
                'Question must have at least 1 correct answer, but none was found')

        # Convert possible answers text
        possibleAnswersText = list(map(lambda a: a.text, self.possibleAnswers))
        # Pad with None to get to  total length of 4
        pad_value = None
        pad_size = 4 - len(possibleAnswersText)
        possibleAnswersText_padded = [
            *possibleAnswersText, *[pad_value] * pad_size]

        return (
            self.id,
            self.title,
            self.text,
            self.position,
            self.image,
            possibleAnswersText_padded[0],
            possibleAnswersText_padded[1],
            possibleAnswersText_padded[2],
            possibleAnswersText_padded[3],
            correct_answer_idx,
        )
