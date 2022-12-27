import json


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
