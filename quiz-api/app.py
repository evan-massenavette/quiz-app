from flask import Flask, request
from flask_cors import CORS
import auth
from models import Question

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
    payload = request.get_json()
    if auth.is_password_valid(payload["password"]):
        try:
            token = auth.create_token()
            return {"token": token}, 200
        except Exception:
            return "Internal Server Error", 500
    else:
        return 'Unauthorized', 401


@app.route('/questions', methods=['POST'])
def add_question():
    request.headers.get('Authorization')
    payload = request.get_json()
    mama = Question(payload)
    print()
    print(mama.to_json())
    print(mama["possibleAnswers"].to_json())
    print()
    return 'aze', 200


if __name__ == "__main__":
    app.run()
