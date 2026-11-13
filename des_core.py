# -*- coding: utf-8 -*-
"""
DES complet (folosit pentru verificare). Pastreaza toti pasii intermediari
ai fiecarei runde, ca sa se poata compara cu rezultatul sarcinii 2.10.
"""

from tables import IP, FP, E, P, PC1, PC2, SHIFTS, SBOX
from bits import permute, xor_bits


def sbox_lookup(box_index, six_bits):
    """Cutia-S: bitii 1 si 6 dau linia, bitii 2-5 dau coloana."""
    row = int(six_bits[0] + six_bits[5], 2)
    col = int(six_bits[1:5], 2)
    return SBOX[box_index][row][col]


def key_schedule(key_bits64):
    """Genereaza K+, C0, D0 si cheile de runda K1..K16."""
    k_plus = permute(key_bits64, PC1)            # K+ (56 biti)
    c, d = k_plus[:28], k_plus[28:]
    keys = []
    for shift in SHIFTS:
        c = c[shift:] + c[:shift]
        d = d[shift:] + d[:shift]
        keys.append(permute(c + d, PC2))         # Ki (48 biti)
    return k_plus, keys


def des_encrypt_trace(block_bits64, key_bits64):
    """
    Cripteaza un bloc de 64 de biti si intoarce (criptograma_biti, runde).
    Fiecare element din 'runde' contine toti pasii intermediari ai rundei.
    """
    _, keys = key_schedule(key_bits64)
    ip = permute(block_bits64, IP)
    left, right = ip[:32], ip[32:]
    rounds = []
    for i in range(16):
        e_r = permute(right, E)                  # E(R_{i-1}), 48 biti
        xored = xor_bits(keys[i], e_r)           # K_i + E(R_{i-1})
        b_groups = [xored[j * 6:(j + 1) * 6] for j in range(8)]   # B1..B8
        s_values = [sbox_lookup(j, b_groups[j]) for j in range(8)]
        s_out = "".join(format(v, "04b") for v in s_values)       # 32 biti
        p_out = permute(s_out, P)                # P(S1(B1)...S8(B8))
        new_right = xor_bits(left, p_out)        # R_i = L_{i-1} + f
        rounds.append({
            "i": i + 1, "L_prev": left, "R_prev": right, "K": keys[i],
            "E": e_r, "xor": xored, "B": b_groups, "S_values": s_values,
            "S_out": s_out, "P_out": p_out, "R": new_right, "L": right,
        })
        left, right = right, new_right
    cipher = permute(right + left, FP)           # R16 L16 -> IP^-1
    return cipher, rounds