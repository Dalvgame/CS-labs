# -*- coding: utf-8 -*-
"""Constante si setari pentru cifrul Vigenere (alfabetul romanesc, 31 de litere)."""

# Alfabetul romanesc (31 de litere); pozitia in sir = codul literei (0..30)
ALPHABET = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
N = len(ALPHABET)  # 31

# litera -> cod
CHAR_TO_CODE = {ch: i for i, ch in enumerate(ALPHABET)}

# Lungimea minima a cheii (cerinta din enunt)
MIN_KEY_LEN = 7

# Criptograma poate contine Ă, Â, Î, Ș, Ț (fac parte din alfabetul de 31 de litere).
# Daca profesoara vrea strict doar A-Z/a-z si la decriptare, puneti False.
ALLOW_ROMANIAN_LETTERS_IN_CRYPTOGRAM = True

# Variante cu sedila (ş, ţ) se transforma in variantele corecte cu virgula (ș, ț)
CEDILLA_FIX = str.maketrans({"Ş": "Ș", "ş": "ș", "Ţ": "Ț", "ţ": "ț"})

# Mesaj afisat cand utilizatorul introduce caractere nepermise
RANGE_HINT = ("Sunt permise doar caracterele 'A'-'Z' si 'a'-'z' "
              "(spatiile din mesaj sunt eliminate automat).")