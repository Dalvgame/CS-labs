# -*- coding: utf-8 -*-
"""Citirea si validarea datelor de intrare; generarea datelor aleatorii."""

import random

from bits import hex_to_bits

HEX_DIGITS = set("0123456789abcdefABCDEF")

HINT_32 = ("Formate acceptate: 32 de biti (0/1, cu sau fara spatii), "
           "8 cifre hexazecimale (cate una pentru fiecare Sj(Bj)), "
           "sau 8 numere zecimale 0-15 separate prin virgula.")


def parse_32(text):
    """Transforma textul introdus in 32 de biti sau ridica ValueError."""
    t = text.strip()
    if "," in t:                                    # 8 valori zecimale 0..15
        parts = [p.strip() for p in t.split(",") if p.strip() != ""]
        if len(parts) != 8 or not all(p.isdigit() and 0 <= int(p) <= 15 for p in parts):
            raise ValueError("Trebuie sa introduceti exact 8 numere intre 0 si 15.")
        return "".join(format(int(p), "04b") for p in parts)

    t = t.replace(" ", "").replace("_", "")
    if t.lower().startswith("0x"):
        t = t[2:]
    if len(t) == 32 and set(t) <= {"0", "1"}:
        return t
    if len(t) == 8 and set(t) <= HEX_DIGITS:
        return hex_to_bits(t, 32)
    raise ValueError(f"Valoare invalida ({len(t)} caractere). " + HINT_32)


def read_32(prompt):
    while True:
        try:
            return parse_32(input(prompt))
        except ValueError as err:
            print("  Eroare:", err)


def read_round(prompt="Numarul rundei i (1-16): "):
    while True:
        raw = input(prompt).strip()
        if raw.isdigit() and 1 <= int(raw) <= 16:
            return int(raw)
        print("  Eroare: introduceti un numar intreg intre 1 si 16.")


def read_hex64(prompt):
    """Citeste 16 cifre hexazecimale; Enter = generare aleatorie."""
    while True:
        raw = input(prompt).strip().replace(" ", "")
        if raw == "":
            return random_bits(64)
        if len(raw) == 16 and set(raw) <= HEX_DIGITS:
            return hex_to_bits(raw, 64)
        print("  Eroare: introduceti exact 16 cifre hexazecimale (0-9, A-F) "
              "sau apasati Enter pentru valori aleatorii.")


def random_bits(n):
    return "".join(random.choice("01") for _ in range(n))