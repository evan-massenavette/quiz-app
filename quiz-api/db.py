import sqlite3
from models import Question, Answer


def tuple_to_question(tuple: tuple) -> Question:
    if tuple == None:
        return None
    possible_answers = []
    for idx_question in range(4):
        possible_answers.append(Answer(
            {"text": tuple[5+idx_question], "isCorrect": idx_question == tuple[9]}))
    return Question({"title": tuple[1], "text": tuple[2],
                     "position": tuple[3], "image": tuple[4], "possibleAnswers": possible_answers})


def question_to_tuple(question: Question) -> tuple:
    correct_answer = 0
    for i in range(4):
        if question.possibleAnswers[i].isCorrect == True:
            correct_answer = i
            break
    return (question.title, question.text, question.position, question.image,
            question.possibleAnswers[0].text, question.possibleAnswers[1].text, question.possibleAnswers[2].text, question.possibleAnswers[3].text, correct_answer)


class Database():
    """
    Ouvre et ferme la base de données
    """

    def __init__(self, url: str):
        self.connection = sqlite3.connect(url, isolation_level=None)
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()

    # Queries on questions
    def get_question_id(self, question_id: int) -> Question:
        res = self.cursor.execute(
            "SELECT * FROM Question WHERE id=?;", (question_id,))
        return tuple_to_question(res.fetchone())

    def get_question_pos(self, question_pos: int) -> Question:
        res = self.cursor.execute(
            "SELECT * FROM Question WHERE position=?;", (question_pos,))
        return tuple_to_question(res.fetchone())

    def get_all_questions(self) -> list:
        res = self.cursor.execute("SELECT * FROM Question")
        return list(map(lambda x: tuple_to_question(x), res.fetchall()))

    def add_question(self, question: Question):
        self.cursor.execute("INSERT INTO Question (title, text, position, image, answer0, answer1, answer2, answer3, correct_answer) VALUES (?, ?, ?, ?);",
                            question_to_tuple(question))

    def update_question(self, question: Question, question_id: int):
        self.cursor.execute("UPDATE Question SET title = ?, text = ?, position = ?, image = ?, answer0 = ?, answer1 = ?, answer2 = ?, answer3 = ?, correct_answer = ? WHERE id=?;",
                            question_to_tuple(question)+(question_id,))

    def delete_question(self, question_id: int):
        self.cursor.execute(
            "DELETE FROM Question WHERE id=?;", question_id)

    # Queries on scores
    def get_score(self):
        pass

    def get_all_scores(self):
        pass

    def set_score(self):
        pass
