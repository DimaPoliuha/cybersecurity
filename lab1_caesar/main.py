import argparse
from pathlib import Path

from cipher.caesar_cipher import CaesarCipher


def main(process: str, key: int, input_file: Path, output_file: Path):
    with open(input_file, "r") as f:
        text = f.read()

    cipher_obj = CaesarCipher()
    if process == "encrypt":
        result = cipher_obj.encrypt(text, key)
    elif process == "decrypt":
        result = cipher_obj.decrypt(text, key)
    else:
        raise Exception("No such process")

    with open(output_file, "w") as f:
        f.write(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Caesar cipher")

    parser.add_argument("--process", help="encrypt/decrypt", required=True, type=str)
    parser.add_argument("--key", help="key", required=True, type=int)
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
    key = args.key
    input_file = args.input_file
    output_file = args.output_file
    if not input_file:
        input_file = Path("results/input.txt") if process == "encrypt" else Path("results/encrypted.txt")
    if not output_file:
        output_file = Path("results/encrypted.txt") if process == "encrypt" else Path("results/decrypted.txt")

    main(process, key, input_file, output_file)
