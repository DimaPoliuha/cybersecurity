import argparse

from caesar_cipher import CaesarCipher


def main(process, key, input_file, output_file):
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

    parser.add_argument("--process", required=True)
    parser.add_argument("--key", required=True, type=int)
    parser.add_argument("--input_file", required=False, default=None)
    parser.add_argument("--output_file", required=False, default=None)
    args = parser.parse_args()
    process = args.process
    key = args.key
    input_file = args.input_file
    output_file = args.output_file
    if not input_file:
        input_file = "results/input.txt" if process == "encrypt" else "results/encrypted.txt"
    if not output_file:
        output_file = "results/encrypted.txt" if process == "encrypt" else "results/decrypted.txt"

    main(process, key, input_file, output_file)
