import re


def validate_password(password: str) -> dict:
    if " " in password:
        return {"is_valid": False, "errors": ["Password cannot contain spaces"]}

    pattern = (
        r'^(?=.*[a-z])'
        r'(?=.*[A-Z])'
        r'(?=(?:.*\d){2,})'
        r'(?=.*[^A-Za-z0-9])'
        r'(?!^[^A-Za-z0-9]+$)'
        r'.{8,}$'
    )

    is_valid = bool(re.fullmatch(pattern, password))
    return {
        "is_valid": is_valid,
        "errors": [] if is_valid else ["Password is invalid"]
    }

