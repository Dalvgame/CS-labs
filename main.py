import sys

import alphabet
import cipher
import input_reader


def main() -> None:
    # Make sure Ă, Â, Î, Ș, Ț are read and printed correctly
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stdin.reconfigure(encoding="utf-8")

    print("=== Caesar cipher - Romanian alphabet (n = 31) ===")

    while True:
        print()
        operation = input_reader.read_choice(
            "Choose an operation: [E]ncrypt, [D]ecrypt, or e[X]it: ", "EDX")
        if operation == "X":
            break

        mode = input_reader.read_choice(
            "Cipher type: [1] Caesar (Task 1.1), [2] Caesar with keyword permutation (Task 1.2): ", "12")

        active = alphabet.LETTERS
        if mode == "2":
            keyword = input_reader.read_keyword()
            active = alphabet.build_permuted(keyword)
            print(f"Permuted alphabet: {active}")
        else:
            print(f"Romanian alphabet: {active}")

        shift = input_reader.read_shift()

        if operation == "E":
            text = input_reader.read_text("Enter the message (spaces are removed): ")
            print(f"Encrypted text: {cipher.encrypt(text, shift, active)}")
        else:
            text = input_reader.read_text("Enter the ciphertext (spaces are removed): ")
            print(f"Decrypted text: {cipher.decrypt(text, shift, active)}")


if __name__ == "__main__":
    main()