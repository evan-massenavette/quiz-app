import sqlite3
from models import Question, Answer


def insert_question(question: Question) -> int:
    # (n'utilise pas l'isolation)
    conn = sqlite3.connect("bdd.db", isolation_level=None)

    try:
        # gere les commit/rollback avec le ressources managers
        with conn:
            question_insertion_result = conn.execute("INSERT INTO Question (title, text, position, image) VALUES (?, ?, ?, ?)", (
                question.title, question.text, question.position, question.image))
            question_id = question_insertion_result.lastrowid
            answers_list = list(
                map(lambda x: (x.text, x.isCorrect, question_id), question.possibleAnswers))
            conn.executemany(
                "INSERT INTO Answer (text, isCorrect, id_question) VALUES (?, ?, ?)", answers_list)

    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()

    return question_id
