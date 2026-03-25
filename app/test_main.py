from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_too_short_password() -> None:
    assert check_password("Str@ng") is False


def test_no_digit() -> None:
    assert check_password("Password@") is False


def test_no_special_char() -> None:
    assert check_password("Password1") is False


def test_no_uppercase() -> None:
    assert check_password("pass@word1") is False


def test_too_long_password() -> None:
    assert check_password("VeryL0ngP@ssword123") is False


def test_min_length_valid() -> None:
    assert check_password("Abcdef@1") is True


def test_max_length_valid() -> None:
    assert check_password("Abcdefghij@1234") is True


def test_invalid_character() -> None:
    assert check_password("Pass word1@") is False


def test_only_allowed_special_chars() -> None:
    assert check_password("Good#Pass1") is True
