# Laboratory Work No. 4 – DES Block Cipher

**Course:** Cryptography and Security
**Student:** Cuibari Vladislav, **Group:** FAF-243
**Task:** 2.10 (register number 10, `10 mod 11 = 10`)

## Task 2.10

In round *i* of DES the outputs of the S-boxes `S1(B1)S2(B2)…S8(B8)` (32 bits) and `L(i-1)` (32 bits) are known. Compute `R(i)`:

```
R(i) = L(i-1) XOR f(R(i-1), K(i))        f = P( S1(B1) S2(B2) ... S8(B8) )
=>  R(i) = L(i-1) XOR P( S1(B1) ... S8(B8) )
```

## Features

- Shows the table P (8 × 4), the S-box outputs, the bit-by-bit permutation (`bit j <- bit P[j]`) and the final XOR.
- Input can be typed or generated randomly.
- Accepted formats for 32-bit values: 32 bits (spaces allowed), 8 hex digits (one per `Sj(Bj)`), or 8 decimals `0–15` separated by commas.
- **Verification mode:** runs a full DES (16 rounds) on a key and a block and checks that the Task 2.10 result equals the real `R(i)`.

## Files

| File           | Purpose                                                       |
|----------------|---------------------------------------------------------------|
| `main.py`      | Menu and workflow (manual / random / verification)            |
| `task_2_10.py` | The task: permutation P and XOR with L(i-1)                   |
| `tables.py`    | All DES tables (IP, FP, E, P, PC1, PC2, shifts, S-boxes)      |
| `bits.py`      | Bit-string helpers (hex, XOR, permutation, grouping)          |
| `des_core.py`  | Full DES with all intermediate values (used for verification) |
| `display.py`   | Printing of tables and steps                                  |
| `inputs.py`    | Input reading, validation and random generation               |

## Run

```
python main.py
```

Python 3.8+ and the standard library only. Keep all files in the same folder.

## Testing

The DES core reproduces the standard test vector (key `133457799BBCDFF1`, block `0123456789ABCDEF` -> `85E813540F0AB405`, `K1 = 1B02EFFC7072`, `R1 = EF4A6544`). The Task 2.10 function was also checked against 300 random DES runs × 16 rounds.