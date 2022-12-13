from flask import Flask, request
from flask_cors import CORS
import auth

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    x = 'world'
    return f"Hello, {x}"

@app.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    if auth.is_password_valid(payload["password"]):
        try:
            token=auth.create_token()
            return {"token":token}, 200
        except Exception:
            return "Internal Server Error", 500
    else:
        return 'Unauthorized', 401

if __name__ == "__main__":
    app.run()
