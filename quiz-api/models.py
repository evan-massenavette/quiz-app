import json


class JSONable():
    def __init__(self, json_obj):
        self.json_obj = json_obj

    def to_json(self):
        return json.dumps(self, cls=JSONableEncoder)

    def __getitem__(self, key):
        return self.json_obj[key]

    def __setitem__(self, key, value):
        return self.json_obj[key] = value


class Answer(JSONable):
    def __init__(self, text: str, isCorrect: bool):
        super.__init__({
            'text': text,
            'isCorrect': isCorrect
        })

    def __init__(self, json_obj: dict[str]):
        super().__init__(json_obj)


class Question(JSONable):
    def __init__(self, text: str, title: str, image: str, position: int, possibleAnswers: list[Answer]):
        super().__init__({
            "title": title,
            "text": text,
            "position": position,
            "image": image,
            "possibleAnswers": possibleAnswers
        })
        self.possibleAnswers = possibleAnswers

    def __init__(self, json: dict[str]):
        super().__init__({
            "title": json["title"],
            "text": json["text"],
            "position": json["position"],
            "image": json["image"],
            "possibleAnswers": list(map(lambda x: Answer(x), json["possibleAnswers"]))
        })
        self.possibleAnswers = list(
            map(lambda x: Answer(x), json["possibleAnswers"]))


class JSONableEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, JSONable):
            return obj.json_obj
        else:
            return json.JSONEncoder.default(self, obj)
