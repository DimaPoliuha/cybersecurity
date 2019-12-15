import argparse
from pathlib import Path

from cipher.xor_cipher import XORCipher


def main(process: str, input_file: Path, output_file: Path, key_file: Path):
    with open(input_file, "r") as f:
        text = f.read()

    cipher_obj = XORCipher()
    if process == "encrypt":
        key, key_f = XORCipher.generate_key()
        with open(key_file, "wb") as f:
            f.write(key_f)
        result = cipher_obj.encrypt(text, key)
    elif process == "decrypt":
        with open(key_file, "rb") as f:
            key = f.read()
        key = (ord(symbol) for symbol in key.decode('utf-16'))
        result = cipher_obj.decrypt(text, key)
    else:
        raise Exception("No such process")

    with open(output_file, "w") as f:
        f.write(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="XOR cipher")

    parser.add_argument("--process", help="process", required=True, type=str)
    parser.add_argument("--key_file", help="key", required=False, default=Path("results/key.txt"), type=Path)
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

    if not input_file:
        input_file = Path("results/input.txt") if process == "encrypt" else Path("results/encrypted.txt")
    if not output_file:
        output_file = Path("results/encrypted.txt") if process == "encrypt" else Path("results/decrypted.txt")

    main(process, input_file, output_file, key_file)
