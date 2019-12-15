import re
import itertools
from cipher.base_cipher import BaseCipher
from random import choice


class LitFragCipher(BaseCipher):
    def _algorithm(self, text: str, key, process: str) -> str:
        result_text = []
        key = self.parse_key(key)
        separators_idxs = [m.start() for m in re.finditer("\n", key)]
        if process == "decrypt":
            text = text.split(",")
        for symbol in text:
            if symbol == ".":
                symbol = "\."
            if process == "encrypt":
                sep = ","
                try:
                    idxs = [m.start() for m in re.finditer(symbol, key)]
                except:
                    idxs = None
                if idxs:
                    res_symbol_idx = choice(idxs)
                    count_sep = sum(sep < res_symbol_idx for sep in separators_idxs)
                    res = f"{res_symbol_idx - count_sep + 1}/{count_sep + 1}"
                else:
                    res = "?"
                result_text.append(res)
            elif process == "decrypt":
                sep = ""
                if not symbol == "?":
                    symbol = symbol.split("/")
                    symbol = key[int(symbol[0]) + int(symbol[1]) - 2]
                result_text.append(symbol)
            else:
                raise Exception("No such process")
        return sep.join(result_text)

    @staticmethod
    def parse_key(key):
        key = [k for k in key.split("\n") if k]
        return "\n".join(key).lower()
