class BaseCipher:
    # UNICODE_COUNT = 1114111
    # UNICODE_COUNT = 255
    UNICODE_COUNT = 127

    def encrypt(self, text: str, key: int):
        raise NotImplementedError

    def decrypt(self, text: str, key: int):
        raise NotImplementedError

    def brute_force(self, text: str):
        raise NotImplementedError
