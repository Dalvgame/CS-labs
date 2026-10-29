# -*- coding: utf-8 -*-
"""Pregatirea si validarea textului introdus de utilizator."""

import string

from config import (CHAR_TO_CODE, CEDILLA_FIX, MIN_KEY_LEN, RANGE_HINT)


def is_latin_letter(ch):
    """True daca ch este in 'A'-'Z' sau 'a'-'z'."""
    return ch in string.ascii_letters


def prepare(text, allow_romanian=False):
    """
    Pregateste textul: 1) elimina spatiile, 2) transforma in majuscule.
    Intoarce (text_pregatit, lista_caractere_invalide).
    """
    text = text.translate(CEDILLA_FIX)
    no_spaces = "".join(text.split())      # pasul 1: elimina spatiile
    upper = no_spaces.upper()              # pasul 2: majuscule

    invalid = []
    for original, ch in zip(no_spaces, upper):
        ok = is_latin_letter(original)
        if allow_romanian and ch in CHAR_TO_CODE:
            ok = True
        if not ok and original not in invalid:
            invalid.append(original)
    return upper, invalid


def read_text(prompt, allow_romanian=False, min_len=1, what="textul"):
    """Citeste de la tastatura pana cand textul este valid."""
    while True:
        raw = input(prompt)
        text, invalid = prepare(raw, allow_romanian)
        if invalid:
            print(f"  Eroare: caractere nepermise in {what}: {' '.join(invalid)}")
            print("  " + RANGE_HINT)
            continue
        if len(text) < min_len:
            if min_len == MIN_KEY_LEN:
                print(f"  Eroare: cheia trebuie sa aiba cel putin {MIN_KEY_LEN} litere "
                      f"(ai introdus {len(text)}).")
            else:
                print(f"  Eroare: {what} nu poate fi gol.")
            continue
        return text