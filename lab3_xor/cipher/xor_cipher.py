import itertools
from cipher.base_cipher import BaseCipher
from random import randint


class XORCipher(BaseCipher):
    def _algorithm(self, text: str, key, process: str) -> str:
        result_text = ""
        keys = itertools.cycle(key)
        for symbol, key_code in zip(text, keys):
            if process == "encrypt":
                symbol_code = ord(symbol) + key_code
            elif process == "decrypt":
                symbol_code = ord(symbol) - key_code
            else:
                raise Exception("No such process")
            if symbol_code > self.UNICODE_COUNT or symbol_code < 0:
                symbol_code = symbol_code % self.UNICODE_COUNT
            result_text += chr(symbol_code)
        return result_text

    @classmethod
    def generate_key(cls, len_t):
        key = [randint(0, cls.UNICODE_COUNT) for _ in range(len_t + randint(100, 1000))]
        key_f = "".join(map(chr, key)).encode('utf-16', 'surrogatepass')
        return key, key_f
