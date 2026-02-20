from utils import UPPERCASE, LOWERCASE, NUMBERS, SYMBOLS


def check(password):
    score = 0

    length = len(password)

    if length >= 8:
        score += 1
    elif length >= 12:
        score += 2
    elif length >= 16:
        score += 3
    else:
        score += 4

    has_upper = False
    has_lower = False
    has_numbers = False
    has_symbols = False

    for char in password:
        if has_upper and has_lower and has_numbers and has_symbols:
            break

        if char in UPPERCASE:
            has_upper = True
        elif char in LOWERCASE:
            has_lower = True
        elif char in NUMBERS:
            has_numbers = True
        elif char in SYMBOLS:
            has_symbols = True

    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_numbers:
        score += 1
    if has_symbols:
        score += 1

    if score <= 3:
        strength = "Weak"
    elif score <= 6:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength