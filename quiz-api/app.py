from flask import Flask, request
from flask_cors import CORS
import auth
from models import Question
import db

app = Flask(__name__)
CORS(app)


@app.route('/quiz-info', methods=['GET'])
def get_quiz_info():
    # Get info from database
    database = db.Database("bdd.db")
    try:
        size = database.get_question_size()
        scores = database.get_all_scores()
    except Exception as e:
        return f'Error while requesting content: {e}', 500
    finally:
        database.close()

    return {"size": size, "scores": scores}, 200


@app.route('/login', methods=['POST'])
def login():
    payload: dict = request.get_json()  # type: ignore
    if auth.is_password_valid(payload["password"]):
        try:
            token = auth.create_token()
            return {"token": token}, 200
        except Exception:
            return "Internal Server Error", 500
    else:
        return 'Unauthorized', 401


@app.route('/questions/all', methods=['DELETE'])
def delete_all_question():
    # Check for admin auth
    # request.headers.get('Authorization')

    # Delete all questions from database
    database = db.Database("bdd.db")
    try:
        database.delete_all_question()
    except Exception as e:
        return f'Error while deleting content: {e}', 500
    finally:
        database.close()

    return 'All content deleted', 200


@app.route('/questions/<int:id>', methods=['GET'])
def get_question_id(id: int):
    # Check if the id arg was given
    if (id < 0):
        return 'Question id must be given', 422

    # Get request question or database
    database = db.Database("bdd.db")
    try:
        question = database.get_question_id(id)
    except Exception as e:
        return f'Error while requesting content: {e}', 500
    finally:
        database.close()

    # On vérifie que la question a bien été trouvé
    if question == None:
        return 'No question found', 404

    return question.to_json(), 200


@app.route('/questions/<int:id>', methods=['PUT'])
def update_question(id: int):
    # Check for admin auth
    # request.headers.get('Authorization')

    # Check if the id arg was given
    if (id < 0):
        return 'Question id must be given', 422

    # Read question in request
    try:
        payload: dict = request.get_json()  # type: ignore
        question = Question.from_json(payload)
    except Exception as e:
        return f'Cannot read question: {e}', 400

    # Update question at given postion in database
    database = db.Database("bdd.db")
    try:
        database.update_question(question, id)
    except Exception as e:
        return f'Error while updating content: {e}', 500
    finally:
        database.close()

    return 'Question updated', 200


@app.route('/questions', methods=['POST'])
def add_question():
    # Check for admin auth
    # request.headers.get('Authorization')

    # Read question in request
    try:
        payload: dict = request.get_json()  # type: ignore
        question = Question.from_json(payload)
    except Exception as e:
        return f'Cannot read question: {e}', 400

    # Add question in database
    database = db.Database("bdd.db")
    try:
        database.add_question(question)
    except Exception as e:
        return f'Error while inserting content: {e}', 500
    finally:
        database.close()

    return "Question inserted", 200


def score(questions, answers):
    # Calculate score
    score = 0
    for i in range(len(answers)):
        if questions[i].possibleAnswers[answers[i]-1].isCorrect:
            score += 1

    return score


@app.route('/participations', methods=['POST'])
def add_participation():
    try:
        payload = request.get_json()
        name = payload.name
        answers = payload.answers
    except Exception as e:
        return f'Cannot read question: {e}', 400

    # Get question in database
    database = db.Database("bdd.db")
    try:
        questions = database.get_all_questions()
        calculatedScore = score(questions, answers)
        database.set_score(name, calculatedScore)
    except Exception as e:
        return f'Error while getting or setting content: {e}', 500
    finally:
        database.close()

    return "Participation added", 200


if __name__ == '__main__':
    app.run()
