# -*- coding: utf-8 -*-
"""Constante si setari pentru cifrul Vigenere (alfabetul romanesc, 31 de litere)."""

# Alfabetul romanesc (31 de litere); pozitia in sir = codul literei (0..30)
ALPHABET = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
N = len(ALPHABET)  # 31

# litera -> cod
CHAR_TO_CODE = {ch: i for i, ch in enumerate(ALPHABET)}

# Lungimea minima a cheii (cerinta din enunt)
MIN_KEY_LEN = 7

# True  = cheia, mesajul si criptograma pot contine si Ă, Â, Î, Ș, Ț (alfabetul de 31 de litere)
# False = strict 'A'-'Z' si 'a'-'z' pentru cheie si mesaj (conform citirii literale a enuntului);
#         criptograma accepta oricum cele 5 litere, altfel programul nu si-ar putea decripta rezultatul.
ALLOW_ROMANIAN_LETTERS_IN_INPUT = True

# Variante cu sedila (ş, ţ) se transforma in variantele corecte cu virgula (ș, ț)
CEDILLA_FIX = str.maketrans({"Ş": "Ș", "ş": "ș", "Ţ": "Ț", "ţ": "ț"})

# Mesaj afisat cand utilizatorul introduce caractere nepermise
_RANGE_STRICT = ("Sunt permise doar caracterele 'A'-'Z' si 'a'-'z' "
                 "(spatiile din mesaj sunt eliminate automat).")
_RANGE_ROMANIAN = ("Sunt permise doar literele alfabetului romanesc "
                   "'A'-'Z', 'a'-'z' si Ă, Â, Î, Ș, Ț, ă, â, î, ș, ț "
                   "(spatiile din mesaj sunt eliminate automat).")
RANGE_HINT = _RANGE_ROMANIAN if ALLOW_ROMANIAN_LETTERS_IN_INPUT else _RANGE_STRICT