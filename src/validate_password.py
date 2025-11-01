def validate_password(password):
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters")

    digits = sum(c.isdigit() for c in password)
    if digits < 2:
        errors.append("The password must contain at least 2 numbers")

    if not any(c.islower() for c in password):
        errors.append("The password must contain at least one lowercase letter")

    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }
