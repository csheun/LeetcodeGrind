import re

class Solution:
    def isValid(self, word: str) -> bool:
        word = word.lower()
        vowels = 'aeiou'
        cond_1 = len(word) >= 3
        cond_2 = bool(re.fullmatch(r'[a-z0-9]+', word))
        cond_3 = any(c in vowels for c in word)
        cond_4 = any(c.isalpha() and c not in vowels for c in word)
        return cond_1 and cond_2 and cond_3 and cond_4
        