import random
import re
import string


class PasswordGenerator:
    """
    Random password generator
    """

    def __init__(self, words: str, length: int = 12) -> None:
        self.words = words.split()
        self.length = length

    def generate(self) -> str:
        password = ""
        while len(password) < self.length - 8:
            word = random.choice(self.words)
            password += word.capitalize() if len(password) == 0 else word
        password += random.choice(string.punctuation)
        password += random.choice(string.digits)
        password += random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        symbols = string.punctuation + string.digits + string.ascii_letters
        while any(c in password for c in symbols):
            password += random.choice(symbols)
            symbols = symbols.replace(password[-1], "")
        password = "".join(random.sample(password, len(password)))
        return password

    @classmethod
    def user_secret_words(cls) -> str:
        while True:
            words = input("Enter some words separated by spaces: ")
            words_regex = re.compile(r"\b\D+\b(?:,\s*\b\D+\b)*")
            if not words_regex.match(words):
                print("Response not valid! Kindly enter a valid sentence...")
                cls.user_secret_words()
            break
        return words


def main():
    words = PasswordGenerator.user_secret_words()
    password_generator = PasswordGenerator(words)
    password = password_generator.generate()
    print(f"Your generated password is: {password}")


if __name__ == "__main__":
    main()
