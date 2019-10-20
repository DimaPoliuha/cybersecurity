import argparse

from ciphers.caesar_cipher import CaesarCipher

ciphers = {"caesar": CaesarCipher}


def main(cipher_name: str, text: str, key: int):
    cipher = ciphers.get(cipher_name)
    # data_path.mkdir(mode=0o777, exist_ok=True)

    if cipher is None:
        raise Exception("No such cipher")

    cipher_obj = cipher()
    result = cipher_obj.encrypt(text, key)
    print(result.encode("utf-8"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cybersecurity tool")

    parser.add_argument("--cipher", help="cipher name", required=True, type=str)
    parser.add_argument("--text", help="text to encrypt", required=True, type=str)
    parser.add_argument("--key", help="key", required=True, type=int)
    # parser.add_argument(
    #     "--data_path",
    #     help="path to store bot data",
    #     required=False,
    #     default=Path("bot_data/"),
    #     type=Path,
    # )
    args = parser.parse_args()
    cipher = args.cipher
    text = args.text
    key = args.key

    main(cipher, text, key)
