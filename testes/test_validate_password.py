import pytest
from src.validate_password import validate_password


@pytest.mark.parametrize("password, expected_valid", [
    ("", False),
    ("abc", False),
    ("abcdefgh", False),
    ("ab1xyz2h", True),
    ("AB12@XYZ", False),
    ("@&-@&-@_", False),
    ("Abcdefg1", False),
    ("Ab12@xyz", True),
    ("password12", False),
    ("Pass12word@", True),
    ("12345678", False),
    ("ABCDEFGH12@", False),
    ("aB12cdef@", True),
    ("A1b@", False),
    ("Aa11@aaaa", True),
])
def test_password_cases(password, expected_valid):
    result = validate_password(password)
    assert result["is_valid"] == expected_valid
