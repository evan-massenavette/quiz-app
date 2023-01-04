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

    # Build database tables
    def build_tables(self):
        drop_table_question = "DROP TABLE IF EXISTS Question"
        drop_table_result = "DROP TABLE IF EXISTS Result"
        create_table_question = """
        CREATE TABLE Question (
            id INTEGER NOT NULL UNIQUE,
            title TEXT NOT NULL,
            text TEXT NOT NULL,
            position INTEGER NOT NULL UNIQUE,
            image TEXT NOT NULL,
            answer0 TEXT NOT NULL,
            answer1 INTEGER NOT NULL,
            answer2 INTEGER,
            answer3 INTEGER,
            correct_answer    INTEGER NOT NULL,
            PRIMARY KEY(id AUTOINCREMENT)
        )
        """
        create_table_result = """
        CREATE TABLE Result (
            id INTEGER NOT NULL UNIQUE,
            name TEXT NOT NULL,
            score INTEGER NOT NULL,
            PRIMARY KEY(id AUTOINCREMENT)
        )
        """
        self.cursor.execute(drop_table_question)
        self.cursor.execute(drop_table_result)
        self.cursor.execute(create_table_question)
        self.cursor.execute(create_table_result)
        return 200, "Ok"

    def add_initial_data(self):
        return 501, 'Not implemented yet'

    # Queries on questions

    def get_max_position(self) -> int:
        res = self.cursor.execute('SELECT MAX(position) FROM Question;')
        max_position = res.fetchone()[0]
        if max_position is None:
            return 0
        return int(max_position)

    def get_questions_amount(self) -> int:
        return self.cursor.execute('SELECT COUNT(*) FROM Question;').fetchone()[0]

    def get_question_from_id(self, question_id: int) -> Question:
        """Get a question from its id. Raises a ValueError if no question is found with the given id."""
        res = self.cursor.execute(
            'SELECT * FROM Question WHERE id=?;', (question_id,))

        # Check if result is not empty
        question_tuple = res.fetchone()
        if question_tuple is None:
            raise ValueError(f'No question exists with id {question_id}')
        return Question.from_tuple(question_tuple)

    def get_question_from_pos(self, question_pos: int) -> Question:
        """Get a question from its position. Raises a ValueError if no question is found with the given position."""
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

    def update_question_from_id(self, question: Question, question_id: int) -> bool:
        """Returns True if it succeeds, otherwise returns False"""
        try:
            self.cursor.execute('UPDATE Question SET title = ?, text = ?, position = ?, image = ?, answer0 = ?, answer1 = ?, answer2 = ?, answer3 = ?, correct_answer = ? WHERE id=?;',
                                question.to_tuple()+(question_id,))
        except IndexError:
            return False
        return True

    def update_question_from_pos(self, question: Question, question_pos: int) -> bool:
        """Returns True if it succeeds, otherwise returns False"""
        try:
            self.cursor.execute('UPDATE Question SET title = ?, text = ?, position = ?, image = ?, answer0 = ?, answer1 = ?, answer2 = ?, answer3 = ?, correct_answer = ? WHERE position=?;',
                                question.to_tuple()+(question_pos,))
        except IndexError:
            return False
        return True

    def delete_question(self, question_id: int):
        """Deletes question with given id from the database. Raises a ValueError if no question with a matching id is found"""
        self.cursor.execute(
            'DELETE FROM Question WHERE id=?;', (question_id,))
        # Check if a question was deleted
        if self.cursor.rowcount == 0:
            raise ValueError(f'No question exists with id {question_id}')

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
