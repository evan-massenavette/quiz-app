from flask import Flask, request
from flask_cors import CORS
import auth
from models import Question
import database

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    x = 'world'
    return f"Hello, {x}"


@app.route('/quiz-info', methods=['GET'])
def get_quiz_info():
    return {"size": 0, "scores": []}, 200


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

    return 'Not implemented', 501


@app.route('/questions', methods=['GET'])
def get_question():
    # Check if the position arg was given
    if (not request.args['position']):
        return 'Question position must be given', 422

    # Get request question or database<

    return 'Not implemented', 501


@app.route('/questions', methods=['PUT'])
def update_question():
    # Check for admin auth
    # request.headers.get('Authorization')

    # Read question in request
    try:
        payload: dict = request.get_json()  # type: ignore
        question = Question.from_json(payload)
    except Exception as e:
        return f'Cannot read question: {e}', 400

    # Update question at given postion in database

    return 'Not implemented', 501


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

    question_id = database.insert_question(question)
    return {"id": question_id}, 200


if __name__ == '__main__':
    app.run()
