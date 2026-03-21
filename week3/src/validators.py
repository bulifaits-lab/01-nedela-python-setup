# --- Validācijas funkcijas ---

def is_email(text):
    """
    Pārbauda, vai teksts ir vienkāršs e-pasts (satur @ un .).

    Args:
        text (str): ievades teksts

    Returns:
        bool: True, ja derīgs e-pasts

    Example:
        >>> is_email("anna@inbox.lv")
        True
    """
    if not isinstance(text, str):
        return False

    return "@" in text and "." in text and text.index("@") < text.rfind(".")


def is_phone_number(text):
    """
    Pārbauda, vai teksts ir Latvijas telefona numurs (+371 XXXXXXXX).

    Args:
        text (str): ievades teksts

    Returns:
        bool: True, ja derīgs numurs

    Example:
        >>> is_phone_number("+371 26123456")
        True
    """
    if not isinstance(text, str):
        return False

    if not text.startswith("+371 "):
        return False

    number_part = text[5:]

    return number_part.isdigit() and len(number_part) == 8


def is_valid_age(age):
    """
    Pārbauda, vai vecums ir derīgs (0–150).

    Args:
        age (int): vecums

    Returns:
        bool: True, ja derīgs vecums

    Example:
        >>> is_valid_age(25)
        True
    """
    if not isinstance(age, int):
        return False

    return 0 <= age <= 150


def is_strong_password(text):
    """
    Pārbauda, vai parole ir droša:
    vismaz 8 simboli, satur burtus un ciparus.

    Args:
        text (str): parole

    Returns:
        bool: True, ja droša parole

    Example:
        >>> is_strong_password("abc12345")
        True
    """
    if not isinstance(text, str):
        return False

    if len(text) < 8:
        return False

    has_letter = False
    has_digit = False

    for char in text:
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_digit = True

    return has_letter and has_digit


def is_valid_date(text):
    """
    Pārbauda, vai datums ir formātā YYYY-MM-DD (pamata pārbaude).

    Args:
        text (str): datums

    Returns:
        bool: True, ja derīgs formāts

    Example:
        >>> is_valid_date("2024-01-01")
        True
    """
    if not isinstance(text, str):
        return False

    parts = text.split("-")

    if len(parts) != 3:
        return False

    year, month, day = parts

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False

    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return False

    month = int(month)
    day = int(day)

    if not (1 <= month <= 12):
        return False

    if not (1 <= day <= 31):
        return False

    return True


# --- Testēšana ---

if __name__ == "__main__":
    print("# --- is_email ---")
    print(is_email("anna@inbox.lv"))   # True
    print(is_email("anna"))            # False
    print(is_email("anna@"))           # False

    print("\n# --- is_phone_number ---")
    print(is_phone_number("+371 26123456"))  # True
    print(is_phone_number("26123456"))       # False
    print(is_phone_number("+371 123"))       # False

    print("\n# --- is_valid_age ---")
    print(is_valid_age(25))   # True
    print(is_valid_age(-1))   # False
    print(is_valid_age(200))  # False

    print("\n# --- is_strong_password ---")
    print(is_strong_password("abc12345"))  # True
    print(is_strong_password("abcdefg"))   # False
    print(is_strong_password("12345678"))  # False

    print("\n# --- is_valid_date ---")
    print(is_valid_date("2024-01-01"))  # True
    print(is_valid_date("2024-13-01"))  # False
    print(is_valid_date("01-01-2024"))  # False