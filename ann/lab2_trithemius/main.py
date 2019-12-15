import argparse

from trithemius_cipher import TrithemiusCipher


def main(process, input_file, output_file, key):
    with open(input_file, "r") as f:
        text = f.read()

    cipher_obj = TrithemiusCipher()
    if process == "encrypt":
        result = cipher_obj.encrypt(text, key)
    elif process == "decrypt":
        result = cipher_obj.decrypt(text, key)
    else:
        raise Exception("No such process")

    with open(output_file, "w") as f:
        f.write(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trithemius cipher")

    parser.add_argument("--process", required=True)
    parser.add_argument("--key_file", required=False, default="results/key.txt")
    parser.add_argument("--a", required=False, default=None, type=int)
    parser.add_argument("--b", required=False, default=None, type=int)
    parser.add_argument("--c", required=False, default=None, type=int)    
    parser.add_argument("--input_file", required=False, default=None)
    parser.add_argument("--output_file", required=False, default=None)
    args = parser.parse_args()
    process = args.process
    input_file = args.input_file
    output_file = args.output_file
    key_file = args.key_file
    a = args.a
    b = args.b
    c = args.c

    if a is not None and b is not None and c is not None:
        key = lambda x: a * x ** 2 + b * x + c
    elif a is not None and b is not None:
        key = lambda x: a * x + b
    elif key_file:
        with open(key_file) as f:
            key = f.read()
        key = [ord(symbol) for symbol in key]

    if not input_file:
        input_file = "results/input.txt" if process == "encrypt" else "results/encrypted.txt"
    if not output_file:
        output_file = "results/encrypted.txt" if process == "encrypt" else "results/decrypted.txt"

    main(process, input_file, output_file, key)
