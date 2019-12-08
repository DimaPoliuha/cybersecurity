class BaseCipher:
    UNICODE_COUNT = 1114111

    def encrypt(self, text: str, key: int):
        raise NotImplementedError

    def decrypt(self, text: str, key: int):
        raise NotImplementedError
