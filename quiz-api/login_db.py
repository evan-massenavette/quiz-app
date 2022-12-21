import sqlite3
from models import Question, Answer


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


class QueryMaker():
    """
    Fais des requêtes vers la base de données
    """

    def __init__(self, db: Database):
        self.db = db

    # Queries on questions
    def get_question(self, question_id: int) -> tuple:
        res = self.db.cursor.execute(
            "SELECT * FROM Question WHERE id IN (?)", question_id)
        return res.fetchone()

    def get_all_questions(self) -> list:
        res = self.db.cursor.execute("SELECT * FROM Question")
        return res.fetchall()
    """retourne une liste de tuples"""

    def add_question(self, question: Question):
        self.db.cursor.execute("INSERT INTO Question (title, text, position, image) VALUES (?, ?, ?, ?);",
                               (question.title, question.text, question.position, question.image))

    def add_questions(self, question_list: list):
        self.db.cursor.executemany(
            "INSERT INTO Question (title, text, position, image) VALUES (?, ?, ?, ?);", question_list)

    def update_question(self, question: Question, question_id: int):
        self.db.cursor.execute("UPDATE Question SET title = ?, text = ?, position = ?, image = ? WHERE id IN (?);",
                               (question.title, question.text, question.position, question.image, question_id))

    def delete_question(self, question_id: int):
        self.db.cursor.execute(
            "DELETE FROM Question WHERE id IN (?);", question_id)

    # Queries on answers
    def get_answer(self, answer_id: int) -> tuple:
        res = self.db.cursor.execute(
            "SELECT * FROM Answer WHERE id IN (?)", answer_id)
        return res.fetchone()

    def get_all_answers_of_question(self, question_id: int) -> list:
        res = self.db.cursor.execute(
            "SELECT * FROM Answer WHERE id_question IN (?);", question_id)
        return res.fetchall()
    """retourne une liste de tuples"""

    def get_all_answers(self) -> list:
        res = self.db.cursor.execute("SELECT * FROM Answer")
        return res.fetchall()
    """retourne une liste de tuples"""

    def add_answer(self, answer: Answer, question_id: int):
        self.db.cursor.execute("INSERT INTO Answer (text, isCorrect, id_question) VALUES (?, ?, ?);",
                               (answer.text, answer.isCorrect, question_id))

    def add_answers(self, answers_list: list):
        self.db.cursor.executemany(
            "INSERT INTO Answer (text, isCorrect, id_question) VALUES (?, ?, ?);", answers_list)

    def update_answer(self, answer: Answer, question_id: int, answer_id: int):
        self.db.cursor.execute("UPDATE Answer SET text = ?, isCorrect = ?, id_question = ? WHERE id IN (?);",
                               (answer.text, answer.isCorrect, question_id, answer_id))

    def delete_answer(self, answer_id: int):
        self.db.cursor.execute(
            "DELETE FROM Answer WHERE id IN (?);", answer_id)

    # Queries on scores
    def get_score(self):
        pass

    def get_all_scores(self):
        pass

    def set_score(self):
        pass
