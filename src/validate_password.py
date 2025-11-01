def validate_password(password: str) -> bool:
    password = password.strip()

    if len(password) == 0:
        return False
    if len(password) < 8:
        return False

    if sum(c.isdigit() for c in password) < 2:
        return False


    return True