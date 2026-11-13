# -*- coding: utf-8 -*-
"""Afisarea tabelelor si a pasilor intermediari."""

from tables import P
from bits import group, bits_to_hex


def line(title=""):
    print("\n" + "=" * 64)
    if title:
        print(title)
        print("=" * 64)


def print_grid(values, cols, width=3):
    """Afiseaza o lista de valori ca tabel cu 'cols' coloane."""
    for r in range(0, len(values), cols):
        print("   " + " ".join(f"{v:>{width}}" for v in values[r:r + cols]))


def print_p_table():
    print("Tabelul permutarii P (32 -> 32), 8 linii x 4 coloane:")
    print_grid(P, 4)


def print_s_outputs(s_groups):
    print("Iesirile cutiilor-S (cate 4 biti):")
    for j, g in enumerate(s_groups, start=1):
        print(f"   S{j}(B{j}) = {g}  (zecimal {int(g, 2):>2}, hex {int(g, 2):X})")
    print("Concatenate S1(B1)...S8(B8) =", group("".join(s_groups)))


def print_permutation_steps(s_out_bits, p_out):
    """Arata cum fiecare bit al rezultatului provine dintr-un bit de intrare."""
    print("Bitii de intrare (numerotati 1..32), in tabel 8x4:")
    for r in range(8):
        cells = [f"{r * 4 + c + 1:>2}:{s_out_bits[r * 4 + c]}" for c in range(4)]
        print("   " + "  ".join(cells))
    print("\nBitul j din rezultat = bitul P[j] din intrare:")
    for r in range(8):
        cells = []
        for c in range(4):
            j = r * 4 + c
            cells.append(f"{j + 1:>2}<-{P[j]:>2} = {p_out[j]}")
        print("   " + "   ".join(cells))
    print("\nP(S1(B1)...S8(B8)) =", group(p_out))
    print("                  hex =", bits_to_hex(p_out))


def print_xor(l_prev, p_out, r_i):
    print("L_{i-1}             =", group(l_prev), "  hex", bits_to_hex(l_prev))
    print("P(S-box output)     =", group(p_out), "  hex", bits_to_hex(p_out))
    print("-" * 64)
    print("R_i = L_{i-1} XOR P =", group(r_i), "  hex", bits_to_hex(r_i))