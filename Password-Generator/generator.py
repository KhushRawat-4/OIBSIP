import random
import string


def generate_password(
    length,
    uppercase=True,
    lowercase=True,
    numbers=True,
    symbols=True
):
    """
    Generate a random password based on the selected options.
    """

    characters = ""

    if uppercase:
        characters += string.ascii_uppercase

    if lowercase:
        characters += string.ascii_lowercase

    if numbers:
        characters += string.digits

    if symbols:
        characters += "!@#$%^&*()-_=+[]{}<>?/"

    if not characters:
        raise ValueError("Select at least one character type.")

    password = "".join(
        random.choice(characters)
        for _ in range(length)
    )

    return password