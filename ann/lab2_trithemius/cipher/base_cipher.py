from abc import ABC


class BaseCipher(ABC):
    UNICODE_COUNT = 1114111

    def encrypt(self, text: str, key: int) -> str:
        return self._algorithm(text, key, "encrypt")

    def decrypt(self, text: str, key: int) -> str:
        return self._algorithm(text, key, "decrypt")

    def _algorithm(self, text: str, key: int, process: str) -> str:
        pass
