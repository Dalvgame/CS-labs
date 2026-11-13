# -*- coding: utf-8 -*-
"""Functii ajutatoare pentru lucrul cu siruri de biti (str de '0' si '1')."""


def hex_to_bits(hex_str, n_bits):
    """Transforma un sir hexazecimal in sir de biti de lungime n_bits."""
    return bin(int(hex_str, 16))[2:].zfill(n_bits)


def bits_to_hex(bits):
    """Transforma un sir de biti (lungime multiplu de 4) in sir hexazecimal."""
    return format(int(bits, 2), "0{}X".format(len(bits) // 4))


def xor_bits(a, b):
    """XOR bit cu bit intre doua siruri de biti de aceeasi lungime."""
    return "".join("1" if x != y else "0" for x, y in zip(a, b))


def permute(bits, table):
    """Aplica o permutare: bitul j din rezultat = bitul table[j] din intrare (numerotare de la 1)."""
    return "".join(bits[pos - 1] for pos in table)


def group(bits, size=4):
    """Imparte sirul de biti in grupuri de 'size' biti, separate prin spatiu."""
    return " ".join(bits[i:i + size] for i in range(0, len(bits), size))


def text_to_bits(text8):
    """8 caractere ASCII -> 64 de biti."""
    return "".join(format(ord(c), "08b") for c in text8)