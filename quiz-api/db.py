import sqlite3
from models import Question, Answer


class Database():
    """
    Open and close connection to the database. Make queries while database is open.
    """

    def __init__(self, url: str):
        self.connection = sqlite3.connect(url, isolation_level=None)
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()

    # Queries on questions
    def get_questions_amount(self) -> int:
        return self.cursor.execute('SELECT COUNT(*) FROM Question;').fetchone()[0]

    def get_question_from_id(self, question_id: int) -> Question:
        res = self.cursor.execute(
            'SELECT * FROM Question WHERE id=?;', (question_id,))

        # Check if result is not empty
        question_tuple = res.fetchone()
        if question_tuple is None:
            raise ValueError(f'No question exists with id {question_id}')
        return Question.from_tuple(question_tuple)

    def get_question_from_pos(self, question_pos: int) -> Question:
        res = self.cursor.execute(
            'SELECT * FROM Question WHERE position=?;', (question_pos,))

        # Check if result is not empty
        question_tuple = res.fetchone()
        if question_tuple is None:
            raise ValueError(f'No question exists at position {question_pos}')
        return Question.from_tuple(question_tuple)

    def get_all_questions(self) -> list[Question]:
        res = self.cursor.execute(
            'SELECT * FROM Question ORDER BY position ASC')
        return [Question.from_tuple(x) for x in res.fetchall()]

    def add_question(self, question: Question):
        self.cursor.execute('INSERT INTO Question (title, text, position, image, answer0, answer1, answer2, answer3, correct_answer) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);',
                            question.to_tuple())
        return self.cursor.lastrowid

    def update_question(self, question: Question, question_id: int) -> bool:
        try:
            self.cursor.execute('UPDATE Question SET title = ?, text = ?, position = ?, image = ?, answer0 = ?, answer1 = ?, answer2 = ?, answer3 = ?, correct_answer = ? WHERE id=?;',
                                question.to_tuple()+(question_id,))
        except IndexError:
            return False
        return True

    def delete_question(self, question_id: int) -> bool:
        self.cursor.execute(
            'DELETE FROM Question WHERE id=?;', (question_id,))
        return self.cursor.rowcount > 0

    def delete_all_questions(self):
        self.cursor.execute('DELETE FROM Question;')

    # Queries on scores
    def get_all_scores(self) -> list[dict]:
        res = self.cursor.execute('SELECT * FROM Result;')
        return [{'name': x.name, 'score': x.score} for x in res.fetchall()]

    def set_score(self, name, score):
        self.cursor.execute(
            'INSERT INTO Result (name,score) VALUES (?, ?);', (name, score))

    def delete_all_scores(self):
        self.cursor.execute('DELETE FROM Result;')
