import random
import string
from Crypto.Cipher import DES
from cipher.base_cipher import BaseCipher


class DesCipher(BaseCipher):
    def _algorithm(self, text: str, key, process: str) -> str:
        iv = self.gen_initial()
        key = key.ljust(8)[:8].encode()
        des = DES.new(key, DES.MODE_CBC)

        if process == "encrypt":
            text = self.pad(text)
            text = text.encode('utf-8')
            encryptedText = des.encrypt(text).hex()
            return encryptedText
        elif process == "decrypt":
            text = bytes.fromhex(text)
            decryptedText = des.decrypt(text)
            return decryptedText
        else:
            raise Exception("No such process")

    def pad(self, text):
        while len(text) % 8 != 0:
            text += ' '
        return text

    def gen_initial(self):
        iv = ""
        for _ in range(16):
            iv += random.choice(string.ascii_letters)
        return iv
