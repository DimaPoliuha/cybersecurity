from ciphers.base_cipher import BaseCipher


class CaesarCipher(BaseCipher):
    def _algorithm(self, text: str, key: int, process: str) -> str:
        result_text = ""
        for symbol in text:
            if process == "encrypt":
                symbol_code = ord(symbol) + key
            elif process == "decrypt":
                symbol_code = ord(symbol) - key
            else:
                raise Exception("No such process")
            if symbol_code > self.UNICODE_COUNT or symbol_code < 0:
                symbol_code = symbol_code % self.UNICODE_COUNT
            result_text += chr(symbol_code)
        return result_text
