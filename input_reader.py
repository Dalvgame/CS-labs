import sys

import alphabet


def _ask(prompt: str) -> str:
    try:
        return input(prompt)
    except EOFError:
        sys.exit(0)


def read_choice(prompt: str, allowed: str) -> str:
    while True:
        value = _ask(prompt).strip().upper()
        if len(value) == 1 and value in allowed:
            return value
        print(f"Invalid choice. Allowed values: {', '.join(allowed)}.")


def read_shift() -> int:
    """Key 1: integer from 1 to 30 inclusive."""
    while True:
        value = _ask(f"Enter the numeric key ({alphabet.MIN_SHIFT}-{alphabet.MAX_SHIFT}): ").strip()
        if value.isascii() and value.isdigit():
            shift = int(value)
            if alphabet.MIN_SHIFT <= shift <= alphabet.MAX_SHIFT:
                return shift
        print(f"Invalid key. Enter an integer from {alphabet.MIN_SHIFT} to {alphabet.MAX_SHIFT} inclusive.")


def read_keyword() -> str:
    """Key 2: Romanian letters only, at least 7 characters. Returned in uppercase."""
    while True:
        keyword = alphabet.normalize(
            _ask(f"Enter the keyword (at least {alphabet.MIN_KEYWORD_LENGTH} Romanian letters): ").strip()
        )

        invalid = next((c for c in keyword if not alphabet.is_letter(c)), None)
        if invalid is not None:
            print(f"Invalid keyword character: '{invalid}'. "
                  f"Use only Romanian alphabet letters (no spaces): {alphabet.LETTERS}.")
            continue

        if len(keyword) < alphabet.MIN_KEYWORD_LENGTH:
            print(f"Invalid keyword. It must contain at least {alphabet.MIN_KEYWORD_LENGTH} "
                  f"letters (you entered {len(keyword)}).")
            continue

        return keyword


def read_text(prompt: str) -> str:
    """Letters (upper or lower case) and spaces. Returned uppercase, spaces removed."""
    while True:
        text = alphabet.normalize(_ask(prompt))

        invalid = next((c for c in text if c != " " and not alphabet.is_letter(c)), None)
        if invalid is not None:
            print(f"Invalid text character: '{invalid}'. "
                  f"Use only spaces and Romanian alphabet letters: {alphabet.LETTERS}.")
            continue

        text = text.replace(" ", "")
        if not text:
            print("The text is empty. Enter at least one letter.")
            continue

        return text