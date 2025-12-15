from bcrypt import hashpw, gensalt, checkpw

def pass_hash(password: str):
    return hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")

def verify_pass(password: str, hash_password: str) -> str:
    try:
        return checkpw(password.encode("utf-8"), hash_password.encode("utf-8"))
    except ValueError:
        return False