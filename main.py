# -*- coding: utf-8 -*-
"""
Lucrare de laborator nr. 3, Sarcina 3.2 - Cifrul Vigenere (limba romana, 31 de litere).
Rulare:  python main.py
"""

from config import MIN_KEY_LEN, ALLOW_ROMANIAN_LETTERS_IN_CRYPTOGRAM
from validation import read_text
from vigenere import vigenere
from display import print_alphabet, print_table


def main():
    print("=== Cifrul Vigenere - alfabetul romanesc (31 de litere) ===")
    print_alphabet()

    while True:
        print("\nAlegeti operatia:")
        print("  1 - Criptare")
        print("  2 - Decriptare")
        print("  0 - Iesire")
        choice = input("Optiunea dumneavoastra: ").strip()

        if choice == "0":
            print("La revedere!")
            break
        if choice not in ("1", "2"):
            print("  Optiune invalida. Introduceti 1, 2 sau 0.")
            continue

        decrypt = (choice == "2")

        # 1) cheia (minim 7 litere, doar A-Z / a-z)
        key = read_text(f"Introduceti cheia (minim {MIN_KEY_LEN} litere): ",
                        allow_romanian=False, min_len=MIN_KEY_LEN, what="cheie")

        # 2) mesajul sau criptograma
        if decrypt:
            text = read_text("Introduceti criptograma: ",
                             allow_romanian=ALLOW_ROMANIAN_LETTERS_IN_CRYPTOGRAM,
                             what="criptograma")
        else:
            text = read_text("Introduceti mesajul: ",
                             allow_romanian=False, what="mesajul")

        result, steps = vigenere(text, key, decrypt)

        print(f"\nCheia folosita (majuscule): {key}")
        print_table(steps, decrypt)
        if decrypt:
            print(f"\nMesajul decriptat: {result}")
            print("(Spatiile dintre cuvinte se adauga manual, dupa sensul mesajului.)")
        else:
            print(f"\nCriptograma: {result}")


if __name__ == "__main__":
    main()