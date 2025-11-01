from src.validate_password import validate_password

def test_password_has_less_than_two_digits():
    password = "abcdefgiklm"
    assert validate_password(password) == False
    result = validate_password(password)

def test_password_missing_capital_letters():
        password = "ab12@abcd"
        assert validate_password(password) == False
        result = validate_password(password)



