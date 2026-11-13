# -*- coding: utf-8 -*-
"""
Sarcina 2.10.
In runda i a algoritmului DES se cunoaste S1(B1)S2(B2)...S8(B8) (32 de biti)
si L_{i-1} (32 de biti). Sa se calculeze R_i.

Formula DES:   R_i = L_{i-1} XOR f(R_{i-1}, K_i)
unde           f   = P( S1(B1) S2(B2) ... S8(B8) )
Deci:          R_i = L_{i-1} XOR P( S1(B1) ... S8(B8) )
"""

from tables import P
from bits import permute, xor_bits


def compute_ri(s_out_bits, l_prev_bits):
    """
    Intrare:  s_out_bits  - 32 de biti: S1(B1)S2(B2)...S8(B8), cate 4 biti fiecare
              l_prev_bits - 32 de biti: L_{i-1}
    Iese:     dictionar cu pasii intermediari si rezultatul R_i.
    """
    s_groups = [s_out_bits[j * 4:(j + 1) * 4] for j in range(8)]   # S1(B1)..S8(B8)
    p_out = permute(s_out_bits, P)             # pasul 1: permutarea P
    r_i = xor_bits(l_prev_bits, p_out)         # pasul 2: XOR cu L_{i-1}
    return {"s_groups": s_groups, "p_out": p_out, "R_i": r_i}