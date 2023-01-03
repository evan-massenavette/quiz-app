from flask import Flask, request
from flask_cors import CORS
import auth
from models import Question
from db import Database

app = Flask(__name__)
CORS(app)

DB_URL = 'bdd.db'

###
# questions requests
###


@app.route('/quiz-info', methods=['GET'])
def get_quiz_info():
    # Get info from database
    database = Database(DB_URL)
    try:
        size = database.get_questions_amount()
        scores = database.get_all_scores()
    except Exception as e:
        return f'Error while requesting content: {e}', 500
    finally:
        database.close()

    return {'size': size, 'scores': scores}, 200


@app.route('/questions/<int:id>', methods=['GET'])
def get_question_from_id(id: int):
    # Check if the id arg was given
    if (id < 0):
        return 'Question id must be given', 422

    # Get request question or database
    database = Database(DB_URL)
    try:
        question = database.get_question_from_id(id)
    except ValueError:
        return 'Non existent content', 404
    except Exception as e:
        return f'Error while requesting content: {e}', 500
    finally:
        database.close()

    # On vérifie que la question a bien été trouvé
    if question == None:
        return 'No question found', 404

    return question.to_json(), 200


@app.route('/questions', methods=['GET'])
def get_question_from_pos():
    # Check if the pos arg was given
    pos = request.args.get('position', None, type=int)
    if pos is None:
        return 'Question pos must be given', 422

    # Get request question or database
    database = Database(DB_URL)
    try:
        question = database.get_question_from_pos(pos)
    except ValueError:
        return 'Non existent content', 404
    except Exception as e:
        return f'Error while requesting content: {e}', 500
    finally:
        database.close()

    # On vérifie que la question a bien été trouvé
    if question == None:
        return 'No question found', 404

    return question.to_json(), 200


@app.route('/login', methods=['POST'])
def login():
    payload = dict(request.get_json())  # type: ignore
    if auth.is_password_valid(payload['password']):
        try:
            token = auth.create_token()
            return {'token': token}, 200
        except Exception:
            return 'Internal Server Error', 500
    else:
        return 'Unauthorized', 401


@app.route('/questions/all', methods=['DELETE'])
def delete_all_questions():
    # Check for admin auth
    # request.headers.get('Authorization')

    # Delete all questions from database
    database = Database(DB_URL)
    try:
        database.delete_all_questions()
    except Exception as e:
        return f'Error while deleting content: {e}', 500
    finally:
        database.close()

    return 'All content deleted', 204


@app.route('/questions/<int:id>', methods=['DELETE'])
def delete_question(id: int):
    # Check for admin auth
    # request.headers.get('Authorization')

    # Delete all questions from database
    database = Database(DB_URL)
    try:
        if not database.delete_question(id):
            return 'No existing content', 404
    except Exception as e:
        return f'Error while deleting content: {e}', 500
    finally:
        database.close()

    return 'Content deleted', 204


@app.route('/questions/<int:id>', methods=['PUT'])
def update_question(id: int):
    # Check for admin auth
    # request.headers.get('Authorization')

    # Check if the id arg was given
    if (id < 0):
        return 'Question id must be given', 422

    # Read question in request
    try:
        payload = dict(request.get_json())  # type: ignore
        question = Question.from_json(payload)
    except Exception as e:
        return f'Cannot read question: {e}', 400

    # Update question at given position in database
    database = Database(DB_URL)
    try:
        if not database.update_question(question, id):
            return 'Non existent content', 404
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
        payload = dict(request.get_json())  # type: ignore
        question = Question.from_json(payload)
    except Exception as e:
        return f'Cannot read question: {e}', 400

    # Add question in database
    database = Database(DB_URL)
    try:
        id = database.add_question(question)
    except Exception as e:
        return f'Error while inserting content: {e}', 500
    finally:
        database.close()

    return {"id": id}, 200

###
# Participations requests
###


def score(questions, answers):
    # Calculate score
    score = 0
    for i in range(len(questions)):
        if questions[i].possibleAnswers[answers[i]-1].isCorrect:
            score += 1

    return score


@app.route('/participations', methods=['POST'])
def add_participation():
    try:
        payload = dict(request.get_json())  # type: ignore
    except Exception as e:
        return f'Cannot read question: {e}', 400

    # Get question in database
    database = Database(DB_URL)
    try:
        questions = database.get_all_questions()
        answers = payload['answers']
        if len(questions) != len(answers):
            return 'Wrong number of answers', 400
        calculatedScore = score(questions, answers)
        database.set_score(payload['name'], calculatedScore)
    except Exception as e:
        return f'Error while getting or setting content: {e}', 500
    finally:
        database.close()

    return "Participation added", 200


@app.route('/participations/all', methods=['DELETE'])
def delete_all_participations():
    # Check for admin auth
    # request.headers.get('Authorization')

    # Delete all questions from database
    database = Database(DB_URL)
    try:
        database.delete_all_scores()
    except Exception as e:
        return f'Error while deleting content: {e}', 500
    finally:
        database.close()

    return 'All content deleted', 204


if __name__ == '__main__':
    app.run()
