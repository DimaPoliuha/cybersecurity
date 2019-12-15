class CaesarCipher:
    UNICODE_COUNT = 1114111

    def encrypt(self, text: str, key: int) -> str:
        result_text = ""
        for symbol in text:
            symbol_code = ord(symbol) + key
            if symbol_code > self.UNICODE_COUNT or symbol_code < 0:
                symbol_code = symbol_code % self.UNICODE_COUNT
            result_text += chr(symbol_code)
        return result_text

    def decrypt(self, text: str, key: int) -> str:
        result_text = ""
        for symbol in text:
            symbol_code = ord(symbol) - key
            if symbol_code > self.UNICODE_COUNT or symbol_code < 0:
                symbol_code = symbol_code % self.UNICODE_COUNT
            result_text += chr(symbol_code)
        return result_text
