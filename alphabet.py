import unicodedata

# Table 2 of the handout: the position of a letter in this string is its numeric code.
# A Ă Â B C D E F G H I Î J K L M N O P Q R S Ș T Ț U V W X Y Z
# Written with \u escapes so editor encoding can never corrupt it.
LETTERS = "A\u0102\u00C2BCDEFGHI\u00CEJKLMNOPQRS\u0218T\u021AUVWXYZ"

N = len(LETTERS)  # 31

MIN_SHIFT = 1
MAX_SHIFT = 30
MIN_KEYWORD_LENGTH = 7


def normalize(value: str) -> str:
    """Uppercase and turn the cedilla variants (Ş, Ţ) into Ș, Ț."""
    value = unicodedata.normalize("NFC", value).upper()
    return value.replace("\u015E", "\u0218").replace("\u0162", "\u021A")


def is_letter(c: str) -> bool:
    return c in LETTERS


def build_permuted(keyword: str) -> str:
    """Keyword letters first (first occurrence only), then the remaining letters."""
    seen = []
    for c in keyword + LETTERS:
        if c not in seen:
            seen.append(c)
    return "".join(seen)