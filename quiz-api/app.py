from flask import Flask, request
from flask_cors import CORS

import auth
from database import Database
from models import Question

app = Flask(__name__)
CORS(app)

DB_URL = 'bdd.db'

###
# Rebuild database / Add static data
###


@app.route('/rebuild-db', methods=['POST'])
def rebuild_database():
    database = Database(DB_URL)
    try:
        database.build_tables()
    except Exception as e:
        return f'Error while rebuilding database: {e}', 500
    finally:
        database.close()
    return 'Ok', 200


@app.route('/add-initial-data', methods=['POST'])
def add_initial_data():
    return 501, 'Not implemented yet'


###
# Questions requests
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
    jwt = request.headers.get('Authorization')
    if not auth.is_correctly_authenticated(jwt):
        return 'Unauthorized', 401

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
    jwt = request.headers.get('Authorization')
    if not auth.is_correctly_authenticated(jwt):
        return 'Unauthorized', 401

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


def shift_questions(database: Database, pos_range: range, pos_shift: int):
    pos_list = list(pos_range)
    if pos_shift > 0:
        pos_list.reverse()

    for old_pos in pos_list:
        question_to_change = database.get_question_from_pos(old_pos)
        question_to_change.position += pos_shift
        database.update_question_from_pos(question_to_change, old_pos)


@app.route('/questions/<int:id>', methods=['PUT'])
def update_question(id: int):
    # Check for admin auth
    jwt = request.headers.get('Authorization')
    if not auth.is_correctly_authenticated(jwt):
        return 'Unauthorized', 401

    # Check if id arg is valid
    if (id < 0):
        return 'Question id must be positive', 422

    # Read question in request
    try:
        payload = dict(request.get_json())  # type: ignore
        question = Question.from_json(payload)
    except Exception as e:
        return f'Cannot read question: {e}', 400

    # Connect to database
    database = Database(DB_URL)

    try:
        question_with_same_id = database.get_question_from_id(id)
    except ValueError as e:
        database.close()
        return f'No question exists with id {id}', 404
    old_position = question_with_same_id.position
    new_position = question.position

    if new_position == old_position:
        database.update_question_from_id(question, id)
        return 'Question updated', 204

    # Check that new_position is in valid bounds
    max_position = database.get_max_position()
    if new_position > max_position:
        database.close()
        return f'Given position ({new_position}) is higher than maximum position ({max_position})', 500

    # Move question out of the way to allow for shifting
    question.position = max_position+2
    res = database.update_question_from_id(question, id)

    # Question gets moved down in position : move others up in position
    if (new_position < old_position):
        pos_range = range(new_position, old_position)
        pos_shift = 1

    # Question gets moved up in position : move others down in position
    else:
        pos_range = range(old_position+1, new_position+1)
        pos_shift = -1

    # Reorder questions
    try:
        shift_questions(database, pos_range, pos_shift)
    except Exception as e:
        database.close()
        return f'Error while reordering questions: {e}', 500

    # Update given question in database
    try:
        question.position = new_position
        database.update_question_from_id(question, id)
    except Exception as e:
        return f'Error while updating content: {e}', 500
    finally:
        database.close()

    return 'Question updated', 204


@app.route('/questions', methods=['POST'])
def add_question():
    # Check for admin auth
    jwt = request.headers.get('Authorization')
    if not auth.is_correctly_authenticated(jwt):
        return 'Unauthorized', 401

    # Read question in request
    try:
        payload = dict(request.get_json())  # type: ignore
        question = Question.from_json(payload)
    except Exception as e:
        return f'Cannot read question: {e}', 400

    # Connect to database
    database = Database(DB_URL)

    new_max_position = database.get_max_position() + 1
    new_position = question.position

    # Check that old_position is in valid bounds
    if new_position > new_max_position:
        database.close()
        return f'Given position ({new_position}) is higher than maximum allowed position ({new_max_position})', 500

    # Question gets added at new pos : move others up in position
    pos_range = range(new_position, new_max_position)
    pos_shift = 1

    # Reorder questions
    try:
        shift_questions(database, pos_range, pos_shift)
    except Exception as e:
        database.close()
        return f'Error while reordering questions: {e}', 500

    # Add question in database
    try:
        id = database.add_question(question)
    except Exception as e:
        return f'Error while inserting content: {e}', 500
    finally:
        database.close()

    return {'id': id}, 200

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
    jwt = request.headers.get('Authorization')
    if not auth.is_correctly_authenticated(jwt):
        return 'Unauthorized', 401

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
