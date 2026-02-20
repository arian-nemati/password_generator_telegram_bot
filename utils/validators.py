def is_valid_number(text):
    return text.isdigit() and int(text) >= 8


def is_valid_yes_no(text):
    return text.lower().strip() in ["yes", "no", "y", "n"]