def validate_password(password: str) -> bool:
    password = password.strip()

    if len(password) == 0:
        return False

    return True