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

    def __init__(self, json_obj: dict[str]):
        self.text = json_obj['text']
        self.isCorrect = json_obj['isCorrect']


class Question(JSONable):
    def __init__(self, title: str, text: str, image: str, position: int, possibleAnswers: list[Answer]):
        self.title = title
        self.text = title
        self.image = image
        self.position = position
        self.possibleAnswers = possibleAnswers

    def __init__(self, json_obj: dict[str]):
        self.title = json_obj['title']
        self.text = json_obj['title']
        self.image = json_obj['image']
        self.position = json_obj['position']
        self.possibleAnswers = list(
            map(lambda x: Answer(x), json_obj["possibleAnswers"]))
