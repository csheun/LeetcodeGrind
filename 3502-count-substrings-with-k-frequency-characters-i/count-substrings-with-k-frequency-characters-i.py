from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        res = 0
        for i in range(0, len(s) - k + 1):
            # find the right idx that fulfils the condition
            freq = defaultdict(int)
            for j in range(i, len(s)):
                freq[s[j]] += 1
                if freq[s[j]] == k:
                    # found and ad to res:
                    res += (len(s) - j)
                    break
        return res

            

        