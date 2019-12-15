import itertools
from cipher.base_cipher import BaseCipher


class TrithemiusCipher(BaseCipher):
    def _algorithm(self, text: str, key: int, process: str) -> str:
        result_text = ""
        for symbol, key_code in zip(text, itertools.cycle(key)):
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
