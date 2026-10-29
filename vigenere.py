# -*- coding: utf-8 -*-
"""
Algoritmul Vigenere pe alfabetul de 31 de litere.
  criptare:   c_i = (m_i + k_i) mod 31
  decriptare: m_i = (c_i - k_i) mod 31
"""

from config import ALPHABET, CHAR_TO_CODE, N


def vigenere(text, key, decrypt=False):
    """
    Intoarce (rezultat, pasi); 'pasi' permite afisarea tabelului de calcul.
    Fiecare pas: (litera, cod, litera_cheie, cod_cheie, cod_rezultat, litera_rezultat).
    """
    result = []
    steps = []
    for i, ch in enumerate(text):
        t = CHAR_TO_CODE[ch]                # m_i (sau c_i la decriptare)
        k_char = key[i % len(key)]          # cheia se repeta ciclic
        k = CHAR_TO_CODE[k_char]            # k_i
        r = (t - k) % N if decrypt else (t + k) % N
        result.append(ALPHABET[r])
        steps.append((ch, t, k_char, k, r, ALPHABET[r]))
    return "".join(result), steps