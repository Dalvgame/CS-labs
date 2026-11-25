# Laboratory Work No. 3 – Vigenère Cipher (Romanian Alphabet)

**Course:** Cryptography and Security
**Student:** Cuibari Vladislav
**Group:** FAF-243
**Task:** 3.2 – Vigenère cipher (register number 10, even)
**University:** Technical University of Moldova (UTM), Faculty of Computers, Informatics and Microelectronics

## Description

An interactive console program that encrypts and decrypts messages with the **Vigenère cipher** for the **31-letter Romanian alphabet**. The letters are encoded with the numbers 0–30:

```
A=0  Ă=1  Â=2  B=3  C=4  D=5  E=6  F=7  G=8  H=9  I=10  Î=11  J=12  K=13  L=14  M=15
N=16 O=17 P=18 Q=19 R=20 S=21 Ș=22 T=23 Ț=24 U=25 V=26 W=27 X=28 Y=29 Z=30
```

Because the alphabet has 31 letters, all calculations use **modulo 31**:

```
encryption:  c_i = (m_i + k_i) mod 31
decryption:  m_i = (c_i - k_i) mod 31
```

The key is repeated cyclically over the whole text.

## Requirements covered

- Implemented in Python, for Romanian messages (31 letters coded 0, 1, …, 30).
- The key, the message and the cryptogram may contain the letters of the Romanian alphabet (`A`–`Z`, `a`–`z` and `Ă Â Î Ș Ț`). For any other character the program shows the rejected character and the allowed range, then asks again.
- The key must have **at least 7 letters**.
- In the message, **spaces are removed first**, and then all letters are converted to **uppercase**.
- The user chooses the operation (encryption or decryption), enters the key and the message (or the cryptogram), and receives the cryptogram (or the decrypted message).
- Encryption and decryption follow the formulas above.
- A step-by-step calculation table is printed for every operation.

## Project structure

| File            | Purpose                                                                 |
|-----------------|-------------------------------------------------------------------------|
| `main.py`       | Entry point: menu, user interaction, connects the other modules         |
| `config.py`     | Alphabet, letter-to-code map, minimum key length, settings, error text  |
| `validation.py` | Space removal, uppercase conversion, character checks, input retry loop |
| `vigenere.py`   | The cipher: encryption and decryption of a prepared text                |
| `display.py`    | Prints the alphabet and the calculation table                           |

All five files must be in the **same folder**.

## Requirements

- Python 3.8 or newer (standard library only, no extra packages)

## How to run

```
python main.py
```

In PyCharm: open `main.py` and press **Run**. If the terminal shows broken diacritics on Windows, run `chcp 65001` first or use the PyCharm console.

## Usage example

```
Alegeti operatia:
  1 - Criptare
  2 - Decriptare
  0 - Iesire
Optiunea dumneavoastra: 1
Introduceti cheia (minim 7 litere): CRIPTOGRAFIE
Introduceti mesajul: Maine invatam criptografia

Criptograma: QRRBYWȚMAZISGHRDMBNHALRE
```

Decrypting that cryptogram with the same key returns `MAINEINVATAMCRIPTOGRAFIA`. The spaces between words are restored manually, according to the meaning of the message: `MAINE INVATAM CRIPTOGRAFIA`.

## Design decisions

- **Romanian letters in the input.** The assignment says the characters are between `A`–`Z` and `a`–`z`, but the messages are in Romanian (31 letters), so `Ă`, `Â`, `Î`, `Ș`, `Ț` are accepted in the key, message and cryptogram. To follow the literal range strictly, set `ALLOW_ROMANIAN_LETTERS_IN_INPUT = False` in `config.py`; the cryptogram still accepts the five letters, because the cipher can produce them.
- **Validation per field.** An invalid message or cryptogram does not ask the user to choose the operation or enter the key again; only the wrong field is requested again.
- **Cedilla letters.** `ş` and `ţ` (with cedilla) are converted to the correct `ș` and `ț` (with comma) when a cryptogram is entered.

## Limitations

- Vigenère is a historical cipher and is **not secure** for protecting real data. A repeated key leaves statistical patterns (for example, it can be attacked with the Kasiski examination).
- The decrypted text has no spaces; they must be added manually.

## Author

Cuibari Vladislav, FAF-243