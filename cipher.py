def _transform(text: str, shift: int, alphabet: str, direction: int) -> str:
    n = len(alphabet)
    result = []
    for letter in text:
        x = alphabet.index(letter)             # numeric code = position in alphabet
        y = (x + direction * shift) % n        # Python's % is never negative, so (1-3) % 26 = 24
        result.append(alphabet[y])
    return "".join(result)


def encrypt(text: str, shift: int, alphabet: str) -> str:
    return _transform(text, shift, alphabet, +1)   # c = (x + k) mod n


def decrypt(text: str, shift: int, alphabet: str) -> str:
    return _transform(text, shift, alphabet, -1)   # m = (y - k) mod n