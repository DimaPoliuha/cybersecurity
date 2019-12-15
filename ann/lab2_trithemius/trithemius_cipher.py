import itertools


class TrithemiusCipher:
    UNICODE_COUNT = 1114111

    def encrypt(self, text, key):
        result_text = ""
        key = self.parse_key(key, text)
        for symbol, key_code in zip(text, key):
            symbol_code = ord(symbol) + key_code
            if symbol_code > self.UNICODE_COUNT or symbol_code < 0:
                symbol_code = symbol_code % self.UNICODE_COUNT
            result_text += chr(symbol_code)
        return result_text

    def decrypt(self, text, key):
        result_text = ""
        key = self.parse_key(key, text)
        for symbol, key_code in zip(text, key):
            symbol_code = ord(symbol) - key_code
            if symbol_code > self.UNICODE_COUNT or symbol_code < 0:
                symbol_code = symbol_code % self.UNICODE_COUNT
            result_text += chr(symbol_code)
        return result_text

    def parse_key(self, key, text):
        if type(key) == list:
            key = itertools.cycle(key)
        else:
            key = [key(index) for index in range(len(text))]
        return key
