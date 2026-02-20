from utils import UPPERCASE, LOWERCASE, NUMBERS, SYMBOLS
import secrets

class PasswordPolicy:
    def __init__(self, length=8, use_upper=True, use_lower=True, use_numbers=True, use_symbols=True):
        self.length = length
        self.use_upper = use_upper
        self.use_lower = use_lower
        self.use_numbers = use_numbers
        self.use_symbols = use_symbols


class PasswordGenerator:
    def __init__(self, policy: PasswordPolicy):
        self.policy = policy

    def generate(self):
        chars = ""

        if self.policy.use_upper:
            chars += UPPERCASE
        if self.policy.use_lower:
            chars += LOWERCASE
        if self.policy.use_numbers:
            chars += NUMBERS
        if self.policy.use_symbols:
            chars += SYMBOLS

        password = ""
        for i in range(self.policy.length):
            password += secrets.choice(chars)

        return password

