# --- Virkņu funkcijas ---

def capitalize(text):
    """
    Pārveido virknes pirmo burtu par lielo.

    Args:
        text (str): ievades teksts

    Returns:
        str: teksts ar lielo sākumburtu

    Example:
        >>> capitalize("hello")
        'Hello'
    """
    if not isinstance(text, str):
        raise ValueError("text jābūt virknei (str)")
    return text[:1].upper() + text[1:]


def truncate(text, max_len=20):
    """
    Apgriež tekstu līdz max_len simboliem un pievieno "...", ja nepieciešams.

    Args:
        text (str): ievades teksts
        max_len (int): maksimālais garums

    Returns:
        str: apgrieztais teksts

    Example:
        >>> truncate("Šis ir ļoti garš teksts", 10)
        'Šis ir ļ...'
    """
    if not isinstance(text, str):
        raise ValueError("text jābūt virknei (str)")
    if not isinstance(max_len, int) or max_len < 0:
        raise ValueError("max_len jābūt nenegatīvam veselam skaitlim")

    if len(text) <= max_len:
        return text
    return text[:max_len] + "..."


def count_words(text):
    """
    Saskaita vārdus tekstā.

    Args:
        text (str): ievades teksts

    Returns:
        int: vārdu skaits

    Example:
        >>> count_words("Hello world!")
        2
    """
    if not isinstance(text, str):
        raise ValueError("text jābūt virknei (str)")
    return len(text.split())


# --- Skaitļu funkcijas ---

def clamp(num, low, high):
    """
    Ierobežo skaitli norādītajā diapazonā.

    Args:
        num (int|float): skaitlis, ko ierobežot
        low (int|float): minimālā robeža
        high (int|float): maksimālā robeža

    Returns:
        int vai float: ierobežotā vērtība

    Example:
        >>> clamp(15, 0, 10)
        10
    """
    if low > high:
        raise ValueError("low nedrīkst būt lielāks par high")
    return max(low, min(num, high))


def is_prime(num):
    """
    Pārbauda, vai skaitlis ir pirmskaitlis.

    Args:
        num (int): skaitlis

    Returns:
        bool: True, ja pirmskaitlis

    Example:
        >>> is_prime(7)
        True
    """
    if not isinstance(num, int):
        raise ValueError("num jābūt veselam skaitlim")
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def factorial(n):
    """
    Aprēķina n! (faktoriālu).

    Args:
        n (int): nenegatīvs vesels skaitlis

    Returns:
        int: n faktoriāls

    Example:
        >>> factorial(5)
        120
    """
    if not isinstance(n, int):
        raise ValueError("n jābūt veselam skaitlim")
    if n < 0:
        raise ValueError("n jābūt >= 0")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# --- Sarakstu funkcijas ---

def total(numbers):
    """
    Aprēķina saraksta summu (bez sum()).

    Args:
        numbers (list): skaitļu saraksts

    Returns:
        int|float: summa

    Example:
        >>> total([1, 2, 3])
        6
    """
    if not isinstance(numbers, list):
        raise ValueError("numbers jābūt sarakstam")

    s = 0
    for num in numbers:
        s += num
    return s


def average(numbers):
    """
    Aprēķina saraksta vidējo vērtību.

    Args:
        numbers (list): skaitļu saraksts

    Returns:
        float: vidējā vērtība

    Example:
        >>> average([1, 2, 3])
        2.0
    """
    if not isinstance(numbers, list):
        raise ValueError("numbers jābūt sarakstam")
    if len(numbers) == 0:
        raise ValueError("saraksts nedrīkst būt tukšs")

    return total(numbers) / len(numbers)


# --- Demonstrācija ---

if __name__ == "__main__":
    print(capitalize("hello"))
    print(truncate("Šis ir ļoti garš teksts", 10))
    print(count_words("Šis ir tests"))

    print(clamp(15, 0, 10))
    print(is_prime(7))
    print(factorial(5))

    print(total([1, 2, 3, 4]))
    print(average([1, 2, 3, 4]))
