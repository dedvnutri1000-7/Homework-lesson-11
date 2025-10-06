class SuperStr(str):
    def is_repeatance(self, s: str) -> bool:
        if not s:
            return False
        return self == s * (len(self) // len(s)) and len(self) % len(s) == 0

    def is_palindrom(self) -> bool:
        lowered = self.lower()
        return lowered == lowered[::-1]


s = SuperStr("abcabcabc")
print("abcabcabc")
print(s.is_repeatance("abc"))
print(SuperStr("Level").is_palindrom())