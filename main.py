# -*- coding: utf-8 -*-
"""
Lucrare de laborator nr. 4 - Algoritmul DES.
Sarcina 2.10:  se cunosc S1(B1)...S8(B8) si L_{i-1}; de calculat R_i.
Rulare:  python main.py
"""

import random

from bits import group, bits_to_hex, xor_bits
from tables import SBOX
from inputs import read_32, read_round, read_hex64, random_bits
from task_2_10 import compute_ri
from des_core import des_encrypt_trace
from display import (line, print_p_table, print_s_outputs,
                     print_permutation_steps, print_xor)


def solve_and_show(i, s_out, l_prev):
    """Rezolva sarcina 2.10 si afiseaza tabelele si toti pasii intermediari."""
    line(f"SARCINA 2.10 - calculul lui R{i}")
    print(f"Date de intrare (runda i = {i}):")
    result = compute_ri(s_out, l_prev)

    print_s_outputs(result["s_groups"])
    print(f"\nL{i - 1} =", group(l_prev), " hex", bits_to_hex(l_prev))

    line("Pasul 1: permutarea P aplicata iesirii cutiilor-S")
    print_p_table()
    print()
    print_permutation_steps(s_out, result["p_out"])

    line(f"Pasul 2: R{i} = L{i - 1} XOR P(S1(B1)...S8(B8))")
    print_xor(l_prev, result["p_out"], result["R_i"])

    line("REZULTAT")
    print(f"R{i} (binar) = {group(result['R_i'])}")
    print(f"R{i} (hex)   = {bits_to_hex(result['R_i'])}")
    return result["R_i"]


def manual_mode():
    i = read_round()
    print("\nIntroduceti S1(B1)S2(B2)...S8(B8).")
    s_out = read_32("S1(B1)...S8(B8) = ")
    l_prev = read_32(f"L{i - 1} (32 de biti sau 8 cifre hex) = ")
    solve_and_show(i, s_out, l_prev)


def random_mode():
    i = random.randint(1, 16)
    s_out = "".join(format(random.randint(0, 15), "04b") for _ in range(8))
    l_prev = random_bits(32)
    print(f"\nDate generate aleatoriu: i = {i}")
    solve_and_show(i, s_out, l_prev)


def verify_mode():
    """Ruleaza un DES complet si compara runda i cu rezultatul sarcinii 2.10."""
    line("VERIFICARE cu algoritmul DES complet")
    key = read_hex64("Cheia (16 cifre hex, Enter = aleatoare): ")
    block = read_hex64("Blocul de mesaj (16 cifre hex, Enter = aleator): ")
    i = read_round()

    cipher, rounds = des_encrypt_trace(block, key)
    r = rounds[i - 1]

    print(f"\nCheia          = {bits_to_hex(key)}")
    print(f"Blocul         = {bits_to_hex(block)}")
    print(f"\nRunda {i}:")
    print(f"  L{i - 1}            =", group(r["L_prev"]))
    print(f"  R{i - 1}            =", group(r["R_prev"]))
    print(f"  K{i}             =", group(r["K"], 6))
    print(f"  E(R{i - 1})        =", group(r["E"], 6))
    print(f"  K{i} + E(R{i - 1})  =", group(r["xor"], 6))
    for j in range(8):
        b = r["B"][j]
        row, col = int(b[0] + b[5], 2), int(b[1:5], 2)
        print(f"  B{j + 1} = {b}  -> S{j + 1}: linia {row}, coloana {col:>2} "
              f"-> {r['S_values'][j]:>2} = {format(r['S_values'][j], '04b')}")

    mine = solve_and_show(i, r["S_out"], r["L_prev"])
    line("COMPARATIE")
    print(f"R{i} calculat (sarcina 2.10) = {bits_to_hex(mine)}")
    print(f"R{i} din DES complet         = {bits_to_hex(r['R'])}")
    print("Rezultat:", "COINCID  ✓" if mine == r["R"] else "DIFERA  ✗")
    print(f"\nCriptograma completa (16 runde) = {bits_to_hex(cipher)}")


def main():
    print("=== Lab 4 - DES, Sarcina 2.10: calculul lui R_i ===")
    print("R_i = L_{i-1} XOR P(S1(B1)S2(B2)...S8(B8))")
    while True:
        print("\nAlegeti modul:")
        print("  1 - Introducere manuala a datelor")
        print("  2 - Date generate aleatoriu")
        print("  3 - Verificare cu DES complet")
        print("  0 - Iesire")
        choice = input("Optiunea dumneavoastra: ").strip()
        if choice == "0":
            print("La revedere!")
            break
        elif choice == "1":
            manual_mode()
        elif choice == "2":
            random_mode()
        elif choice == "3":
            verify_mode()
        else:
            print("  Optiune invalida. Introduceti 0, 1, 2 sau 3.")


if __name__ == "__main__":
    main()