import jwt_utils

def is_password_valid(password: str) -> bool:
    return password == "flask2023"

def is_correctly_authenticated(jwt: str) -> bool:
    try:
        jwt_utils.decode_token(jwt)
    except jwt_utils.JwtError:
        return False
    return True

def get_identity(jwt: str) -> str:
    return jwt_utils.decode_token(jwt)

def create_token() -> str:
    try:
        return jwt_utils.build_token() 
    except Exception as e:
        raise RuntimeError("Can't create token") from e
        