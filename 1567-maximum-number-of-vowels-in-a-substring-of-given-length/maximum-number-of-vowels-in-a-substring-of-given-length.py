from collections import defaultdict
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        # sliding window
        res = 0
        curr_window = 0
        for i in range(len(s)):
            if i >= k:
                if s[i - k] in vowels:
                    curr_window -= 1
            if s[i] in vowels:
                curr_window += 1
                res = max(curr_window, res)
        return res
            

        