# -*- coding: utf-8 -*-
"""Afisarea alfabetului si a tabelului de calcul."""

from config import ALPHABET, N


def print_alphabet():
    print("Alfabet: " + " ".join(f"{ch}={i}" for i, ch in enumerate(ALPHABET)))


def print_table(steps, decrypt):
    """Afiseaza tabelul de calcul (ca in exemplul din laborator)."""
    in_name = "C" if decrypt else "M"
    out_name = "M" if decrypt else "C"
    op = "-" if decrypt else "+"
    print(f"\nTabel de calcul ({out_name}_i = ({in_name}_i {op} K_i) mod {N}):")
    print(f"{'poz':>4} {in_name + '(litera)':>9} {in_name + '(cod)':>7} "
          f"{'K(litera)':>10} {'K(cod)':>7} {out_name + '(cod)':>7} {out_name + '(litera)':>9}")
    for pos, (ch, t, kc, k, r, rc) in enumerate(steps, start=1):
        print(f"{pos:>4} {ch:>9} {t:>7} {kc:>10} {k:>7} {r:>7} {rc:>9}")