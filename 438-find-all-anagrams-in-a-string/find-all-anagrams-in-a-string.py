from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if (len(p) > len(s)):
            return []
        res = []
        p_freq = Counter(p)
        freq = Counter(s[:len(p)])
        if (freq == p_freq):
            res.append(0)

        for i in range(1, len(s) - len(p) +  1):
            # remove prev element, add the next element
            # compare again
            freq[s[i - 1]] -= 1
            if (freq[s[i - 1]] == 0):
                del freq[s[i - 1]]
            if s[i + len(p) - 1] not in freq:
                freq[s[i + len(p) - 1]] = 0
            freq[s[i + len(p) - 1]] += 1
            if (freq == p_freq):
                res.append(i)
        
        return res
        