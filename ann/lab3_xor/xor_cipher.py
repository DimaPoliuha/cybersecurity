import itertools
from random import randint


class XORCipher:
    UNICODE_COUNT = 1114111

    def encrypt(self, text: str, key: int) -> str:
        result_text = ""
        keys = itertools.cycle(key)
        for symbol, key_code in zip(text, keys):
            symbol_code = ord(symbol) + key_code
            if symbol_code > self.UNICODE_COUNT or symbol_code < 0:
                symbol_code = symbol_code % self.UNICODE_COUNT
            result_text += chr(symbol_code)
        return result_text

    def decrypt(self, text: str, key: int) -> str:
        result_text = ""
        keys = itertools.cycle(key)
        for symbol, key_code in zip(text, keys):
            symbol_code = ord(symbol) - key_code
            if symbol_code > self.UNICODE_COUNT or symbol_code < 0:
                symbol_code = symbol_code % self.UNICODE_COUNT
            result_text += chr(symbol_code)
        return result_text

    def generate_key(self):
        key = [randint(0, self.UNICODE_COUNT) for _ in range(randint(100, 1000))]
        key_f = "".join(map(chr, key)).encode('utf-16','surrogatepass')
        return key, key_f
