from ciphers.base_cipher import BaseCipher


class CaesarCipher(BaseCipher):
    def encrypt(self, text: bytes, key: int) -> str:
        result_text = ""
        for symbol in text:
            encrypted_symbol_code = ord(symbol) + key
            if encrypted_symbol_code > self.UNICODE_COUNT or encrypted_symbol_code < 0:
                encrypted_symbol_code = encrypted_symbol_code % self.UNICODE_COUNT
            result_text += chr(encrypted_symbol_code)
        return result_text

    def decrypt(self, text: bytes, key: int):
        result_text = ""
        for symbol in text:
            decrypted_symbol_code = ord(symbol) - key
            if decrypted_symbol_code > self.UNICODE_COUNT or decrypted_symbol_code < 0:
                decrypted_symbol_code = decrypted_symbol_code % self.UNICODE_COUNT
            result_text += chr(decrypted_symbol_code)
        return result_text
