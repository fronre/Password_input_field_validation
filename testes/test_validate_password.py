import pytest
from src.validate_password import validate_password


@pytest.mark.parametrize("password, expected_valid", [
    ("", False),
    ("abc", False),
    ("abcdefgh", False),
    ("ab12xyz", True),
])
def test_password_cases(password, expected_valid):
    result = validate_password(password)
    assert result["is_valid"] == expected_valid
