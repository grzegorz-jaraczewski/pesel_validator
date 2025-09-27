from datetime import datetime

from validator.constants import weights


def validate_pesel(pesel: str) -> dict:
    """
    Validate a Polish PESEL number and extract basic information.

    A PESEL (Polish national identification number) contains encoded
    information about the holder's date of birth, gender, and includes
    a checksum for validation.

    Validation steps:
        - Must be exactly 11 digits long.
        - Must have a valid checksum according to PESEL weights.
        - Must encode a valid birth_date (with century inferred from month).
        - Determines gender based on the 10th digit.

    Args:
        pesel (str): The PESEL number as a string of 11 digits.

    Returns:
        dict: A dictionary with the following keys:
            - "valid" (bool): True if the PESEL is valid, False otherwise.
            - "birth_date" (datetime.date, optional): Extracted date of birth if valid.
            - "gender" (str, optional): "Male" or "Female" if valid.
            - "error" (str, optional): Reason for invalidity if not valid.
    """

    if not pesel.isdigit() or len(pesel) != 11:
        return {"valid": False, "error": "PESEL must be 11 digits."}

    pesel_digits = [int(d) for d in pesel]
    pesel_check_sum = (10 - sum(w * d for w, d in zip(weights, pesel_digits)) % 10) % 10
    if pesel_check_sum != pesel_digits[-1]:
        return {"valid": False, "error": "Invalid checksum."}

    year, month, day = int(pesel[0:2]), int(pesel[2:4]), int(pesel[4:6])

    if 1 <= month <= 12:
        century = 1900
    elif 21 <= month <= 32:
        century = 2000
        month -= 20
    elif 41 <= month <= 52:
        century = 2100
        month -= 40
    elif 61 <= month <= 72:
        century = 2200
        month -= 60
    elif 81 <= month <= 92:
        century = 1800
        month -= 80
    else:
        return {"valid": False, "error": "Invalid month in PESEL."}

    try:
        birth_date = datetime(century + year, month, day).date()
    except ValueError:
        return {"valid": False, "error": "Invalid date in PESEL."}

    gender = "Female" if pesel_digits[9] % 2 == 0 else "Male"

    return {
        "valid": True,
        "birth_date": birth_date,
        "gender": gender
    }
