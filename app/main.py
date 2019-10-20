import argparse
from pathlib import Path

from ciphers.caesar_cipher import CaesarCipher

ciphers = {"caesar": CaesarCipher}


def main(cipher_name: str, process: str, key: int, input_file: Path, output_file: Path):
    cipher = ciphers.get(cipher_name)
    with open(input_file, "rb") as f:
        text = f.read()

    if cipher is None:
        raise Exception("No such cipher")

    cipher_obj = cipher()
    if process == "encrypt":
        result = cipher_obj.encrypt(text, key)
    elif process == "decrypt":
        result = cipher_obj.decrypt(text, key)
    elif process == "bruteforce":
        result = cipher_obj.brute_force(text)
    else:
        raise Exception("No such process")

    with open(output_file, "wb") as f:
        f.write(result.encode("utf-8"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cybersecurity tool")

    parser.add_argument("--cipher", help="cipher name", required=True, type=str)
    parser.add_argument("--process", help="process", required=True, type=str)
    parser.add_argument("--key", help="key", required=False, default=0, type=int)
    parser.add_argument("--input_file", help="file with text", required=True, type=Path)
    parser.add_argument(
        "--output_file",
        help="file to store result",
        required=False,
        default=Path("app/output.txt"),
        type=Path,
    )
    args = parser.parse_args()
    cipher = args.cipher
    process = args.process
    key = args.key
    input_file = args.input_file
    output_file = args.output_file

    main(cipher, process, key, input_file, output_file)
