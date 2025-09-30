from datetime import date
from validator.utils import validate_pesel


def test_valid_pesel_1900s_male():
    """
    Verify that a valid PESEL from the 1900s is correctly parsed.

    - PESEL: 44051401359
    - Expected birth_date: 14 May 1944
    - Expected gender: Male
    """
    pesel = "44051401359"
    output = validate_pesel(pesel)
    assert output["valid"] is True
    assert output["birth_date"] == date(year=1944, month=5, day=14)
    assert output["gender"] == "Male"


def test_valid_pesel_2000s_female():
    """
    Verify that a valid PESEL from the 2000s is correctly parsed.

    - PESEL: 02311311145
    - Expected birth_date: 13 November 2002
    - Expected gender: Female
    """
    pesel = "02311311145"
    output = validate_pesel(pesel)
    assert output["valid"] is True
    assert output["birth_date"] == date(year=2002, month=11, day=13)
    assert output["gender"] == "Female"


def test_invalid_length():
    """
    A PESEL must be exactly 11 digits.
    This test ensures that too short or too long inputs are rejected.
    """
    pesel = "12345"
    output = validate_pesel(pesel)
    assert output == {"valid": False, "error": "PESEL must be 11 digits."}


def test_non_digit_characters():
    """
    A PESEL must consist only of digits.
    This test ensures that alphanumeric strings are rejected.
    """
    pesel = "1234abc8911"
    output = validate_pesel(pesel)
    assert output == {"valid": False, "error": "PESEL must be 11 digits."}


def test_invalid_checksum():
    """
    A PESEL must pass its checksum validation.
    This test ensures that otherwise well-formed PESELs with a bad checksum are rejected.
    """
    pesel = "80060910045"
    output = validate_pesel(pesel)
    assert output == {"valid": False, "error": "Invalid checksum."}


def test_invalid_month():
    """
    A PESEL must encode a valid month (or century-modified month).
    This test uses a PESEL with an invalid month (19).
    """
    pesel = "99191512340"
    output = validate_pesel(pesel)
    assert output == {"valid": False, "error": "Invalid month in PESEL."}


def test_invalid_date():
    """
    A PESEL must encode a valid calendar date.
    This test uses 31 February 1999, which is invalid.
    """
    pesel = "99023112340"
    output = validate_pesel(pesel)
    assert output == {"valid": False, "error": "Invalid date in PESEL."}
