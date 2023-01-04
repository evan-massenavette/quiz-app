import jwt_utils


def strip_token(jwt: str):
    return jwt.split(' ')[1]


def is_password_valid(password: str) -> bool:
    return password == "flask2023"


def is_correctly_authenticated(jwt: str | None) -> bool:
    if jwt is None:
        return False
    try:
        jwt_utils.decode_token(strip_token(jwt))
    except jwt_utils.JwtError:
        return False
    return True


def get_identity(jwt: str) -> str:
    return jwt_utils.decode_token(strip_token(jwt))


def create_token() -> str:
    try:
        return jwt_utils.build_token()
    except Exception as e:
        raise RuntimeError("Can't create token") from e
