🧩 Kata 3 – Password Input Field Validation
📖 Description

This kata focuses on implementing and testing a password validation function.
The goal is to verify that a given password meets a set of predefined security rules using regular expressions (regex) and automated tests with pytest.

🧠 Requirements

A valid password must satisfy all the following conditions:

At least 8 characters long

Contains at least two digits

Contains at least one lowercase letter

Contains at least one uppercase letter

Contains at least one special character (symbol)

Must not consist only of symbols

⚙️ Implementation

The validation logic is implemented in:
src/validate_password.py

import re

def validate_password(password: str) -> dict:
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d.*\d)(?=.*[^A-Za-z0-9])(?!^[^A-Za-z0-9]+$).{8,}$'
    is_valid = bool(re.match(pattern, password))
    return {
        "is_valid": is_valid,
        "errors": [] if is_valid else ["Password is invalid"]
    }

🧪 Tests

The tests are implemented using pytest in:
testes/test_validate_password.py

import pytest
from src.validate_password import validate_password

@pytest.mark.parametrize("password, expected_valid", [
    ("aB1@", False),
    ("abc123", False),
    ("Ab12@", False),
    ("Abcdefgh@", False),
    ("Abcdefg1@", False),
    ("AB12@XYZ", False),
    ("1234@AAAA", False),
    ("ab12@xyz", False),
    ("password12@", False),
    ("Ab12xyz3", False),
    ("Pass12word", False),
    ("@#$%^&*!", False),
    ("@@@@@@@_", False),
    ("12345678", False),
    ("9876543210", False),
    ("abcdefgh", False),
    ("ABCDEFGH", False),
    ("12@34@56", False),
    ("Ab12@xyz", True),
    ("Pass12word@", True),
    ("Aa11@aaaa", True),
    ("Hello12@", True),
    ("StrongP@ss12", True),
    ("MyPass123@", True),
    ("A1b2@c3D", True),
    ("Aa12#test", True),
    ("Good@P4ssword", True),
    ("Y0u$GotIt12", True),
    ("123@@@", False),
    ("Ab12 @xyz", False),
    ("Ab12", False),
])
def test_password_cases(password, expected_valid):
    result = validate_password(password)
    assert result["is_valid"] == expected_valid, f"Failed for password: {password}"

▶️ Run Tests

Make sure you have pytest installed:

pip install pytest


Then run all tests:

pytest

✅ Example Output
=========================== test session starts ============================
collected 33 items

testes/test_validate_password.py .........................         [100%]

=========================== 33 passed in 0.25s ============================

🧾 Author

Name: hala nohammed islam
Project: Password Validation Kata (TDD Approach)
Year: 2025
