import argparse
from pathlib import Path

from cipher.trithemius_cipher import TrithemiusCipher


def main(process: str, input_file: Path, output_file: Path, key):
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

    parser.add_argument("--process", help="process", required=True, type=str)
    parser.add_argument("--key_file", help="key", required=False, default=Path("results/key.txt"), type=Path)
    parser.add_argument("--a", required=False, default=None, type=int)
    parser.add_argument("--b", required=False, default=None, type=int)
    parser.add_argument("--c", required=False, default=None, type=int)    
    parser.add_argument(
        "--input_file", 
        help="file with text",
        required=False,
        default=None,
        type=Path
    )
    parser.add_argument(
        "--output_file",
        help="file to store result",
        required=False,
        default=None,
        type=Path,
    )
    args = parser.parse_args()
    process = args.process
    input_file = args.input_file
    output_file = args.output_file
    key_file = args.key_file
    a = args.a
    b = args.b
    c = args.c

    key = TrithemiusCipher.parse_key(key_file, a, b, c)

    if not input_file:
        input_file = Path("results/input.txt") if process == "encrypt" else Path("results/encrypted.txt")
    if not output_file:
        output_file = Path("results/encrypted.txt") if process == "encrypt" else Path("results/decrypted.txt")

    main(process, input_file, output_file, key)
